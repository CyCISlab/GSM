import sys
outF = open("Outputs/output"+sys.argv[1] +".txt","w")
file = open("logs.txt", "r")
for line in file:
    if "TMSI" in line:
      my_string=line
      outF.write(my_string.split("TMSI",1 )[1].replace(" matches"," ").replace("0x","").replace(" (not for us)",""))
outF = open("logs.txt", "w")
