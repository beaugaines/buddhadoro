#!/usr/bin/python

"""
Crude but functional auditory Pomodoro timer, with a Buddhist-y air
"""

import sys
import time
import subprocess

# Sound constants

BOWL = "tibetan_bowl.ogg"
BELL1 = "lutine_bell_1.ogg"
BELL2 = "lutine_bell_2.ogg"
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
  print "Welcome to Buddhadoro!"
  print "You're going to do %s work sessions of %s minutes duration,\
 with %s minute rests in between." % (work_sessions, twork, trest)
  while a < work_sessions:
    alarm(BOWL)
    time.sleep(twork * 60)
    a += 1
    if a == work_sessions:
      break
    else:
      alarm(BOWL)
      time.sleep(trest * 60)
      print "You have completed %d work sessions." % a

  # Long rest session
  alarm(BELL1)
  print "You completed all %d of your work sessions.\
  Time for your long rest." % a
  time.sleep(15 * 60)
  alarm(BELL2)
  print('Well done!  You worked!')

if __name__=="__main__":
  sys.exit(main(sys.argv))


