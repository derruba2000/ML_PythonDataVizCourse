import sys
###########################################
import SubModule.EX01AccessingDatawithPandas as EX01
import SubModule.EX02FilteringDatawithPandas as EX02
import SubModule.EX03AUnivariateplottingwithpandas as EX03A
import SubModule.EX04Facetingwithseaborn as EX04
import SubModule.EX05Multivariateplotting as EX05



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
    if (sys.argv[1]=="3A"):
        print("Exercise 03A")
        EX03A.RunExercise()
    if (sys.argv[1]=="4"):
        print("Exercise 04")
        EX04.RunExercise()
    if (sys.argv[1]=="5"):
        print("Exercise 05")
        EX05.RunExercise()



