
# Homework 1 part 1, CSE 468 Fall 2022

## Notes

This is an individual assignment. DO NOT share your solution with others or use
solutions from others.  You may have high-level discussions with your
classmates about how to do the assignment, but the act of installing Linux and
carrying out the commands to complete the assignment must be done by you.

You should never, throughout the course of the semester, share your security
token  (which will be used to identify you as a student in future assignments)
with any of your classmates or anybody else other than the TA and myself.

**WARNING: START EARLY! Getting the right access may take some time.**

## Preparation: Make sure you have access to general.asu.edu

Unless you have access to a Linux shell (no need to be root) on another
machine, you should ssh to general.asu.edu using the ASU ID that is the first part of your @asu.edu email address.  E.g., for me it's:

```bash
ssh jrcranda@general.asu.edu
```

You'll need to enter your password and probably do Duo two-factor
authentication.

## Assignment: Create an MD5 digest that (unless something astronomically unlikely happens) is unique to you

You should perform the following step in a Linux shell (again, no need for root):

```bash
dd if=/dev/urandom bs=1 count=128 2>/dev/null | md5sum | cut -b 1-32
```

A screencap showing examples is [here](md5songeneral.png).  I recommend running the command a few times to make sure you get a different answer every time, as a sanity check that you typed it correctly.  The output of any of them can be your security token.  If you want to be extra paranoid, you can Google it to make sure it doesn't exist on the web.  You security token should be a string that is 32 characters long, a 32-nibble hex number representing a 128-bit MD5 digest.

## How to submit your security token

In Piazza, I'll post a link to a Google Forms form that you can use to submit
your security token.  You can resubmit as many times as you like, the grader
will give you the highest grade out of all submissions based on the late
submission policy.  Please refrain from submitting more than a couple of times,
though, the multiple submissions is just for you to be able to fix mistakes.


__Due date: 2 September 2022 at 11:59pm MST__

__10 out of 100 points__

Homework set 1 will be 100 points total in several parts, this part (part 1)
will be 10 points out of that 100.  I may assign partial credit in some cases,
but partial credit is not guaranteed if you don't follow *all* instructions.

