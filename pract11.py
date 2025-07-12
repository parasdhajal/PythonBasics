def find_biggest_number(samplearray):
    biggestno = samplearray[0]
    for index in range(1, len(samplearray)):
        if samplearray[index] > biggestno:
            biggestno = samplearray[index]
    print("The biggest number is:", biggestno)

samplearray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
find_biggest_number(samplearray)