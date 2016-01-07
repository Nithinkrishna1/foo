import pyfpdf
class CreateFile(object):
	def create(self,individual_data,user_data):
		str1 = " ".join(str(x) for x in individual_data)
		str2 = " ".join(str(x) for x in user_data)
		pdf = pyfpdf.FPDF(format='letter')
		pdf.add_page()
		pdf.set_font("Arial", size=12)
		pdf.cell(200, 10, txt=str1, ln=1, align="C")
		pdf.cell(200, 10, txt=str2, align="C")
		pdf.output("test.pdf")

