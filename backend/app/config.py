import logging
import sys
from functools import cached_property
from os import environ
from os.path import abspath, exists, isfile

from yaml import YAMLError, safe_load

# configure logging with filename, function name and line numbers
logging.basicConfig(
    datefmt="%I:%M:%S %p %Z",
    format="%(levelname)s [%(asctime)s - %(filename)s:%(lineno)s::%(funcName)s]\t%(message)s",
    stream=sys.stdout,
    level=logging.INFO,
)
log = logging.getLogger(__name__)


class Settings:
    def __init__(self):
        secrets_filename = "/etc/iamp/.secrets.yml"
        if isfile(".secrets.yml"):
            secrets_filename = ".secrets.yml"
        else:
            secrets_filename = "backend/.secrets.yml"

        secrets = Settings._get_secrets(secrets_filename)

        self.config = dict()
        self.config.update(secrets)

    @cached_property
    def in_production(self) -> bool:
        return environ.get("RUNTIME_MODE") == "production"

    @cached_property
    def pg_connection_uri(self) -> str:
        pg_config = self.config["postgres"]
        user: str = pg_config["username"]
        pwd: str = pg_config["password"]
        db = "iam-playspace"

        if self.in_production:
            return f"postgresql://{user}:{pwd}@postgres:5432/{db}"

        return f"postgresql://{user}:{pwd}@localhost:15432/{db}"

    @cached_property
    def redis_connection_uri(self) -> str:
        pwd: str = self.config["redis"]["password"]
        if self.in_production:
            return f"redis://redis:6379?password={pwd}"

        return f"redis://localhost:16379?password={pwd}"

    @property
    def app_secret(self) -> str:
        return self.config["app"]["secret"]

    @staticmethod
    def _invalid_config_exit(message: str):
        log.error(
            "Unable to start due to error %s while parsing secrets file. Exiting...",
            message,
        )
        sys.exit(1)

    @staticmethod
    def _get_secrets(secrets_filename: str) -> dict:  # type: ignore

        secrets_filename = abspath(secrets_filename)
        if not exists(secrets_filename) or not isfile(secrets_filename):
            Settings._invalid_config_exit(
                "Missing secrets file %s" % (secrets_filename)
            )

        try:
            with open(secrets_filename, "r") as f:
                secrets = safe_load(f)
                log.info(
                    f"secrets read from file {secrets_filename} with secrets: {secrets.keys()}"
                )
                return secrets

        except YAMLError as err:
            Settings._invalid_config_exit(
                f"Got exception when reading invalid YAML in {secrets_filename} {err}"
            )
        except Exception as e:
            Settings._invalid_config_exit(
                f"Unknown error {e} reading secrets file {secrets_filename}"
            )


settings = Settings()

if __name__ == "__main__":
    print(settings.pg_connection_uri)
