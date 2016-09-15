import json
from termcolor import colored

#objects used to validate commands against definitions provided in options.json and arguments.json

class Validator:

  def __init__(self,command):
    # accepts a command object as an argument (see ArgParser.py for details on command objects)
    self.command = command 
  
  def validArguments(self):
    #Validate Arguments Against the arguments.json file
    ArgSchemaFile = "modules/{0}/arguments.json".format(self.command.name)
    with open(ArgSchemaFile, 'r') as fh:
      data = json.load(fh)
    #checking if more arguments than are accepted have been provided
    if len(self.command.arguments) > data['number_of_possible_arguments']:
      print colored("[!!] To many arguments provided", "red")
      return False
    #checking if the arguments passed contain the minimum required
    elif len(self.command.arguments) < data['number_of_required_arguments']: 
      print colored("[!!] Missing required arguments", "red")
      return False
    else:
      return True

  def validOptions(self):
    OptSchemaFile = "modules/{0}/options.json".format(self.command.name)
    with open(OptSchemaFile, 'r') as fh:
      data = json.load(fh)    
    #checking if the options passed exceed maximum possible
    if len(self.command.options) > data['number_of_possible_options']: 
      print colored("[!!] To many options provided", "red")
      return False
    #checking if the options passed do not include required options
    elif len(self.command.options) < data['number_of_required_options']: 
      print colored("[!!] Missing required options", "red")
      return False
    else:
      suppliedOptions = [] #list of options parsed from the command line
      numberInvalid = 0 # total number of options provided that are not provided for in options.json
      invalidOptions = [] #list of incorrect options passed

      #iterate through all options to check them against those defined in options.json
      for option in self.command.options:
        suppliedOptions.append(option['name'])
      availableOptions = []
      for option in data['available_options']:
        availableOptions.append(option['name'].encode("utf8"))
      for option in suppliedOptions:
        if option not in availableOptions:
          numberInvalid = numberInvalid + 1
          invalidOptions.append(option)
      if numberInvalid > 0:
        print colored("[!!] The following invalid options for {0} were provided:".format(self.command.name), "red")
        for option in invalidOptions:
          print colored(option, "red") 
        return False
      else:
        return True

