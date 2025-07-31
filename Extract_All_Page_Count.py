import os
import csv
from datetime import datetime
from pypdf import PdfReader

# Folder path (change this accourding to your laptop path where the file reside) Yesh: message me if you see any error
folder_path = r"C:\Users\F53K6OQ\Downloads\Testing script"
output_csv = os.path.join(folder_path, "PDF_File_Report.csv")

# Prepare list of data
pdf_data = []

# Iterate through PDF files in the folder and sub-folders
if os.path.exists(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(".pdf"):
                file_path = os.path.join(root, filename)
                try:
                    # For File Details
                    stats = os.stat(file_path)
                    modified_time = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                    file_size_kb = round(stats.st_size / 1024, 2)
                    file_type = "PDF Document"

                    # Get number of pages
                    reader = PdfReader(file_path)
                    num_pages = len(reader.pages)

                    # Prepare data
                    pdf_data.append([file_path, filename, modified_time, file_type, file_size_kb, num_pages])
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

    # Write to CSV file
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Path", "Name", "Date Modified", "Type", "Size (KB)", "Pages"])
        writer.writerows(pdf_data)

    print(f"PDF report saved to: {output_csv}")
else:
    print(f"The folder path does not exist: {folder_path}")
