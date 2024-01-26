#!/bin/bash

pidof stress | sort -n | sed "s/ /\n/g" | while read p; do
#cat /proc/$p/cmdline
#echo ""
echo $p
cat /proc/$p/sched | grep vruntime
done
