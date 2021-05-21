"""
    Use with IDE
    Edit the revenue and units file name and run the program
    Edit the date and month variables
    Returns a csv file (UTF-8 encoded) with revenue and id matched based on opty id present for both
        assuming the units and revenue files have same rows with same opty id
"""

import csv

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
    # import files
    units = readCSV("Mar 21 2checkout HED units.csv")
    revenue = readCSV("Mar 21 2checkout HED revenue.csv")
    # variables
    month = "March"
    date = "03/31/2021"
    # list to keep a record of new rows added
    newCsv = []

    # we are assuming units and revenue file will have the same number of entry
    for unitRow in units:
        unitRow = list(unitRow.items())
        newRow = {}
        for revenueRow in revenue:
            revenueRow = list(revenueRow.items())
            # check if the id matches
            if (unitRow[0][1] == revenueRow[0][1]):
                # opportunity insert operation needed fields
                newRow["Account Id"] = ""
                newRow["Name"] = month + " 2021 Courseware Adoption"
                newRow["Close Date"] = date
                newRow["Purchase Date"] = date
                newRow["Stage"] = "Closed Won"
                newRow["Market"] = "HED_Adoption"
                newRow["Type"] = "Existing Business"
                # opportunity product insert needed fields
                newRow['Old/Given Opty Id'] = unitRow[0][1]
                newRow['Opportunity Id'] = ""
                newRow["Product Id"] = ""
                newRow["PriceBookEntry Id"] = ""
                newRow['Quantity'] = unitRow[1][1]
                newRow['Total Price'] = revenueRow[1][1]
                newRow['B2C App Units'] = 0
                newRow['Line Description'] = "2Checkout/Avangate"
                newRow['Date'] = date
                # opportunity update needed fields
                newRow["Account Owner"] = ""

                newCsv.append(newRow.copy())
                break
    print(newCsv)
    writeDictToCSV("revenue_and_units.csv", newCsv)
