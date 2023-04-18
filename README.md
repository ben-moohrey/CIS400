# CIS400 - Term Project

## Getting started

### Project Dependencies
You will need **git**, a **GitHub** account, **python 3.10**, **pipenv** and **vscode** to get started with the project. You can skip the steps if you know you have everything installed already.

1. Install python 3.10 (this project uses 3.10 please make sure you have this version installed to your computer)
2. Install **git**
   1. Windows
      1. Download the installer from https://git-scm.com/download/win and follow the directed steps (I used the default)
      2. Run`git --version` in the command line
   2. Mac should already have git installed
3. Install **pipenv**
   1. Mac/Windows
      1. Open a terminal/powershell and run `pip -V` to see if you have pip installed
      2. If pip is installed then run `pip install --user pipenv`
      3. Run` pipenv --version` to check that the installation worked
         1. (if this did not work you may need to run pipenv)

## Setup Git

### Step 1: Generating an SSH Key Pair and Adding it to the ssh-agent
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent


### Step 2: Adding the SSH Key to Your GitHub Account
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

### Step 3: Clone the repository
In a terminal/powershell navigate to the directory you want your local copy of the code base to be and then enter: `git clone git@github.com:ben-moohrey/CIS400.git`.

If cloning the repository gives an error then your key was not setup correctly.

## Install dependencies
1. Open terminal/powershell 
2. `cd` into the cloned directory

**Mac**
```bash
pipenv install
```

**Windows** (if pipenv is not in your PATH environment variable you may need to use this command)
```bash
python -m pipenv install
```

## Running the project
**Mac**
```bash
pipenv run main
```
**Windows** (if pipenv is not in your PATH environment variable you may need to use this command)
```bash
python -m pipenv run main
```

## Git Workflow
We are using Git to share and colloborate on the same project at the same time. If you haven't used git before you may wan't to watch a tutorial on youtube to familiarize youself with the tool but below is a explanation of how we will be using git with VSCode.

#### Step 1: Create and Checkout a New Branch

Choose a descriptive name for your branch based on the feature or bugfix you are working on. For example, if you are working on a login feature, you could name your branch feature-login.

1. Open the Source Control tab on the left sidebar
2. Click on the "..." menu at the top of the tab
3. Select "Create Branch" from the menu
4. Enter your chosen branch name and press Enter
   
#### Step 2: Make Changes to the Branch and Periodically Sync to GitHub

Edit the codebase, commit your changes with meaningful messages, and push your changes to the remote repository.

1. Open the Source Control tab on the left sidebar
2. Review your changes and stage them by clicking the "+" icon next to each file (or just press commit and then yes when the pop-up shows)
3. Enter a commit message and click the checkmark icon to commit
4. Click the button where the commit button used to be to "push and pull" from GitHub 
5. Repeat until you are done with the change

#### Step 3: Create a Pull Request on GitHub

After completing your feature or bugfix, create a pull request on GitHub to merge your changes into the main branch.

1. Go to the repository's GitHub page
2. Click on the "Pull Requests" tab
3. Click the "New Pull Request" button
4. Choose the base branch (usually "main") and the compare branch (your working branch)
5. Review your changes and click "Create Pull Request"
6. Add a title and description for the pull request, then click "Create Pull Request" again

#### Step 4: Merge the Branch to the Main Branch

Once your pull request has been reviewed and approved by your teammates, merge your changes into the main branch.

1. On the pull request page, click "Merge Pull Request"
2. Confirm the merge by clicking "Confirm Merge"
3. Optionally, delete the merged branch by clicking "Delete Branch"

#### Step 5: Start Over with a New Branch

After successfully merging your changes, you can start the process over with a new branch for the next feature or bugfix. Remember to update your local main branch by pulling the latest changes from the remote repository before creating a new branch.

1. Switch to the main branch by clicking the current branch name in the lower left corner and selecting "main"
2. Open the Source Control tab on the left sidebar
3. Click the "..." menu at the top of the tab and select "Pull" to update your local main branch

