
import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)


    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

  # Read each row of data after the header
    for row in csvreader:
        print(row)

