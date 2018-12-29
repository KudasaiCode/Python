import re, shutil, os

#Renames  Zip and Rar extensions to their 
#Comic Book extension
def rename_archive(option):
	for ext in os.listdir("."):
		if option == '1':
			os.rename(ext, re.sub('(.zip$)', ".cbz", ext)) #regex ensures only end is renamed
		elif option == '2':
			os.rename(ext, re.sub('(.rar$)', ".cbr", ext))
		elif option == '3':
			os.rename(ext, re.sub('(.cbz$)', ".zip", ext))
		elif option == '4':
			os.rename(ext, re.sub('(.cbr$)', ".rar", ext))			

#Replaces string with another
def rename_filename(word, replacement):
	for ext in os.listdir("."):
		os.rename(ext, ext.replace(word, replacement).strip())

#Creates new directory, and moves files by name
def move_file(folder_name, file_name):		
	os.mkdir(os.getcwd() + "\\" + folder_name)
	new_path = os.getcwd() + "\\" + folder_name

	for files in os.listdir("."):
		if files.startswith(file_name):
			shutil.move(files, new_path)


print('=================================')
print('Directory: ' + os.getcwd())    #Important. Changes cannot be reverted.
print('=================================')
print('1) Rename extensions\n2) Rename Files\n3) Move Files\n4) Show Direcotry\n5) Exit')
print('---------------------------------')
option = input('Select: ')

while option != '5':
	if option == '1':
		print('\t\nCHANGE EXTENSIONS')
		print('==================')
		print('1) ZIP > CBZ\t2) RAR > CBR\n3) CBZ > ZIP\t4) CBR > RAR')
		print('---------------------------------')
		option = input('Select: ')
		rename_archive(option)
	elif option == '2':
		print('\t\nCHANGE FILENAME')
		print('=====================')
		word = input('Word to replace: ')
		replacement = input('Replace ' + word + ' with: ').strip()
		rename_filename(word, replacement)
	elif option == '3':
		print('\t\nMOVE FILES')
		print('===================')
		folder_name = input('New Folder ' + os.getcwd() + '\\')
		file_name = input('Files to move to ' + os.getcwd() + '\\' + folder_name + ': ')
		move_file(folder_name, file_name)
	elif option == '4':
		print('\n\n' + os.getcwd() + '\n\n' + str(os.listdir(".")))
	else:
		print('Invalid Option')
	
	print('\n=================================')
	print('1) Rename extensions\n2) Rename Files\n3) Move Files\n4) Show Direcotry\n5) Exit')
	print('--------------------------------')
	option = input('Select: ')
		
