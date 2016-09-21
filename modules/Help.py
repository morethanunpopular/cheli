#!/usr/bin/python
import json
class Helper:
  def __init__(self,command):
    self.command = command.name
    OptSchemaFile = "modules/{0}/options.json".format(self.command)
    with open(OptSchemaFile, 'r') as fh:
      data = json.load(fh)
    self.options = data['available_options'] 
    CommandSchemaFile = "modules/{0}/command.json".format(self.command)
    with open(CommandSchemaFile, 'r') as fh:
      data = json.load(fh)
    self.description = data['description']
    self.example = data['example']
       
    
  def PrintHelpMessage(self):
    print "Name:"
    print "\t{0}\n".format(self.command.encode('utf8'))
    print "Description:"
    print "\t{0}\n".format(self.description.encode('utf8'))
    print "Usage:"
    print "\t{0}\n".format(self.example.encode('utf8'))
    print "Available Options:"
    for option in self.options:
     print '\t"{0}"        {1}'.format(option['name'].encode('utf8'), option['description'].encode('utf8'))
    print "\n"

class command:
  def __init__(self):
    self.name = "HelloWorld"

