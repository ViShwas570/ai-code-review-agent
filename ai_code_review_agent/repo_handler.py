
import os
from git import Repo

def clone_repo(repo_url, clone_dir="cloned_repo"):
    if os.path.exists(clone_dir):
        return clone_dir
    Repo.clone_from(repo_url, clone_dir)
    return clone_dir
