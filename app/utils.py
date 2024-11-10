import tomllib


def read_pyproject_toml():
    with open("./pyproject.toml", "rb") as file:
        return tomllib.load(file)
