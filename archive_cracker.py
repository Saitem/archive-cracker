import zipfile
import rarfile
import os

def logo():
    print(''' 
                   _     _            _____                _             
    /\            | |   (_)          / ____|              | |            
   /  \   _ __ ___| |__  ___   _____| |     _ __ __ _  ___| | _____ _ __ 
  / /\ \ | '__/ __| '_ \| \ \ / / _ \ |    | '__/ _` |/ __| |/ / _ \ '__|
 / ____ \| | | (__| | | | |\ V /  __/ |____| | | (_| | (__|   <  __/ |   
/_/    \_\_|  \___|_| |_|_| \_/ \___|\_____|_|  \__,_|\___|_|\_\___|_|   
                                                                          
''')

logo()

path_archive = input('Enter archive path: ')
path_list = input('Enter file passwords list path:')
path_from_archive = input('Enter the path where you want to download the unarchived files: ')

def ident_file(file):
    archive = None
    if file[file.find('.'):] == '.zip':
        archive = zipfile.ZipFile(os.path.join(file), 'r')
    if file[file.find('.'):] == '.rar':
        archive = rarfile.RarFile(os.path.join(file), 'r')
    return archive

def brute_force():
    potential_password = open(os.path.join(path_list), 'r').read().split('\n')
    archive = ident_file(path_archive)
    for password in potential_password: 
        check = check_password(archive, password)
        if check:
            print(password)
            break
    else:
        print('This password is not in the list, try another list')

def check_password(zipfile, password):
    try:
	    zipfile.extractall(os.path.join(path_from_archive), pwd=password)
	    return password
    except:
	    return        

brute_force()

