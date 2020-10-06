import datetime

def openFile(filepath):
	with open(filepath, 'r+') as file:
		contents = file.readlines()
	return contents

lessons = openFile("lessons.txt")
users = openFile("users.txt")
participants = openFile("participants.txt")
quality = openFile("quality.txt")

step_phys = []

for line in lessons:
	if line.find('phys') != -1:
		line = line.replace(" ", "").split('|')
		line[3] = line[3][:18]
		line[3] = (datetime.datetime.strptime(line[3], '%Y-%m-%d%H:%M:%S') + datetime.timedelta(hours=3)).strftime("%Y-%m-%d")
		step_phys.append(line)


step_marks = []

for phys in step_phys:
	for mark in quality:
		mark = mark.replace(" ", "").replace("\n", "").split('|')
		if mark[0] in phys and mark[1] != '':
			phys.append(list(mark[1]))
	step_marks.append(phys)

marks = []

for empline in step_marks:
	if len(empline) > 4:
		marks.append(empline)

mark = []

for i in marks:
	i[4] = sum(i[4:], [])
	i[4] = list(map(int, i[4]))
	i = i[:5]
	mark.append(i)
		
teachers = {}

for id_user in users[2:len(users)-2]:
	id_user = id_user.replace(" ", "").split('|')
	if id_user[1] == 'tutor\n':
		teachers[id_user[0]] = id_user[1]

findTeacher = []

for t_id in participants[2:len(participants)-2]:
	t_id = t_id.replace(" ", "").split('|')
	for teacher in teachers.items():
		if teacher[0] in t_id[1]:
			t_id.append(teacher[1])
	if len(t_id) > 2:
		findTeacher.append(t_id)

step_lessons = []

qualities_per_day = set()

for teach in findTeacher:
	qualities_per_day.add(teach[1])
	lst = list(qualities_per_day)

for i in mark:
	for j in findTeacher:
		if j[0] in i[1]:
			i.append(j[1])
	step_lessons.append(i)

qualities_per_day_for_teachers = {}

for lesson in step_lessons:
	if lesson[3] in qualities_per_day_for_teachers:
		if lesson[5] in qualities_per_day_for_teachers[lesson[3]]:
			qualities_per_day_for_teachers[lesson[3]][lesson[5]].extend(lesson[4])
		else:
			qualities_per_day_for_teachers[lesson[3]][lesson[5]] = lesson[4]
	else:
		qualities_per_day_for_teachers[lesson[3]] = {lesson[5]: (lesson[4])}


for date in qualities_per_day_for_teachers:
	for teacher in qualities_per_day_for_teachers[date]:
		qualities_perday = []
		for lesson in qualities_per_day_for_teachers[date][teacher]:
			qualities_perday.append(lesson)
		qualities_per_day_for_teachers[date][teacher] = round(sum(qualities_perday)/len(qualities_perday), 2)

for date in sorted(qualities_per_day_for_teachers):
	min_mark_for_teacher = min(qualities_per_day_for_teachers[date], key=lambda i: qualities_per_day_for_teachers[date][i])
	qualities_per_day_for_teachers[date][min_mark_for_teacher]
	print('date: {}, id: {}, min_avg_mark: {}'.format(date, min_mark_for_teacher, qualities_per_day_for_teachers[date][min_mark_for_teacher]))
