# Homework 3

__Due date: 3 December 2021 at 11:59pm MST__

Homework 3 has only one part, and is substantially more simple and less
time consuming that homeworks 1 and 2, but is still worth 100 points.

Download [files.tgz](files.tgz), which has ten files in it.  Then submit your
answers to the questions that are [here]() through the Google form.  You can
submit as many times as you like up until the deadline, the grading script will
grade the most recent one (i.e., the last one) that you submit.

## Notes

Feel free to work in small groups of up to 5 people, or work alone.  Don't give
anybody the answers, rather help them work through the solutions on their own
or work through them together.  Do not post solutions in forums that students
outside your group of up to 5 will see.

This is an individual assignment. DO NOT share your solution with others or use
solutions from others, unless they're in your group and you help them
understand the solution.  You may have high-level discussions with your
classmates (in your group or not) about it, and you may share any source code
that existed before the assignment was assigned and is not related to any
similar assignment for any past offering of CSE 365 at ASU.  But no source code
should be necessary, Linux command line tools can be used to answer all the
questions.


Everything you need except for exif should be installed on any Linux distro.
On Debian-based distros you can do this to get exif:

```bash
sudo apt install exif
```

## Some hints

There will be no way to check your answers (you can certainly get help from the instructor and TAs, but there will be no explicit checking of answers).

You should read the man pages about each of these commands/system calls, after you install exif:

```bash
man gzip
man bzip2
man tar
man hexdump
man exif
man objdump
man strings
man file
man base64
man chmod
man 2 chmod
man tr
man bc
```

Some use cases of the above commands that might be helpful:

```bash
objdump -D -Mintel,i386 -b binary -m i386 sample.bin
strings sample.bin
cat sample.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
echo "obase=16; ibase=8; 444" | bc
```

For the basics of x86 assembly, you can find a good YouTube tutorial like [this one](https://www.youtube.com/watch?v=75gBFiFtAb8).

