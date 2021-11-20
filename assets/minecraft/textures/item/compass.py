from shutil import copyfile

for i in range(1, 32) :
    if i<10 :
        copyfile("compass_00_s.png", "compass_0"+str(i)+"_s.png")
        copyfile("compass_00_n.png", "compass_0"+str(i)+"_n.png")
    else :
        copyfile("compass_00_s.png", "compass_"+str(i)+"_s.png")
        copyfile("compass_00_n.png", "compass_"+str(i)+"_n.png")

