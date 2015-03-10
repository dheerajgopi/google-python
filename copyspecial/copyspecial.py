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

def get_special_path(directory):
# To get a list of paths of special files i.e filenames containing leading and trailing '__'
  special_paths = []
  files = os.listdir(directory)
  for filename in files:
    special_check = re.search(r'__(\w+)__', filename)
    if special_check:
      file_path = os.path.abspath(filename)
      special_paths.append(file_path)
  return special_paths

def copy_to(paths, directory):
# To copy the special files to dir
  if not os.path.exists(directory):
    os.mkdir(directory)

  for path in paths:
    shutil.copy(path, directory)

def zip_to(paths, zippath):
# To zip all the files
  cmd = 'zip -j ' + zippath + ' ' + ' '.join(paths)
  (status, out) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit()
  else:
    print "ZipFile created"


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

  paths = []

  for dirname in args:
    paths.extend(get_special_path(dirname))

  if todir:
    copy_to(paths, todir)
  elif tozip:
    zip_to(paths, tozip)
  else:
    print '\n'.join(paths)  

if __name__ == "__main__":
  main()
