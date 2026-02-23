

# Clean Slate
If you want your entire local folder to exactly match the GitHub repository and you don't care about any local changes you've made, use a hard reset.

Warning: This will permanently delete any uncommitted local code.

## 1. Fetch the latest data from the server
git fetch origin main

## 2. Force your local branch to match the server exactly
git reset --hard origin/main




# hardcore reset
git clean -fd
-f (force): Required because Git won't delete untracked files unless you explicitly tell it to.

-d: This tells Git to also remove untracked directories.

If you want to be extra thorough:
Sometimes there are files ignored by your .gitignore (like local settings or temporary build files) that you still want to get rid of. To wipe everything that isn't in the GitHub repo:

git clean -fdx
(The -x flag tells it to ignore the .gitignore rules and delete those files too.)



Pro-Tip: The "Dry Run"
git clean -nfd





