########### Reading Zip File #############
import zipfile
import datetime

newzip=zipfile.ZipFile('testzip0.zip','r') #open zip file
newzip.printdir() #print zip file detils

#read the specific file
data=newzip.read('testzip0/jsonfile.txt.txt')
print('\nDisplay File data:')
print(data)

data1=newzip.read('testzip0/test.txt.txt')
print(data1)

##################################################
import zipfile
import datetime
newzip=zipfile.ZipFile('testzip0.zip','r') #open zip file
newzip.printdir() #print zip file detils
#get information of specific file
info=newzip.getinfo('testzip0/test.txt.txt')
print('\nInformation of file: ',info)
print('\nDetailed information of file:');print('Name:',info.filename)
print('Modified:' + str(datetime.datetime(*info.date_time)))
print('Size in bytes:');print('File uncompressed Size:',info.file_size)
print('File compressed Size:',info.compress_size)
#get information of zip file
for info in newzip.infolist():
    print('\nInformation of zip file');print('Name:',info.filename)
    print('System:' + str(info.create_system) + '(0 = Windows, 3 = Unix)')
    print('Modified:' + str(datetime.datetime(*info.date_time)))
    print('Size in bytes:');print('File uncompressed Size:',info.file_size)
    print('File compressed Size:',info.compress_size)
print('\nInformation of zip file:',newzip.infolist()) #information of zip file

########################################
#print name of the files of zip folder
import zipfile
newzip=zipfile.ZipFile('testzip0.zip','r') #open zip file
print(newzip.namelist()) 

#########################################
import zipfile
#open zip file
newzip=zipfile.ZipFile('testzip0.zip','r')
#print zip file detils
newzip.printdir()
#extract specific files of zip folder
newzip.extract('testzip0/test.txt.txt')
print('Successfully all files extracted')


