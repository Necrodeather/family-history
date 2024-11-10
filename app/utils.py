import tomllib
from typing import Any


def read_pyproject_toml() -> dict[str, Any]:
    with open("./pyproject.toml", "rb") as file:
        return tomllib.load(file)
