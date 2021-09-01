
# Homework 1 part 1

## Notes

This is an individual assignment. DO NOT share your solution with others or use
solutions from others.  You may have high-level discussions with your
classmates about how to do the assignment, but the act of installing Linux and
carrying out the commands to complete the assignment must be done by you.

You should never, throughout the course of the semester, share the file you
create or the MD5 digest of it (which will be used to identify you as a student
in future assignments) with any of your classmates or anybody else other than
the TAs and myself.

**WARNING: START EARLY! Getting Linux installed may take some time.**

## Preparation: Get Linux installed, so that you have sudo access

Follow the instructions in Piazza to get your own Linux virtual machine (or
physical machine, if you prefer) running.  I recommend using VirtualBox and the
provided exported appliance, but you're welcome to use other approaches (such
as VMWare and/or installing MX Linux on your own).  You will need sudo (i.e.,
root) access for later assignments, so don't put off this preparation step
because it'll put you behind on future homeworks.

## Assignment: Create a file and an MD5 digest of that file

You should perform the following steps in a Linux shell:

1. Create a text file, using you favorite text editor (such as vim, emacs, or
nano---if you're not familiar with any of these you'll find nano the easiest to
learn).  In the file, on separate lines you should type (as this info appears
in the ASU system for your registration in this course) your full name and your
ASURITE ID.  The formatting is forgiving, so it doesn't really matter if you do
last name first and first name last or vice versa.  Then, add at least 200
bytes of text onto the end of the file, on the same line or on separate lines.
The additional text can be anything, you can type your thoughts, put random
text, or anything.  An example text file is
[here](4b7611b7fcc254a837f7d93db3411878.txt).  All text in your text file
should be printable ASCII, and it must end with a newline (`\n`).  You can run
something like `hexdump -c 4b7611b7fcc254a837f7d93db3411878.txt` to verify that
there are not funny characters that don't print on the terminal (will look like
`034` or `DB` or `\r`), and that `\n` is the last byte in the file.  There should be no escaped characters other than the newlines (`\n`).

2. Calculate the MD5 digest of the file using the `md5sum` Linux command.

3. Rename the file so that the basename is the md5 digest as outputted in ASCII-encoded hexadecimal by the `md5sum` command.  An easy way to accomplish steps 2 and 3 with one command is:

```
cp afile.txt `md5sum afile.txt | cut -b 1-32`.txt
```

A screencap showing examples is [here](md5sumandcut.png).

## How to submit your file

In Piazza, I'll post a link to a Google Forms form that you can use to submit
your file.  You'll answer a few questions and upload the file.  Make sure the
file you upload is named correctly so that the basename and the MD5 digest of
it match.  If you followed instructions your MD5 digest should not match that
of any other student in the class.  Your file name should look something like `4b7611b7fcc254a837f7d93db3411878.txt` but have a different MD5 digest.

You can submit directly using the virtual machine, or you can look into options
for getting the file off the virtual machine onto another machine, such as
`scp` or a folder that is shared between your virtual machine guest and the
host operating system.

## Extra credit

Optionally, for up to 4 points of extra credit, you can create a separate file.
The separate file should have the same MD5 digest as your homework submission,
but with different contents.  You should add `-extracredit` to the end of the
basename.  So, for example, if your file for the homework submission is named
as in the example above then the extra credit file will be named
`4b7611b7fcc254a837f7d93db3411878-extracredit.txt`.  This file should be for a
shadow student, with the name of your favorite Disney/Pixar character (you can
use other fictional characters if you like, but they should be obviously
fictional) and a silly email address (feel free to create an ASU email alias if
you like, but the email address doesn't need to be real because I won't send
any email to it).  I'll be able to link the extra credit file to you and give
you extra credit because the MD5 digest will match the one you submitted for
the assignment.

__Due date: 9 September 2021 at 11:59pm MST__

__40 out of 100 points__

Homework set 1 will be 100 points total in four parts, this part (part 1) will
be 40 points out of that 100.  I may assign partial credit in some cases, but
partial credit is not guaranteed if you don't follow *all* instructions.

