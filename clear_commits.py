import os
import subprocess

REPO_PATH = "./"
REPO_URL = "git@mitm.github.com:PenRomain/PenRomain.git"

def reset_repository():
    if not os.path.exists(REPO_PATH):
        subprocess.run(["git", "clone", REPO_URL, REPO_PATH])

    os.chdir(REPO_PATH)
    subprocess.run(["git", "pull"])

    subprocess.run(["git", "checkout", "--orphan", "new_branch"])

    subprocess.run(["git", "rm", "-rf", "."])

    with open("RESET_HISTORY.txt", "w") as file:
        file.write("Reset repository history")
    subprocess.run(["git", "add", "RESET_HISTORY.txt"])
    subprocess.run(["git", "commit", "-m", "Reset repository history"])

    subprocess.run(["git", "branch", "-D", "main"])
    subprocess.run(["git", "branch", "-m", "main"])

    subprocess.run(["git", "reflog", "expire", "--expire=now", "--all"])
    subprocess.run(["git", "gc", "--prune=now", "--aggressive"])

    subprocess.run(["git", "push", "--force", "--set-upstream", "origin", "main"])

    print("Repository history has been completely reset.")

reset_repository()
