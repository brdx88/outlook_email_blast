import openpyxl
import os
import msoffcrypto

def create_excel_file(file_path):
    # Create a new Excel file
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sample Sheet"
    ws["A1"] = "Hello"
    ws["B1"] = "World"
    wb.save(file_path)
    print(f"Excel file created at {file_path}")

def encrypt_excel_file(input_file, output_file, password):
    with open(input_file, 'rb') as f:
        excel = msoffcrypto.OfficeFile(f)
        excel.encrypt(password)
        with open(output_file, 'wb') as encrypted_file:
            excel.save(encrypted_file)
    print(f"Encrypted file saved at {output_file}")

# Define paths
input_file = "sample.xlsx"
encrypted_file = "sample_encrypted.xlsx"
password = "securepassword123"

# Create Excel file
create_excel_file(input_file)

# Encrypt the file
encrypt_excel_file(input_file, encrypted_file, password)

# Clean up the original file (optional)
os.remove(input_file)
