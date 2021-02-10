import random
def noMh(text):
	result = text
	a = []
	b = []
	for i in range(len(result)):
		if result[i] == "'":
			a.append(i)
		if result[i] == '"':
			b.append(i)
	for i in range(0, len(a) // 2):
		result = result.replace(result[a[2 * i]:a[2 * i + 1]] + "'", "")
	for i in range(0, len(b) // 2):
		result = result.replace(result[b[2 * i]:b[2 * i + 1]] + '"', "")
	return result
def rmds(lines, d, s):
	temp = []
	result = []
	if d != [] or s != []:
		for i in range(len(lines)):
			for j in range(0, len(d) // 2):
				if i not in range(d[2 * j], d[2 * j + 1] + 1):
					temp.append(lines[i])
		for i in range(len(temp)):
			for j in range(0, len(s) // 2):
				if i not in range(s[2 * j], s[2 * j + 1] + 1):
					result.append(temp[i])
	else:
		return lines
	return result
def rmExp(lines):
	result = []
	for line in lines:
		result_line = ""
		empty = True
		for char in line:
			result_line += char
			if char != " " or char != "	":
				empty = False
			if char == "#":
				continue
		if not empty:
			result.append(result_line)
	d = []
	s = []
	for i in range(len(result)):
		if '"""' in result[i]:
			d.append(i)
		if "'''" in result[i]:
			s.append(i)
	return rmds(result, d, s)
def bulidVar(lines):
	string = lines[0]
	for i in range(1, len(lines)):
		string += "\n" + lines[i]
	var = []
	for line in lines:
		line = noMh(line)
		t = ""
		s = ""
		pd = False
		if "def" in line:
			temp = line.split("def")[1]
			temp = temp.split("(")[0]
			temp = temp.replace(" ", "")
			var.append(temp)
		if "(" in line:
			ktemp = line.split("(")[-1]
			ktemp = ktemp.split(")")[0]
			ktemp = ktemp.replace(" ","")
			if "," in ktemp:
				ktemp = ktemp.split(",")
				for i in ktemp:
					try:
						tt = int(i)
						break
					except:
						for j in i:
							if j not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_":
								pd = True
						if not pd and i not in var:
							var.append(i)
			else:
				try:
					tt = int(ktemp)
				except:
					for i in ktemp:
						if i not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_":
							pd = True
					if not pd and ktemp not in var:
						var.append(ktemp)
		if "=" in line:
			for i in line.split(" "):
				t += i
			for i in t.split("	"):
				s += i
			if "+=" in line:
				temp = s.split("+=")[0]
			elif "-=" in line:
				temp = s.split("-=")[0]
			elif "*=" in line:
				temp = s.split("*=")[0]
			elif "/=" in line:
				temp = s.split("/=")[0]
			else:
				temp = s.split("=")[0]
			for i in line:
				if i == ":":
					pd = True
			if pd == True:
				continue
			if "," in temp:
				temp = temp.split(",")
				for j in temp:
					if j not in var:
						var.append(j)
			elif temp not in var:
				var.append(temp)
	var.sort(key = lambda i:len(i),reverse=True)
	print(var)
	for i in range(len(var)):
		if var[i] not in "def for while in elif if else not break continue __init__ super class self object input" and "[" not in var[i] and var[i] != "True" and var[i] != "False" and "." not in var[i]:
			#string = string.replace(var[i], "var" + str(i))
			nm = random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM__')
			for j in range(15):
				nm += random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890__')
			string = string.replace(var[i], nm)
	return string
fin = open(input("输入python文件名："),"r")
lines = fin.read().split("\n")
fin.close()
lines = rmExp(lines)
fout = open("result.py","w")
fout.write(bulidVar(lines))
fout.close()