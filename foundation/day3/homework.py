#!/bin/env python
#coding:utf-8
import pickle,hashlib

def md5algorithm(varchar):
  hashmd5 = hashlib.md5()
  hashmd5.update(str(varchar))
  result = hashmd5.hexdigest()
  return result
def login(username,userpass,verfile='D:/workspace/test/foundation/day3/homework/users'):
  with open(verfile,'r') as f:
    users = pickle.load(f)
    if users[username] == md5algorithm(userpass):
      return True
    else:
      raise ValueError
def input_examine(input_prompt,error_prompt):
  result = raw_input(input_prompt)
  if result != 'q':
    try:
      assert result.isdigit()
      return result
    except Exception:
      print error_prompt
      return None
      raise
  else:
    return 0

money_quota = 15000
ware_list = [('iphone','6000'),('computer','4000'),\
('app air','5000'),('water','30')]
price_list = [ int(x[1]) for x in ware_list]
#商品列表    
shopping_cart = []
shopping_prompt = 'pls chose the ware index'
cost = 0

while True:
  try:
    money = int(input_examine('pls input your salary:\n','salary only can be digit'))
  except Exception:
    pass
  else:
    break
#输入工资
if money > 0:
  while True:
    print 'Press any key to push out'
    for index,ware in enumerate(ware_list):
      print index+1,": ".join(ware)
    ware_index = raw_input('%s\n'%shopping_prompt)

    if  not ware_index.isdigit():
      print 'your balance: %s' %money
      quit_flag = raw_input('Pls input q to quit else Press any key to continue\n')
      if quit_flag == 'q':
        print 'your balance: %s,your wares: %s'%(money,shopping_cart)
        break
      else:
        continue
    elif int(ware_index) > len(price_list):
        shopping_prompt = 'Pls input a valid number'
        continue
    #退出判断

    if money >= int(ware_list[int(ware_index)-1][1]):
      try:
        money -= int(ware_list[int(ware_index)-1][1])
        shopping_cart.append(ware_list[int(ware_index)-1][0])
      except IndexError:
        shopping_prompt = 'Pls input a valid number'
        continue
      else:
        shopping_prompt = 'Pls chose the ware index'
    #elif money < min(price_list):#把这个换成else
    else:
      getmoney_flag = raw_input("Your balance insufficient,now you have %s',would you like to get some moeny?\n Press any key to push out or Press y to Ebter"%money)
      while getmoney_flag == 'y':
        username = raw_input('pls input your username:')
        userpass = raw_input('pls input your password:')
        try:
          login(username, userpass)
        except Exception:
          print 'login failed'
          pass
        else:
          draw_money = raw_input('pls input how many money you want to draw?')
          if not draw_money.isdigit():
            print "you cant't draw these money"
            continue
          elif int(draw_money) > money_quota:
            print "you cant't draw these money"
            continue
          else:
            money += int(draw_money)
            money_quota -= int(draw_money)
            print 'now you have %s' %money
            break
      else:
        continue
else:
  print "quit!"