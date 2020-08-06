import os
import shutil
def main():
   path = 'F:\\OfficeHomeDataset\\RealWorld\\'
   destPath = 'F:\\dataset\\'
   for filename in os.listdir(path):
      for f in os.listdir(path + filename):

         my_dest = filename + '\\' +  '3' + f
         pasteDest = destPath + my_dest
         beforeRename = path + filename + '\\' + f 
         afterRename = path + my_dest
         #print(my_source, my_dest, copydest)
         os.rename(beforeRename, afterRename)
         shutil.copyfile(afterRename, pasteDest)

if __name__ == '__main__':
   # Calling main() function
   main()
   print("SUCCESS")