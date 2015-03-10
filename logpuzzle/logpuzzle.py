#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def url_sorter(url):
  url_match = re.search(r'p-(\w\w\w\w)-(\w\w\w\w)', url)
  if url_match:
    return url_match.group(2)
  else:
    return url

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  find_host = re.search(r'_(.+)', filename)
  host_name = 'http://' + find_host.group(1)
  puzzle_url = []

  with open(filename) as f:
    for lines in f:
      find_urls = re.search(r'GET\s([\S\w]+puzzle[\S\w]+)\sHTTP', lines)
      if find_urls:
        url = host_name + find_urls.group(1)
        if not url in puzzle_url:
          puzzle_url.append(url)
  puzzle_url.sort(key = url_sorter)
  return puzzle_url


def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # Exits the program if directory name already exists
  try:
    os.mkdir(dest_dir)

  except OSError:
    print "Folder already exists!!! Try another name"
    sys.exit()

  # Retrieving image from url, naming the image file and generating html code
  count = 1
  img_tag = ''
  for url in img_urls:
    print "Retrieving--------->" + url
    image_name = os.path.abspath(dest_dir) + '/' + "img" + str(count)
    urllib.urlretrieve(url, filename = image_name)
    img_tag = img_tag + '<img src=' + '"' + image_name + '">'
    count += 1

  index_html = '<verbatim>\n<html>\n<body>\n' + img_tag + '\n<body>\n<html>'

  index_file = open(dest_dir + '/' + 'index.html', 'w')
  index_file.write(index_html)
  index_file.close()

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])
  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
