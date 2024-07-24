#!/bin/bash

for file in ./GFShd/GFS/**/*/*; do
  newname=${file/prb2/pgrb2}
  mv ${file} ${newname}
done
