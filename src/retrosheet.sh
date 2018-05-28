#!/bin/bash
for i in {1953..1979}
do
   python retrosheet.py -y $i
done
