for i in range(0, 10, 1):
    if i == 6 or i == 5:
        print(i)
    else:
        pass  #place holder that does nothing

# |  i  |  condition  |  o/p  |
#  |0   | 0==6 F 0==5 F|pass ---so no print
#  |1  | i==6 F 1==5 F|pass---so no print
#  |5  | 5==6 F 5==5 T|print 5---so no print
#  |6  | 6==6 T 6==5 F|print 6---so no print



