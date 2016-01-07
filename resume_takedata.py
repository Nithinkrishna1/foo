import resume_writedata

class Reader(object):
	def read_data(self):
		name=raw_input("Name:\n")
		age = raw_input("Age:\n")
		qualification = raw_input("qualification\n")
		individual_detail =[name,age,qualification]
		resume_writedata.Writer().write_data(individual_detail)

	
new = Reader_writer()
new.read_data()