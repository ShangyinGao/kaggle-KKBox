import time
import threading
from queue import Queue 
import platform

# # 3nd video
# def thread_job():
# 	# print('current thread %s' % threading.current_thread())
# 	print('T1 start')
# 	for i in range(10):
# 		time.sleep(0.1)
# 	print('T1 stop')

# def T2():
# 	print('T2 start')
# 	print('T2 stop')

# def main():
# 	thread1 = threading.Thread(target = thread_job, name = 'T1')
# 	thread2 =  threading.Thread(target = T2, name = 'T2')
# 	thread1.start()
# 	thread2.start()
# 	thread1.join()
# 	print('all done')
# 	# print(threading.active_count())
# 	# print(threading.enumerate())
# 	# print(threading.current_thread())

# if __name__ == '__main__':
#     main()


# 4th video
def job(l, q):
	for i in range(len(l)):
		l[i] = l[i]**2
	q.put(l)


def multithreading():
	q = Queue()
	threads = []
	data = [[1, 2, 3], [4, 5, 6], [4, 4, 4], [3, 5, 7]]

	for i in range(4):
		t = threading.Thread(target = job, args = (data[i], q))
		t.start()
		threads.append(t)
	for thread in threads:
		thread.join()
	results = []
	for _ in range(4):
		results.append(q.get())
	print(results)



if __name__ == '__main__':
	multithreading()
	print('This is ', platform.system())
