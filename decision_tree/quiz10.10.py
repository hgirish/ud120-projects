def featureScaling(arr):
    mindata = min(arr)
    maxdata = max(arr)
    scaled = [0.5,0.5, 0.5]
    if mindata == maxdata:
        return scaled
    for i in range(0,3):
        x = float(arr[i])
        print("i: {0}, x: {1}".format(i,x))
        scaled[i] = (x - mindata)/(maxdata - mindata)
        print("i: {0}, x: {1}, scaled[{0}]: {2}".format(i,x, scaled[i]))
    
    return scaled

data = [115,140,175]
print(featureScaling(data))