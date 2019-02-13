# @author: ajfernandez
# @last_edited: 10/02/19
# @repo: https://github.com/aj-fernandez/

from lxml import etree, objectify


def Load_Fullxml(xmlFile):

    global readedXml
    global root
    global numElem

    with open(xmlFile, "br") as targetFile:
        readedXml = targetFile.read()

    root = objectify.fromstring(readedXml)

    numElem = len(root.getchildren())


def Data_Harvester(action):

    if action == "add":

        title = input("What's the title? ")
        screenwriter = input("Who is the screenwriter? ")
        producer = input("Which is the film producer? ")
        director = input("Who is the director? ")
        protagonist = input("Who is the protagonist? ")
        summary = input("Type a little summary: ")

        pos = input("The number of element in the XML is: {}, in what position \
do you want store the new element?".format(numElem))

        Add_Node(title, screenwriter, producer,
                 director, protagonist, summary, pos)

    elif action == "mod":

        targetElem = input("Enter a title to modify it:  ")

        title = input("What's the new title? ")
        screenwriter = input("Who is the new screenwriter? ")
        producer = input("Which is the new film producer? ")
        director = input("Who is the new director? ")
        protagonist = input("Who is the new protagonist? ")
        summary = input("Type a little new summary: ")

        Modify_Node(title, screenwriter, producer, director,
                    protagonist, summary, targetElem)


def Add_Node(*arg):

    newEle = objectify.Element("pelicula")

    newEle.titulo = arg[0]
    newEle.guionista = arg[1]
    newEle.productora = arg[2]
    newEle.director = arg[3]
    newEle.actor = arg[4]
    newEle.sinopsis = arg[5]

    root.insert((int(arg[6])-1), newEle)

    objectify.deannotate(newEle, pytype=True, xsi=True,
                         xsi_nil=True, cleanup_namespaces=True)

    newXml = etree.tostring(root, pretty_print=True)

    with open("new8.xml", "bw") as target:
        target.write(newXml)

    Menu()


def Modify_Node(*arg):

    for elemNode in root.getchildren():
        for target in elemNode.getchildren():
            if target.text == str(arg[6]):
                elemNode.titulo = arg[0]
                elemNode.guionista = arg[1]
                elemNode.productora = arg[2]
                elemNode.director = arg[3]
                elemNode.actor = arg[4]
                elemNode.sinopsis = arg[5]
                objectify.deannotate(elemNode, pytype=True, xsi=True,
                                     xsi_nil=True, cleanup_namespaces=True)
                newXml = etree.tostring(root, pretty_print=True)
                with open("new8.xml", "bw") as target:
                    target.write(newXml)


def Delete_Node():

    title = input("Enter a title for delete it:  ")

    for elemNode in root.getchildren():
        for target in elemNode.getchildren():
            if target.text == str(title):
                root.remove(elemNode)
                newXml = etree.tostring(root, pretty_print=True)
                with open("new8.xml", "bw") as target:
                    target.write(newXml)
                Menu()
    else:
        print("\nThe typed title doesnt exist.")
    
    Menu()

# Only for test purpose; a different way to show the content more similar to json.


def My_Parser():

    for elemNode in root.getchildren():
        print(elemNode.tag + ": {")
        for subNode in elemNode.getchildren():
            if not subNode.text:
                value = "None"
            else:
                value = subNode.text
            print("\t" + "\"" + subNode.tag +
                  "\"" + ": " + "\"" + value + "\"")
        print("}")

    Menu()


def Show_Fullxml():

    print(etree.tostring(root, pretty_print=True).decode())
    print("\n\n The number of elements is: {}\n".format(numElem))
    
    Menu()


def Menu():

    print("\n1. Show the full XML document.\n2. Add a new node \
to XML document.\n3. Modify a node from XML doc.\n4. Delete a  \
node from XML doc.\n5. Show the full XML in pretty mode.\n6. Exit.\n")

    choice = input("Select an options:  ")

    Load_Fullxml("new8.xml")

    while True:
        if choice == "1":
            Show_Fullxml()
        elif choice == "2":
            Data_Harvester("add")
        elif choice == "3":
            Data_Harvester("mod")
        elif choice == "4":
            Delete_Node()
        elif choice == "5":
            My_Parser()
        elif choice == "6":
            print("\nBye bye!!\n")
            exit(0)
        break


Menu()