import csv
class CreateCsv(object):
	def csv_create(self,individual_detail,user_data):
		new = open('resume.csv','w')
		csv_writer = csv.writer(new)
		csv_writer.writerows([individual_detail,user_data])
		print "\nresume.csv is created"
		