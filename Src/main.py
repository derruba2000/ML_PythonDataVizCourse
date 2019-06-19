import sys
###########################################
import SubModule.EX01AccessingDatawithPandas as EX01
import SubModule.EX02FilteringDatawithPandas as EX02
import SubModule.EX03Univariateplottingwithpandas as EX03
import SubModule.EX04Facetingwithseaborn as EX04



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
    if (sys.argv[1]=="3"):
        print("Exercise 03")
        EX03.RunExercise()
    if (sys.argv[1]=="4"):
        print("Exercise 04")
        EX04.RunExercise()



