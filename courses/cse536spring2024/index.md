

# Course Info

- Course Name: CSE 536, Advanced Operating Systems
- Semester: Spring 2024
- Instructor: [Jed Crandall](https://jedcrandall.github.io)
- More info is in the syllabus, see below.  Also check Canvas.

# Syllabus

- The syllabus is [here](syllabus.html), also available as a [PDF](syllabus.pdf).

The class will be organized around the game Werewolves, a Linux-based game
based on Mafia that involves interprocess communication and exploitation of
side channels.  For the first half of the course, we'll learn all the ins and
outs of a Linux system and its basic security mechanisms (process separation
via virtual memory, file systems, CPU scheduling, etc.) through readings,
homework assignments, and playing Werewolves.   We'll mostly read papers that
attack the security of Linux and UNIX systems because those papers are the best
way to learn how a system works.  For the second half of the course, we'll read
some foundational papers about distributed systems and work on a project to
re-think Werewolves as a distributed system.

# Midterm and Final dates

- The midterm will be during the regularly scheduled class period on Monday, March 25th. 
- The final will be on Wednesday, May 1st from 9:50am to 11:40am.

# Slides

- [Course intro](courseintro.pdf)
- [UNIX and security basics](unixandsecbasics.pdf)
- [Scheduling and wait queues](schedandwaitqueues.pdf), and a script for the [demo](sched.sh)
- The newest version of Werewolves is [here](werewolves-spring24.tgz)
- [Virtual memory, Rowhammer, and Meltdown](virtualmemrowhammerandmeltdown.pdf)
- [File systems](fs.pdf)
- [Intro to distributed systems and concurrency](distributedsystemsintro.pdf)
- [Semaphores, deadlocks, mutex's, monitors, futex's, etc.](concurrencybasics.pdf)
- [Midterm notes](midtermnotes.pdf)
- [Asynchronous I/O](asynchio.pdf)

# Wednesday Readings


- 1/17: *Two readings* about Werewolves... [this one](CSET12.pdf) *and* [this one](3GSE2014.pdf) 
- 1/24: *Two readings* about the confinement problem... [a note](lampson73.pdf) *and* [a comment](https://dl.acm.org/doi/pdf/10.1145/800213.806537) 
- 1/31: [setuid() demystified](setuid-usenix02.pdf)
- 2/7: [Fixing races for fun and profit](borisov.pdf) 
- 2/14: [Rowhammer](https://googleprojectzero.blogspot.com/2015/03/exploiting-dram-rowhammer-bug-to-gain.html) 
- 2/21: [MELTDOWN](sec18-lipp.pdf) 

- 2/28: [BK16](https://arsenalexperts.com/persistent/resources/pages/BK-Case-Rona-Wilson-Report-II.zip) (Link is broken, so archived [here](BK-Case-Rona-Wilson-Report-II.zip))
- 3/6: Sring break
- 3/13: [Lamport](time-clocks.pdf) 
- 3/20: [Dijkstra](EWD123.PDF) 
- 3/27: [RPC](birrell842.pdf)
- 4/3: [Elements of Interaction](https://dl.acm.org/doi/pdf/10.1145/151233.151240)
- 4/10: [Eraser](Tocs97.pdf) (optional)
- 4/17: [p2p](cacm03.pdf) (optional)
- 4/24: [Priority inversion](https://www.cse.chalmers.se/~risat/Report_MarsPathFinder.pdf) (optional)

# Homework assignments

- Will be posted in Canvas, not here.

