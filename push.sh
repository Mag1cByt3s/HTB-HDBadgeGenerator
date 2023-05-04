#!/bin/bash

# Change directory to the git repository
cd /home/generator/HTB-HDBadgeGenerator

# Add the files to git
git add *

# Commit the changes
git commit --allow-empty -am "Update 878647.html"

# Push the changes to the remote repository
git push -u origin main
