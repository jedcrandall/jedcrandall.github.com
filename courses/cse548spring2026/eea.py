# Run it with something like this...
# python3 eea.py > euclideexample.tex && pdflatex euclidexample.tex

import random

thebeginning=r'''
\documentclass[11pt]{beamer}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usetheme{default}
\begin{document}
'''

def egcd(a, b, maxsteps):
    steps = 2
    r = []
    s = []
    t = []
    q = []
    q.append(-666)
    q.append(-666)
    r.append(a)
    r.append(b)
    s.append(1)
    s.append(0)
    t.append(0)
    t.append(1)
    print("\\begin{tabular}{|c|c|c|c|c|}")
    print("\\hline")
    print(" i & q & r & s & t \\\\")
    i = 0
    print(" " + str(i) + " & " + "---" + " & " + str(r[i]) + " & " + str(s[i]) + " & " + str(t[i]) + " \\\\")
    i = 1
    if (maxsteps > 0):
        print(" " + str(i) + " & " + "---" + " & " + str(r[i]) + " & " + str(s[i]) + " & " + str(t[i]) + " \\\\")
    i = 2
    while True:
        q.append(int(r[i - 2]/r[i - 1]))
        r.append(r[i - 2] - q[i] * r[i - 1])
        s.append(s[i - 2] - q[i] * s[i - 1])
        t.append(t[i - 2] - q[i] * t[i - 1])
        if (steps <= maxsteps):
            print(" " + str(i) + " & " + str(q[i]) + " & " + str(r[i]) + " & " + str(s[i]) + " & " + str(t[i]) + " \\\\")
        else:
            print(" & & & & \\\\")
        if r[i] == 0:
            break
        i += 1
        steps = steps + 1
    print("\\hline")
    print("\\end{tabular}")
    return r[i - 1], steps, s[i - 1], t[i - 1]

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        abefore = a
        bbefore = b
        a, b = b, a%b
        newa = a
        newb = b
        print("$" + str(abefore) + "$ = ", end="")
        print((str(bbefore)) + " $\\times$ ", end="")
        if bbefore != 0:
            print(str(int(abefore/bbefore)), end="")
        else:
            print("Divide by zero?\\\\")
        print(" + " + str(newb) , end="")
        print("\\\\", end="")
    return a

print(thebeginning)
print(r'''
    \begin{frame}
        \vspace{10mm}  % some space from the top
        {\Huge \color{blue}Extended Euclidean Algorithm and Fermat's Little Theorem}\\
        \vspace{2mm}   % some sapc between the text and the line
        \hrule         % the line itself
        \vspace{2mm}   % some space between the line and the following text
        {\Large \color{darkgray}CSE 468 Fall 2025 -- jedimaestro@asu.edu}
    \end{frame}
''')

slidetop = r'''
    \begin{frame}
        \vspace{10mm}  % some space from the top
'''
slidebottom = r'''
    \end{frame}
'''

if True:#for i in range(10):
    print(slidetop)
    j = 888#random.randint(2,20)
    k = 54#random.randint(2,20)
    print("gcd($" + str(j) + "$,$" + str(k) + "$) == ???\\\\\smallskip")
    g = gcd(j, k)
    print(slidebottom)
    print(slidetop)
    print("gcd($" + str(j) + "$,$" + str(k) + "$) == $" + str(g) + "$")
    print(slidebottom)

if True:#for i in range(10):
    print(slidetop)
    j = 240#random.randint(2,20)
    k = 46#random.randint(2,20)
    print("egcd($" + str(j) + "$,$" + str(k) + "$) == ???\\\\\smallskip")
    g, stepsittook, s, t = egcd(j, k, 500)
    print(slidebottom)
    print(slidetop)
    print("egcd($" + str(j) + "$,$" + str(k) + "$) == $" + str(g) + "$ in " + str(stepsittook) + " steps\\\\\smallskip")
    print(str(g) + " == " + str(s) + " $\\times$ " + str(j) + " $+$ " + str(t) + " $\\times$ " + str(k))
    print(slidebottom)
    for i in range(stepsittook + 1):
        print(slidetop)
        print("egcd($" + str(j) + "$,$" + str(k) + "$) == ???\\\\\smallskip")
        g, stepsittookthistime, s, t = egcd(j, k, i)
        print(slidebottom)
    print(slidetop)
    print("egcd($" + str(j) + "$,$" + str(k) + "$) == $" + str(g) + "$\\\\\smallskip")
    print(str(g) + " == " + str(s) + " $\\times$ " + str(j) + " $+$ " + str(t) + " $\\times$ " + str(k))
    print(slidebottom)

if True:
    print(slidetop)
    p = 239 # should be prime
    e = 49 # should be less than p
    print("How to calculate $" + str(e) + "^{" + str(-1) + "}$ mod $" + str(p) + "$?\\\\")
    print("\\smallskip")
    print("Fermat's little theorem: $" + str(e) + "^{" + str(-1) + "} = " + str(e) + "^{" + str(p) + " - 2} = " + str(e) + "^{" + str(p - 2) + "} = ", str(pow(e, p - 2, p)) + "$ (mod $" + str(p) + "$)")
    print(slidebottom)

if True:#for i in range(10):
    print(slidetop)
    j = 239#random.randint(2,20)
    k = 49#random.randint(2,20)
    print("egcd($" + str(j) + "$,$" + str(k) + "$) == ???\\\\\smallskip")
    g, stepsittook, s, t = egcd(j, k, 500)
    print(slidebottom)
    print(slidetop)
    print("egcd($" + str(j) + "$,$" + str(k) + "$) == $" + str(g) + "$ in " + str(stepsittook) + " steps\\\\\smallskip")
    print(str(g) + " == " + str(s) + " $\\times$ " + str(j) + " $+$ " + str(t) + " $\\times$ " + str(k))
    print(slidebottom)
    for i in range(stepsittook + 1):
        print(slidetop)
        print("egcd($" + str(j) + "$,$" + str(k) + "$) == ???\\\\\smallskip")
        g, stepsittookthistime, s, t = egcd(j, k, i)
        print(slidebottom)
    print(slidetop)
    print("egcd($" + str(j) + "$,$" + str(k) + "$) == $" + str(g) + "$\\\\\smallskip")
    print(str(g) + " == " + str(s) + " $\\times$ " + str(j) + " $+$ " + str(t) + " $\\times$ " + str(k) + "\\\\\smallskip")

    if (t > 0):
       print("$" + str(k) + "^{" + str(-1) + "} = " + str(t) + "$") 
    else:
       print("$" + str(k) + "^{" + str(-1) + "} = " + str(j) + " - " + str(-t) + " = " + str(j-(-t)) + "$") 
    print(slidebottom)



print("\end{document}")
