# wap to shutdown/restart/logoff pc with python codes
# The Program Is Coded By Basanta chaudhary
import os
import string
import numbers
import io
import sys


class pc():
    def shutdown():
        os.system('shutdown -s -t 600')

    def restart():
        os.system('shutdown/r')

    def logoff():
        os.system('shutdown/l')

    def sleep():
        os.system('shutdown/h')

    def abort():
        os.system('shutdown/a')



print("\n\n\n")
print("\n\n\n\n\t\t\t\t\t\t\t\tSystem Managment Project\n")
who = str(input("\t\t\t\t\t\t\t  Who Are You . . .? "))
# os.system('cls')

print("\n\t\t\t\t\t\t\t\tNamste ", who, " !\n")
user = str(input("\t\t\t\t\t\t\t\t\tuser : "))
pas = str(input("\t\t\t\t\t\t\t\t\tPass : "))
print("\n\t\t\t\t\t\t\t\t   _________choose________")
if user=='admin'  and pas=='admin123' :
    while  True:
        print("\n\t\t\t\t\t\t\t\t\t[1] shutdwon")
        print("\t\t\t\t\t\t\t\t\t[2] restart")
        print("\t\t\t\t\t\t\t\t\t[3] logg off")
        print("\t\t\t\t\t\t\t\t\t[4] sleep")
        #print("\t\t\t\t\t\t\t\t\t[5] cancell")
        choose = int(input("\t\t\t\t\t\t\t\t\t[5] cancell "))
        if choose == 1:
            pc.shutdown()
        elif choose == 2:
            pc.restart()
        elif choose == 3:
            pc.logoff()
        elif choose == 4:
            pc.sleep()
        elif choose == 5:
            pc.abort()
        # elif choose==6:
        #     sys.exit
        else:
            print("\n\t\t\t\t\t\t\t\t    ---Invalid Choose !---")

else:
    print("\t\t\t\t\t\t\tuser && pass are Invalid !")
