from Reseau import Reseau
from GUI import GUI
from tkinter import Tk

#!/usr/bin/python3
#-*-coding:utf-8-*-

# =============================================================================
# Lien vers le git : https://github.com/MaxencePRSZ/Proj-631-Sibra
# =============================================================================



def openFile(file):
    """Ouvre et trie les informations utiles dans le fichiers data entré 
        en paramètre

    Parameters
    ----------
    file : file
        Un fichier qui contient les données qui nous interessent

    Returns
    -------
    list
        Liste contenant les données parsées
    """
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
    """renseigne les dates passées en paramètres en un dictionnaire

    Parameters
    ----------
    list : dates
        Une liste des horaires qui ont été séparés précedemment

    Returns
    -------
    dict
        retourne un dictionnaire des dates
    """
    dic = {}
    splitted_dates = dates.split("\n")
#    print(splitted_dates)
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
#    print(dic)
    return dic

def parseBusStops(data):
    """Parse le + comme un N pour plsu de facilité lors du traitement des données

    Parameters
    ----------
    list : data
        une liste contenant les noms des arrets séparé d'un N ou d'un +

    Returns
    -------
    list
        Liste des arrets de bus
    """
    return data[0].replace(" + ", " N ").split(" N ")

def fillHoraire(reseau, data):
    """renseigne les horaires pour chaque arrets de bus

    Parameters
    ----------
    reseau : reseau
        Objet reseau qui est l'objet 'pere', qui correspond à la structure du 
        projet
    list : data
        une liste contenant les noms des arrets séparé d'un N ou d'un +

    Returns
    -------
    """
    for i in range(1, 6):
        if i == 3 :
            continue;
        reseau.fillHoraires(dates2dic(data[i]), i)

def addLigneFromtxt(reseau, file):
    """Ajoute les lignes du fichier passé en paramètre dans la structure reseau

    Parameters
    ----------
    reseau : reseau
        Objet reseau qui est l'objet 'pere', qui correspond à la structure du 
        projet
    file : file
        Un fichier qui contient les données qui nous interessent

    Returns
    -------
    """
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
#print(reseau.djikstraShortest(reseau.listBusStop[4], reseau.listBusStop[21]))
print(reseau.djikstraForemost(reseau.listBusStop[1], reseau.listBusStop[8], "10:00"))

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