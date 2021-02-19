# MetroGnome
A simple metronome written in Python using GTK. Requires Python 3.9.1 and some distribution of Linux.

New in v0.0:
* Change Time-Signature to any arbitrary fraction
* Speed Drill: Allows you to gradually increase or decrease the BPM to a target value
* Adjustable Volume

Features planned for future releases:
* Fix slight timing error introduced due to `sounddevice.wait()`. This also fixes auto-stop after 128 bars and reduces RAM usage drastically.
* Add 'Current BPM' display in Speed Drill.

To install and run, execute the following (skip packages if already installed)
```
pip install numpy scipy sounddevice gobject
git clone git@github.com:satyam-bhardwaj/metrognome.git
cd metrognome/
chmod +x metro_gui
./metro_gui
```
