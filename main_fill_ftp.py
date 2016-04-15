import os
import random
import multiprocessing as mp
from multiprocessing import Process, Pipe, Array, Manager, Pool
import threading

from FTP_server_test import ftp_files

if __name__ == '__main__':
	jobs = []
	cameras = [ftp_files.get_camera_id() for i in range(100)]
	threads = [threading.Thread(target=ftp_files.fill_ftp, args=(camera,)) for camera in cameras]
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()


