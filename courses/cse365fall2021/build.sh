#!/bin/bash

python -m markdown -x markdown.extensions.tables syllabus.md > syllabus.html
python -m markdown -x markdown.extensions.tables _index.md > index.html

