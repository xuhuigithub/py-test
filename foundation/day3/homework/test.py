#!/bin/env python
#coding:utf-8
def input_examine(input_prompt,error_prompt):
  try:
    result = raw_input(input_prompt)
    assert result.isdigit()
    return result
  except Exception:
    print error_prompt
    return None
    raise

while True:
  try:
    result = input_examine('Pls input a number', 'ERROR')
    print result
  except Exception:
    pass
