import write

class Reader_writer(object):
	def read_data(self):
		name=raw_input("Name:\n")
		age = int(raw_input("Age:\n"))
		qualification = raw_input("qualification\n")
		write.Writer().write_data(name,age,qualification)
	

new = Reader_writer()
new.read_data()