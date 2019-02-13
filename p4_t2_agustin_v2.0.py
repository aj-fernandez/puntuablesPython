# @author: ajfernandez
# @last_edited: 10/02/19
# @repo: https://github.com/aj-fernandez/

from lxml import etree, objectify


def Load_Fullxml(xmlFile):

    with open(xmlFile, "br") as targetFile:
        readedXml = targetFile.read()

    root = objectify.fromstring(readedXml)

    numElem = len(root.getchildren())

    return(root, numElem)


def Save_File(toSave):

    newXml = etree.tostring(toSave, pretty_print=True)
    with open("peliculas.xml", "bw") as target:
        target.write(newXml)


def Data_Harvester():

    title = input("What's the new title? ")
    screenwriter = input("Who is the new screenwriter? ")
    producer = input("Which is the new film producer? ")
    director = input("Who is the new director? ")
    protagonist = input("Who is the new protagonist? ")
    summary = input("Type a little new summary: ")

    return(title, screenwriter, producer,
           director, protagonist, summary)


def Data_Handler(action):

    coreData = [None]*2
    coreData = Load_Fullxml("peliculas.xml")

    if action == "add":
        pos = input("The number of element in the XML is: {}, in what position \
do you want store the new element?".format(coreData[1]))
        newData = Data_Harvester()
        Add_Node(newData, pos)
    elif action == "mod":
        targetElem = input("Enter a title to modify it:  ")
        newData = Data_Harvester()
        Modify_Node(newData, targetElem)


def Add_Node(*arg):

    coreData = [None]*2
    coreData = Load_Fullxml("peliculas.xml")

    newEle = objectify.Element("pelicula")

    newEle.titulo = arg[0][0]
    newEle.guionista = arg[0][1]
    newEle.productora = arg[0][2]
    newEle.director = arg[0][3]
    newEle.actor = arg[0][4]
    newEle.sinopsis = arg[0][5]

    coreData[0].insert((int(arg[1])-1), newEle)

    objectify.deannotate(newEle, pytype=True, xsi=True,
                         xsi_nil=True, cleanup_namespaces=True)
    Save_File(coreData[0])
    Menu()


def Modify_Node(*arg):

    coreData = [None]*2
    coreData = Load_Fullxml("peliculas.xml")

    for elemNode in coreData[0].getchildren():
        for target in elemNode.getchildren():
            if target.text == str(arg[1]):
                elemNode.titulo = arg[0][0]
                elemNode.guionista = arg[0][1]
                elemNode.productora = arg[0][2]
                elemNode.director = arg[0][3]
                elemNode.actor = arg[0][4]
                elemNode.sinopsis = arg[0][5]
                objectify.deannotate(elemNode, pytype=True, xsi=True,
                                     xsi_nil=True, cleanup_namespaces=True)
                Save_File(coreData[0])
                Menu()
    else:
        print("\nThe typed title doesnt exist.")

    Menu()


def Delete_Node():

    coreData = [None]*2
    coreData = Load_Fullxml("peliculas.xml")

    title = input("Enter a title for delete it:  ")

    for elemNode in coreData[0].getchildren():
        for target in elemNode.getchildren():
            if target.text == str(title):
                coreData[0].remove(elemNode)
                Save_File(coreData[0])
                Menu()
    else:
        print("\nThe typed title doesnt exist.")

    Menu()

# Only for test purpose; a different way to show the content more similar to json.


def My_Parser():

    coreData = [None]*2
    coreData = Load_Fullxml("peliculas.xml")

    for elemNode in coreData[0].getchildren():
        print(elemNode.tag + ": {")
        for subNode in elemNode.getchildren():
            if not subNode.text:
                value = "None"
            else:
                value = subNode.text
            print("\t" + "\"" + subNode.tag +
                  "\"" + ": " + "\"" + value + "\"")
        print("}")

    print("\n\n The number of elements is: {}\n".format(coreData[1]))

    Menu()


def Show_Fullxml():

    coreData = [None]*2
    coreData = Load_Fullxml("peliculas.xml")
    print(etree.tostring(coreData[0], pretty_print=True).decode())
    print("\n\n The number of elements is: {}\n".format(coreData[1]))

    Menu()


def Menu():

    print("\n1. Show the full XML document.\n2. Add a new node \
to XML document.\n3. Modify a node from XML doc.\n4. Delete a  \
node from XML doc.\n5. Show the full XML in pretty mode.\n6. Exit.\n")

    choice = input("Select an options:  ")

    # Load_Fullxml("peliculas.xml")

    while True:
        if choice == "1":
            Show_Fullxml()
        elif choice == "2":
            Data_Handler("add")
        elif choice == "3":
            Data_Handler("mod")
        elif choice == "4":
            Delete_Node()
        elif choice == "5":
            My_Parser()
        elif choice == "6":
            print("\nBye bye!!\n")
            exit(0)
        break


Menu()
