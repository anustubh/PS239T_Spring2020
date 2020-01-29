# The Unix Shell: Git basics 

> ### Learning objectives
> 
> * Explain purpose of Git and version control.
> * Explain how to use Git to get files for this class.
> * Explain how to use GitHub for final project.  

## 1. Version Control 

A **version control** system "tracks the history of changes as people and teams collaborate on projects together" (see [Github Guides](https://guides.github.com)). Specifically, it helps to track the following information:

* Which changes were made?
* Who made the changes?
* When were the changes made?
* Why were changes needed?

![Why you should do version control](https://i2.wp.com/cdn-images-1.medium.com/max/399/1*7HHA_UkjUK7wp7qP4CYu1g.png?zoom=1.75&w=456&ssl=1)

For more information on the varieties of version control systems, please read [Petr Baudis's review](https://pdfs.semanticscholar.org/4490/4c70bc91e1bed4fe02b9e2282f031b7c90ea.pdf) on that subject.

## 2. Git 

Git is a very powerful and widely used tool for collaborating and tracking changes to a project. Compared to other version-control systems, it has many valuable features for large-scale collaboration. If you are interested, read through [Github's Git Handbook](https://guides.github.com/introduction/git-handbook/). 

Git tracks changes to **repositories**. 
> A repository is the most basic element of GitHub. They're easiest to imagine as a project's folder. A repository contains all of the project files (including documentation), and stores each file's revision history. Repositories can have multiple collaborators and can be either public or private. 
> -Source: [GitHub glossary](https://help.github.com/en/articles/github-glossary)

## 3. GitHub

GitHub is a private company that hosts Git repositories. Repositories hosted by GitHub can be viewed on GitHub.com. In other words, GitHub uses Git as part of a service that it provides, but using Git does not require using GitHub. 

## 4. Shell

The shell is one way of interacting with Git. 

When we want to use commands from a program like git (or R, or python, etc.), we first write the name of the program (in this case `git`) before a program-specific command. 

> Mini-challenge:  
> Recall that when we cloned the course repository, we used the following line of code: 
> ```{shell}
> $ git clone https://github.com/anustubh/PS239T_Spring2020
> ```
> Now, see what happens when we forget to add `git` before the command: 
> ```{shell}
> $ clone https://github.com/anustubh/PS239T_Spring2020
> ```
> What happens? 

## 5. Some Git Commands

We'll start with telling Git who you are.
```shell
$ git config --global user.name "Firstname Lastname"
$ git config --global user.email username@company.extension
```

You can clone an existing repository on your local machine. 
```{shell}
$ git clone /path/to/repository
```

To update the cloned course materials directory on your computer, `cd` to the cloned subfolder (`PS239T_Fall2019`) and run the following command: 
```{shell}
$ git fetch origin
```

Note that this command will overwrite changes to any files on your computer unless they only exist on your computer. **If you make changes** to any files, make sure to **re-name the files** so that you don't lose your changes. 

You can try to merge your changes with my changes by using the `git pull` command instead, but in past years, students have been more successful with the `git fetch origin` command. [This stackoverflow thread](https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch) has more details about the difference. 

For the final project, you will be uploading your final projects to GitHub. You should try to do this using the shell in order to get practice, but if you are running short on time or can't figure it out, there is a way to upload your final project using the GitHub GUI. 

For the purposes of the final project, the following commands are likely sufficient for your repository after you've edited or added files. In Git terms, this action is called committing changes. 
```{shell}
$ git add . # update every change. In Git terms, you're staging. 
$ git add file_name # or stage a specific file.
$ git commit -m "your comment" # your comment for the commit. 
$ git push origin master # commit the change. Origin is a defaul name given to a server by Git. 
```

## 6. gitignore files 

Files that are listed in a gitignore file are ignored by Git. Sometimes we don't want a file available on GitHub (i.e. files with private information like passwords) but we can't or don't want to delete the file from the directory. If we add these files to the gitignore document, any changes will not be synced with your GitHub repo. 


If you don't want a file to be 

## 7. Directory Organization

Although we will be covering organization in more detail later this semester, starting to think through directory organization will be useful to you right away. Having well-organized files is a key part of managing projects and version control. 

### Naming files 

- Machine readable (avoid spaces, punctuation, periods, and any other special characters except _ and -)
- Human readable (should be meaningful. No text1, image1, etc.,)
- Ordering (e.g., 01, 02, 03,  ... )

### File structure 

First, organize your files so that different types of files are stored seperately. Everyone uses a slightly different template, but there are a few general princples for project organization.  

Generally, create subfolders for each part of the project. Thus, R scripts should be in a seperate subfolder from graphs and other output. Importantly, you should always keep a copy of your raw data (typically in a seperate subfolder). 

Here is an example file structure based on a great [article](http://www.rebeccabarter.com/blog/2019-03-07_reproducible_pipeline/) by Rebecca Barter:
- /code
	- exploration
	- scripts
		- functions
- /data
	- /raw 
		- data_orig.csv
	- /processed 
		- data_clean.csv
	- /results 
		- model_results.csv
- /output 
	- /figures
		- plot.pdf
	- /reports
		- robustness_checks.pdf
- /documents
	- meeting_notes.md
	- other_notes.md
- .gitignore (for Git)
- name_of_project.Rproj (for R)
- README.md (for Git) 


******************************************

## Exercises

#### Challenge 0: Clone course files & Tell Git who you are

If you have not done so already, clone the course materials by following these instructions: 

1. Decide where you want to keep files for this class on your computer. 
2. Change your working directory to this subfolder using `cd`. This is where you will keep a copy of the the `PS239T` materials. 
3. Type `git clone https://github.com/juliachristensen/PS239T_Fall2019` and hit enter. 
4. Wait until a copy of the files from the class GitHub page are copied to your computer. 

If you have not already done so, tell Git who you are
```shell
$ git config --global user.name "Firstname Lastname"
$ git config --global user.email username@company.extension
```

#### Challenge 1: Update course files

1. Change your working directory to the cloned subfolder called `PS239T_Fall2019` using `cd`.
3. Type `git fetch origin` and hit enter. 
4. Wait until a copy of the files from the class GitHub page are copied to your computer. 

#### (Optional) Challenge 2: Create GitHub Account

[Sign Up](https://github.com/join)

#### (Optional) Challenge 3: Create repository for your final project

You can create a new subfolder on your computer and add it to GitHub, but it's usually easier to use the GitHub website (aka the GUI) to make a new repository. 

1. Sign into (/create) your account on GitHub.com
2. On GitHub.com, follow the instructions to add a new repository (click on `+` sign in right-hand corner). Call it something like `final-project-239T`. Click box that says `Initialize this repository with a README`.
3. Clone this repository onto your computer (see the instructions from challenge 1 for help). 
4. Update the README file on your computer and save (use any text editor). 
5. Change your working directory to the cloned subfolder. 
6. Follow instructions for pushing your changes to GitHub (see A3 below). 
7. Look on GitHub.com and verify that the README file has been updated. 
8. Add file structure subfolders on your computer and repeat steps 5 to 7. 


******************************************

## Additional Reference Information

### A1. Source(s)

The content of this unit is adapted from [the git-fundamentals workshop materials](https://github.com/dlab-berkeley/git-fundamentals/blob/master/0-1_introduction.md) prepared by Dillon Niederhut at D-Lab and other resources from [Pro Git](https://git-scm.com) by Scott Chacon and Ben Straub. 

### A2. Version control system 

Git is a case of a [distributed version control system](https://en.wikipedia.org/wiki/Distributed_version_control), common in open source and commercial software development. This is no surprising given that Git [was originally created](https://lkml.org/lkml/2005/4/6/121) to deal with Linux kernal development. 

* If you're curious about how the Intenret works, learn one of the key ideas of the Internet: [end-to-end principle](https://en.wikipedia.org/wiki/End-to-end_principle). This also explains why [net neutrality](https://en.wikipedia.org/wiki/Net_neutrality) matters. 

The following images, from [Pro Git](git-scm.com), show how a centralized (e.g., CVS, Subversion, and Perforce) and decentralized VCS (e.g., Git, Mercurial, Bazzar or Darcs) works differently. 

![Centralized version control system](https://git-scm.com/book/en/v2/images/centralized.png)

Figure 2. Centralized VCS.

![Decentralized version control system](https://git-scm.com/book/en/v2/images/distributed.png)

Figure 3. Decentralized VCS.

For more information on the varieties of version control systems, please read [Petr Baudis's review](https://pdfs.semanticscholar.org/4490/4c70bc91e1bed4fe02b9e2282f031b7c90ea.pdf) on that subject.

### A3. Useful Commands

#### Setup 

We'll start with telling Git who you are.

```shell
$ git config --global user.name "Firstname Lastname"
$ git config --global user.email username@company.extension
```
#### Making a repository 

Create a new directory and move to it. 

```shell 
$ mkdir code_exercise 
$ cd code_exercise 
```

```{shell}
$ git init 
```

Alternatively, you can create a Git repository via Github and then clone it on your local machine. 

```{shell}
$ git clone /path/to/repository
```

If you're unfamiliar with basic Git commands, then please refer to [this Git cheet sheet](http://rogerdudler.github.io/git-guide/files/git_cheat_sheet.pdf).

#### Commit changes 

These feature show how Git works as a version control system. 

If you edited files or added new ones, then you need to update your repository. In Git terms, this action is called committing changes. 

```{shell}
$ git add . # update every change. In Git terms, you're staging. 
$ git add file_name # or stage a specific file.
$ git commit -m "your comment" # your comment for the commit. 
$ git push origin master # commit the change. Origin is a defaul name given to a server by Git. 
```
Another image from [Pro Git](https://git-scm.com/about/staging-area) well illustrates this process.

![Git Workflow](https://git-scm.com/images/about/index1@2x.png)

Figure 4. Staging and committing in Git.

#### Other useful commands for tracking history

```{shell}
$ git diff # to see what changed (e.g., inside a file)
$ git log # to track who committed what
$ git checkout the commit hash (e.g., a5e556) file name (fruit_list.txt) # to recover old files 
$ git revert 1q84 # revert to the previous commit 
```
#### Doing other than adding 

```{shell}
$ git rm file_name # remove 
$ git mv old_file_name new_file_name # rename a file 
```

#### Push and pull (or fetch)

These features show how Git works as a collaboration tool. 

If you have not already done, let's clone PS239T directory on your local machine.

```{shell}
$ git clone https://github.com/jaeyk/PS239T # clone 
```

Then, let's learn more about the repository.

```{shell}
$ git remote -v 
```

Previously, we learned how to send your data save in the local machine to the remote (the Github server). You can do that by editing or creating files, committing, and then typing **git push**. 

Instead, if you want to update your local data with the remote data, then you can type **git pull origin** (something like pwd in bash). Alternatively, you can use fetch (retrieve data from a remote). When you do that, Git retrieves the data and merge it into your local data.

```{shell}
$ git fetch origin
```

#### Branching 

It's an advanced feature of Git's version control system that allows developers to "diverge from the main line of development and continue to do work without messing with that main line" according to [Scott Chacon and Ben Straub](https://git-scm.com/book/en/v1/Git-Branching). 

If you start working on a new feature, then create a new branch. 

```{shell}
$ git branch new_features
$ git checkout new_features
```

You can see the newly created branch by typing **git branch**.

In short, branching makes Git [works like](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics) a mini file system.

#### Collaborations 

Two options. 

* Sharing a repository (suitable for a private project).
* Fork and pull (suitable for an open source project). 
    ​    * The one who maintains the repository becomes the maintainer. 
    ​    * The others can [fork](https://help.github.com/articles/about-forks/), make changes, and even [pull](https://help.github.com/articles/about-pull-requests/) them back.

#### Other stuff 

```{shell}
$ git status # show the status of changes 
$ git branch # show the branch being worked on locally
$ git merge # merge branches 
$ git reset --hard # restore the pristine version
$ git commit -a -m "additional backup" # to save the state again
```


