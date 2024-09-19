import os
import re
import shutil


def fix_whitespace(filename: str) -> None:
    """Fix whitespace from Jinja2 template generated file

    Notes
    -----
    - Fixes whitespace when intermediate if-templates insert newlines when not active.
    - Fixes trailing whitespace.

    Parameters
    ----------
    filename : str
        Relative path of file to fix (relative to generated project root)
    """    
    with open(filename, "r") as file:
        content = file.read()
        
    content = re.sub(r"\n{3,}", "\n\n", content)
    
    with open(filename, "w") as file:
        file.write(content.strip())


def remove_mlflow_folder() -> None:
    """Remove mlflow folder from generated project root"""
    shutil.rmtree("./mlflow/")


def remove_tests_folder() -> None:
    """Remove tests folder from generated project root"""
    shutil.rmtree("./tests/")


def remove_pyproject_toml_file() -> None:
    """Remove pyproject.toml file from generated project root"""
    os.remove("./pyproject.toml")


def remove_pyrightconfig_json_file() -> None:
    """Remove pyrightconfig.json file from generated project root"""
    os.remove("./pyrightconfig.json")


def main() -> None:
    """Perform post-generation cleanup based on Cookiecutter template variables"""
    # Fix whitespace for all files that use Jinja2 templates.
    fix_whitespace("./Makefile")
    fix_whitespace("./docker/.env")
    fix_whitespace("./docker/docker-compose.yml")
    fix_whitespace("./{{ cookiecutter.__package_name }}/Dockerfile")
    fix_whitespace("./{{ cookiecutter.__package_name }}/requirements.txt")

    # Remove MLFlow folder if unused.
    if "{{ cookiecutter.experiment_tracker }}" != "mlflow":
        remove_mlflow_folder()

    print("{{ cookiecutter.setup_devtools }}") 
    # Remove tests folder and devtools configuration file if unused.
    if not bool("{{ cookiecutter.setup_devtools }}"):
        remove_tests_folder()
        remove_pyproject_toml_file()
        remove_pyrightconfig_json_file()


if __name__ == "__main__":
    main()