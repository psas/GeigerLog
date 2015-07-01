GeigerLog
=========

Originally written by David Ramage.  Yay David!

Written to run on the PSAS RasPi camera system number 2.  See our website
http://psas.pdx.edu/

Each time the SparkFun geiger board registers a particle or ray entering the
tube, it outputs a character (0 or 1) to the serial port.  The Geiger python
script listens on /dev/ttyUSB0 and writes the current UNIX timestamp in seconds
to a log.  Each geiger event gets one line in the log file, so multiple entries
of a single time means multiple events in that second.

uniq -c radlog-4.dat will produce a list of occurances of each second.  The
first column is the count and the second column is the timestamp in seconds.

To install the init.d startup script make a symlink from /etc/init.d/geiger to
init.d-geiger.
