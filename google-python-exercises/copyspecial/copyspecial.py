#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def get_special_paths(dir):
  filenames = os.listdir(dir)
  absolutePaths = []
  for each in filenames:
    match = re.search(r'__\w+__', each)
    if match:
      path = os.path.join(dir,each)
      absolutePaths.append(os.path.abspath(path))
  return absolutePaths

def copy_to(paths,dir):
  if not os.path.exists(dir):
    os.mkdir(dir)
  for path in paths:
    shutil.copy(path, dir)

def zip_to(paths, zippath):
  zipees = ''
  for each in paths:
    zipees = zipees +' '+ each
  cmd = 'zip -j ' +zippath+' '+zipees
  print 'Command Im going to do:' + cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status:    
    sys.stderr.write(output)
    sys.exit(status)

# Write functions and modify main() to call them



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
    
  for each in args:
    result = get_special_paths(each)
    zip_to(result,tozip)
    if not todir == '':
      copy_to(result,todir)
    else: print result
  # Call your functions
  
if __name__ == "__main__":
  main()
