f = open('/Users/christianyurianja/Learning/Linkeding Learning/Using Python for Automation/Ex_Files'
         '_Python_Automation/Exercise Files/inputFile.txt', 'r')
passFile = open('/Users/christianyurianja/Learning/Linkeding Learning/Using Python for Automation/Ex_Files'
                '_Python_Automation/Exercise Files/PassFile.txt', 'w')
failFile = open('/Users/christianyurianja/Learning/Linkeding Learning/Using Python for Automation/Ex_Files'
                '_Python_Automation/Exercise Files/FailFile.txt', 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)
f.close()
passFile.close()
failFile.close()
