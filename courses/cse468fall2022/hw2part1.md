# Homework 2, part 1

__Due date: 7 November 2022 at 11:59pm MST__

Homework 2 has two parts, this is the first one.  It has ten questions, 0
through 9, which are each worth 6 points for a total of 60 possible.  The second
part of homework 2 will be due at the same time as the first part, but will not
require any time outside of the regularly scheduled class period unless you
miss class (in which case you'll watch a video of no more than 1 hour and 15
minutes as a make up assignment).

## Notes

This is an individual assignment. DO NOT share your solution with others or use
solutions from others.  You may have high-level discussions with your
classmates about it, and you may use/share any source code that existed before
the assignment was assigned and is not related to any similar assignment or any
past offering of CSE 468 or a related class at ASU.  You may use any source
code I provided for lecture purposes at any time.

## Preparation: Downloading your tarball

Start by "ratcheting" your MD5 token from homework 1.1 to find out the name of your tar ball.  Do the following:

```bash
echo -n "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN" | md5sum | cut -c 1-32
```

But replace "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN" with your MD5 token.  The output
of the above command will tell you which tar ball
[here](https://github.com/jedcrandall/jedcrandall.github.com/tree/master/courses/cse468fall2022/hw21tarballs)
is yours.  Just add ".enc" to the end of your ratcheted MD5 token.  Download
and it decrypt it like this, using your original MD5 token as the password:

```bash
openssl aes-256-cbc -md sha256 -d -in NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN.enc -out ~/mytarball.tgz
```

You should be able to perform the above command on general.asu.edu or any Linux
system.  Then you can find your plaintext tarball for the assignment in your
home directory, and decompress/untar it wherever you plan to do your homework.
Don't use /tmp on general.asu.edu for anything related to your tar ball, it
caused students various errors and problems on earlier homeworks.

Do not share your tarball, MD5 token, tarball name, or anything that identifies
you or your assignment in this way with others.

## Ten multiple choice questions

__60 out of 100 points__

In your tar ball, you'll find a text file called "questions.txt".  The
questions refer to packet captures and other info you'll find in [this tar
ball](hw21files.tgz).  Choose *the best answer* of the four possible answers
for each question.

## How to submit

You will copy and paste your answers into the Google form, no need to upload
files.  The Google Forms link will be provided in Piazza, note that every
assignment will have a different Google Forms link to use.  Try to avoid
including any whitespace or newline characters, but the grading script should
do a good job of removing them anyway.  You will submit a string of 10
characters, corresponding to your answers for questions 0 through 9,
respectively.  E.g., you might submit something that looks like "babbcdbadc",
"aabddcbcab", or "ddcaabcbab" with the exact letters depending on what the
correct answers are.  Note that the question numbers start at 0.