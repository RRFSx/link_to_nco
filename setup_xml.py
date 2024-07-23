#!/usr/bin/env python
#
import os, sys, stat
from xml_funcs.base import header_begin, header_entities, header_end, source, \
  wflow_begin, wflow_log, wflow_cycledefs, wflow_end
from xml_funcs.tasks1 import rap

### setup_xml
def setup_xml(expdir):
  # source the config cascade
  source('exp.setup')
  #
  dcCycledef={}
  dcCycledef['rap']=os.getenv('CYCLEDEF_RAP')
  dcCycledef['rap_g2']=os.getenv('CYCLEDEF_RAP_G2')

  fPath=f"{expdir}/link.xml"
  with open(fPath, 'w') as xmlFile:
    header_begin(xmlFile)
    header_end(xmlFile)
    wflow_begin(xmlFile)
    log_fpath=f'{expdir}/logs/rrfs.@Y@m@d/@H/link.log'
    wflow_log(xmlFile,log_fpath)
    wflow_cycledefs(xmlFile,dcCycledef)
    
    # assemble tasks for an experiment or setup/generate an xml file
    rap(xmlFile,expdir)
    #rap_g2(xmlFile,expdir)
    #
    wflow_end(xmlFile)

  fPath=f"{expdir}/run_rocoto.sh"
  with open(fPath,'w') as rocotoFile:
    text= \
f'''#!/usr/bin/env bash
source /etc/profile
module load rocoto
cd {expdir}
rocotorun -w rrfs.xml -d rrfs.db
'''
    rocotoFile.write(text)

  # set run_rocoto.sh to be executable
  st = os.stat(fPath)
  os.chmod(fPath, st.st_mode | stat.S_IEXEC)

  print(f'link.xml and run_rocoto.sh has been created.')
### end of setup_xml

### run setup_xml.py from the command line
if __name__ == "__main__":
  expdir = os.path.dirname(os.path.realpath(__file__))
  setup_xml(expdir)
