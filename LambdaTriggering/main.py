import os
import time

'''
script to calcluate average number of round trip
'''

def run(x):

    start = time.time()
    
    for i in range(x):
        os.system(<trigger_link>)
    
    print ((time.time()-start)/x)

if __name__ == '__main__':
    
    run(50)
