import os
import csv

with open("filenames.csv", 'w', newline='\n') as myfile:
  myfile.write('filenames,\n')
  for file in os.listdir("./"):
      if file.endswith(".csv"):
          print(file)
          myfile.write(file)
          myfile.write(',\n')
          
