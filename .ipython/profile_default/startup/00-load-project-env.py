"""Load project .env when IPython/Jupyter starts (any notebook cwd under the repo)."""

import sys
from pathlib import Path


def _project_root() -> Path | None:
    cwd = Path.cwd().resolve()
    for directory in (cwd, *cwd.parents):
        if (directory / "pyproject.toml").is_file() and (directory / ".env").is_file():
            return directory
    return None


try:
    root = _project_root()
    if root is not None:
        root_str = str(root)
        if root_str not in sys.path:
            sys.path.insert(0, root_str)
        from env_loader import load_project_env

        load_project_env(start=root)
except Exception:
    pass
