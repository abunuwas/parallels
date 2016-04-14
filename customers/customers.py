import multiprocessing as mp
import requests
import time

def call_app():
	r = requests.get('http://127.0.0.1:5000/')
	e=0
	while True:
		e += 1
		print(r.status_code, ' in iteration %s' % str(e))
		time.sleep(2)

if __name__ == '__main__':
	jobs = []
	for i in range(0, 10):
		process = mp.Process(target=call_app)
		jobs.append(process)

	for j in jobs:
		j.start()

	for j in jobs:
		j.join()


