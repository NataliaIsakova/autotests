bugs = [
"Ошибка 1 — High",
"Ошибка 2 — Low",
"Ошибка 3 — High",
"Ошибка 4 — Low",
"Ошибка 5 — High"
]

print(bugs)
bugs.append("Ошибка 6 — Medium")
print(bugs)

new_bugs = []
for bug in bugs:
    if "— Low" not in bug:
        new_bugs.append(bug)

bugs = new_bugs
print("Без Low багов:", bugs)

high_bugs = []
medium_bugs = []
low_bugs = []


for bug in bugs:
    if "— High" in bug:
        high_bugs.append(bug)
    elif "— Medium" in bug:
        medium_bugs.append(bug)
    elif "— Low" in bug:
        low_bugs.append(bug)


bugs = high_bugs + medium_bugs + low_bugs
print(bugs)