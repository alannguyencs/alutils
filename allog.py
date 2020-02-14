# from . import altime

# def update_content(file_path, content):
# 	log_file = open(file_path, 'a')
# 	log_file.write(content + '\n')
# 	log_file.close()

# class Allog():
# 	def __init__(self, log_file_path):
# 		self.log_file_path = log_file_path

# 		time_stamp = altime.get_timestamp()
# 		header_content = '\n' * 3 + '-' * 100 + '\n' + time_stamp
# 		update_content(self.log_file_path, header_content)

# 	def update(self, content):
# 		print (content)
# 		update_content(self.log_file_path, content)
from sys import stdout
import logging

class Allog():
	def __init__(self, log_file_path):
		logging.basicConfig(filename=log_file_path,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)

		self.log = logging.getLogger()
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		handler = logging.StreamHandler(stdout)
		handler.setFormatter(formatter)
		self.log.addHandler(handler)

	def info(self, message):
		self.log.info(message)