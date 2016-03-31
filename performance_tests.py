from producer import event_threading, event_processing

import timeit

if __name__ == '__main__':
	'''
	The following runs reveal that threading is faster than multiprocessing. Perhaps due to the 
	overhead of launching new processes. Threading in this case works as expected, with every
	thread executing whenever another thread is idle. 
	'''
	print(timeit.timeit('event_threading()', setup='from __main__ import event_threading', number=10))
	print(timeit.timeit('event_processing()', setup='from __main__ import event_processing', number=10))