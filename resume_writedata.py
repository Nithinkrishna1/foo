class Writer(object):
	def write_data(self,individual_detail):
		filehandler = open("resume.txt",'a')
		for item in individual_detail:
			filehandler.write("{}\t".format(item))
		filehandler.write("\n")
		filehandler.close()