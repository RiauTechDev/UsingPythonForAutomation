f = open('/Users/christianyurianja/Learning/Linkeding Learning/Using Python for Automation/Ex_Files'
         '_Python_Automation/Exercise Files/inputFile.txt', 'r')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        print(line)
f.close()