import resume_writedata
import write_csv

class Reader(object):
	def user_detail(self):
		user_data=[]
		individual_detail =['name','age','qualification']
		for title in individual_detail:
			print "enter {}".format(title)
			data = raw_input()
			user_data.append(data)
		self.export_option(individual_detail,user_data)

		
 	def export_option(self,individual_detail,user_data): 

 		option = int(raw_input("EXPORT OPTIONS:\n1:\ttext file\n2:\tcsv\n"))
 		if (option == 1):
 			resume_writedata.Writer().write_data(user_data)
 		elif(option == 2):
 			write_csv.CreateCsv().csv_create(individual_detail,user_data)


new = Reader()
new.user_detail()