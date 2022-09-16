
1. List all the branches in this repository and, for each branch, list the commits.

    - Use `git branch` to list the branches in this repository.
    - Use `git checkout` to explore each branch.
    - Use `git log --decorate` to explore the structure of commits.

```
==>For "git branch" command:
* master
  math
  
  This explains that we are currently in the master branch
  
==>For "git checkout" command:

since we are already on the master branch lets checkout the math branch.
>> git checkout math
Switched to branch 'math'

==> For "git log --decorate" command 

commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (HEAD -> math)
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:13:48 2019 -0700

    Adding some more knowledge to the function

commit 654b490a181dedf82dd6deda5f9848d6cca05918
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:12:14 2019 -0700

    Added a draft of A.py

commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:08:47 2019 -0700

     Creating all files (all empty)

```

2. Try `git log --graph --all` to see the commit tree. Paste the result here and write a paragraph to provide an interpretation of what you found.
```
==> For "git log --graph --all" command:

* commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (master)
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:15:28 2019 -0700
|
|     Making a small change here
|
| * commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (HEAD -> math)
|/  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
|   Date:   Wed Aug 14 23:13:48 2019 -0700
|
|       Adding some more knowledge to the function
|
* commit 654b490a181dedf82dd6deda5f9848d6cca05918
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:12:14 2019 -0700
|
|     Added a draft of A.py
|
* commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
  Date:   Wed Aug 14 23:08:47 2019 -0700

       Creating all files (all empty)

The "git log --graph --all" is used to list all the logs committed to a repository.

By observing the above graph of logs, first all the files are created and they are empty
Next, the file A.py is added with some content
Next, a branch has been created named "math", and some more content has been added
Fibally we returned to the master branch againn to make some changes..

```

3. Use `git diff BRANCH_NAME` to view the differences from a branch and the current branch. Summarize the difference from master to the other branch.

```
==> Using the command "git diff master"
 This command gives out the list of files and the content in the files.
 Since the B.py has no content in it as of now it just displays the file name and no content.
 
 ==> Using the command "git diff math"
 This command gives out nothing because the math  branch has no commits as of now.
```

4. Write a command sequence to merge the non-master branch into `master`.

```

Step 1: git checkout master
Step 2: git merge non_master_branch


```


5. Write a command (or sequence) to (i) create a new branch called `math` (from the `master`) and (ii) change to this branch.

```
$ git branch math
The above command creates a math branch.

$ git checkout math
The above command is used to change to math branch.

```
   
6. Edit B.py adding the following source code below the content you have there.
```
print 'I know math, look:'
print 2+2
```

7. Write a command (or sequence) to commit your changes.
```
$ git commit

```

8. Change back to the `master` branch and change B.py adding the following source code (commit your change to `master`):
```
print 'hello world!'
```

9. Write a command sequence to merge the `math` branch into `master` and describe what happened.
```
$ git checkout master

$ git merge math

There was some merge conflict during this process. I guess this is because of the master has not been updated.

```
   
10. Write a set of commands to abort the merge.
```
git merge --abort

```
   
11. Now repeat item 9, but proceed with the manual merge (editing B.py). All implemented methods are needed. Explain your procedure.
```


```

12. Write a command (or set of commands) to proceed with the merge and make `master` branch up-to-date.
```
$ git checkout master

$ git merge math

$ git checkout master 
$ git pull 
$ git checkout -  
$ git rebase master 
```

13. Complete Part 2. Then, come back here and answer the following:
Report your experience of submitting the Part 2. Please, include the steps you followed, the commands you used, and the hurdles you faced (within the file you created for the **Part 1**).
```

In part 2 we have exprienced the conepts of forking the Repository and submitting a Pull Request.

I have created a markdown file and created a report on the paper I read recently(actually the one I published :):) ).

Then I have committed the file to my own repository &created a pull request to the course repository.


```
