#imports function convert_from_path from pdf2image library
from pdf2image import convert_from_path

# a variable that's string literal containing the pdf's file name
pdf_file = r"sample-pdf-file.pdf"

# creates a variable pages that uses function convert_from_path
# https://pdf2image.readthedocs.io/en/latest/reference.html
# I also recommend reading this regarding paths in python 
# https://www.btelligent.com/en/blog/best-practice-working-with-paths-in-python-part-1/
pages = convert_from_path(pdf_file, 500, poppler_path= r"bin")

# changes "sample-pdf-file.pdf" string to just "sample-pdf-file" (uses string.replace function to replace the .pdf with an empty string)
# https://www.tutorialspoint.com/python/string_replace.htm
img_file = pdf_file.replace(".pdf", "")

# we define an integer type variable to give our images number assigment 
# (useful if we have multiple pages)
count = 0

#for loop through all pages
for page in pages:

    #we add +1 every for loop to the count int variable
    count += 1

    # we define the jpeg file name 
    jpeg_file = img_file + "_page" + str(count) + ".jpg"

    #we save the page as jpeg
    page.save(jpeg_file, 'JPEG')