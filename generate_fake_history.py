import os
import random
import subprocess
from datetime import datetime, timedelta

REPO_PATH = "./"
REPO_URL = "git@mitm.github.com:PenRomain/PenRomain.git"
COMMIT_MESSAGE = "Random commit"
AUTHOR_NAME = "PenRomain"
AUTHOR_EMAIL = "romandreevich@icloud.com"
COMMITS_PER_DAY = (1, 5)

if not os.path.exists(REPO_PATH):
    subprocess.run(["git", "clone", REPO_URL, REPO_PATH])

os.chdir(REPO_PATH)

subprocess.run(["git", "pull"])

start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)
current_date = start_date

while current_date <= end_date:
    num_commits = random.randint(*COMMITS_PER_DAY)
    for _ in range(num_commits):
        random_time = current_date + timedelta(
            hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59)
        )
        commit_date = random_time.strftime("%Y-%m-%d %H:%M:%S")

        with open("README.md", "a") as readme_file:
            readme_file.write(f"Random commit on {commit_date}\n")

        env = {
            "GIT_COMMITTER_DATE": commit_date,
            "GIT_AUTHOR_DATE": commit_date,
            "GIT_AUTHOR_NAME": AUTHOR_NAME,
            "GIT_AUTHOR_EMAIL": AUTHOR_EMAIL,
        }
        subprocess.run(["git", "add", "README.md"], env=env)
        subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], env=env)

    current_date += timedelta(days=1)

subprocess.run(["git", "push", "origin", "main"])

print("Random commit history for 2021 has been added to the repository.")
