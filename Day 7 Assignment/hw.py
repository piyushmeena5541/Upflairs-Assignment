import os
import shutil

def create_folders():
    folders = ['image_folder', 'text_folder', 'pdf_folder']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

def filter_files():
    files = os.listdir('JECRC')
    for file in files:
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            shutil.move(os.path.join('JECRC', file), 'image_folder')
        elif file.endswith('.txt'):
            shutil.move(os.path.join('JECRC', file), 'text_folder')
        elif file.endswith('.pdf'):
            shutil.move(os.path.join('JECRC', file), 'pdf_folder')

if __name__ == "__main__":
    create_folders()
    filter_files()
    print("Files filtered and moved successfully.")
