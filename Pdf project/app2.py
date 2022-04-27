from fpdf import FPDF

class PDF(FPDF):
  def header(self):
    #logo
    self.image('lion_vector.jpg', 10,8,30)
    #font of title
    self.set_font('helvetica','B',20)
    #padding of title
    self.cell(80)
    #title
    self.cell(30,10,'Title',ln=1,align='C')
    #line break
    self.ln(20)

  def footer(self):
    #position
    self.set_y(-10)
    #font
    self.set_font('helvetica', 'I', 10)
    # page number
    self.cell(0,10, f'Page{self.page_no()}/{{nb}}', align='C')

# Create it's object
pdf = PDF('P','mm','A4')

# Add a page
pdf.add_page()

#specify font

pdf.set_font('helvetica','B',16 )

#add text

for i in range (1,31):
  pdf.cell(0,10, f'I love Hugo {i} times', ln=1)

pdf.output('testpdf2.pdf')


