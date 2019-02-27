# @author: ajfernandez
# @last_edited: 24/02/19
# @repo: https://github.com/aj-fernandez/

from urllib.request import urlopen as urlReq
from bs4 import BeautifulSoup as bSoup


def Pull_Site():
    url = "http://www.safa.edu"
    siteResponse = urlReq(url)
    parsedPage = bSoup(siteResponse, "html.parser")
    return(parsedPage)


def Pretty_Site(parsedContent):
    print(parsedContent.prettify())


def Find_Links(parsedContent):
    count = 0
    for link in parsedContent.find_all("a", href=True):
        if link.get("href") != "#":
            count += 1
            print(link.get("href"))
    print("\nThere are: {} links in this site".format(count))


def Find_Images(parsedContent):
    count = 0
    for img in parsedContent.find_all("img", src=True):
        count += 1
        print(img.get("src"))
    print("\nThere are: {} images in this site".format(count))


def JS_Count(parsedContent):
    hardcodedCount = 0
    linkedCount = 0

    for js in parsedContent.find_all("script"):
        if not js.has_attr("src"):
            hardcodedCount += 1
            # print("The hardcoded JS code is:\n\t{}\n".format(js.text))
        elif js.has_attr("src"):
            linkedCount += 1
            # print("The linked JS code path is: {}".format(js.get("src")))

    print("\nThere are: {} hardcoded JS snippets in this site".format(hardcodedCount))
    print("There are: {} linked JS snippets in this site".format(linkedCount))


def Class_Count(parsedContent):
    dirtyClasses = [] # Middle storage rhat contains repeated classes
    cleanClasses = [] # This list DOESNOT contains repeated classes

    dirtyClasses = [elem.get("class") for elem in parsedContent.find_all(
        "div", class_=True) if elem.get("class") not in dirtyClasses]

    # here furthemore than use again a comprehension list like above could using only .drop() in dirtyClasses works fine  
    for i in range(len(dirtyClasses)):
        for j in range(len(dirtyClasses[i])):
            if dirtyClasses[i][j] not in cleanClasses:
                cleanClasses.append(dirtyClasses[i][j])

    print("\n".join(cleanClasses))
    print("\nThere are: {} differents classes".format(len(cleanClasses)))


def Menu():
    print("\n1. Show the full HTML document.\n2. Show founded links \
and the number of occurrences.\n3. Show image paths and number of \
occurrences.\n4. Show JS occurrences.\n5. Show the whole classes div \
catalogue.\n6. Exit.\n")

    choice = input("Select an options:  ")

    while True:
        if choice == "1":
            target = Pull_Site()
            Pretty_Site(target)
            Menu()
        elif choice == "2":
            target = Pull_Site()
            Find_Links(target)
            Menu()
        elif choice == "3":
            target = Pull_Site()
            Find_Images(target)
            Menu()
        elif choice == "4":
            target = Pull_Site()
            JS_Count(target)
            Menu()
        elif choice == "5":
            target = Pull_Site()
            Class_Count(target)
            Menu()
        elif choice == "6":
            print("\nBye bye!!\n")
            exit(0)
        break


Menu()
