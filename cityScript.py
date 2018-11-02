listOfCity = ['Kansas City', 'Philadelphia', 'Poznan', 'Washington', 'Ottawa', 'Montreal'];
letters = 75
for i in listOfCity:
    index = ord((i[0]))
    if index > letters and len(i) > 6:
        print(i)