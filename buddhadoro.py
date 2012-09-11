#!/usr/bin/python

"""
Second shot at a pomodoro timer
"""

import sys
import time
import subprocess

# Sound files
ALARM = "/home/sircharles/Dropbox/Dotfiles/BuddhaDoro/tibetan_bowl.ogg"
# DONE = "/home/sircharles/Sounds/alarm_clock.ogg"
DEV_NULL = open("/dev/null", "w")

def alarm(alarm):
  
  cmd = ["ogg123", alarm]
  p = subprocess.Popen(cmd, stdout = DEV_NULL, stderr = subprocess.PIPE)
  p.wait()

def main(args):
	twork, trest = args[1:]
	alarm(ALARM)
	time.sleep(int(twork) * 60)
	alarm(ALARM)
	time.sleep(int(trest) * 60)
	alarm(ALARM)

	time.sleep(int(twork) * 60)
	alarm(ALARM)
	time.sleep(int(trest) * 60)
	alarm(ALARM)

	time.sleep(int(twork) * 60)
	alarm(ALARM)
	alarm(ALARM)
	time.sleep(15 * 60)
	alarm(ALARM)

if __name__=="__main__":
	sys.exit(main(sys.argv))


