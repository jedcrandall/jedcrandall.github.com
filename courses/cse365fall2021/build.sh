#!/bin/bash

python3 -m markdown -x markdown.extensions.tables syllabus.md > syllabus.html
python3 -m markdown -x markdown.extensions.tables _index.md > index.html
python3 -m markdown -x markdown.extensions.tables hw1part1.md > hw1part1.html
python3 -m markdown -x markdown.extensions.tables hw1rest.md > hw1rest.html

