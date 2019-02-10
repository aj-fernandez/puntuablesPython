# @author: ajfernandez
# @last_edited: 10/02/19
# @repo: https://github.com/aj-fernandez/

# 1) Presentar el árbol de datos completo del documento
# 2) Añadir nuevo nodo al documento
# 3) Modificar datos de un nodo del documento
# 4) Eliminar un nodo concreto del documento
# 5) Salir

from lxml import etree


def load_fullxml():
    global fullXML
    fullXML = etree.parse("peliculas.xml")


def show_fullxml(docXML):
    print(etree.tostring(docXML, pretty_print=True).decode())


def add_element():  # print in stdout well, do that write it on file.
    global rootElem
    rootElem = etree.Element("peliculas")
    newItem = etree.SubElement(rootElem, "pelicula")
    etree.SubElement(newItem, "titulo").text = "The nevernding story"
    etree.SubElement(newItem, "guionista").text = "Michael Ende"
    etree.SubElement(newItem, "productora").text = "Neue Constantin Film"
    etree.SubElement(newItem, "director").text = "Wolfgang Petersen"
    etree.SubElement(newItem, "actor").text = "Barret Oliver,  Noah Hathaway"
    etree.SubElement(newItem, "sinopsis").text = "Escondido en el desván de su colegio, Bastian devora durante las horas de clase un libro enigmático, ”La historia interminable”, que relata la paulatina destrucción del Reino de Fantasía. Una especie de ”Nada” misteriosa destruye el país y a las criaturas que lo habitan. A medida que avanza en la lectura, Bastian se da cuenta de que la salvación de Fantasía depende de él; de que consiga entrar dentro del libro..."

    # This record the element but erase the rest
    with open("peliculas.xml", "wb") as targetFile:
        targetFile.write(etree.tostring(newItem, pretty_print=True))


load_fullxml()
add_element()
show_fullxml(rootElem)
