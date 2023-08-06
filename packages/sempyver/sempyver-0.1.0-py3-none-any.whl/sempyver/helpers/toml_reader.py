"""
Just a TOML reader
"""
from functools import lru_cache
from pathlib import Path
import toml


@lru_cache
def read_toml() -> dict:
    """Read the pyproject.toml file from the origin path.

    Returns:
        the dict with all the information coming from the `pyproject.toml` for the
        sempyver project.
    """
    pyproject_info: dict = {}
    try:
        with open(str(Path().absolute())+"/pyproject.toml", encoding="utf-8") as pyproject:
            pyproject_info = toml.load(pyproject)
    except FileNotFoundError as error:
        raise FileNotFoundError(
            "Could not find a pyproject.toml in this repository.") from error
    # Now, check if it has the `sempyver` on the project
    if "sempyver" not in pyproject_info["tool"]:
        raise ValueError(
            "There's no `sempyver` configuration in the `pyproject.toml` file.")
    # If everything is fine, return the sempyver part
    return pyproject_info["tool"]["sempyver"]
