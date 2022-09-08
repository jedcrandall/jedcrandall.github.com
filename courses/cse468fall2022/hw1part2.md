# Homework 1, part 2

__Due date: 19 September 2022 at 11:59pm MST__

Homework 1 has three parts, this is the second one.  It has two questions, (a) and (b), each will be worth 30 points for 60/100 total.

## Notes

This is an individual assignment. DO NOT share your solution with others or use
solutions from others.  You may have high-level discussions with your
classmates about it, and you may use/share any source code that existed before
the assignment was assigned and is not related to any similar assignment or
any past offering of CSE 468 or a related class at ASU.

## Preparation: Downloading your tarball

Start by "ratcheting" your MD5 token from homework 1.1 to find out the name of your tar ball.  Do the following:

```bash
echo -n "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN" | md5sum | cut -c 1-32
```

But replace "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN" with your MD5 token.  The output of the above command will tell you which tar ball [here](https://github.com/jedcrandall/jedcrandall.github.com/tree/master/courses/cse468fall2022/hw12tarballs) is yours.  Download and it decrypt it like this, using your MD5 token as the password:

```bash
openssl aes-256-cbc -d -pbkdf2 -in NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN.enc -out /tmp/mytarball.tgz
```

Do not share your tarball, MD5 token, tarball name, or anything that identifies you or your assigment in this way with others.

## Homework 1, part 2, question (a)

__30 out of 100 points__

In your tar ball, in a subdirectory called "a", you will find a ciphertext file
and a key.   The ciphertext was created by XORing the plaintext with the key,
in a bitwise fashion.  Decrypt the plaintext and submit it.

## Homework 1, part 2, question (b)

__30 out of 100 points__

This is the same as question (a), but you are not provided with the key.
Instead, you are given one ciphertext and two plaintexts.  Find the missing
plaintext.

## How to submit

You will copy and paste the entire plaintext into the Google form, no need to
upload files.  The Google Forms link will be provided in Piazza, note that
every assignment will have a different Google Forms link to use.  Try to avoid including any whitespace or newline characters, but the grading script should do a good job of removing them anyway.  There will be a lot of dash characters ('-') in your plaintext, leave them in there.
