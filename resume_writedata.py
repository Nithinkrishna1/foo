class Writer(object):
	def write_data(self,name,age,qualification):
		filehandler = open("resume.txt",'a')
		filehandler.write(name)
		filehandler.write(" ")
		filehandler.write(str(age))
		filehandler.write(" ")
		filehandler.write(qualification)