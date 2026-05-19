"""
Load API keys and other secrets from the project-root .env file.

Development uses .env in the repository root (see .env.example).
Production can inject the same variable names via systemd, shell export, etc.
Existing environment variables are never overwritten (override=False).
"""

from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv

# Repository root (directory containing pyproject.toml)
PROJECT_ROOT = Path(__file__).resolve().parent
ENV_FILE = PROJECT_ROOT / ".env"


def find_project_root(start: Path | None = None) -> Path | None:
    """Walk parents from *start* until we find pyproject.toml and .env."""
    start = (start or Path.cwd()).resolve()
    for directory in (start, *start.parents):
        if (directory / "pyproject.toml").is_file() and (directory / ".env").is_file():
            return directory
    return None


def load_project_env(*, start: Path | None = None) -> bool:
    """
    Load .env from the project root if present.

    Returns True when a .env file was found and loaded.
    """
    root = find_project_root(start) or PROJECT_ROOT
    env_path = root / ".env"
    if not env_path.is_file():
        return False
    load_dotenv(env_path, override=False)
    return True
