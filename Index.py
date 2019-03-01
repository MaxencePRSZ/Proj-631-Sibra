from Reseau import Reseau
from GUI import GUI
from tkinter import Tk

#!/usr/bin/python3
#-*-coding:utf-8-*-

def openFile(file):
    try:
        with open(file, 'r') as f:
            content = f.read()
    except OSError:
        # 'File not found' error message.
        print("File not found")
    slited_content = content.split("\n\n")
#    regular_path = slited_content[0]
#    regular_date_go = dates2dic(slited_content[1])
#    regular_date_back = dates2dic(slited_content[2])
#    we_holidays_path = slited_content[3]
#    we_holidays_date_go = dates2dic(slited_content[4])
#    we_holidays_date_back = dates2dic(slited_content[5])
#    print("#########\n#########\n")
#    print(slited_content)
    return slited_content

def dates2dic(dates):
    dic = {}
    splitted_dates = dates.split("\n")
#    print(splitted_dates)
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
#    print(dic)
    return dic

def parseBusStops(data):
    return data[0].replace(" + ", " N ").split(" N ")

def fillHoraire(reseau, data):
    for i in range(1, 6):
        if i == 3 :
            continue;
        reseau.fillHoraires(dates2dic(data[i]), i)

def addLigneFromtxt(reseau, file): 
    reseau.incrementCountLigne()
    numLigne = reseau.getCountLigne()
    data = openFile(file)
    busStops = parseBusStops(data)
    reseau.addBusStops(busStops, numLigne)
    fillHoraire(reseau, data)

# =============================================================================
#                       Execution
# =============================================================================

#Récupération des fichiers
data_file_name1 = 'data/1_Poisy-ParcDesGlaisins.txt'
data_file_name2 = 'data/2_Piscine-Patinoire_Campus.txt'

#Création du réseau
reseau = Reseau()
addLigneFromtxt(reseau, data_file_name1)
addLigneFromtxt(reseau, data_file_name2)
#print(reseau.djikstra(reseau.listBusStop[6], reseau.listBusStop[9]))
print(reseau.djikstraFastest(reseau.listBusStop[1], reseau.listBusStop[4], "10:00"))

# =============================================================================
#           INTERFACE UTILISATEUR
# =============================================================================

root = Tk()
ww = GUI(root)
for count, i in enumerate(reseau.listBusStop):
    ww.listBox1.insert(count, i.name)
ww.listBox1.pack()
#root.mainloop()



# =============================================================================
#           Information de data
# =============================================================================
#
#data[0] -> bus stops sur le trajet aller
#dates2dic(data[1]) -> Dictionnaire des horaires du trajet aller 
#dates2dic(data[2]) -> Dictionnaire des horaires du trajet retour
#dates2dic(data[3]) -> Dictionnaire des arrets en période de vacance
#dates2dic(data[4]) -> Dictionnaire des horaires du trajet aller durant les vacs
#dates2dic(data[5]) -> Dictionnaire des horaires du trajet retour durant les vacs