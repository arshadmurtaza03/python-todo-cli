# Python To-Do CLI

A beginner-friendly command-line To-Do List application built with Python. This repository is the practical project used in my **Git and GitHub** video assignment.

The project demonstrates how to create a local Git repository, track code changes, create meaningful commits, use `.gitignore`, publish code to GitHub, work with a feature branch, and merge changes using a Pull Request.

> **Video walkthrough:** The public/unlisted video explanation is submitted in the course task's **Video** field.

## Project features

- Add tasks from the terminal
- View saved tasks
- Mark a task as completed
- Save task data locally in `tasks.txt`
- Keep local task data out of GitHub with `.gitignore`
- Use a feature branch and Pull Request for the task-completion feature

## Technologies used

- Python 3
- Git
- GitHub
- Visual Studio Code

## Project structure

```text
python-todo-cli/
├── app.py         # Command-line To-Do List application
├── README.md      # Project documentation
├── .gitignore     # Files and folders Git should ignore
└── tasks.txt      # Created while the app runs; intentionally not tracked
```

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/arshadmurtaza03/python-todo-cli.git
cd python-todo-cli
```

### 2. Run the application

```bash
python app.py
```

If `python` is not recognized on Windows, try:

```bash
py app.py
```

### 3. Use the menu

```text
1. View tasks
2. Add task
3. Mark task as completed
4. Exit
```

The app creates `tasks.txt` automatically after a task is added. This file is intentionally ignored because it contains local user data.

## Git and GitHub concepts

| Topic | Simple explanation |
|---|---|
| Git | A version-control tool that tracks changes in a project on a local computer. |
| GitHub | An online platform for hosting Git repositories, sharing code, and collaborating. |
| Commit | A saved snapshot of selected project changes. |
| Branch | A separate line of work for a feature or experiment. |
| Pull Request | A request to review and merge changes from one branch into another. |

## Commands demonstrated

This project and its video demonstrate the following essential Git and GitHub commands in a practical workflow.

| Command | Purpose in this project |
|---|---|
| `git init` | Initialized the local Git repository. |
| `git status` | Checked untracked, modified, and staged files. |
| `git add README.md` | Staged one specific file. |
| `git add .` | Staged all intended project changes. |
| `git commit -m "message"` | Saved meaningful snapshots of the project. |
| `git log --oneline` | Viewed a concise commit history. |
| `git diff` | Reviewed code and documentation changes before committing. |
| `git branch -M main` | Set the primary branch name to `main`. |
| `git remote add origin <repository-url>` | Connected the local repository to GitHub. |
| `git push -u origin main` | Published the local `main` branch to GitHub. |
| `git switch -c add-complete-task-feature` | Created and switched to a feature branch. |
| `git push -u origin add-complete-task-feature` | Published the feature branch to GitHub. |
| `git switch main` | Returned to the main branch. |
| `git pull origin main` | Downloaded merged changes from GitHub. |
| `git clone <repository-url>` | Downloaded a complete existing GitHub repository locally. |

## Practical workflow followed

```text
Create local Python project
        ↓
Initialize Git repository
        ↓
Track files and create commits
        ↓
Use .gitignore for local task data
        ↓
Create an empty GitHub repository
        ↓
Connect remote and push main branch
        ↓
Create feature branch
        ↓
Add and test task-completion feature
        ↓
Commit and push feature branch
        ↓
Open and merge Pull Request
        ↓
Pull latest main branch changes
        ↓
Clone repository to demonstrate downloading an existing project
```

## GitHub workflow evidence

The repository history shows a real incremental workflow rather than a single upload:

- `docs: add project README`
- `feat: add basic Python todo application`
- `docs: add run instructions`
- `feat: add task completion option`
- Merged Pull Request: `#1 feat: add task completion option`

## Learning outcomes

After completing this project, I can:

- Explain the difference between Git and GitHub
- Initialize and manage a local Git repository
- Check status, stage changes, create commits, and inspect history
- Use `.gitignore` to avoid tracking local or sensitive files
- Push a local project to GitHub
- Create and work with a feature branch
- Create, review, and merge a Pull Request
- Pull updates and clone an existing GitHub repository

## Author

**Arshad Murtaza**

- GitHub: [@arshadmurtaza03](https://github.com/arshadmurtaza03)

---

If this project helped you, consider giving the repository a star.