# A relaxing, auditory pomodoro timer written in Python.

A simple Python script for enthusiasts of the the [Pomodoro Technique](http://www.pomodorotechnique.com) that is easy to use and delimits your work periods not by annoyingly locking your screen with no warning, and not by having a dancing gnome pop up and beg you to take a break, but with a tranquil and soothing *GONG* of a Tibetan bowl.  The whole point of taking a break is to not look at your screen, and with an audible cue you can do that:  have a lie down, do some exercises, meditate, walk around the office, eat a pop tart.  The possibilities are endless.

## Dependencies

You'll need to have python and ogg123 installed.  Should work on all Unices.  Otherwise unknown.

## Usage:

python buddhadoro.py 'NUMBER_OF_WORK_SESSIONS WORK_TIME BREAK_TIME'

e.g:

python buddhadoro.py 4 25 3 
(4 work sessions of 25 minutes each, 3 minute breaks)

After four work sessions you have a fifteen minute break.  If you haven't
eaten your pop tart by then, this is your chance.

## To-Do

- I'd like a selection of different tones for the alarm.  Or at least different pitches of that tibetan bowl, to make the start and end of periods more obvious.
- I'd like a gui
- I'd like to add functionality to keep track of the various pomodoros we do during   the day - probably via SQLite

## License

&copy; 2012 Beau Gaines, release under the MIT license.

