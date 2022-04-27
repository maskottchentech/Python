from enum import auto
from os import link
from textwrap import fill
from fpdf import FPDF

title= 'DRAGON BALL Z'

class PDF(FPDF):
  def header(self):
    self.set_font('helvetica','B',20)
    #calculate width of title & position
    title_w = self.get_string_width(title)+6
    doc_w = self.w
    self.set_x((doc_w - title_w) / 2)
    # colors
    self.set_draw_color(165, 105, 189)
    self.set_fill_color(244, 208, 63)
    self.set_text_color(52, 73, 94)
    # frame thickness
    self.set_line_width(1)
    # title
    self.cell(title_w,10,title, border=1,ln=1, align='C',fill=1)
    self.ln(20)

  def footer(self):
    self.set_y(-10)
    self.set_font('helvetica', 'I', 10)
    self.set_text_color(169,169,169)
    self.cell(0,10, f'Page{self.page_no()}/{{nb}}', align='C')

  # chapter title
  def chapter_title(self, ch_num,ch_title, link):
    self.set_link(link)
    self.set_font('helvetica','',12)
    self.set_fill_color(200,220,255)
    chapter_title = f'Chapter{ch_num}: {ch_title}'
    self.cell(0,5, chapter_title, ln=1, fill=1)
    self.ln()




  # Chapter content
  def chapter_body(self,name):
    # read file
    with open(name,'rb') as fh:
      txt=fh.read().decode('latin-1')
      # set font
      self.set_font('times','', 12)
        # insert text
      self.multi_cell(0,5,txt)
      # line break
      self.ln()  
      #end of each chapter
      self.set_font('times','I',12)
      self.cell(0,5,'END OF CHAPTER')

  def print_chapter(self, ch_num, ch_title,name,link):
    self.add_page()
    self.chapter_title(ch_num,ch_title,link)
    self.chapter_body(name)


# Create it's object
pdf = PDF('P','mm','A4')
pdf.alias_nb_pages()

# create metadata
pdf.set_title(title)
pdf.set_author('Karan Raj')

#Create Links
website= 'https://www.pdfdrive.com/'
ch1_link= pdf.add_link()
ch2_link = pdf.add_link()

# set page break
pdf.set_auto_page_break(auto=1, margin=15)

# Add a BLANK intro page
pdf.add_page()
pdf.image('cover.jpg',x=-0.5, w=pdf.w+1)

# add links
pdf.cell(0,10, 'Text Source', ln=1, link=website)
pdf.cell(0,10, 'Chapter 1', ln=1, link=ch1_link)
pdf.cell(0,10, 'Chapter 2', ln=1, link=ch2_link)

pdf.print_chapter(1, 'HERE COMES GOKU', 'chap1.txt', ch1_link)
pdf.print_chapter(2, 'THE FACTORY','chap2.txt',ch2_link)
# for i in range (1,31):
#   pdf.cell(0,10, f'I love Hugo {i} times', ln=1)

pdf.output('testpdf3.pdf')


