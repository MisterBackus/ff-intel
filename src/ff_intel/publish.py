"""Push the generated board (and engine) to the live GitHub repo bots read."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

from ff_intel.config import GITHUB_REPO


ENGINE_PATHS = [
    "src/ff_intel",
    "tests",
    "pyproject.toml",
    "README.md",
    ".gitignore",
    # .github/workflows/board.yml needs the `workflow` OAuth scope; skip it
    # so a repo-scoped login can still publish the bot board.
]


def _run(cmd: list[str], cwd: Path, env: dict[str, str] | None = None) -> None:
    subprocess.run(cmd, cwd=cwd, check=True, env=env)


def _github_remote() -> str:
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        return f"https://x-access-token:{token}@github.com/{GITHUB_REPO}.git"
    return f"https://github.com/{GITHUB_REPO}.git"


def publish_github(root: str = "ff-intel", commit_message: str = "intel: update") -> None:
    workspace = Path.cwd()
    dest = Path(os.environ.get("FF_INTEL_GITHUB_DIR") or "/tmp/ff-intel-publish")
    if dest.exists():
        shutil.rmtree(dest)
    remote = _github_remote()
    _run(["git", "clone", "--depth", "1", remote, str(dest)], cwd=workspace)

    src_root = workspace / root
    dest_root = dest / "ff-intel"
    dest_root.mkdir(parents=True, exist_ok=True)
    (dest_root / "archive").mkdir(exist_ok=True)
    for name in ("latest.md", "latest.json"):
        shutil.copy2(src_root / name, dest_root / name)
    archive = src_root / "archive"
    if archive.exists():
        for path in archive.iterdir():
            if path.is_file():
                shutil.copy2(path, dest_root / "archive" / path.name)

    for rel in ENGINE_PATHS:
        src = workspace / rel
        if not src.exists():
            continue
        target = dest / rel
        if src.is_dir():
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(src, target)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, target)

    _run(["git", "add", "-A"], cwd=dest)
    staged = subprocess.run(["git", "diff", "--staged", "--quiet"], cwd=dest)
    if staged.returncode == 0:
        print(f"github.com/{GITHUB_REPO}: no board changes")
        return
    _run(["git", "config", "user.name", "ff-intel-bot"], cwd=dest)
    _run(["git", "config", "user.email", "ff-intel-bot@users.noreply.github.com"], cwd=dest)
    _run(["git", "commit", "-m", commit_message], cwd=dest)
    _run(["git", "push", "origin", "HEAD:main"], cwd=dest)
    print(f"published {commit_message} to github.com/{GITHUB_REPO}")
