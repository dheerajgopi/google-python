#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

def file_read(filename):
# generator function for yielding lines
  with open(filename) as f:
    for lines in f:
      yield lines.split()

def build_dict(filename):
# building dict with word as key and count as value
  res_dict = {}
  for lines in file_read(filename):
    for words in lines:
      word = words.lower()
      res_dict[word] = res_dict.setdefault(word, 0) + 1
  return res_dict

def build_list(word_dict):
# for building a list containing tuples of word and count
  word_list = []
  for k, v in word_dict.items():
    word_list.append((k, v))
  return word_list

def print_words(filename):
# printing the words and its count in alphabetic order
  word_dict = build_dict(filename)
  word_list = build_list(word_dict)
  word_list.sort()
  for word, count in word_list:
    print word, '---', count

def print_top(filename):
# printing 20 most commonly used words
  word_dict = build_dict(filename)
  word_list = build_list(word_dict)
  word_list.sort(key = lambda x:x[1], reverse = True)
  for i in xrange(20):
    print word_list[i][0],'----', word_list[i][1]

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
