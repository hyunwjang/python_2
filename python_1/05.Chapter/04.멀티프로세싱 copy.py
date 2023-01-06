from multiprocessing import Process
import time

class subprocess(Process):

    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print(f'[sub] {self.name} start')
        time.sleep(2)
        print(f'[sub] {self.name} end')



if __name__ == '__main__':
    print('[main] start')
    p = subprocess(name = 'startcoding')
    p.start()
    p.join()
    print('[main] end')
