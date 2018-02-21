import os
import csv

print("Financial Analysis")
print("---------------------------------")

pybank_path = os.path.join("budget_data_1.csv")

#find total months value
with open(pybank_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    data = list(csvreader)

    row_count = len(data)
    print("Total Months: " + str(row_count))
    
#find total revenue - create revenue list 
with open(pybank_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    total = 0
    revenue = []
    date = []
    rev_change = []
    
    for row in csv.reader(csvfile):
        total += int(row[1])
        #add to the lists
        revenue.append(float(row[1]))
        date.append(row[0])
    print("Total Revenue: $" + str(total)) 
    

#find average revenue change, max and min revenue changes
    avg_rev_change = 0
    max_rev = 0
    min_rev = 0
    max_rev_date = ""
    min_rev_date = ""
    
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)
        max_rev = int(max(rev_change))
        min_rev = int(min(rev_change))

        max_rev_date = str(date[rev_change.index(max(rev_change))+1])
        min_rev_date = str(date[rev_change.index(min(rev_change))+1])


    print("Average Revenue Change: $", round(avg_rev_change))
    print ("Greatest Increase in Revenue: " + max_rev_date + " ($" + str(max_rev) + ")")
    print("Greatest Decrease in Revenue: " + min_rev_date + " ($" + str(min_rev) + ")")

#create output text file of results
output_path = os.path.join("pybank_summary.txt")
with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow(["Total Months: " +str(row_count)])
    csvwriter.writerow(["Total Revenue: $" +str(total)])
    csvwriter.writerow(["Average Revenue Change: $", round(avg_rev_change)])
    csvwriter.writerow(["Greatest Increase in Revenue: " + max_rev_date + " ($" + str(max_rev) + ")"])
    csvwriter.writerow(["Greatest Decrease in Revenue: " + min_rev_date + " ($" + str(min_rev) + ")"])