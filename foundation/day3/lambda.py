#coding:utf-8
import multiprocessing
a = ['hehe']
data = ['hehe']*1000

def shard(data,process=7):
  '''
  default process equal 7
  '''
  multiplication = lambda x,y:x*y
  delivery = divmod(len(data),process)
  step = delivery[0]
  for num in xrange(0, process):
    start = multiplication(step,num)
    end = len(data) if  num == (process-1) else multiplication((num+1),step)
    handle_data = data[start:end]
    yield handle_data
def demo(shard,x):
  for i in shard:
    print i,x

if __name__ == "__main__":
  sharded_data = shard(data,process=4)
  pool = multiprocessing.Pool()
  for i in sharded_data:
  #返回的数量正是进程的数量
    pool.apply_async(demo,(data,2))
  pool.close()
  pool.join()
  #调用4个进程去打印hehe