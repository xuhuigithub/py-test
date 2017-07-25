#coding:utf-8
'''
if data == 'account/login':
  account.login()
elif data == 'account/logout':
  account.logout()
import backend.account
mode1 = getattr(backend.account,'account')
mode1.login()

data = raw_input('请输入地址')
array = data.split('/')
print array
userspace = __import__('backend.' + array[0])
mode1 = getattr(userspace,array[0])

func = getattr(mode1,array[1])

func()



data = raw_input('请输入地址')

array = data.split('/')
print array
userspace = __import__('backend.' + array[0])
#假设这只是import了一个文件夹
module1 = getattr(userspace,array[0])
#而真正的模块在文件夹中，需要用getattr取出
func = getattr(module1,array[1])


func()
'''
def urlsplit(request,viewfile,arg):
  view = request.split('/')[0]
  action = request.split('/')[1]
  namespce = __import__("%s.%s"%(viewfile,view))
  module = getattr(namespce,view)
  func = getattr(module,action)
  if arg:
    result = func(arg)
  else:
    result = func()
  return result

if __name__ == '__main__':
  urlsplit('account/login','backend')
