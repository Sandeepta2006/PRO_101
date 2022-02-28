import dropbox 

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, folder_from, folder_to):
        dbx= dropbox.Dropbox(self.access_token)

        f= open(folder_from, 'rb')
        dbx.folder_upload(f.read(), folder_to)

def main():
    access_token= 'sl.BC4GjqU4-RYWF3EV7BjQnnXgo-MvirQJK2y_J8mfDriEBq7s6LPlHDNNZsBiF6Nmu3pXX0ed4EIVv7tLzmTqd0iB5LGNwfGa02vrL_hglUhsXmg0e0Db-3mNdhT0G9wAcnTmDnc'
    transferData=TransferData(access_token)
    folder_from= input('Enter the folder path to transfer:')
    folder_to= input('Enter the full path to upload to dropbox:')
    transferData.upload_folder(folder_from, folder_to)
    print("Folder has been moved.")

main()