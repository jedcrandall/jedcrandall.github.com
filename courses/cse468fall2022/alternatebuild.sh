#!/bin/bash

# python3 -m markdown -x markdown.extensions.tables syllabus.md > syllabus.html
# python3 -m markdown -x markdown.extensions.tables _index.md > index.html
# python3 -m markdown -x markdown.extensions.tables hw1part1.md > hw1part1.html
# python3 -m markdown -x markdown.extensions.tables hw1rest.md > hw1rest.html

#pandoc hw3.md -t html -o hw3.html
#pandoc hw2.md -t html -o hw2.html
#pandoc hw1rest.md -t html -o hw1rest.html
pandoc index.md -t html -o index.html
pandoc syllabus.md -t html -o syllabus.html
pandoc hw1part1.md -t html -o hw1part1.html
pandoc hw1part2.md -t html -o hw1part2.html
pandoc hw1part3.md -t html -o hw1part3.html
