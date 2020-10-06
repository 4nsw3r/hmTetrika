import re
with open('hits.txt', 'r+') as file:
	line = file.read()
ip = re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', line)
#print(ip)
cnt = dict()
for i in ip:
	if i in cnt:
		cnt[i]+=1
	else:
		cnt[i] = 1
tpl = sorted(cnt.items(), reverse = True, key=lambda x: x[1])
for top_ip in tpl[:6]:
	print(top_ip[0])
