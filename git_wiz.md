# How To make another github branch purely for pushing to Gradescope
1.  Create a new branch
g brach submission

2. move to new branch
g checkout submission

3. Add files/directories you want to submit like so:
g add ...

- if you did g add . or g add -A congrats now you need to go get rid of unwanted files and dirs w/
rm -rf unwanted/dir/
rm unwanted/file/

4. sync with online github acc with 
git commit -m "Initial commit on new branch"
git push -u origin <branch>

**Now you are done with setting up the branch!**

## Update submission branch with new updated content etc
1. this replaces the current files with the same name/dir with the updated ones in your main
g checkout main -- file1 dir/file
g checkout main -- dir/
g checkout main -- path/to/dir

2. push latest for github
g add .
g commit -am "view diff"
g push
