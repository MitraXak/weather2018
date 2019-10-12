with open("weather2018.csv", "r", encoding="utf-8") as w:
	aTotal = []
	maxCold = 15.1;
	maxColdDay = "31.08.2018";
	maxHat = 15.1;
	maxHatDay = "31.08.2018";
	aDay = [];
	day = 31;
	aDays = [];
	rainDays = 1;
	totalDay = 0;
	for string in w:
		if(string[0] == "#"):
			continue
		else:
			
			string1 = string.split(';')
			if float(string1[0][1:3]) == day:
				aDay.append(float(string1[1][1:-1]))
			else:
				if "".join(string1[23]).find("Осадков нет") != -1:
					rainDays += 1
				if "".join(string1[23]).find(" ") != -1:
					rainDays += 1
				totalDay += 1
				day = float(string1[0][1:3])
				aDays.append(round(sum(aDay),2)/len(aDay))
				aDay = []
			if  float(string1[1][1:3]) < maxCold:
				maxCold = float(string1[1][1:3])
				maxColdDay = string1[0][1:11]
			if  float(string1[1][1:3]) > maxHat:
				maxHat = float(string1[1][1:3])
				maxHatDay = string1[0][1:11]

	aTotal = sum(aDays)/len(aDays)
	print(round(aTotal,2), maxColdDay, maxHatDay, rainDays, totalDay)
input()
