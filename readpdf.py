from pdf2image import convert_from_path
dpi = 800
pages = convert_from_path('images/pdf_file.pdf', dpi, r"C:\Program Files\Poppler\bin")
#Saving pages in jpeg format

i = 0
for page in pages:
    i+=1
    name = 'out-'+str(dpi)+'-page-'+str(i)+'.jpg'
    page.save(name, 'JPEG')