#!/bin/bash

# sleep for some period of time to give internet connection a chance to come up, in case
# this is being run right after machine wakes up from sleep.
sleep 10

echo "$(date) calling: python /Users/peter/Documents/baseball/bbos/src/bbos.py -r"

python /Users/peter/Documents/baseball/bbos/src/bbos.py -r

echo "$(date) done calling: python /Users/peter/Documents/baseball/bbos/src/bbos.py -r"


