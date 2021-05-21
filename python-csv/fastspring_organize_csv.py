"""
    Use with IDE
    Edit the csv file name and run the program - this is the original csv we get from the report;
    if the report header changes, this script is subjected to change
    Edit the date and month variables
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
    # import file
    originalCsv = readCSV("purchase_report (14).csv")
    # variables
    month = "February"
    date = "02/28/2021"
    # list to keep a record of new rows added
    newCsv = []

    end = False
    price = []
    quantity = []
    for x in range(0, len(originalCsv)):
        # see if we are at the last line
        if x + 1 == len(originalCsv):
            end = True
        rowFirst = list(originalCsv[x].items())
        # check if we are done
        if rowFirst[3][1] is None:
            continue
        if not end:
            rowNext = list(originalCsv[x + 1].items())

        # initialize some variables for the iteration
        newRow = {}
        name = rowFirst[0][1]

        # append price after converting it to float
        newPrice = rowFirst[3][1].strip()
        newPrice = newPrice.replace("$", "")  # this will help us convert it into a float
        # see if price is negative
        if newPrice[0] == "(":
            newPrice = newPrice.replace("(", "")
            newPrice = newPrice.replace(")", "")
            newPrice = float(newPrice) * -1
        else:
            newPrice = float(newPrice)

        # append price and quantity after converting them
        price.append(newPrice)
        quantity.append(int(rowFirst[6][1]))
        if end or rowFirst[0][1] != rowNext[0][1]:
            # schools name don't match, calculate new row to be added
            totalPrice = sum(price)
            totalQuantity = sum(quantity)
            # add per unit price to the csv, this is to decide if we have a 2 year or 3 year product
            newRow["Price per unit"] = totalPrice / totalQuantity
            if totalPrice < 1 or totalQuantity < 1:
                newRow["Note"] = "Alert! You may want to double check this row."
            # change totalPrice to csv readable format
            if totalPrice < 0:
                totalPrice = totalPrice * -1
                totalPrice = "($"+str(totalPrice)+")"
            else:
                totalPrice = "$"+str(totalPrice)

            # create a new row since it's the last iteration for the same school name
            # opportunity insert operation needed fields
            newRow["Account Name"] = rowFirst[0][1]
            if rowFirst[0][1] == "": newRow["Account Name"] = "Fastspring"
            newRow["Name"] = month + " 2021 Courseware Adoption"
            newRow["Close Date"] = date
            newRow["Purchase Date"] = date
            newRow["Stage"] = "Closed Won"
            newRow["Market"] = "HED_Adoption"
            newRow["Type"] = "Existing Business"
            # opportunity product insert needed fields
            newRow['Opportunity Id'] = ""
            newRow["Product Id"] = ""
            newRow["PriceBookEntry Id"] = ""
            newRow['Quantity'] = totalQuantity
            newRow['Total Price'] = totalPrice
            newRow['B2C App Units'] = 0
            newRow['Line Description'] = "Fastspring Purchase"
            newRow['Date'] = date
            # opportunity update needed fields
            newRow["Account Owner"] = ""

            newCsv.append(newRow.copy())

            # reinitialize the price and quantity arrays
            price = []
            quantity = []
            # print(newRow)

    writeDictToCSV(month + " Fastspring purchase report.csv", newCsv)