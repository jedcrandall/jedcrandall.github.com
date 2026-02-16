#!/bin/bash

watch "ps -eo args,wchan,euid,pid | grep pipe"
