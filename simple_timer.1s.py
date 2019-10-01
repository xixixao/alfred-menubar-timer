#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3

### README
# This is both an executable script for setting up a timer and a
# [bitbar](https://getbitbar.com/) plugin for displaying the timer.
# Put it in the plugin folder for Bitbar.
#
# For alfred workflow, choose a shorcut (like `t`) and Argument required,
# then use Run Script node with `/bin/bash` and:
#   `/Applications/BitBar\ Plugins/simple_timer.1s.py {query}`
# (replace with appropriate plugin folder path). Prepared Alfred workflow
# is saved next to this script.

import math
import time
import os
import sys
import re

def match(string, regex):
  result = re.match(regex, string)
  return None if result is None else int(result.group(1))

def write(string):
  f = open(os.path.expanduser("~/.alfred_timer_start"), "w")
  f.write(string)
  f.close()

if len(sys.argv) > 1:
  timeArg = sys.argv[-1]
  nameArg = sys.argv[-2] if len(sys.argv) > 2 else None

  if timeArg == 'stop':
    write("")
  else:
    inputTimeMatch = None
    seconds = match(timeArg, r'^(\d+)s(ec(onds?)?)?$')
    if seconds is not None:
      inputTimeMatch = seconds
    else:
      minutes = match(timeArg, r'^(\d+)m(in(utes?)?)?$')
      if minutes is not None:
        inputTimeMatch = minutes * 60
      else:
        hours = match(timeArg, r'^(\d+)h(ours?)?$')
        if hours is not None:
          inputTimeMatch = hours.group(1) * 3600

    name = " {}".format(nameArg) if nameArg is not None else ''

    if inputTimeMatch is not None:
      deadline = int(time.time()) + inputTimeMatch
      write("{}{}".format(deadline, name))
else:
  deadline = None
  name = ''
  with open(os.path.expanduser("~/.alfred_timer_start"), "r") as f:
    input = re.match(r'^(\d+)( (.*))?$', f.read())
    if input is not None:
      deadline = int(input.group(1))
      nameString = input.group(3)
      if nameString is not None:
        name = '{} '.format(nameString)
  if deadline is not None:
    totalSeconds = math.ceil(deadline - time.time())
    minutes = math.floor(totalSeconds / 60)
    seconds = totalSeconds % 60

    print('{}{}:{}'.format(name, minutes,seconds))
  # Delete this branch if you don't want to display the icon instead of "Bitbar"
  else:
    print('⏱')
