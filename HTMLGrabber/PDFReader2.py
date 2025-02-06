import fitz  # PyMuPDF
import requests
import json

pdf_url = "https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2021/20018539.pdf"  # Replace with your PDF URL
response = requests.get(pdf_url)
# Step 2: Write the PDF content to a local file
with open("Tempfile.pdf", "wb") as file:
    file.write(response.content)
# Open the PDF file
pdf_path = "Tempfile.pdf"  # Replace with the path to your PDF file
pdf_document = fitz.open(pdf_path)

# Example: Extract text from a specific page (e.g., page 0)
page_number = 0  # Pages are 0-indexed (0 is the first page)

# Access the page
page = pdf_document.load_page(page_number)

# Extract text from the page
text = page.get_text()  # You can also use 'text("text")' for different types of extraction

# Print the extracted text
#print("Text from page", page_number + 1, ":\n")
#print(text)

# Optional: Extract text from all pages in the document
all_text = ""
for page_num in range(pdf_document.page_count):
    page = pdf_document.load_page(page_num)
    all_text += page.get_text()

# Print the text from all pages
#print("\nText from all pages:\n")
#print(all_text)
splitText = text.split("\n")
stockCount=0
for line in range(len(splitText)-1): #for all lines
    if(len(splitText[line]) == 21 and splitText[line][2] == '/' and splitText[line][5] == '/' and splitText[line][10] == ' ' and splitText[line][13] == '/' and splitText[line][16] == '/'):
        #above checks if we have both dates on a line
        if("(" in splitText[line-2] and ")" in splitText[line-2]): #shows there is a stock here
            stockCount+=1
            print("--------------------------1")
            print(splitText[line-2].split("(")[1].split(")")[0].upper())
            print(splitText[line]) #this is the date we are looking for
            BuyRange = splitText[line+1].split(" - ")
            if(len(BuyRange)==1):
                min = BuyRange[0].split("$")[1].split(" -")[0]
                max = splitText[line+2].split("$")[1]
            else:
                min = BuyRange[0].split("$")[1]
                max = BuyRange[1].split("$")[1]
            print(f"Min: {min} Max:{max}")
            if(splitText[line-1][0] == "P"):
                print("Purchase")
            else:
                print("Sale")
        elif(("(" in splitText[line-3] and ")" in splitText[line-3])):
            #stock is 1 higher
            stockCount+=1
            print("--------------------------2")
            print(splitText[line-3].split("(")[1].split(")")[0].upper())
            print(splitText[line]) #this is the date we are looking for
            BuyRange = splitText[line+1].split(" - ")
            if(len(BuyRange)==1):
                min = BuyRange[0].split("$")[1].split(" -")[0]
                max = splitText[line+2].split("$")[1]
            else:
                min = BuyRange[0].split("$")[1]
                max = BuyRange[1].split("$")[1]
            print(f"Min: {min} Max:{max}")
            if(splitText[line-1][0] == "P"):
                print("Purchase")
            else:
                print("Sale")
    elif(len(splitText[line]) == 10 and splitText[line][2] == '/' and splitText[line][5] == '/'):
        if(len(splitText[line+1]) == 10 and splitText[line+1][2] == '/' and splitText[line+1][5] == '/'):
            #stocks on two lines for some reason idk
            if("(" in splitText[line-2] and ")" in splitText[line-2]): #shows there is a stock here
                stockCount+=1
                print("--------------------------3")
                print(splitText[line-2].split("(")[1].split(")")[0].upper())
                print(splitText[line] + " " +  splitText[line+1]) #this is the date we are looking for
                BuyRange = splitText[line+2].split(" - ")
                if(len(BuyRange)==1):
                    min = BuyRange[0].split("$")[1].split(" -")[0]
                    max = splitText[line+3].split("$")[1]
                else:
                    min = BuyRange[0].split("$")[1]
                    max = BuyRange[1].split("$")[1]
                print(f"Min: {min} Max:{max}")
                if(splitText[line-1][0] == "P"):
                    print("Purchase")
                else:
                    print("Sale")
            elif(("(" in splitText[line-3] and ")" in splitText[line-3])):
                #stock is 1 higher
                stockCount+=1
                print("--------------------------4")
                print(splitText[line-3].split("(")[1].split(")")[0].upper())
                print(splitText[line] + " " +  splitText[line+1]) #this is the date we are looking for
                BuyRange = splitText[line+2].split(" - ")
                if(len(BuyRange)==1):
                    min = BuyRange[0].split("$")[1].split(" -")[0]
                    max = splitText[line+2].split("$")[1]
                else:
                    min = BuyRange[0].split("$")[1]
                    max = BuyRange[1].split("$")[1]
                print(f"Min: {min} Max:{max}")
                if(splitText[line-1][0] == "P"):
                    print("Purchase")
                else:
                    print("Sale")


if(stockCount==0):
    print("No stocks here D:")
print("--------------------------")
