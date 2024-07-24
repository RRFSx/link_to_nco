#!/usr/bin/env bash
src="/lfs4/BMC/wrfruc/Chunhua.Zhou/data/GFS"
dst="/lfs5/BMC/nrtrr/FIX_RRFS2/staged_data/ops_tmp/GFS"

#2414818000078
#gfs.yyymmdd/HH/gfs.t12z.pgrb2.0p25.f002 
for GRIBFILE in ${src}/*; do
  fname=${GRIBFILE##*/}
  echo ${fname}
  yyyy=20${fname:0:2}
  ndays=$(( ${fname:2:3} - 1 ))
  yyyymmdd=$(date -d "${ndays} days ${yyyy}-01-01" +"%Y%m%d")
  HH=${fname:5:2}
  fhr=$((10#${fname:7:6}))
  fhr=$(printf "%03d" ${fhr})

  fpath=${dst}/gfs.${yyyymmdd}/${HH}
  mkdir -p ${fpath}
  ln -snf ${GRIBFILE} ${fpath}/gfs.t${HH}z.pgrb2.0p25.f${fhr} #do hard links by the file owner if possible
  #ln -f ${GRIBFILE} ${fpath}/gfs.t${HH}z.pgrb2.0p25.f${fhr} #do hard links by the file owner if possible
done
