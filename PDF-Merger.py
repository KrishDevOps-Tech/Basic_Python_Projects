# PDF Merger Script
import os
from pypdf import PdfWriter

merger = PdfWriter()
folder_path = r"C:\Users\user\Documents\PDF_Test"
output_file_name = "final_merged.pdf" 

# 1. Yeh folder path exist karta hai ya nahi check karega
if not os.path.exists(folder_path):
    print(f"Error: Folder path does not exist -> {folder_path}")
    exit()

files = os.listdir(folder_path)
pdf_files_found = []

for file_name in files:
    # .pdf check karenge aur ensure karenge ki output file khud merge list me na aaye
    if file_name.lower().endswith(".pdf") and file_name != output_file_name:
        pdf_files_found.append(file_name)

pdf_count = len(pdf_files_found)

# 2. Conditions check
if pdf_count == 0:
    print("No PDF files found in the specified folder.")

elif pdf_count == 1:
    print(
        f"Only one PDF file found ({pdf_files_found[0]}). At least 2 files are needed to merge."
    )

else:
    for file_name in pdf_files_found:
        file_path = os.path.join(folder_path, file_name)
        merger.append(file_path)
        print(f"Added Successfully: {file_name}")

    # Ab Output save karenge.
    output_path = os.path.join(folder_path, output_file_name)
    merger.write(output_path)
    merger.close()
    print(f"\nTotal {pdf_count} files combined successfully into '{output_file_name}'!")
