

# Course Info

- Course Name: CSE 536, Advanced Computer Network Security
- Semester: Fall 2026
- Instructor: [Jed Crandall](https://jedcrandall.github.io)
- Meeting location: Tempe Campus BYENG 209
- Canvas is where to find other course info

# Syllabus

- The syllabus is [here](https://jedcrandall.github.io/courses/cse536fall2026/syllabus.pdf).

# Slides

- [Course intro](firstdayofclasses536.pdf)
- [UNIX and OS basics](unixetc.pdf), and [some demo scripts](unixbasics.tgz)
- More to come...

# Six required reading assignments (the date on which you're responsible for each on pop quizzes is listed in parentheses)

- [Hacker's Manifesto](https://phrack.org/issues/7/3) (August 25th)
- [The UNIX Time-Sharing System](https://dl.acm.org/doi/10.1145/361011.361061) (September 1st) 
- [Capability Myths Demolished](https://papers.agoric.com/assets/pdf/papers/capability-myths-demolished.pdf) (September 15th)
- [Toward Real Microkernels](https://dl.acm.org/doi/10.1145/234215.234473) (September 29th)
- [CAP Twelve Years Later: How the "Rules" Have Changed](https://sites.cs.ucsb.edu/~rich/class/cs293b-cloud/papers/brewer-cap.pdf) (October 15th)
- [Earliest Eligible Virtual Deadline First](https://web.archive.org/web/20260225090858/https://citeseerx.ist.psu.edu/document?doi=805acf7726282721504c8f00575d91ebfd750564&repid=rep1&type=pdf) (October 27th)

# Optional reading assignments

- [Malicious Life podcast about Operation Sundevil](https://malicious.life/episode/episode-166/)
- Two papers about Werewolves, [the original](https://jedcrandall.github.io/courses/cse536spring2024/CSET12.pdf) and [a follow-up](https://jedcrandall.github.io/courses/cse536spring2024/3GSE2014.pdf)
- [Rowhammer](https://googleprojectzero.blogspot.com/2015/03/exploiting-dram-rowhammer-bug-to-gain.html)
- [MELTDOWN](sec18-lipp.pdf)
- [Fixing races for fun and profit](borisov.pdf)
- [BK16](https://arsenalexperts.com/persistent/resources/pages/BK-Case-Rona-Wilson-Report-II.zip) (Link is broken, so archived [here](BK-Case-Rona-Wilson-Report-II.zip))
- More to come...

# Homework assignments

- Will be posted in Canvas only

# What we'll be covering this semester

- UNIX basics
    - Processes, files, file systems
    - Kernel memory management
    - Pipes, wait queues, etc.
    - Security basics, user IDs, authentication, TOCTTOU, etc.
    - Rowhammer and MELTDOWN
    - Concurrency (pthreads, mutexes, etc.)
    - Virtual memory (LRU, MGLRU, etc.)
    - Interprocess communication (System V RPC, messaging queues, semaphores, shared memory, etc.)
- Advanced IPC and isolation mechanisms
    - Landlock, jails, cgroups 
    - SELinux and Mandatory Access Controls
    - Virtualization, Docker containers 
    - Wayland 
    - Android Binders 
    - Asynchronous I/O (e.g., `epoll` and `io_uring`)
    - Advanced multithreading 
    - NTSYNC 
    - Microkernels 
    - Capabilities 
    - DBUS, XNU, Mach and message passing
- Distributed systems
    - The CAP theorem 
    - REST, SOAP, PACELC, etc.
    - Two generals problem  
    - Partially ordered events 
    - Message passing and RPC
    - Distributed shared memory 
- Advanced topics in Linux CPU scheduling
    - Multilevel Feedback Queues (Solaris), CFS, and other background 
    - Linux's Earliest Eligible Deadline First scheduler 
    - Applications of `sched_ext` to AI 
    - Linux's real-time scheduling 
    - eBPF  

There will be four projects throughout the course of the semester.  Details for
each will be posted as an assignment in Canvas and you'll submit through
Canvas.  Roughly speaking, for the first three projects you'll build a
Werewolves-like game, add advanced features to it (like asynchronous I/O or a
security feature), and then make it into a distributed system.  The fourth
project will not necessarily build on your game (but maybe it could?).  It will
instead be related to Linux's new EEVDF scheduler, and you can tailor the
project to your own interests (user interfaces, AI, real-time applications,
etc.).

