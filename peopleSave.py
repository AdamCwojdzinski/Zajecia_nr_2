import pickle


with open('people.txt', 'wb') as handel:
    listPerson = []
    while True:
        for x in range(2):
            fp_firstname = str(input("Enter firstname new person: "))
            if fp_firstname == " ":
                break
            fp_lastname = str(input("Enter lasrname new person: "))
            if fp_lastname == " ":
                break
            fp_age = str(input("Enter age new person: "))
            if fp_age == " ":
                break
            listDataPerson = [fp_firstname, fp_lastname, fp_age]
            listPerson.append(listDataPerson)
        pickle.dump(listPerson, handel)
        break

with open('people.txt', 'rb') as handelR:
    data = pickle.load(handelR)
    for i in data:
        print('Imię: {0}, Nazwisko: {1}, Wiek: {other}.'.format(i[0], i[1], other=i[2]))
        #print(i)
