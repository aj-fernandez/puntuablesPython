# @author: ajfernandez
# @last_edited: 10/02/19
# @repo: https://github.com/aj-fernandez/

# 1) Presentar el árbol de datos completo del documento
# 2) Añadir nuevo nodo al documento
# 3) Modificar datos de un nodo del documento
# 4) Eliminar un nodo concreto del documento
# 5) Salir

from lxml import etree, objectify


def load_fullxml(xmlFile):

    global parsedXml
    global readedXml
    
    parsedXml = etree.parse("peliculas.xml")
    
    with open(xmlFile, "br") as targetFile:
        readedXml = targetFile.read()


def show_fullxml(docXml):

    print(etree.tostring(docXml, pretty_print=True).decode())


def add_element():  # print in stdout well, do that write it on file.

    global objXml

    objXml = objectify.fromstring(readedXml)

    titulo = objXml.pelicula.titulo.text
    guionista = objXml.pelicula.guionista.text
    productora = objXml.pelicula.productora.text
    director = objXml.pelicula.director.text
    actor = objXml.pelicula.actor.text
    sinopsis = objXml.pelicula.sinopsis.text

    data_harvester()


def modNode(*arg):

    objXml.pelicula.titulo = arg[0]
    objXml.pelicula.guionista = arg[1]
    objXml.pelicula.productora = arg[2]
    objXml.pelicula.director = arg[3]
    objXml.pelicula.actor = arg[4]
    objXml.pelicula.sinopsis = arg[5]

    show_fullxml(parsedXml)
    
    newXml = etree.tostring(objXml, pretty_print=True)
    # objectify.deannotate(newXml, xsi_nil=True, cleanup_namespaces=True)

    with open("new2.xml", "bw") as target:
        target.write(newXml)

    # objXml.pelicula.titulo.text = title
    # objXml.pelicula.guionista.text = screenwriter
    # objXml.pelicula.productora.text = producer
    # objXml.pelicula.director.text = director
    # objXml.pelicula.actor.text = protagonist
    # objXml.pelicula.sinopsis.text = summary
   
# Im having troubles here because the "encoding" explicit declaration in xml file (while etree object expect bytes)
# Solution? 2 ways:
#       1- Remove encoding declaration from xml file (this require handle the target file and dont seems to be teh better way).
#       2- open(), without mode declaration (only target file), opens it by default in "r" mode and, the quid, "text" mode, that
#               means that the file will be decoded from bytes to a unicode string, until here right but
#               in "rootElem = etree.fromstring(xml)" we expect BYTES, not an already decoded unicode string from bytes, this means
#               that if we open the file in byte mode, "br", the problem gone.


def my_Parse(xmlFile):
    with open(xmlFile, "br") as targetFile:
        xml = targetFile.read()

    rootElem = etree.fromstring(xml)

    for elemNode in rootElem.getchildren():
        for subNode in elemNode.getchildren():
            if not subNode.text:
                value = "None"
            else:
                value = subNode.text
            print(subNode.tag + " => " + value)

def data_harvester():

    title = input("What's the title? ")
    screenwriter = input("Who is the screenwriter? ")
    producer = input("Which is the film producer? ")
    director = input("Who is the director? ")
    protagonist = input("Who is the protagonist? ")
    summary = input("Type a little summary: ")

    modNode(title, screenwriter, producer, director, protagonist, summary)

if __name__ == "__main__":
    load_fullxml("peliculas.xml")
    add_element()





# def add_element():  # print in stdout well, do that write it on file.
#     global rootElem
#     rootElem = etree.Element("peliculas")
#     newItem = etree.SubElement(rootElem, "pelicula")
#     etree.SubElement(newItem, "titulo").text = "The nevernding story"
#     etree.SubElement(newItem, "guionista").text = "Michael Ende"
#     etree.SubElement(newItem, "productora").text = "Neue Constantin Film"
#     etree.SubElement(newItem, "director").text = "Wolfgang Petersen"
#     etree.SubElement(newItem, "actor").text = "Barret Oliver,  Noah Hathaway"
#     etree.SubElement(newItem, "sinopsis").text = "Escondido en el desván de su colegio, Bastian devora durante las horas de clase un libro enigmático, ”La historia interminable”, que relata la paulatina destrucción del Reino de Fantasía. Una especie de ”Nada” misteriosa destruye el país y a las criaturas que lo habitan. A medida que avanza en la lectura, Bastian se da cuenta de que la salvación de Fantasía depende de él; de que consiga entrar dentro del libro..."

# This records the element but erase the rest
#     with open("peliculas.xml", "wb") as targetFile:
#         targetFile.write(etree.tostring(newItem, pretty_print=True))