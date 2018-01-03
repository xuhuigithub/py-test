#!/usr/bin/env python
# encoding: utf-8
import logging
import threading, traceback, sys
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s [%(threadName)s]')
logger = logging.getLogger('test_thread')
import requests



class runScriptThread(threading.Thread):  # The timer class is derived from the class threading.Thread
    def __init__(self, funcName, *args):
        threading.Thread.__init__(self)
        self.args = args
        self.funcName = funcName
        self.exitcode = 0
        self.exception = None
        self.exc_traceback = ''

    def run(self):  # Overwrite run() method, put what you want the thread do here
        try:
            self._run()
        except Exception as e:
            self.exitcode = 1  # 如果线程异常退出，将该标志位设置为1，正常退出为0
            self.exception = e
            self.exc_traceback = ''.join(traceback.format_exception(*sys.exc_info()))  # 在改成员变量中记录异常信息

    def _run(self):
        try:
            self.funcName(*(self.args))
        except Exception as e:
            raise e

def printSth(sth):
    print requests.get("http://192.168.62.9").text

if __name__ == '__main__':
    sth = 'hello world'
    try:
        aChildThread = runScriptThread(printSth,sth)
        aChildThread.start()
        aChildThread.join()
    except Exception as e:
        print(aChildThread.exc_traceback)
