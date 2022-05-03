import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files:
                # construct the full local path
                local_path = os.path.join(root, filename)

                # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join("/Uploads/" + str(file_from) + "/" + relative_path)

                # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    print("Welcome To Dropbox Cloud Services!")
    print()

    access_token = input("Enter Your Access Token: ")
    transferData = TransferData(access_token)
    print()

    file_from = str(input(r"Enter The Folder Name To Transfer: "))
    file_to = input(r"Enter The Full Folder Path To Upload To Dropbox: ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print(file_from + " has been moved!!!")

main()
