from importlib.machinery import PathFinder
from pathlib import Path
from typing import Optional

from pydantic import BaseSettings
from pydantic.color import Color


class Settings(BaseSettings):
    SIGNOUT_URL: Optional[str] = None
    CURRENT_PACKAGE = __name__.split(".")[0]
    BASE_PATH: str = str(Path(PathFinder().find_spec(CURRENT_PACKAGE).origin).parent)  # type: ignore
    DATA_DIR: str = str(Path.cwd() / "appdata")
    """Root directory for storing app data"""
    APP_TAG_TEXT: str = "Development"
    """text that will appear next the application logo"""
    APP_TAG_BACKGROUND: Color = Color("#00a9ce")
    """background colour of the APP_TAG_TEXT"""
    DEBUG: bool = False
    """Enable debug information in the app"""
    DEBUG_MOCK_SESSION: bool = False
    """Mock the session headers returned when deployed to AWS"""
    USE_COGNITO: bool = False
    """Use AWS Cognito for Auth"""
    COGNITO_COOKIE: str = "AWSELBAuthSessionCookie"
    """If set cookies with this prefix will be deleted on signout"""
    COGNITO_GROUPS: str = "app-fracg"
    """One of these comma separated groups must be present in the user's `cognito:groups`"""
    NO_ACCESS_MSG: str = "Error: You do not have permission to use this app."
    """Error message displayed when a user doesn't have permission to use the app"""
    STREAMLIT_SERVER_BASE_URL_PATH: str = ""
    """The base path for the URL where Streamlit should be served from"""
    MONGO_CONNECTION_STRING: str = ""
    """Mongo DB connection string"""
    DATABASE_NAME: str = ""
    """Mongo DB Database Name"""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
