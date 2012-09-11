# A most basic pomodoro timer written in Python.

A simple script, mostly cribbed from others code.
But it gets the job done.  And that job is is to
provide a timer for the [Pomodoro Technique](http://www.pomodorotechnique.com)
that is easy to use and delimits your work periods not by annoyingly locking your screen with no warning, and not by having a dancing gnome pop up and beg you to take a break, but with a tranquil and soothing *GONG* of a Tibetan bowl.  The whole point of taking a break is to not look at your screen, and with an audible cue you can do that:  have a lie down, do some exercises, meditate, walk around the office, eat a pop tart.  The possibilities are endless.

## Dependencies

You'll need to have python and ogg123 installed.  I run this on Linux but it should work on other Unices.

## Usage:


python buddhadoro.py 'WORK_TIME BREAK_TIME NUMBER_OF_WORK_SESSIONS'

e.g:

python buddhadoro.py 4 25 3 
(4 work sessions of 25 minutes each, 3 minute breaks)

After four work sessions you have a fifteen minute break.  If you haven't
eaten your pop tart by then, this is your chance.
