__all__ = ["ChatcellHandler", "run", "get_bot"]

# from importlib.metadata import version as _get_version

# load env vars
from dotenv import load_dotenv as _load_dotenv

from chatcell.base import ChatcellHandler
from chatcell.config import settings
from chatcell.logging import get_logger
from chatcell.server import get_bot, run

_load_dotenv()

# __version__ = _get_version("chatcell")
