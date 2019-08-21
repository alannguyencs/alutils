from . import altime

def update_content(file_path, content):
	log_file = open(file_path, 'a')
	log_file.write(content + '\n')
	log_file.close()

class Allog():
	def __init__(self, log_file_path):
		self.log_file_path = log_file_path

		time_stamp = altime.get_timestamp()
		header_content = '\n' * 3 + '-' * 100 + '\n' + time_stamp
		update_content(self.log_file_path, header_content)

	def update(self, content):
		print (content)
		update_content(self.log_file_path, content)
