import resume_writedata
import fileexport

class Reader(object):
	def user_detail(self):
		user_data=[]
		individual_detail =['name','age','qualification']
		for title in individual_detail:
			print "enter {}".format(title)
			data = raw_input()
			user_data.append(data)
		fileexport.CreateFile().create(individual_detail,user_data)



new = Reader()
new.user_detail()