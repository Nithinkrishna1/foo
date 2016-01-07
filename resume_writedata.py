class Writer(object):
	def write_data(self,var):
		filehandler = open("resume.txt",'a')
		filehandler.write(var)
		filehandler.write(" ")
		filehandler.close()
		