# Homeworks 1.2, 1.3, and 1.4: Cryptography and cryptanalysis

This assignment has three parts, with three different due dates.  Please be
mindful of that.  Everything you submit through Google Forms will be
ASCII-encoded and look at least somewhat like English, so don't click the
submit button if you can't read it.  Also, sha512 sums will be provided, so if
you want a guaranteed 100% of the points, work to match the sha512 sum before
submitting.  

## Preparation: Downloading your tarball and installing packages

First, you must fill out [this Google form](https://forms.gle/yJbZ2Q8BNNSaLqcm6) so that I have an MD5 digest for
you, then wait until I've added you in the gradebok and added your tarball.  If
you get this done before 11:59pm on Thursday, September 23rd I'll get your tar
ball uploaded by Friday, September 24th.  Otherwise, it'll just happen when I
get around to it.

You will download a tarball by taking this URL and replacing
"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN" with your MD5 digest:

[https://207.246.62.10/filesforstudents/NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN.tgz](https://207.246.62.10/filesforstudents/NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN.tgz)

The SHA-256 sum for the certificate on that web server is
"7E:F1:12:D4:A5:4F:92:30:AA:DC:D1:F5:14:3C:D8:D0:A5:FE:DB:52:9E:FC:A6:D2:22:4F:D1:D7:7A:BA:71:8C",
please confirm it manually and then make an exception for your web browser to
go to the site.

The tar balls are
unique to each student.  Do not share your tarball with others.

There is also a common tarball, with source code and other things you will find helpful, [here](commontarball.tgz).

For all of the code provided to run properly, you'll need to set up your environment.  If you're using the same version of MX Linux as me, this should be as simple as:

```bash
sudo apt install python3-pip
pip3 install --upgrade setuptools
pip3 install pyshark
sudo apt install python3-crypto
```

There are two different ways to install libraries for Python 3 as shown above.
One is to `apt install` the package, which usually looks like `python3-*` for
the package name, and the other is to use pip3.  They each have their
advantages, for this assignment if you try one and it doesn't work, try the
other way.

## Notes

This is an individual assignment. DO NOT share your solution with others or use
solutions from others.  You may discuss the assignment at a high level with
your classmates and others, e.g., exploring potential solutions without giving
the answer.  You may use, and share with your classmates, any code that existed
before this assignment was assigned and is not related to any similar
assignment for any pat offering of CSE 365 at ASU.  You may not share any code
with future students of CSE 365 at ASU.  If you're not sure about if any
particular activity will be considered cheating or not, ask.

About grading, make sure your answer matches the sha512 sum before submitting,
and you'll get full points.  Don't open the file in Windows or do anything else
that could modify it before submitting, I recommend submitting directly from
your Linux virtual machine.  Be careful about the exact formatting and how the
file should end, to achieve the correct sha512 sum.  If the answer you submit
does not match the sha512 sum, I'll attempt to give you extra credit but I
reserve the right to give you a zero on that part of the assignment.  I.e.,
you're at the mercy of my grading script if the sha 512 sum doesn't match.

For all Google Forms submissions, you *must* use your @asu.edu Google account.

## Homework 1.2: Decrypting when you are given the key

__Due date: 1 October 2021 at 11:59pm MST__

__20 out of 100 points, 10 each cipher__

In your tarball in the `withkey` directory, you'll find five files:

1. `ciphertext.txt` - A ciphertext encrypted with a Caesar cipher. 
2. `caesarkey.txt` - The key used for the Caesar cipher.
3. `juliaplaintext.txt.gz.enc` - A ciphertext encrypted as described below.
4. `juliakey.txt` - The key used for Julia's cipher.
5. `sha512sums.txt` - sha51sums of the correct answers.

For each of the two ciphers, Ceasar's and Julia's, you'll need to write some
code so you can plug in the key and decrypt (and then also decompress if
necessary).  You'll submit two different plaintexts, one for each cipher, for
part 1.  In the `src/` directory `cse365encrypt.py` is the code that was used
for encrypting both ciphertexts. 

For the Caesar cipher, the alphabet for the plaintext and ciphertext is the
capital letters [A-Z], and the key is a number between 0 and 25.

For Julia's cipher, the crypto algorithm is:

```
enc_char = bit_rotate(plain_char, N) xor key_byte
```

where `N` is a fixed integer, and `key_byte` is a byte of the key. If the key is
shorter than the length of the file, the key will be used again for xor from the
beginning.  Julia's cipher works on binary files, so basically raw bytes. 

You will submit  exactly two text files: `plaintext.txt` (for the Caesar
cipher) and `juliaplaintext.txt` (for Julia's cipher).  They should both be
ASCII-encoded English text.  In some cases there may be some extra steps after
decryption before you get to English text.

After completing this part you should be confident with dealing with files and
basic calculations in Python, and familiar with the two cryptosystems (that
you'll be using in the next part, as well).

Submit both the `plaintext.txt` and `juliaplaintext.txt` files for Homework 1.2
using [this Google form](https://forms.gle/kxgjupAj2RHFrWjK9).

## Homework 1.3: Decrypting when you are not given the key, i.e., cryptanalysis

__Due date: 15 October 2021 at 11:59pm MST__

__30 out of 100 points, 15 each cipher__

In your tarball in the `withoutkey` directory, you'll find three files:

1. `ciphertext.txt` - A ciphertext encrypted with a Caesar cipher. 
2. `secretfile.txt.gz.enc` - A ciphertext encrypted with Julia's cipher, as
   described in Homework 1.2.
3. `sha512sums.txt` - sha51sums of the correct answers.

This time you are not provided with any keys.  Use the techniques discussed in
class to mount ciphertext-only attacks on both of these ciphertexts.  Note that
Julia's cipher is not the same as a Vigenere cipher.  You'll need to use the
basic insights you learned, but the specifics from the slides won't be exactly
what you're doing.

You will submit exactly two text files: `plaintext.txt` (Caesar cipher) and
`secretfile.txt` (Julia's cipher).  They should both be ASCII-encoded English
text.

After completing this part you should have some understanding of how simple
codes can leave statistical clues in the ciphertext that lead to plaintext-only
or known plaintext attacks.

Submit both the `plaintext.txt` and `secretfile.txt` files for Homework 1.3
using [this Google form](https://forms.gle/W7xNvygJvV2Ft1M49).

## Homework 1.4: Chosen ciphertext attack on 2048-bit RSA

__Due date: 29 October 2021 at 11:59pm MST__

__10 out of 100 points__

This part will be a significant effort and you shouldn't underestimate the
amount of time it will take compared to the first two parts, or based on the
number of points.  The attack itself is based on a real attack on QQ Browser
that is described at
[https://arxiv.org/abs/1802.03367](https://arxiv.org/abs/1802.03367).  We'll go
over it in class, and the majority of your effort will be in reading Python code
and understanding the attack, the amount of Python you'll actually need to
write is minimal.  Some more info about the attack is available in
`rsaattack.pdf` in the common tar ball.  You are also given
`buildkey-givetostudents.py` and `streamy.py`.  `streamy.py` parses the pcap
file and dumps the stream to stdout, and `buildkey-givetostudents.py` launches
the attack. Between `streamy.py` and `buildkey-givetostudents.py`, you only
need to write two lines of code for this part. However, you'll need to
understand the attack source code to know which two lines to write.

In the `rsa` directory of your tar ball you'll find a packet capture (or pcap)
of an attack that was carried out to recover an AES session key, and thereby
decrypt a message.  The server expects to receive an AES session key RSA
encrypted with its public key, followed by a message encrypted with that AES
session key.  The attacker mounted a side channel attack against the server,
using an encrypted communication that they eavesdropped when a victim client
communicated with the server in the past.  As the attacker carried out their
attack, they left hints embedded in the TCP protocol to make it easier to know
what phase of the attack each TCP session corresponds to.  You'll be provided
with all source code used by the server, client, and attacker, as well as the
server's public key (which you probably don't need).  You'll also be provided
with a Python script to extract the attacker hints from the packet capture and
print them as two integers per line that can be piped into your own source code
for reconstructing the AES session key and decrypting the message to get the
plaintext.  Again, submit the whole plaintext as an ASCII text file.

You will submit exactly one text file: `plaintext.txt`.  It should be
ASCII-encoded English text.  The sha512 sum is available in your tarball.

After completing this part you should have a solid understanding of the
difference between symmetric and asymmetric crypto, knowledge of the AES and RSA
algorithms specifically, and a general idea of how a chosen ciphertext attack on
a modern cipher is structured.

Submit the `plaintext.txt` file for Homework 1.4 using [this Google
form](https://forms.gle/DrXtjjoB1yCL21f98).

## (Extra Credit) Chosen plaintext attack on 3-round AES

__Due date: 31 October 2021 at 11:59pm MST__

__Note that not turning this one in won't count against your grade, it is extra credit__

__Number of points of extra credit TBD__

A 3-round implementation of AES is available in the common tar ball linked to
above.  Develop a chosen plaintext attack against it.  When you have a working
attack (please don't request ciphertext before your attack is actually working
in your own tests because the file transfers will be large and logistics
non-trivial), make arrangements with Prof. Crandall to receive ciphertext
corresponding to plaintext you provide.  Prof. Crandall will use the same key
he used for encrypting `part4ciphertext.bin`, so you can then turn in the
plaintext that corresponds with it along with your source code.  Note that if
you choose to attempt the extra credit you'll be largely on your own when it
comes to figuring out the details of mounting a chosen plaintext attack.  We
can provide resources and general directions but cannot invest too much time in
helping with specifics because of the large number of students who will likely
need help on the main part of the assignment.

**You will submit this one over email to Prof. Crandall.**
Submit a tarball with the plaintext and your source code.

# UPDATE

The new deadline for homeworks 1.2, 1.3, and 1.4 is **October 31st, 2021**.  You
can now resubmit as many times as you like, I'll always grade the latest one.
You can check your grades (which I'll post periodically between now and the
deadline) and update your submission.  You can submit and get full credit even
if you didn't submit anything by the original deadline.  I want to get this
right and make sure you all do well on homework 1.  I'll try to fix all the
logistical issues with how homeworks are submitted for homework 2.

## How to check your grades

You can check your grades on 1.2 and 1.3 by taking this URL and replacing
"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN" with your MD5 digest:

[https://207.246.62.10/gradestoreturn/NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN.txt](https://207.246.62.10/gradestoreturn/NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN.txt)

### I turned something in but there is no text file with my grades, I get a 404 error...

Send me an email from your @asu.edu email address and give me your MD5 and ID number.

### I'm happy with my grade, do I need to re-submit anything?

No, no need to resubmit.

### I thought I got it exactly correct, but the grade doesn't reflect that.

Make sure that you turned in the right file in the right place, everything you
turned in was a text file with something at least resembling English in it, and
that you matched the sha512sum.  If you still don't know what the problem was,
post a private message to me in Piazza and include your ASUrite ID.

### I don't have my tar ball yet, or I don't know where to get started on 1.2 and/or 1.3.

I plan on doing one last round of tar balls soon.  You should have started on
the homework a long time ago, you're benefiting from the extension that was due
to logistical errors but you really need to start keeping up with the course.
Homework 2 will be assigned very soon and overlap with homework 1, so the sooner you get homework 1 done the better.

### I sent you my homework 1.2 or 1.3 by email and/or did the extra credit for 1.1

You'll need to resubmit 1.2 or 1.3 through the Google form.  I received too
many such emails to manually grade them all.  I haven't yet graded the extra
credit for 1.1, but will.
