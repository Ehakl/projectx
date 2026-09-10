import os
import datetime
import subprocess

# Automatically use the directory where this script is located
REPO_PATH = os.path.dirname(os.path.abspath(__file__))

def make_commit():
    os.chdir(REPO_PATH)
    
    # Optionally update a file with a timestamp
    with open("log.txt", "a") as f:
        f.write(f"Commit on {datetime.datetime.now()}\n")
        
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"Auto-commit {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"])
    subprocess.run(["git", "push", "origin", "main"])

if __name__ == "__main__":
    make_commit()
