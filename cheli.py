#!/usr/bin/python
import sys
from modules import ArgParser
from modules import Executrix 
from modules import Validator
from pprint import pprint

def main():
  #process CLI Args
  Args = sys.argv
  Args.pop(0)
  try:
    CommandData = ArgParser.Parser().parse(Args)
  except:
    print "Invalid Arguments or Command provided"
    sys.exit()
  #validate command against provided scheme
  validator = Validator.Validator(CommandData)
  if not validator.validArguments():
    sys.exit()
  if not validator.validOptions():
    sys.exit()

  #execute command
  Executrix.RunCommand(CommandData.name,CommandData.arguments,CommandData.options)

if __name__ == "__main__":
    main()
  
