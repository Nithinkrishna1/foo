import resume_writedata

class Reader_writer(object):
	def read_data(self):
		name=raw_input("Name:\n")
		resume_writedata.Writer().write_data(name)
		age = raw_input("Age:\n")
		resume_writedata.Writer().write_data(age)
		qualification = raw_input("qualification\n")
		resume_writedata.Writer().write_data(qualification)
	

new = Reader_writer()
new.read_data()