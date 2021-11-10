#!/bin/bash

cat $1 | grep -v "^#" | tr -d [:space:]

