#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """


    cleaned_data = []
   

    ### your code goes here
   
    totalValues = len(predictions)
    listOfTupes = []
    for i in  range(0, totalValues):
        rowData= (ages[i], net_worths[i], predictions[i]-net_worths[i])
        listOfTupes.append(rowData)

    sortedTuple = sorted(listOfTupes, key=lambda tup: tup[2])  
    print(sortedTuple[0])
    print(sortedTuple[totalValues-1])  
    x = int(.90 * totalValues)
    print(x)
    cleaned_data = sortedTuple[:x]

    
    return cleaned_data

