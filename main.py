from pickle import FALSE, TRUE


going = TRUE
count = 0
StartingNumber = 1
test = TRUE
Continue = ""



while test == TRUE:
    Placeholder = StartingNumber
    Solved = FALSE
    while Solved == FALSE:
        if Placeholder == 1:
            print('Number', StartingNumber,'is done in', count,'counts')
            Solved = TRUE
        elif Placeholder % 2 == 0:
            Placeholder = Placeholder / 2
            count += 1
            print(Placeholder)
        elif Placeholder % 2 == 1:
            Placeholder = (Placeholder * 3) + 1
            count += 1
            print(Placeholder)
        else:
            print('Error')

    StartingNumberStr = str(StartingNumber)
    CountStr = str(count)

    FileWork_DataList = (StartingNumberStr, CountStr)
    FileWork_NumberList = ('The number', StartingNumberStr, 'is equal to 1 after', CountStr, 'counts')

    FILE1 = open('DataList.txt', "a")
    FILE1.write(str(FileWork_DataList))
    FILE1.write("\n")
    FILE1.close()

    FILE2 = open('NumberList.txt', "a")
    FILE2.write(str(FileWork_NumberList))
    FILE2.write("\n")
    FILE2.close()

    StartingNumber += 1
    count = 0

    
