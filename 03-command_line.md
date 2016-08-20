# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > I've made a few cheat sheets in evernote so they may be a little long for here, but here's a sample:

mkdir: create a directory

mkdir -p directory/directory/directory…: create nested directory (creates all directories in path)

cd: Change directory
     - if your directory has spaces, you need to put the directory name in quotes

cd ~: go to home directory

cd - : got to last directory

. file: current directory (that's a period.)

.. file: directory above (that's two periods..)
     eg: cd …  changes directory to parent of current directory

!! : re-runs the last entered command

cp file1 file2: copy file1 to file2 (overwrites file2 if it already exists)

cp -r directory newdirectory: copy directory and all its contents into new directory (does not rewrite new directory if it
                                             already exists, but moves source dir into newdir)

mv file targetdir: move a file or directory to target directory

mv file, newfilename: mv can also be used to rename a file e.g. create a new location for it if the new name does not
                                   exist.

pwd: print working directory (shows path for current file)

ls: list files in directory

ls -a: show all files including hidden files

ls -l : list files in long format
     - long format includes:
          o file mode
          o number of links
          o owner name
          o group name
          o file size
          o last modified
          o path name

ls -lh : use unit suffixes (byte, kilobyte, megabyte etc...) for long format file size

ls -lah :

ls -t : list all files sorted by time last modified

ls -G : Enable colorized output. Draw colors from environmental variable CLICOLOR

ls -p : put a slash ( / ) after directory names

rm file: remove (delete) file. You can put more than 1 file args separated by spaces

rm - i : inspect file for deletion

rmdir : delete an empty directory

rm -ir directory: inspect a directory and delete all it’s contents

rm -r directory: deletes directory and all of its contents without asking about it (r is for recursively)

pushd dirname: Add a directory to the top of your directory stack  (a stack is like a storage shelf of directories)

popd: pop a directory (remove a directory off the top of your directory stack and go to the new top directory)

dirs: show all directories in your stack

hostname: get my computers network name  (local…)

less file: less is a program to read files 1 page at a time. It comes with it’s own set of commands. See ‘less'

cat file: print the entire contents of a file.  You can put multiple files as arguments and it prints the entire contents of
                   all files in order that they are placed

xargs args…: takes multiple input and executes a function (arg) for each input

find stuff: search for files in given directory with specific args/identifiers… complicated

grep regex + args: find things inside files

grep -i regex args: ignore case (uppercase/lowercase)

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
 * ls: show files in current directory
 * ls -a: show all files including hidden files
 * ls -l: show results in long format (size, date last edited etc)
 * ls -lh: abbreviate filesizes with mb, kb, gb etc...
 * ls -lah: combination of all the above
 * ls -t: sort by date modified
 * ls -Glp: color directories differently from files, use long format, put slashes after directory names...

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
 * ls -d: display only directories
 * ls -1: display as a column
 * ls -t: display newest files first
 * ls -q: display nonprinting characters as '?'
 * ls -m: display as comma separated list

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs is an iterator(?) you can pass it multiple inputs and it performs a function on all of them

 

