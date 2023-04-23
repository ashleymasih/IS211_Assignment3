import argparse
import urllib.request
import csv
import sys
import re
# other imports go here


def downloadData(url):
    urlResponse = urllib.request.urlopen(url)
    print("url downloaded")
    return urlResponse
    



def processData(data):
    lines = [l.decode('utf-8') for l in data.readlines()]
    csvData = csv.reader(lines)
    dateFormat = "%Y-%m-%d %H:%M:%S"
    hits = 0
    imgHits = 0 
    safari = chrome = firefox = msie = 0
    for row in csvData:
        hits += 1
        if(re.search(r"\.(?:jpg|jpeg|gif|png)$", row[0])):
            imgHits += 1

        if(re.search("chrome", row[2])):
            chrome += 1

        if(re.search("Safari", row[2])):
            safari += 1

        if(re.search("Firefox", row[2])):
            firefox += 1

        if(re.search("MSIE", row[2])):
            msie += 1
        
    percent = (imgHits/hits)*100
    percent = round(percent,1)
    biggestHit = max(max(chrome,safari), max(firefox, msie))
    print("Image requests account for " + str(percent) + "% of all requests")
    print("The browser with the biggest hit is " + str(biggestHit))


def max(x, y):
    if(x>y):
        return x
    else:
        return y


def main(url):
    print(f"Running main with URL = {url}...")
    newData = downloadData(url)
    processedData = processData(newData)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
