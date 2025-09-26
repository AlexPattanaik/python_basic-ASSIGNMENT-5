marksheet={"Alice":85,"Alex":65,"Omm":78}
name=input("Enter the student's name: ")
r=marksheet.get(name,"Student not found.")
if r=="Student not found.":
    print (r)
else:
    print(f"{name}'s marks: {r}")
