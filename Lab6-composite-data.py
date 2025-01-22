import csv
import copy
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
myInventoryList = []

with open('lab6_car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
            print("-----")
            #how does he knows myCarPropreties ? 
            #Why myCarProperties works
#myCarProperties is simply a loop variable. Its value is assigned during each iteration of the outer for loop, where it takes on the value of each dictionary in myInventoryList.
#Python allows you to use any variable name in a for loop. 
#The name myCarProperties is chosen by the developer to make the code more descriptive and indicate its purpose (storing the properties of a single car during each iteration).
