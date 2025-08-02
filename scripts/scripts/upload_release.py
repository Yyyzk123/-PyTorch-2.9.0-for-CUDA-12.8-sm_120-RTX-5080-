#!/usr/bin/env python3
"""
upload_release.py – Upload a wheel (or any asset) to a GitHub Release.

Example:
    python upload_release.py --tag v2.9.0-sm120 \
        --whl dist/torch-2.9.0a0+gitc665594-cp310-cp310-linux_x86_64.whl

Prerequisites:
    pip install PyGithub tqdm

Environment variables:
    GITHUB_TOKEN      Personal Access Token with `repo` scope.
    GITHUB_REPOSITORY Repository slug ("<owner>/<repo>"). If omitted, inferred from `git remote get-url origin`.
"""
import argparse
import hashlib
import os
import subprocess
import sys
from pathlib import Path
from github import Github, GithubException  # type: ignore
from tqdm import tqdm  # type: ignore

def sha256(path: Path) -> str:
    """Compute SHA-256 of a file in chunks."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def infer_repository() -> str:
    """Return "owner/repo" from the local git origin URL."""
    try:
        url = (
            subprocess.check_output(["git", "remote", "get-url", "origin"], text=True)
            .strip()
            .removesuffix(".git")
        )
        if url.startswith("git@"):
            return url.split(":", 1)[-1]
        if url.startswith("https://"):
            return "/".join(url.split("/")[-2:])
    except Exception:
        raise SystemExit("Cannot infer GitHub repository. Set GITHUB_REPOSITORY env var or use --repo.")

def upload_asset(release, asset_path: Path):
    """Upload or replace an asset in a release, with progress bar."""
    for asset in release.get_assets():
        if asset.name == asset_path.name:
            print(f"Deleting existing asset {asset.name} ...")
            asset.delete_asset()
            break
    print(f"Uploading {asset_path.name} ({asset_path.stat().st_size / 1e6:.1f} MB)...")
    file_size = asset_path.stat().st_size
    with open(asset_path, "rb") as fp:
        data = fp.read()
    with tqdm(total=file_size, unit='B', unit_scale=True, desc="Upload") as pbar:
        release.upload_asset(
            path=str(asset_path),
            label=asset_path.name,
            content_type="application/octet-stream"
        )
        pbar.update(file_size)
    print("Upload complete.")

def main():
    parser = argparse.ArgumentParser(description="Upload a wheel to GitHub Release, from first principles.")
    parser.add_argument("--tag", required=True, help="Release tag (e.g. v2.9.0-sm120)")
    parser.add_argument("--whl", required=True, type=Path, help="Path to wheel file")
    parser.add_argument("--repo", help="GitHub repo <owner>/<repo> (default: infer)")
    parser.add_argument("--draft", action="store_true", help="Create release as draft (default: published)")
    parser.add_argument("--body", default="Automated build for {tag}\n\nSHA-256: {sha}", help="Release body (default: auto)")
    args = parser.parse_args()

    token = os.getenv("GITHUB_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN not set. Create PAT with repo scope: https://github.com/settings/tokens")

    repo_slug = args.repo or os.getenv("GITHUB_REPOSITORY") or infer_repository()
    gh = Github(token)
    try:
        repo = gh.get_repo(repo_slug)
    except GithubException as e:
        sys.exit(f"Repo access failed: {e.data.get('message')} (Check token permissions or repo name).")

    sha = sha256(args.whl)
    print(f"SHA-256: {sha}")

    try:
        release = repo.get_release(args.tag)
        print(f"Found existing release {args.tag}.")
    except GithubException:
        print(f"Creating release {args.tag} ...")
        body = args.body.format(tag=args.tag, sha=sha)
        release = repo.create_git_release(
            tag=args.tag,
            name=args.tag,
            message=body + "\nPowered by open collaboration.",
            draft=args.draft,
            prerelease=False,
        )

    upload_asset(release, args.whl)
    print(f"Release URL: {release.html_url}")
    print("Success. The wheel is now available for download.")

if __name__ == "__main__":
    main()
