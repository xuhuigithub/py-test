#!/usr/bin/env python
#encoding: utf-8


def main(max):
  i = 0
  while i < max:
    i += 1
    yield i


if __name__ == '__main__':
  for i in main(4):
   print i