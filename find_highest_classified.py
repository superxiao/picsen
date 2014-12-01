import shutil

score_file = open("../../predicted_scores.txt", "r")
lines = score_file.readlines()

sortedls = sorted(lines, key=lambda line: float(line.split(" ")[3]))
for line in sortedls[-20:]:
	cells = line.split(" ")
	path = "../" + cells[0]
	shutil.copy(path, "../../best_score/")
sortedls = sorted(lines, key=lambda line: float(line.split(" ")[2]))
for line in sortedls[-20:]:
	cells = line.split(" ")
	path = "../"+cells[0]
	shutil.copy(path, "../../worst_score/")

sortedls = sorted(lines, key=lambda line: abs(float(line.split(" ")[2]) - float(line.split(" ")[3])))
for line in sortedls[:20]:
	cells = line.split(" ")
	path = "../"+cells[0]
	shutil.copy(path, "../../middle_score/")

sortedls = sorted(lines, key=lambda line: float(line.split(" ")[1]) - float(line.split(" ")[3]))
for line in sortedls[-20:]:
	cells = line.split(" ")
	path = "../"+cells[0]
	shutil.copy(path, "../../missed_good/")

sortedls = sorted(lines, key=lambda line: float(line.split(" ")[3]) - float(line.split(" ")[1]))
for line in sortedls[-20:]:
	cells = line.split(" ")
	path = "../"+cells[0]
	shutil.copy(path, "../../missed_bad/")

hit = 0
for line in sortedls:
	cells = line.split(" ")
	if float(cells[3]) >= float(cells[2]) and int(cells[1]) == 1:
		hit += 1
	elif float(cells[3]) < float(cells[2]) and int(cells[1])  == 0:
		hit += 1
print "Accuracy is " + str(float(hit) / len(sortedls))