#!/bin/bash

python3 -m markdown -x markdown.extensions.tables syllabus.md > syllabus.html
python3 -m markdown -x markdown.extensions.tables _index.md > index.html

