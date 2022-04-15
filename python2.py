print("Bhagya lakshmi deepika")
#import module
import psutil
import csv
import webbrowser
#list declaration
processlist = list()
#iterating over loop
for process in psutil.process_iter():  
     processlist.append(process)
print(processlist)
#opening file in 'w' mode
with open('processlist.csv', 'w') as f:     
      writer = csv.writer(f)     
      writer.writerow(processlist)
 #converting csv to html     
listtostr = ' '.join(map(str, processlist))
with open('processlist.html', 'w') as html_file:     
    html_file.write(listtostr)
print("Completed!!")
