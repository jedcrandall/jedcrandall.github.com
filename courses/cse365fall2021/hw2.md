# Homework 2, parts 1, 2, and 3

This assignment has three parts, with three different due dates.  Please be
mindful of that.  For each you will submit a plain text file (not a zip or
anything like that) that has a very specific format.  Please be mindful of the
format as the grading is automated.  More info about the format is at the
bottom.

The `streamy.py` file provided for the last homework assignment is a good
starting point for how to write a Python script to parse a pcap file.  For each
question, think about whether tshark, Wireshark, a custom Python script you
write, or something else is the right tool for the job.

## Notes

This is an individual assignment. DO NOT share your solution with others or use
solutions from others.  You may have high-level discussions with your
classmates about it, and you may share any source code that existed before the
assignment was assigned and is not related to any similar assignment for any
past offering of CSE 365 at ASU.

**WARNING: START EARLY! Each part is a substantial amount of work.**

Before you even start on homework 2 you should make sure you've watched [this recorded lecture](https://drive.google.com/file/d/1p6fsOmWWOsBgPQRcZTLl4SH4oTnBZBCa/view?usp=sharing).

## Preparation: Downloading your tarball

[https://207.246.62.10/filesforstudents/NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN-netsec.tgz](https://207.246.62.10/filesforstudents/NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN-netsec.tgz)

The SHA-256 sum for the certificate on that web server is
"7E:F1:12:D4:A5:4F:92:30:AA:DC:D1:F5:14:3C:D8:D0:A5:FE:DB:52:9E:FC:A6:D2:22:4F:D1:D7:7A:BA:71:8C",
please confirm it manually and then make an exception for your web browser to
go to the site.

Do not share your tarball with others.

WireShark, tshark, and pyshark should all be installed on your VM already if
you used my VM image and did Homework 1.4.  If not, on Debian-based distros you
can do:

```bash
sudo apt install python3-pip
sudo apt install wireshark tshark
pip3 install --upgrade setuptools
pip3 install pyshark
```

## Homework 2.1: A horizontal port scan

__Due date: 18 November 2021 at 11:59pm MST__

__40 out of 100 points__

In your tarball you'll find `horizontal.pcap` and `part1.txt`. Edit `part1.txt`
to answer the questions, keeping in mind the format requirements below. Then
submit your edited version of the `part1.txt` file without any compression or
anything like that.  Don't change the name of the file.

## Homework 2.2: A vertical port scan

__Due date: 19 November 2021 at 11:59pm MST__

__40 out of 100 points__

In your tarball you'll find `vertical.pcap` and `part2.txt`. Edit `part2.txt` to
answer the questions, keeping in mind the format requirements below. Then submit
your edited version of the `part2.txt` file without any compression or anything
like that.  Don't change the name of the file.

## Homework 2.3: A TCP/IP side channel

__Due date: 20 November 2021 at 11:59pm MST__

__20 out of 100 points__

In your tarball you'll find `sidechannel.pcap` and `part3.txt`. Edit `part3.txt`
to answer the questions, keeping in mind the format requirements below. Then
submit your edited version of the `part3.txt` file without any compression or
anything like that.  Don't change the name of the file.

## Format of the text file you'll upload

It's very important that you preserve the format of the text file you submit for
each part.  We recommend simply editing `part1.txt` for Homework 2.1,
`part2.txt` for Homework 2.2, and `part3.txt` for Homework 2.3 and submitting
that, with the questions still intact.  You can delete lines that start with
__\#__, or add lines that start with __\#__ for your own comments if you really
want to.  The automatic grader will ignore all lines that begin with __\#__.
However, if you leave the questions in place it will make manual grading easier
if that should become necessary for some reason.

The lines that don't begin with __\#__ are your answers.  Every answer should be
a single line with no whitespace (the grader will remove all whitespace before
doing a string comparison, but if your answer has whitespace in it it's probably
not the right answer).  You should edit the lines that don't begin with __\#__
to put the answer there, there should be no lines in the file that are not
answers or comments/questions (comments and homework questions begin with
__\#__).

There are only three kinds of answers:

* IP addresses, where you will replace __N.N.N.N__ with a valid IPv4 address, such as __98.45.6.31__
* MAC/hardware addresses, where you will replace __HH:HH:HH:HH:HH:HH__ with a valid MAC/hardware address, like __a4:50:4e:99:2d:55__
* Other numbers, which contain only decimal digits and dots.  For these you'll replace __N__ with something like __1832__ or __4.1.61__

## How to submit

You'll need to submit through this form at least three times (resubmissions are
okay, but will be graded according to the deadlines).  You'll submit all three
parts through the same form, at three different times.  The grading script will
apply the deadline for each part.

Here is the link to submit each of the three parts:

[https://forms.gle/5jpM85Pg26YLN6W9A](https://forms.gle/5jpM85Pg26YLN6W9A)

Rememeber, do not change the name of the file you submit your answers with.  If
the filename does not contain the string "part1" for Homework 2.1 then it will
be thrown out and not graded, and the same is true for "part2" and "part3" for
Homeworks 2.2 and 2.3, respectively. 

## How to check your answers

For any of the parts, if you answer all questions correctly then you should be
able to match one of [these SHA-256 sums](hw2sha256s.txt).  If you suspect an
extra newline or something is messing up the hash, then try running [this
script](makeuniform.sh) based on [this example](checkingsha256s.png).

