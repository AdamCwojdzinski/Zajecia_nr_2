with open('text.txt', 'w') as handel:
    while True:
        textToWrite = str(input("Enter you message: "))
        handel.write(textToWrite + "\n")
        if textToWrite == ' ':
            break
