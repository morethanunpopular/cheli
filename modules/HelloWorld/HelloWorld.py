#!/usr/bin/python
class execute:
  def __init__(self,arg,option):
    if not arg:
      arg = "World"
    arg = ''.join(arg)
    if option:
      if isinstance(option[0], dict):
        option = option[0]['name']    
      if option == "--reverse":
        print "!{0}, Hello".format(arg)
    else:
      print "Hello, {0}!".format(arg)


