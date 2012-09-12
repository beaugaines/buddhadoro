#!/usr/bin/python

"""
Crude but functional auditory Pomodoro timer, with a Buddhist-y air
"""

import sys
import time
import subprocess

# Sound constants
ALARM = "tibetan_bowl.ogg"
DEV_NULL = open("/dev/null", "w")

# fcns
def alarm(alarm):
  
  cmd = ["ogg123", alarm]
  p = subprocess.Popen(cmd, stdout = DEV_NULL, stderr = subprocess.PIPE)
  p.wait()

def main(args):
  work_sessions, twork, trest = args[1:]
  a = 0
  work_sessions = int(work_sessions)
  twork = int(twork)
  trest = int(trest)

  # begin work session
  print "Beginning work session."
  print "You're going to do %s work sessions of %s minutes length,\
  with %s minute rests in between" % (work_sessions, twork, trest)
  while a < work_sessions:
    time.sleep(twork * 60)
    alarm(ALARM)
    time.sleep(trest * 60)
    a += 1
    alarm(ALARM)

  # Long rest session
  print('Time for your long rest.')
  time.sleep(15 * 60)
  alarm(ALARM)
  print('Well done!  You worked!')

if __name__=="__main__":
  sys.exit(main(sys.argv))


