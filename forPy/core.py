import random as rnd
import numpy as np
import xml.etree.ElementTree as ET


#hexaDic = np.load("hexagrams.npy")
triDic = np.load("trigrams.npy")

wiki_url="https://es.wikipedia.org/wiki/Anexo:Hexagramas_del_I_Ching#Hexagrama_{0}"
compendium_url="http://www.kwan-yin.com.ar/hexagrama{0}.pdf"

hexa_matrix =  (( 2 ,23,  8, 20, 16, 35, 45, 12),
			    (15 ,52, 39, 53, 62, 56, 31, 33),
				( 7 , 4, 29, 59, 40, 64, 47,  6),
				(46 ,18, 48, 57, 32, 50, 28, 44),
				(24 ,27,  3, 42, 51, 21, 17, 25),
				(36 ,22, 63, 37, 55, 30, 49, 13),
				(19 ,41, 60, 61, 54, 38, 58, 10),
				(11 ,26,  5,  9, 34, 14, 43,  1))
tri_matrix = (2, 5, 4, 6, 3, 7, 8, 1)

HEXA_LENGTH = 6
TRI_LENGTH = 3

graph_text_lines_static = {
    "0":"---   ---",
    "1":"---------"
    }

graph_text_lines = {
    "[0 0]":"--- x ---",
    "[1 0]":"---------",
    "[0 1]":"---   ---",
    "[1 1]":"----o----",

    }

lineValueToArrayMap = {
            "6":[0,0],
            "7":[1,0],
            "8":[0,1],
            "9":[1,1],
        }
cointToValueMap = {
            "0":2,
            "1":3,
        }

def getRandomCoreArray() :
    return np.array([[rnd.choice([0,1]) for i in range(2)] for c in range(6)])


def getGraphicLinesArray(staticArray=None,coreArray=None) :
    arrayX = None
    lines = None
    if staticArray is not None :
        arrayX = staticArray
        lines= graph_text_lines_static
    if coreArray is not None :
        arrayX = coreArray
        lines= graph_text_lines
    return [lines[str(x)] for x in arrayX]

def printGraphicLines (staticArray=None, coreArray=None) :
    if staticArray is not None :
        lineArray = getGraphicLinesArray(staticArray=staticArray)
    if coreArray is not None :
        lineArray = getGraphicLinesArray(coreArray=coreArray)

    print("\n")
    for x in lineArray :
        print("\t"+x)
    print("\n")

def printMovement(hexagram) :
    if hexagram.isMov() :
        present = hexagram.staticArray
        proyection = hexagram.proyectionArray
        coreArray = h.coreArray

        coreLineArray = getGraphicLinesArray(coreArray=coreArray)
        presentLineArray = getGraphicLinesArray(staticArray=present)
        proyectionLineArray = getGraphicLinesArray(staticArray=proyection)

        print("\tPRINCIPAL\tMOVIMIENTO\tPROYECCION\n")
        for i in range(len(coreArray)) :
            print ("\t"+presentLineArray[i] +"\t" + coreLineArray[i] + "\t"+ proyectionLineArray[i])

        print("\n")

def printTriInfo(tri, position = None) :
    pos = ""
    if position != None :
        pos = position + ": "
    print (", ".join([
            #"Trigrama "+ str(tri.getFushiNumber()),
            "\n"+ pos + tri['SYMBOL'] + " "+tri['IMG'],
            "NOMBRE: "+tri['CHI_NAME'] + "/" + tri['NAME'],
            "CUALIDAD: "+tri['QUALITY']
            ])
        )

def getLineValueFromArrayMap(lineArray) :
    for val, arr in lineValueToArrayMap.items() :
        if list(lineArray) == arr :
            return val

def loadLinesByHexaNumber(hNumber):
    try :
        root = ET.parse('hex/hex_{0}.xml'.format(hNumber)).getroot()
    except :
        print("problems formating" + 'hex/hex_{0}.xml'.format(hNumber)+"\n")
        root = ET.parse('hex/hex_1.xml').getroot()
    return [i for i in root.find('LINES').findall('LINE')]

def loadHexaDictByHexaNumber(hNumber) :
    try :
        root = ET.parse('hex/hex_{0}.xml'.format(hNumber)).getroot()
    except :
        print("problems formating" + 'hex/hex_{0}.xml'.format(hNumber)+"\n")
        root = ET.parse('hex/hex_1.xml').getroot()
    h_dic = {}
    h_dic["WEN_NUMBER"] = int(root.attrib["ID"])
    for h in root :
        h_dic[h.tag]= h.text
    return h_dic

def printLines(hexagram) :
    if hexagram.debug or hexagram.isMov() :
        input("\nPRESS ENTER FOR SEE THE MOVING LINES... ")
        lines = loadLinesByHexaNumber(hexagram["WEN_NUMBER"])
        coreArray = hexagram.coreArray[::-1]
        print("\n")
        if hexagram.debug :
            for i in range(len(coreArray)):
                value = getLineValueFromArrayMap(coreArray[i])
                print (value + " en la linea "+ str(lines[i].attrib["ID"]) + " significa:\n" + (lines[i].find('TEXT').text)+"\n")
                print ("Interpetacion:\n" + (lines[i].find('INT').text)+"\n")
            if len(lines) > 6 :
                print ("Todas las lineas mutantes significa:\n" + (lines[6].find('TEXT').text)+"\n")
                print ("Interpetacion:\n" + (lines[6].find('INT').text)+"\n")

        elif (hexagram.isMovAll() and len(lines) > 6) :
            print ("Todas las lineas mutantes significa:\n" + (lines[6].find('TEXT').text)+"\n")
            print ("Interpetacion:\n" + (lines[6].find('INT').text)+"\n")
        else :
            for i in range(len(coreArray)):
                value = getLineValueFromArrayMap(coreArray[i])
                if coreArray[i][0] == coreArray[i][1] :
                    print (value + " en la linea "+ str(lines[i].attrib["ID"]) + " significa:\n" + (lines[i].find('TEXT').text)+"\n")
                    print ("Interpetacion:\n" + (lines[i].find('INT').text)+"\n")


def printHexaInfo(hexagram) :
    if hexagram!=None :
        printGraphicLines(staticArray=hexagram.staticArray)
        print("El hexagrama "+str(hexagram["WEN_NUMBER"])+" es llamado "+hexagram['CHI_NAME'] +", "+hexagram['NAME'],
                            "Otras variaciones podrian ser "+hexagram['VAR_NAMES']+"\n")
        #uTri= Hexagram(hexagram["coreArray"][:3])
        #lTri = Hexagram(hexagram["coreArray"][3:])
        print(hexagram.getUpTri()["IMG"] + " sobre " + hexagram.getLoTri()["IMG"])
        print("\nTrigramas:\n")
        printTriInfo(hexagram.getUpTri(),position="Arriba")
        printTriInfo(hexagram.getLoTri(),position="Abajo")
        print("\nEl dictamen dice:\n"+ hexagram["DICT"])
        print("\nInterpretacion:\n"+ hexagram["INT"])
        print("\nImagen:\n"+ hexagram["IMG"])
        if hexagram["IMG_COM"]!= None :
            print("\nComentario Imagen:\n"+ hexagram["IMG_COM"])
        printLines(hexagram)
        print("WIKI URL: " + wiki_url.format(hexagram["WEN_NUMBER"]))
        print("COMPENDIUM URL: " + compendium_url.format(hexagram["WEN_NUMBER"]))
        print("WEN NUMBER: "+ str(hexagram["WEN_NUMBER"]) +" / " + str(hexagram.getWenNumber()))
        #print("HEXA DICT: " + str(loadHexaDictByHexaNumber(hexagram["WEN_NUMBER"])))


def getTrigramsByHexaNumber(hNumber):
    na = np.array(hexa_matrix)
    indexOf = np.where(na==hNumber)
    return (indexOf[0][0],indexOf[1][0])

def getBinaryStringByFuShiValue(fuxiNumber) :
    return "{0:03b}".format(fuxiNumber)[::-1]

def getHexaBinaryStringByTriNumbers(tNumbers) :
    #tNumbers = getTrigramsByHexaNumber(wenNumber)
    return getBinaryStringByFuShiValue(tNumbers[1]) + getBinaryStringByFuShiValue(tNumbers[0])


class Hexagram() :
    def __getitem__(self, key): return self.data[key]
    def __setitem__(self, key, value): self.data[key] = value
    def __init__(self, coreArray=None, staticArray=None, wenNumber=None, debug=False) :
        self.debug = debug
        self.data = {} # for text
        self.mov = None
        self.movAll = None

        if wenNumber!= None :
            binValue = getHexaBinaryStringByTriNumbers(getTrigramsByHexaNumber(wenNumber))
            coreArray = np.array([[int(x),abs(int(x)-1)] for x in binValue])

        if staticArray is not None :
            coreArray = np.array([[x,abs(x-1)] for x in staticArray])
        if coreArray is not None :
            self.coreArray = coreArray

        self.staticArray = [i[0] for i in self.coreArray]
        self.proyectionArray = [abs(i[1]-1) for i in self.coreArray]

        #SETTING UP INFO TEXT FROM CONSTANTS
        if len(self.coreArray) is HEXA_LENGTH :
            #self.data.update(hexaDic[self.getFushiNumber()])
            self.data.update(loadHexaDictByHexaNumber(self.getWenNumber()))
        else :
            self.data.update(triDic[self.getFushiNumber()])

    def getUpTri(self) :
        if  len(self.coreArray) is HEXA_LENGTH :
            return Hexagram(self.coreArray[:3])
        else :
            return self

    def getLoTri(self) :
        if  len(self.coreArray) is HEXA_LENGTH :
            return Hexagram(self.coreArray[3:])
        else :
            return self

    def getFushiNumber(self) :
        return int("".join([str(x) for x in self.staticArray[::-1]]),2) # Invertido para tomar el numero binario desde arriba hacia abajo

    def getWenNumber(self) :
        if len(self.coreArray) is HEXA_LENGTH :
            return hexa_matrix[self.getLoTri().getFushiNumber()][self.getUpTri().getFushiNumber()]
        else :
            return tri_matrix[self.getFushiNumber()]
    def isMov(self) :
        if self.mov == None :
            if self.staticArray == self.proyectionArray :
                self.mov = False
            else :
                self.mov = True
        return self.mov

    def isMovAll(self) :
        if self.movAll == None :
            self.movAll = True
            for i in range(len(self.coreArray)) :
                if(self.staticArray[i]==self.proyectionArray[i]) :
                    self.movAll = False
                    break
        return self.movAll


    def getProyection(self) :
        if self.isMov() :
            return Hexagram(staticArray=self.proyectionArray)
        else :
            return None



def getCoins() :
    return [rnd.choice([0, 1]) for x in range(3)]

class Oracle() :

    def __getitem__(self, key): return self.data[key]
    def __setitem__(self, key, value): self.data[key] = value
    def __init__(self,coins=None, lineValues=None) :
        self.data = {}

        if lineValues != None :
            self.hexagram = Hexagram(coreArray=np.array([lineValueToArrayMap[x] for x in lineValues]))
        else :
            self.coins = np.array(coins[::-1])
            self.hexagram = Hexagram(self.coinsToCoreArray())


    def getHexagram(self) :
        return self.hexagram
    def getProyection(self) :
        if self.hexagram.isMov() :
            return Hexagram(staticArray=self.hexagram.proyectionArray)
        else :
            return None

    def coinsToCoreArray(self) :
        coreArray = []
        for cl in self.coins :
            lv = 0
            for c in cl :
                lv += cointToValueMap[str(c)]
            coreArray.append(lineValueToArrayMap[str(lv)])
        return np.array(coreArray)


#MENU OPERATIONS
def getOptionFromMenu() :
    print("\n\tENTER OPTION")
    print("\n\t1 for Throw Coins")
    print("\t2 for Enter Hexagram Number")
    print("\t3 for Enter Hexagram Line Values")
    print("\t0 for Exit")
    return input("\n\tChose: ")

def getConsultFromLineValues() :
    lv = [None]*HEXA_LENGTH
    for i in range(HEXA_LENGTH) :
        while True :
            lv[i]=input("ENTER LINE {0} VALUE (6-9): ".format(i+1))
            if 6 <= int(lv[i]) and int(lv[i]) <= 9 :
                break
    return Oracle(lineValues=lv[::-1]).getHexagram()

def getConsultFromCoins() :
    input("\n\nPRESS ENTER FOR GET THE ANSWER BY RANDOM COINS\n")
    coins=[]
    for c in range(HEXA_LENGTH) :
        ca = getCoins()
        coins.append(ca)
        lv = cointToValueMap[str(ca[0])] + cointToValueMap[str(ca[1])] + cointToValueMap[str(ca[2])]
        print("LINE "+str(c+1)+" "+str(ca) +"\t"+ str(lv)+"\t"+ graph_text_lines[str(np.array(lineValueToArrayMap[str(lv)]))] )
        if c < 5 : input("\nPRESS ENTER FOR NEXT LINE...\n")
    input("\nPRESS ENTER FOR GET THE ANSWER\n")
    return Oracle(coins).getHexagram()

def getConsultFromWenNumber() :
    hexaNumber = input("Enter the number: ")
    return Hexagram(wenNumber=int(hexaNumber),debug=True)


if __name__ == "__main__" :

    while True :
        option = getOptionFromMenu()
        if option is "1" :
            h = getConsultFromCoins()
        elif option is "2" :
            h = getConsultFromWenNumber()
        elif option is "3" :
            h = getConsultFromLineValues()
        elif option is "0" :
            break

        printMovement(h)
        print("Principal")
        printHexaInfo(h)
        if h.isMov() :
            input("\nPRESIONA ENTER PARA VER EL HEXAGRAMA TENDENCIAL... ")
            print("\n\nTendencial")
            printHexaInfo(h.getProyection())



