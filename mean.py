# Python program to print
# mean of elements

# list of elements to calculate mean
import csv
with open('./height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    #csv.reader method reads and returns the current row and the moves to the next one 
    file_data = list(reader)
    #list method adds the data into the list 
file_data.pop(0)
#remove the title from the data 
# print(file_data)
# sorting data  to get the height of people.
new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(float(n_num))


# #getting the mean
n = len(new_data)
total =0
for x in new_data:
    total += x

mean = total / n
#
print("Mean / Average is: " + str(mean))
