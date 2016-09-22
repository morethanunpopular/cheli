#!/usr/bin/python
import sys
def RunCommand(command,args,options):
  moduleString = "{0}.{0}".format(command)
  commandObject = __import__(moduleString, globals(), locals(), ['execute'], -1) 
  try:
    commandObject.__dict__['execute'].__dict__
  except:
    print "[!!] Fatal Error! Command has no execute class"
    sys.exit()
  commandObject.execute(args,options)
