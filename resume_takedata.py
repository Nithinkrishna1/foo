import resume_writedata

class Reader(object):
	def user_detail(self):
		user_data=[]
		individual_detail =['name','age','qualification']
		for title in individual_detail:
			print "enter {}".format(title)
			data = raw_input()
			user_data.append(data)
		resume_writedata.Writer().write_data(user_data)

	
new = Reader()
new.user_detail()