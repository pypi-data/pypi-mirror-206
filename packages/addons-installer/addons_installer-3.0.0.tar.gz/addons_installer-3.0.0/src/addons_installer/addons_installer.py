import logging
import subprocess
import sys
import warnings
from os.path import exists as path_exists
from os.path import join as path_join
from typing import Dict, Set, Union, List, Type

from .api import OdooAddonsDef, AddonsSuffix
from .git_addons import GitOdooAddons, GitSubDirOdooAddons
from .local_addons import LocalOdooAddons, LocalSubDirOdooAddons

_logger = logging.getLogger("install_addons")
_logger.setLevel(logging.INFO)


class AddonsFinder(object):
    """
    This class try o find all the Odoo dependency Addons from Environ Var
    The Odoo Addons can be declared in 2 ways.
    ADDONS_GIT_XXX or ADDONS_LOCAL_XXX
    In case of `ADDONS_GIT_XXX` then [GitOdooAddons][GitOdooAddons] is used to discover all other necessary Key
    In case of `ADDONS_LOCAL_XXX` then [LocalODooAddons][LocalODooAddons] is used.
    All supported types are defined in `types`

    Attributes:
        type: Contains all the supported Addons Type
    """

    types: List[Type[AddonsSuffix]] = [
        GitSubDirOdooAddons,
        LocalSubDirOdooAddons,
        GitOdooAddons,
        LocalOdooAddons,
    ]

    @staticmethod
    def get_addons(env_vars: Dict[str, str] = None):
        founded = {}
        for env_key in sorted(env_vars.keys()):
            addon = AddonsFinder.try_parse_key(env_key)
            if addon and env_vars.get(env_key) != str(False):
                _logger.info("Found depends %s from %s", addon, addon.identifier)
                founded[addon.identifier] = addon
        return set(founded.values())

    @staticmethod
    def _include_odoo_path(env_vars: Dict[str, str]) -> Dict[str, str]:
        """
        If `ODOO_PATH` is in `env_vars` then we add the native odoo addons path in env.
        With this function we handle the native Odoo addons like any other addons
        :param env_vars: the current env to parse
        :return: a copy of the env with ADDONS_LOCAL
        """
        result = dict(env_vars)
        if result.get("ODOO_PATH"):
            # In the new Docker image, we have a /odoo where odoo is cloned
            # inside /odoo/ooo and /odoo contains the conf file too
            odoo_path = path_join(result.get("ODOO_PATH"), "odoo")
            if "ADDONS_LOCAL_SRC_ODOO_ADDONS" not in env_vars:
                result["ADDONS_LOCAL_SRC_ODOO_ADDONS"] = path_join(odoo_path, "odoo", "addons")
            if "ADDONS_LOCAL_SRC_ODOO_ADDONS_ADDONS" not in env_vars:
                result["ADDONS_LOCAL_SRC_ODOO_ADDONS_ADDONS"] = path_join(odoo_path, "addons")
        return result

    @staticmethod
    def parse_env(env_vars: Dict[str, str] = None) -> Set[OdooAddonsDef]:
        """

        :param env_vars:
        :return:
        """
        env_vars = AddonsFinder._include_odoo_path(env_vars)
        return {f.extract(env_vars) for f in AddonsFinder.get_addons(env_vars)}

    @staticmethod
    def try_parse_key(env_key: str) -> Union[AddonsSuffix, None]:
        """

        :param env_key:
        :return:
        """
        for addon_type in AddonsFinder.types:
            addons: AddonsSuffix = addon_type(env_key)
            if addons.is_valid():
                _logger.info("Found depends %s from %s", addons, env_key)
                return addons
        return None


class AddonsRegistry(AddonsFinder):
    """
    Compatibility with 1.5.0
    @see AddonsFinder
    """

    def __init__(self):
        warnings.warn("Depcrecated, use AddonsFinder insted. will be removed in 2.0.0", DeprecationWarning)
        super(AddonsRegistry, self).__init__()


class OdooAddonsDefInstaller(OdooAddonsDef):
    def install(self):
        AddonsInstaller.install(self)


class AddonsInstaller:
    @staticmethod
    def exec_cmd(cmd: List[str], force_log=True):
        if not cmd:
            return 0
        if force_log:
            _logger.info(" ".join(cmd))
        return AddonsInstaller.exit_if_error(subprocess.Popen(cmd).wait())

    @staticmethod
    def exit_if_error(error_no: int) -> int:
        if error_no:
            sys.exit(error_no)
        return error_no

    @staticmethod
    def install_py_requirements(path_depot: str):
        path_requirements = path_join(path_depot, "requirements.txt")
        if path_exists(path_requirements):
            AddonsInstaller.exec_cmd(
                [sys.executable, "-m", "pip", "install", "-q", "--no-input", "-r", path_requirements], True
            )
        else:
            _logger.debug("No requirements.txt founded in %s", path_requirements)

    @staticmethod
    def install_npm_package(path_depot: str):
        path_npm = path_join(path_depot, "package.json")
        if path_exists(path_npm):
            AddonsInstaller.exec_cmd(["npm", "install", "-g", path_npm], True)
        else:
            _logger.debug("No package.json founded in %s", path_npm)

    @staticmethod
    def install(addons: OdooAddonsDef):
        _logger.info("install %s", addons)
        try:
            for cmd in addons.install_cmd():
                AddonsInstaller.exec_cmd(cmd, True)
            AddonsInstaller.install_py_requirements(addons.addons_path)
            AddonsInstaller.install_npm_package(addons.addons_path)
        except Exception as e:
            _logger.exception("Error", exc_info=e)
            sys.exit(1)
