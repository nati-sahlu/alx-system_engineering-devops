0x00 - Bash Basics

-> By Natan Sahlu
About Bash projects


Concepts

Resources
Read or watch:

What Is “The Shell”?
Navigation
Looking Around
A Guided Tour
Manipulating Files
Working With Commands
Reading Man pages
Keyboard shortcuts for Bash
LTS
Shebang
man or help:

cd
ls
pwd
less
file
ln
cp
mv
rm
mkdir
type
which
help
man

1. What’s in there?

Display the contents list of your current directory.

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 1-listit
  
2. There is no place like home

Write a script that changes the working directory to the user’s home directory.

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 2-bring_me_home
  
3. The long format
Display current directory contents in a long format.

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 3-listfiles
  
4. Hidden files
Display current directory contents, including hidden files (starting with .). Use the long format.

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 4-listmorefiles
  
5. I love numbers

Display current directory contents.

Long format
with user and group IDs displayed numerically
And hidden files (starting with .)

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 5-listfilesdigitonly
  
6. Welcome
Create a script that creates a directory named my_first_directory in the /tmp/ directory.

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 6-firstdirectory
  
7. Betty in my first directory
Move the file betty from /tmp/ to /tmp/my_first_directory.

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 7-movethatfile
  
8. Bye bye Betty
Delete the file betty.
The file betty is in /tmp/my_first_directory

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 8-firstdelete
  
9. Bye bye My first directory
Delete the directory my_first_directory that is in the /tmp directory.

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 9-firstdirdeletion
  
10. Back to the future

Write a script that changes the working directory to the previous one.

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 10-back
  
11. Lists

Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 11-lists
  
12. File type

Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 12-file_type
  
13. We are symbols, and inhabit symbols

Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 13-symbolic_link
  
14. Copy HTML files

Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

You can consider that all HTML files have the extension .html

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 14-copy_html
  
15. Let’s move

Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.

You can assume that the directory /tmp/u will exist when we will run your script

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 100-lets_move
  
16. Clean Emacs

Create a script that deletes all files in the current working directory that end with the character ~.

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 101-clean_emacs
  
17. Tree

Create a script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.

You are only allowed to use two spaces (and lines) in your script, not more.

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 102-tree
  
18. Life is a series of commas, not period
Write a command that lists all the files and directories of the current directory, separated by commas (,).

Directory names should end with a slash (/)
Files and directories starting with a dot (.) should be listed
The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
Only digits and letters are used to sort; Digits should come first
You can assume that all the files we will test with will have at least one letter or one digit
The listing should end with a new line

GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: 103-commas
  
19. File type: School

Create a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.


GitHub repository: alx-system_engineering-devops
Directory: 0x00-shell_basics
File: school.mgc
