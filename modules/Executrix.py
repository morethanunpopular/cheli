#!/usr/bin/python

def RunCommand(command,args,options):
  moduleString = "{0}.{0}".format(command)
  commandObject = __import__(moduleString, globals(), locals(), ['execute'], -1)  
  commandObject.execute(args,options)
