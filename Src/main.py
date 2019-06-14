import sys
###########################################
import SubModule.E01AccessingDatawithPandas as EX01



###########################################



################################################################
# Main
if (len(sys.argv)==1):
    print("Usage: setup <Exercise Number>")
else:
    if (sys.argv[1]=="1"):
        EX01.RunExercise()



