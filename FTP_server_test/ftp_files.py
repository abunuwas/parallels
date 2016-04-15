import os
import time
import shutil 
import random

from settings.config import FTP_SERVER

assets = os.path.join(FTP_SERVER, 'assets')
ftp_repo = os.path.join(FTP_SERVER, 'FTP_repo')

def download_video():
	for root, _, videos in os.walk(assets):
		for v in videos:
			yield os.path.abspath(os.path.join(root, v))

def get_destination_file_name(video, camera_id, serial_number):
	video_name, file_format = os.path.splitext(os.path.basename(video))
	destination_file_name = '{video_name}_{camera_id}_{serial_number}{format}'.format(
									video_name=video_name, camera_id=camera_id, 
									serial_number=serial_number, format=file_format)
	return destination_file_name

def copy_video(video, camera_id, serial_number):
	'''
	shutil.copy preserves little metadata from the file; for this reason shutil.copy2,
	which uses copystat() to preserve metadata, is preferred. However, even shutil.copy2 
	may not be fully capable of preserving all necessary metadata. A better solution might 
	have to be sought if needed. 
	'''
	destination_file_name = get_destination_file_name(video, camera_id, serial_number)
	camera_dir = os.path.join(ftp_repo, camera_id)
	destination = os.path.join(camera_dir, destination_file_name)
	shutil.copy2(video, destination, follow_symlinks=True)

def get_camera_id():
	alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	camera_id = ''
	for i in range(0,4):
		camera_id += alphabet[random.randint(0, len(alphabet)-1)]
	return camera_id

def check_camera_dir(camera_id):
	if camera_id not in os.listdir(ftp_repo):
		os.mkdir(os.path.join(ftp_repo, camera_id))	

def fill_ftp(camera_id):
	e=0
	while True:
		for video in download_video():
			check_camera_dir(camera_id)
			copy_video(video, camera_id, serial_number=e)
			e+=1
			time.sleep(7)


if __name__ == '__main__':
	pass

