#
# Example file for parsing and processing JSON
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request
import json
import ssl

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    # # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    # # output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print(count, "events recorded")

    # for each event, print the place where it occurred
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("--------------\n")

    # print the events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4:
            print(i["properties"]["mag"], i["properties"]["title"])

    # print only the events where at least 1 person reported feeling something
    print("felt quakes: ")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if (feltReports != None):
            if (feltReports > 0):
                     print(i["properties"]["mag"], i["properties"]
                    ["place"], " reported " + str(feltReports) + " times")


def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    ssl._create_default_https_context = ssl._create_unverified_context
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print ("result code: ", webUrl.getcode())
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Recieved an error from the server, cannot print results", webUrl.getcode())

if __name__ == "__main__":
    main()
