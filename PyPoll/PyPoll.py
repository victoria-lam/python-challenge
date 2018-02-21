import os
import csv

print("Election Results")
print("---------------------------------")

pypoll_path = os.path.join("election_data_2.csv")
 
#find total months value
with open(pypoll_path, newline="") as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    data = list(csvreader)

    row_count = len(data)
    print("Total Votes: " + str(row_count))
    print("---------------------------------")

#find candidates, reoccurrance of candidates, and percentage
with open(pypoll_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    candidates = []
    
    for row in csv.reader(csvfile):
        #create list of candidates
        candidates.append(row[2])

#create output text file of results - integrated in order to keep f in loop
output_path = os.path.join("pypoll_summary.txt")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow(["Total Votes: " + str(row_count)])
    csvwriter.writerow(["---------------------------------"])
    
    cand_set = []        
    cand_count_list = []      

    for f in set(candidates):
        #convert set into list 
        cand_set.append(f)
        cand_count = candidates.count(f)
        cand_count_list.append(candidates.count(f))
        cand_percent = round(float((cand_count/row_count) * 100),2)
        print(str(f) + ": " + str(cand_percent) + "% (" + str(cand_count) + ")")
        #find position of max value in list 
        cand_index = cand_count_list.index(max(cand_count_list))
        csvwriter.writerow([str(f) + ": " + str(cand_percent) + "% (" + str(cand_count) + ")"])
    
    #print(cand_set)
    #print(cand_index)
    #print(cand_count_list)
    #print(max(cand_count_list))
    #print(cand_set[cand_index])

    print("---------------------------------")
    print("Winner: " + str(cand_set[cand_index]))
    print("---------------------------------")

    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow(["Winner: " + str(cand_set[cand_index])])
    csvwriter.writerow(["---------------------------------"])