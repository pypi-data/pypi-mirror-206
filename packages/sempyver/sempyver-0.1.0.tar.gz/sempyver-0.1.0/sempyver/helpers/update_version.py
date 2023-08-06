"""
Update the package version using the 
"""
from functools import lru_cache
from typing import Dict, IO
from pathlib import Path
# Local imports
from sempyver.helpers.toml_reader import read_toml
from sempyver.cli_application.utilities.tags_for_change import VERSION_UPDATE


def update_version(change: str) -> str:
    """Update the version to write it on the changelog.

    Args:
        change (str): Type of change.

    Returns:
        str: New version
    """
    version: str = find_version()
    # Use the change list
    position_to_change: int = VERSION_UPDATE[change]
    version_numbers: Dict[str, str] = {
        f"Pos. {i}": v for i, v in enumerate(version.split("."))}
    new_version: Dict[str, str] = {}
    _position = f"Pos. {position_to_change}"
    already_upgrade_version: bool = False
    for position, number_of_version in version_numbers.items():
        if position != _position and already_upgrade_version is False:
            new_version[position] = number_of_version
        elif position == _position:
            new_version[position] = f"{int(number_of_version)+1}"
            already_upgrade_version = True
        else:
            new_version[position] = "0"
    # Return the new version
    return ".".join(version for version in new_version.values())


@lru_cache
def read_version_file(mode: str = "r") -> IO:
    """Read the version from the path specified in the `pyproject.toml`

    Args:
        How to open the file.

    Returns:
        Opened file.
    """
    # From the `pyproject.toml`, get the root path
    root_path = str(Path().absolute())+"/"
    # From there, find the file path that the developer has set in the `pyproject.toml`
    toml = read_toml()
    if "version_file_path" in toml:
        version_file_path = toml["version_file_path"]
    else:
        raise ValueError(
            "Could not find the `version_file_path` configuration in the `pyproject.toml`.")
    # Return the version file
    return open(root_path+version_file_path, mode=mode, encoding="utf-8")


def find_version() -> str:
    """Find the version in the given version file path.

    Returns:
        The major.minor.patch version number
    """
    version_file = read_version_file().readlines()
    version = "\n".join(line for line in version_file).rsplit(
        "=", maxsplit=1)[-1].strip(' ').replace("\"", "").replace("'", "")
    # From there, return the version if we could find one.
    if version is None:
        raise ValueError(
            "Could not find the major.minor.patch version in the given path.")
    # Return the version
    return version


def update_version_file(updated_version: str) -> None:
    """Update the version file given a new updated version

    Args:
        updated_version (str): New major.minor.patch version
    """
    lines = read_version_file().readlines()
    for i, line in enumerate(lines):
        if "=" in line:
            lines[i] = f"{line.split('=')[0]}= \"{updated_version}\"\n"
    # Now, open a file in write mode
    read_version_file(mode="w").writelines(lines)
