#!/usr/bin/python
import re
class Command:
   def __init__(self,name,arguments,options):
       #value of the command
       self.name = name
       #list of arguments
       self.arguments = arguments
       #list of dicts representing options
       self.options = options

class Argument:
  #An Argument given to a command in PulsrShell
   def __init__(self,name,command):
     #name of the argument
     self.name = name
     #command the argument has been passed to
     self.command = command

class Option:
     #An Option given to a command in PulsrShell
     def __init__(self,name,command,value):
       #name of the option
       self.name = name
       #command the option has been evoked upon
       self.command = command
       #value passed to option
       self.value = value

class Parser:
  def __init__(self):
    pass #dont really need to do anything on init
  def parse(self,Args):
    Args = Args 
    CommandString = Args[0] # argv[0] is going to be the command itself
    Args.pop(0)
    Arguments = [] # list of arguments objects
    Options = [] # list of option objects
   
    # Parse argv to separate arguments from options
    for arg in Args:
      match = re.match(r'^--\w+', arg, re.M|re.I) #regex to match options
      if match: #if string matches regex, it is an "option"
        if "=" in arg: #checking if the option has a value 
          list = arg.split('=')
          OptionOb = Option(list[0],CommandString,list[1]) #create option object with the value
        else:
           OptionOb = Option(arg,CommandString,'') #no value given for option, so created with null value
        Options.append({"name": OptionOb.name,"value": OptionOb.value}) # add options object to list
      else:
        ArgOb = Argument(arg,CommandString) # since string did not match above regex, its an argument
        Arguments.append(ArgOb.name)   
    command = Command(CommandString,Arguments,Options) #create command object to be utilized by other components of cheli
    return(command)

