# CIS400 - Term Project


## Getting started

### Project Dependencies
You will need **git**, a **GitHub** account, **python !(3.10)!**, **pipenv** and **vscode\*** to get started with the project
1. Install python 3.10 (this project uses 3.10)
1. Install **git**
   1. Windows
      1. Download the installer from the git website: https://git-scm.com/download/win and follow the directed steps (I used the default)
      2. Run`git --version` in the command line
   2. Mac should already have git installed
2. . Install **pipenv**
   1. Mac/Windows
      1. Open a terminal/powershell and run `pip -V` to see if you have pip installed
      2. If pip is installed then run `pip install --user pipenv`
      3. Run` pipenv --version` to check that the installation worked
         1. (if this did not work you may need to run pipenv)




## Git

### Git Setup

#### Step 1: Generating an SSH Key Pair and Adding it to the ssh-agent
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

#### Step 2: Adding the SSH Key to Your GitHub Account
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

#### Step 3: Clone the repository

### Git Workflow
We are using Git to share and colloborate on the same project at the same time. If you haven't used git before you may wan't to watch a tutorial on youtube to familiarize youself with the tool but below is a explanation of how we will be using git.



#### Create and Checkout a New Branch

Choose a descriptive name for your branch based on the feature or bugfix you are working on. For example, if you are working on a login feature, you could name your branch feature-login.

**Using VSCode's Source Control:**

1. Open the Source Control tab on the left sidebar
2. Click on the "..." menu at the top of the tab
3. Select "Create Branch" from the menu
4. Enter your chosen branch name and press Enter
   


#### Make Changes to the Branch and Periodically Sync to GitHub

Edit the codebase, commit your changes with meaningful messages, and push your changes to the remote repository.

Using VSCode's Source Control
1. Open the Source Control tab on the left sidebar
2. Review your changes and stage them by clicking the "+" icon next to each file
3. Enter a commit message and click the checkmark icon to commit
4. Click the "..." menu at the top of the tab and select "Push" to sync your changes to GitHub


Create a Pull Request on GitHub

Go to the repository's GitHub page
Click on the "Pull Requests" tab
Click the "New Pull Request" button
Choose the base branch (usually "main") and the compare branch (your working branch)
Review your changes and click "Create Pull Request"
Add a title and description for the pull request, then click "Create Pull Request" again

Merge the Branch to the Main Branch
Once your pull request has been reviewed and approved by your teammates, merge your changes into the main branch.

On the pull request page, click "Merge Pull Request"
Confirm the merge by clicking "Confirm Merge"
Optionally, delete the merged branch by clicking "Delete Branch"

Start Over with a New Branch
After successfully merging your changes, you can start the process over with a new branch for the next feature or bugfix. Remember to update your local main branch by pulling the latest changes from the remote repository before creating a new branch.

Using VSCode's Source Control:

Switch to the main branch by clicking the current branch name in the lower left corner and selecting "main"
Open the Source Control tab on the left sidebar
Click the "..." menu at the top of the tab and select "Pull" to update your local main branch
Using Git CLI:
