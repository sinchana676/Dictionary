admission = {
    "Student_ID": 101,
    "Name": "sinchana",
    "Course": "BCA AI & ML",
    "College": "Jain University"
}

print("Admission Details:", admission)

print("Name:", admission.get("Name"))
print("Student ID:", admission.get("Student_ID"))
print("College:", admission.get("College"))

print("Keys:", admission.keys())
print("Values:", admission.values())
print("Items:", admission.items())

admission.update({"Fees": 150000})
print("After Update:", admission)

print("Length:", len(admission))

admission.setdefault("Year", 2026)
print("After Setdefault:", admission)

admission.pop("Fees")
print("After Pop:", admission)

admission.popitem()
print("After Popitem:", admission)

new_admission = admission.copy()
print("Copied Dictionary:", new_admission)

admission.clear()
print("After Clear:", admission)

text=input("enter a string : ")
frequency={}
for ch in text:
    if ch in frequency:
        frequency[ch]=frequency[ch]+1
    else:
             frequency[ch]=1

print("Character Frequency:")

for ch, count in frequency.items():
    print(ch, ":", count)
