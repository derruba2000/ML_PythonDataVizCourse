import sys
###########################################
import SubModule.E01AccessingDatawithPandas as EX01
import SubModule.E02FilteringDatawithPandas as EX02



###########################################



################################################################
# Main
if (len(sys.argv)==1):
    print("Usage: main <Exercise Number>")
else:
    if (sys.argv[1]=="1"):
        print("Exercise 01")
        EX01.RunExercise()
    if (sys.argv[1]=="2"):
        print("Exercise 02")
        EX02.RunExercise()



