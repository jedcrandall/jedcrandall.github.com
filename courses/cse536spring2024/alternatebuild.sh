#!/bin/bash

pandoc index.md -t html -o index.html
pandoc syllabus.md -t html -o syllabus.html
pandoc syllabus.md -t pdf -o syllabus.pdf
