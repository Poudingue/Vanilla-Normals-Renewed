from shutil import copyfile

for i in range(1, 64) :
    if i<10 :
        copyfile("clock_00_s.png", "clock_0"+str(i)+"_s.png")
    else :
        copyfile("clock_00_s.png", "clock_"+str(i)+"_s.png")
