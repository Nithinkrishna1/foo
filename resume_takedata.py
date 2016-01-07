import resume_writedata

class Reader(object):
	def read_data_andcall(self):
		name,age,qualification=raw_input("Enter name age qulaification space separated\n").split()
		individual_detail =[name,age,qualification]
		resume_writedata.Writer().write_data(individual_detail)

	
new = Reader()
new.read_data_andcall()