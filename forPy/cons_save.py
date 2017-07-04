import xml.etree.ElementTree as ET
root = ET.parse('hexagrams.xml').getroot()
tri = []
hexa = [None]*64

hexa_matrix = [  2 ,23,  8, 20, 16, 35, 45, 12,
			    15 ,52, 39, 53, 62, 56, 31, 33,
				 7 , 4, 29, 59, 40, 64, 47,  6,
				46 ,18, 48, 57, 32, 50, 28, 44,
				24 ,27,  3, 42, 51, 21, 17, 25,
				36 ,22, 63, 37, 55, 30, 49, 13,
				19 ,41, 60, 61, 54, 38, 58, 10,
				11 ,26,  5,  9, 34, 14, 43,  1]

for i in range(2,len(root)) :
    if i != 39 :
        h = root[i]
        #lines = ET.Element('LINES')
        #ET.SubElement(lines,'LINE')
        inter = ET.SubElement(h,'INT')
        inter.text = 'hexaInt'
        img = ET.SubElement(h,'IMG')
        img.text = 'hexaImg'

        img_com = ET.SubElement(h,'IMG_COM')
        img_com.text = 'hexaImgCom'

        lines = ET.SubElement(h,'LINES')

        l1 = ET.SubElement(lines,'LINE', attrib={"ID":"1"})
        l1_text = ET.SubElement(l1,'TEXT')
        l1_text.text = "lineText"
        l1_int = ET.SubElement(l1,'INT')
        l1_int.text = "lineInt"

        l2 = ET.SubElement(lines,'LINE', attrib={"ID":"2"})
        l2_text = ET.SubElement(l2,'TEXT')
        l2_text.text = "lineText"
        l2_int = ET.SubElement(l2,'INT')
        l2_int.text = "lineInt"

        l3 = ET.SubElement(lines,'LINE', attrib={"ID":"3"})
        l3_text = ET.SubElement(l3,'TEXT')
        l3_text.text = "lineText"
        l3_int = ET.SubElement(l3,'INT')
        l3_int.text = "lineInt"

        l4 = ET.SubElement(lines,'LINE', attrib={"ID":"4"})
        l4_text = ET.SubElement(l4,'TEXT')
        l4_text.text = "lineText"
        l4_int = ET.SubElement(l4,'INT')
        l4_int.text = "lineInt"

        l5 = ET.SubElement(lines,'LINE', attrib={"ID":"5"})
        l5_text = ET.SubElement(l5,'TEXT')
        l5_text.text = "lineText"
        l5_int = ET.SubElement(l5,'INT')
        l5_int.text = "lineInt"

        l6 = ET.SubElement(lines,'LINE', attrib={"ID":"6"})
        l6_text = ET.SubElement(l6,'TEXT')
        l6_text.text = "lineText"
        l6_int = ET.SubElement(l6,'INT')
        l6_int.text = "lineInt"

        ET.dump(h)
        x = ET.ElementTree(h)
        x.write("hex_{0}.xml".format(i+1),encoding="UTF-8")

"""
for i in range(len(root)) :
    h_dic = {}
    h_dic["WEN_NUMBER"] = int(root[i].attrib["ID"])
#    print("Hexagram " + str(h_dic["WEN_NUMBER"]) +"=" +str(hexa_matrix.index(h_dic["WEN_NUMBER"]) ) )
    for h in root[i] :
        h_dic[h.tag]= h.text
    hexa[hexa_matrix.index(h_dic["WEN_NUMBER"])] = h_dic
"""

#for x in range(len(hexa)) :
#    print(str(hexa[x]["WEN_NUMBER"]) + "\t" +hexa[x]["NAME"])


#import numpy as np
#np.save("hexagrams.npy",hexa)

#hexagrams = np.load("hexagrams.npy")

#for x in range(len(hexagrams)) :
#    print(str(hexagrams[x]["WEN_NUMBER"]) + "\t" +hexagrams[x]["NAME"])


#TRIGRAMS
"""
root = ET.parse('trigrams.xml').getroot()
for i in range(len(root)) :
    t_dic = {}
    for t in root[i] :
        t_dic[t.tag]= t.text
    tri.append(t_dic)

np.save('trigrams.npy', tri)


trigrams = np.load('trigrams.npy')
for i in trigrams : print(i)
"""