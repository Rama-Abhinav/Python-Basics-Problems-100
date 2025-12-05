#Create a dictionary of student marks and print highest scorer.							


Student_Rec = {
    "S1" : 10,
    "S2" : 100,
    "S3" : 50,
    "S4" : 90 
}
Max_marks = float("-inf")
for  Marks in Student_Rec.values():
    if Marks > Max_marks:
        Max_marks = Marks

for key, Val in Student_Rec.items():
    if Val == Max_marks:
        print(f"The Highest Scorer is {key} with a score of {Val}")
    