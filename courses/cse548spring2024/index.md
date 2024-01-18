

# Course Info

- Course Name: CSE 548, Advanced Network Security
- Semester: Spring 2024
- Instructor: [Jed Crandall](https://jedcrandall.github.io)
- More info is in the syllabus, see below.  Also check Canvas.

# Syllabus

- The syllabus is [here](syllabus.html), also available as a [PDF](syllabus.pdf).

We'll take a first principles approach to learning about the cryptography and
protocols that are widely used on the Internet.  If you're likely to see
something in a PCAP or the physical layer of an Internet hop, we want to
understand why things work the way they do all the way down the physics,
history, and mathematics that define it.  E.g., to understand the crypto behind
applications and protocols such as HTTPS (i.e., TLS), Tor, Signal/WhatsApp,
WPA3, etc. we'll drill all the way down into classical and quantum physics.  To
understand why IP and TCP fields such as the IPID, TTL, source port, and flags
are set in certain ways (e.g., randomized) we'll cover the major side channel
attacks that shaped these protocols and implementations over the past 50 years.
To understand why Internet censorship and circumvention tools and techniques
work the way they do, we'll start with how basic results from distributed
systems and Einstein's theory of special relativity define the parameters of
this adversarial relationship.

# Midterm and Final dates

- The midterm will be during the regularly scheduled class period on Wednesday, March 20th. 
- The final will be on Monday, April 29th from 12:10pm to 2:00pm.

# Slides

- [Course intro](courseintro.pdf)
- [Introduction to network security](intronetsecurity.pdf)
- [Symmetric crypto through the 80s](symmetricryptothru80s.pdf)
- [AES and block cipher modes](aesciphermodes.pdf)

# Monday Readings


- 1/22: *Two readings*... [MiniAES specification](miniaesspec.pdf) *and* [a tutorial about linear and differential cryptanalysis](ldc_tutorial.pdf) 
- 1/29: *Two readings*... [Diffie-Hellman](diffiehellman.pdf) *and* [RSA](Rsapaper.pdf)
- 2/5: [OTR](otr-wpes.pdf) 
- 2/12: [Certs and MD5 collisions](md5collisions.pdf) 
- 2/19: [KRACK Attacks](krackccs2017.pdf) 
- 2/26: [An Analysis of China's "Great Cannon"](foci15-paper-marczak.pdf) 
- 3/4: [TSPU: Russia's Decentralized Censorship System](tspu-imc22.pdf) 
- 3/11: Sring break
- 3/18: [Ptacek and Newsham](PtacekNewsham98.pdf) 
- 3/25: [Tor](ADA465464.pdf)
- 4/1: [ScrambleSuit](wpes13-scramblesuit.pdf), [Xue et al. on TLS-in-TLS](https://www.usenix.org/system/files/sec24summer-prepub-465-xue.pdf), [Wails et al.](https://www.robgjansen.com/publications/precisedetect-ndss2024.pdf), *or* [Xue et al. on OpenVPN](https://www.usenix.org/system/files/sec22-xue-diwen.pdf) --- You only have to pick one and read it, but be ready to explain it to those in the class who chose a different paper.
- 4/8: [Knockel FOCI 2014 side channel](foci2014.pdf) and [DV++](https://dl.acm.org/doi/pdf/10.1145/3243734.3243790)
- 4/15: [Blind in/on-path attacks on VPNs](Blind-in-path-attacks-VPN-USENIX21.pdf)
- 4/22: [Pegasus](Million-Dollar-Dissident.pdf)

If you're interested in more cenroship-related papers, check out [CensorBib](https://censorbib.nymity.ch/)


# Homework assignments

- Will be posted in Canvas, not here.

