# GitHub Streak Automator 🟩

A simple Python script to automate GitHub contributions. 

## How it works
When executed, this script:
1. Appends the current timestamp to `log.txt` (creating a file change).
2. Runs `git add .`
3. Runs `git commit` with the current timestamp.
4. Pushes the changes to GitHub.

## Usage
Run the script manually or set it up with a cron job / Windows Task Scheduler to keep your contribution streak alive.

```bash
python auto_commit.py
```
