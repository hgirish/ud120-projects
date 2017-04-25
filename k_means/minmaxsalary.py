import pickle
### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)
myField = 'salary'
tempList = []
for k, v in data_dict.iteritems():
    if v[myField] != 'NaN':
        temprow = (k, float(v[myField]))
        tempList.append(temprow)
sortedData = sorted(tempList, key=lambda t: t[1])
totalRows = len(sortedData)
minrow = sortedData[0]
maxrow = sortedData[totalRows-1]
print("Minimum {2} held by {0} is {1}".format(minrow[0], minrow[1],myField))
print("Maximum {2} held by {0} is {1}".format(maxrow[0], maxrow[1],myField))
