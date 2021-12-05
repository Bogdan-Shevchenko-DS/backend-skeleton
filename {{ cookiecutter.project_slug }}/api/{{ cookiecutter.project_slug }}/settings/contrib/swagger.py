from ..environment import env


SWAGGER_SETTINGS = {
    "DEFAULT_API_URL": env.str("{{ cookiecutter.env_prefix }}BASE_API_URL", default="https://{{ cookiecutter.domain_name }}"),
}
