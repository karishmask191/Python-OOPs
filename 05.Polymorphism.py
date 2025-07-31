'''
5.Polymorphism
#Polymorphism means "many forms". It refers to the ability of an entity (like a function or object) to perform different actions based on the context.   (or)
#Different objects respond differently to the same function call.

Example: Printer
(You can give PDF or Word files to the same printer.
The printer knows how to print both, even though they are different.
This is one function (print) working in multiple forms depending on the file type.)

Example Code:
-------------
# Define classes with same method name
class PDF:
    def print_file(self):
        print("Printing PDF")

class WordDoc:
    def print_file(self):
        print("Printing Word Document")

# Function to demonstrate polymorphism
def start_printing(doc):
    doc.print_file()

# Create objects
pdf = PDF()
word = WordDoc()

# Call method with different object types
start_printing(pdf)
start_printing(word)

Output:
Printing PDF
Printing Word Document
'''
