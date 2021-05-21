"""
    Run on terminal

    Currently the script takes 2 files; one being latest and another from previous months
    It compares the school name and course name from csv
    If they match, opty id, product id, and pricebookentry id are copied to the latest csv

    To run cd to the folder form terminal and run organizecsv.py "latest csv filename" "last month csv filename"

    # These files should have headers in the following format:
    # School Name, Course Name, Price, Quantity, Opportunity Id, Product Id, PriceBookEntry Id, ...
"""
import csv
import sys


def readCSV(filename):
    dicts = []
    reader = csv.DictReader(open(filename))
    for row in reader:
        dicts.append(row.copy())
    return dicts


def writeDictToCSV(filename, dicts_list):
    keys = set().union(*(d.keys() for d in dicts_list))
    with open(filename, 'w', encoding="utf-8-sig", newline="") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dicts_list)


if __name__ == "__main__":
    # Read data from csv's into dictionaries
    csvFile = readCSV(str(sys.argv[1]))
    lastMonthCsv = readCSV(str(sys.argv[2]))

    columnHeaders = list(csvFile[0].copy())
    # create a list to store new row values for the csv files
    # this new file will contain School Name, Course Name, Price, Quantity, Opportunity Id, Product Id, PriceBookEntry Id
    organizedCsv = []

    for currentRow in csvFile:
        newRow = {}

        if currentRow[columnHeaders[0]].strip() == "":  # school name is empty, continue to next one
            continue
        else:
            newRow[columnHeaders[0]] = currentRow[columnHeaders[0]]         # school name
        newRow[columnHeaders[1]] = currentRow[columnHeaders[1]]             # course name
        newRow[columnHeaders[2]] = currentRow[columnHeaders[2]]             # price
        newRow[columnHeaders[3]] = currentRow[columnHeaders[3]]             # quantity

        if currentRow[columnHeaders[0]].strip() != "":
            for lastMonthRow in lastMonthCsv:
                if currentRow[columnHeaders[0]].strip() == lastMonthRow[columnHeaders[0]].strip():  # school name matches
                    # check if course name matches
                    if currentRow[columnHeaders[1]].strip() == lastMonthRow[columnHeaders[1]].strip():
                        # school name and course name matches, get Oid and Pid from last months csv
                        newRow[columnHeaders[4]] = lastMonthRow[columnHeaders[4]].strip()           # opty id
                        newRow[columnHeaders[5]] = lastMonthRow[columnHeaders[5]].strip()           # product id
                        # also get the price book entry id available
                        newRow[columnHeaders[6]] = lastMonthRow[columnHeaders[6]].strip()           # price book entry id
                    else:
                        continue

        organizedCsv.append(newRow.copy())

    # print(organizedCsv)
    writeDictToCSV("organizedCSV.csv", organizedCsv)
