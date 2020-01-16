import csv
import re
import sys

cleanList = []
invalidList = []

validName = re.compile(r"^(?!\-)[A-Za-z\-]+(?!\-)$")


def OpenFile():
    while True:
        file = input("Enter path to file:\n")
        try:
            with open(file, "r") as dirtyNames:
                reader = csv.reader(dirtyNames)
                for row in reader:
                    dirtyList = row
            break
        except:
            print("\nERROR\n" + str(sys.exc_info()[0]) + "\n")
    return dirtyList


def Parse(list):
    for item in list:
        if str(validName.match(item)) == "None":
            invalidList.append(item)
        else:
            cleanList.append(item.title())


def WriteClean():
    with open("CleanNames.csv", "w") as cleanNames:
        csv.writer(cleanNames).writerow(cleanList)


def WriteInvalid():
    with open("InvalidNames.csv", "w") as invalidNames:
        csv.writer(invalidNames).writerow(invalidList)


def complete():
    input("\nComplete\n\nPress RETURN to exit")


Parse(OpenFile())
WriteClean()
WriteInvalid()
complete()
