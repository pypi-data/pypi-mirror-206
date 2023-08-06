import os
from contextlib import contextmanager
from pathlib import Path
from typing import Literal, Optional

from pydantic import BaseSettings, Field, SecretStr, root_validator, validator
from rich import print
from rich.text import Text

import chatcell

# a configurable env file location
ENV_FILE = Path(os.getenv("CHATCELL_ENV_FILE", "~/.chatcell/.env")).expanduser()
ENV_FILE.parent.mkdir(parents=True, exist_ok=True)
ENV_FILE.touch(exist_ok=True)


class Settings(BaseSettings):
    """Chatcell settings"""

    class Config:
        env_file = ".env", str(ENV_FILE)
        env_prefix = "CHATCELL_"
        validate_assignment = True

    def export_to_env_file(self, f: str = None):
        with open(f or self.Config.env_file[0], "w") as env_file:
            for field_name, value in self.dict().items():
                env_key = f"{self.Config.env_prefix}{field_name.upper()}"
                env_value = (
                    str(value)
                    if not isinstance(value, SecretStr)
                    else value.get_secret_value()
                )
                env_file.write(f"{env_key}={env_value}\n")

    home: Path = Path("~/.chatcell").expanduser()
    test_mode: bool = True

    # LOGGING
    verbose: bool = False
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    log_console_width: Optional[int] = Field(
        None,
        description=(
            "Chatcell will auto-detect the console width when possible, but in deployed"
            " settings logs will assume a console width of 80 characters unless"
            " specified here."
        ),
    )
    rich_tracebacks: bool = Field(False, description="Enable rich traceback formatting")

    # OPENAI
    openai_model_name: str = "gpt-3.5-turbo"
    openai_model_temperature: float = 0.8
    openai_model_max_tokens: int = 1250
    openai_api_key: SecretStr = Field(
        "", env=["CHATCELL_OPENAI_API_KEY", "OPENAI_API_KEY"]
    )

    # API
    api_base_url: str = "http://127.0.0.1"
    api_port: int = 4200
    api_reload: bool = Field(
        False,
        description=(
            "If true, the API will reload on file changes. Use only for development."
        ),
    )

    @validator("openai_api_key")
    def warn_if_missing_api_keys(cls, v, field):
        if not v:
            print(
                Text(
                    f"WARNING: `{field.name}` is not set. Some features may not work.",
                    style="red",
                )
            )
        return v

    @root_validator
    def test_mode_settings(cls, values):
        if values["test_mode"]:
            values["log_level"] = "DEBUG"
            values["verbose"] = True
            # remove all model variance
            values["openai_model_temperature"] = 0.0
            # use 3.5 by default
            values["openai_model_name"] = "gpt-3.5-turbo"

        return values

    def __setattr__(self, name, value):
        result = super().__setattr__(name, value)
        # update log level on assignment
        if name == "log_level":
            chatcell.logging.setup_logging()
        return result


settings = Settings()


@contextmanager
def temporary_settings(**kwargs):
    old_settings = settings.dict()
    settings.__dict__.update(kwargs)
    try:
        yield
    finally:
        settings.__dict__.clear()
        settings.__dict__.update(old_settings)
