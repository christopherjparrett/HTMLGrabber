import requests
import PyPDF2

#s means sale P means purchase

# Step 1: Download the PDF
pdf_url = "https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2021/20018539.pdf"  # Replace with your PDF URL
response = requests.get(pdf_url)
# Step 2: Write the PDF content to a local file
with open("Tempfile.pdf", "wb") as file:
    file.write(response.content)

# Step 3: Open the PDF using PyPDF2
with open("Tempfile.pdf", "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()  # Extract text from the page

# Step 4: Print or process the extracted text
print(text)

# Step 5: now we need to isolate company name, trade date, trade amount

