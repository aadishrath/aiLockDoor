# aiLockDoor
Senior Project: facial recognition on a door lock

DO NOT push changes to master branch for any reason whatsoever. Before doing anything, follow few steps:
  - git pull > it pulls any commits made by anyone and updates your code
  - now either create new branch or resuse the one created before by following respective steps

steps to follow to create new branch
  - git branch > shows list of branches are in the repo and which one you're on
  - git checkout -b myNewBranch > -b tells git to create a branch with name "myNewBranch"
  whatever changes are made hereon are committed to your branch. Once pushed, it'll merge into "master" branch. 

If you've created a branch before and want to use the same:
  - git branch
  - git checkout branchName

Once ready to commit your changes:
  - git add .
  - git commit -m "summarized version of changes. Max of 30 char"
  - git push
