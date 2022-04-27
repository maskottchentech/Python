from mmap import mmap
from fpdf import FPDF

# Create it's object
# Layout ('P', 'L')
# Unit('mm', 'cm', 'in')
# Format ('A3','A4', (default), 'Letter','Legal',(100,150))
pdf = FPDF('P','mm','A4')

# Add a page
pdf.add_page()

#specify font
# font ('times','courier', 'helvetica', 'symbol','zpfdingbats')
# bold ('B'), underline ('U'), italics ('I'),combo ('BU')
pdf.set_font('helvetica','',16 )

#add text
# w = width in mm
# h = height in mm
# ln = next line ('0 or False', '1 or True')
# border = ('0 or False', '1 or True')
pdf.cell(40,10, 'Hello World!', ln=True)
pdf.cell(50,20,'Hugo is my son', border=True)

pdf.output('testpdf1.pdf')


