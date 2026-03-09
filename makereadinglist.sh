#!/bin/bash

cat readinglist.txt | while read line; do
  echo -n "["
  echo -n $line
  echo -n "]"
  echo -n "("
  echo -n $line
  echo ")"
  echo ""
done > /tmp/readinglist.md

pandoc /tmp/readinglist.md -t html -o readinglist.html

