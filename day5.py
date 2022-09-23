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