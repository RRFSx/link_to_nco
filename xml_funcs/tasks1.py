#!/usr/bin/env python
import os
from xml_funcs.base import xml_task, source, get_cascade_env

### begin of rap --------------------------------------------------------
def rap(xmlFile, expdir, meta_id, start, stop):
  meta_id=meta_id
  cycledefs=meta_id
  # metatask (nested or not)
  start=start
  stop=stop
  interval=1
  meta_hr= ''.join(f'{i:02d} ' for i in range(start,stop+1,interval)).strip()
  command=f'{expdir}/rap.link_to_nco_namespace.sh'
  meta_bgn=f'''
<metatask name="{meta_id}">
<var name="fhr">{meta_hr}</var>'''
  meta_end=f'\
</metatask>\n'
  task_id=f'{meta_id}_f#fhr#'

  COMINrap=os.getenv("COMINrap","COMINrap_not_defined")
  # Task-specific EnVars beyond the task_common_vars
  dcTaskEnv={
    'CDATE': '<cyclestr>@Y@m@d@H</cyclestr>',
    'GRBFILE': f'<cyclestr>{COMINrap}/@y@j@H0000#fhr#</cyclestr>'
  }

  # dependencies
  timedep=""
  realtime=os.getenv("REALTIME","false")
  starttime=get_cascade_env(f"STARTTIME_{task_id}".upper())
  if realtime.upper() == "TRUE":
    timedep=f'\n    <timedep><cyclestr offset="{starttime}">@Y@m@d@H@M00</cyclestr></timedep>'
  dependencies=f'''
  <dependency>
  <and>{timedep}
    <datadep age="00:01:00"><cyclestr>{COMINrap}/@y@j@H0000#fhr#</cyclestr></datadep>
  </and>
  </dependency>'''
  #
  xml_task(xmlFile,expdir,task_id,cycledefs,dcTaskEnv,dependencies,True,meta_id,meta_bgn,meta_end,command)
### end of rap --------------------------------------------------------
