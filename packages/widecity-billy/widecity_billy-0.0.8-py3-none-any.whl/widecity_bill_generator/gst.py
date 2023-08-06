from simple_image_download import simple_image_download
simp=simple_image_download.Downloader() 
simp.directory = 'widecity_Downloader/'

from docx2pdf import convert
from docx import Document
from python_docx_replace import docx_remove_table, docx_replace, docx_blocks


    
def generate(customer_name,customer_contact,invoice_id,date,building_location):
   
    file = 'download_images/tests/templates/gst_invoice.docx'
    doc = Document(file)

    docx_replace(doc, name=str(customer_name),
                 phone=str(customer_contact),
                 invoice=str(invoice_id),
                 date=str(date),
                 place=str(building_location)
                 )
    # docx_blocks(doc, block=True)
    # docx_remove_table(doc, 0)

    doc.save('temp.docx')
    convert('temp.docx', "widecity_invoice.pdf")

# generate("benny",9946957366,100,"02-03-2022","majapra")