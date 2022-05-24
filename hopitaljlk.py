info_docteur = []
info_patient = []
plaints_patient=[]
horaire_medecien=[]
from random import randint
code_dossier=""
for i in range(1):
    i = chr(randint(65,90))
    for j in range(1):
        j = chr(randint(97,133))
        for k in range(2):
            k = chr(randint(47,56))
            code_dossier=str(code_dossier)+k+i+j
def docteur (nom,prenom,postnom,telephone,matricule,specialisation):
    info_docteur.append(nom)
    info_docteur.append(prenom)
    info_docteur.append(postnom)
    info_docteur.append(telephone)
    info_docteur.append(matricule)
    info_docteur.append(specialisation)
    print("Merci d'avoir remplir notre fiche")
    index()
def patient (nom,prenom,postnom,telephone,poids,taille,genre,code_dossier):
    info_docteur.append(nom)
    info_docteur.append(prenom)
    info_docteur.append(postnom)
    info_docteur.append(telephone)
    info_docteur.append(poids)
    info_docteur.append(taille)
    info_docteur.append(genre)
    info_docteur.append(code_dossier)
    print("Merci d'avoir remplir notre fiche")
    index()
def afficher_docteur():
    for d in range (len(info_patient)):
        print(info_patient[d])
        print("================")
def afficher_patient():
    for P in range (len(info_docteur)):
        print(info_docteur[P])
        print("================")
    index()
def plaints(echo):
    plaints_patient.append(echo)
    print ("votre plaints a était bien enregistre")
    index()
def afficher_plaints():
    for b in range (len(plaints_patient)):
        print(str(b+1)+"°)",plaints_patient[b])
        print("================")
    index()
def recherche(patient):
    if patient in info_patient:
        reche = input ("entrez le nom,prenom et postnom du patient")
        afficher_patient()
def horaire (lundi,mardi,mercredi,jeudi,vendredi,samedi):
    horaire_medecien.append(lundi)
    horaire_medecien.append(mardi)
    horaire_medecien.append(mercredi)
    horaire_medecien.append(jeudi)
    horaire_medecien.append(vendredi)
    horaire_medecien.append(samedi)
    print("Merci d'avoir enregistre votre horaire")
    index()
def verification():
    for v in range (len(horaire_medecien)):
        print(horaire_medecien[v])
        print("================")
    index()
def index():
    print("Bienvenu dans notre hopital")
    print("voici les actions à faire")
    action = ["enregistrer un docteur ",
              "enregistrer un patient  ",
              "chercher un patient par ses identités",
              "chercher un patient par le numero de dossier",
              "Afficher tous les patients",
              "Afficher tous les docteurs",
              "enregistrer  les plaintes de patient",
              "enregistrer  l'horaire de chaque medecin",
              "Verifier disponibilité d'un medecin",
              "Afficher les plaintes",
              "Afficher l'IMC",
              ]
    taille=len(action)
    for a in range(taille):
        print (str(a+1)+")",action[a])
    actionUser=int(input("Tapez sur un chiffre de votre préoccupations    :"))
    while actionUser < 1 or actionUser > 11:
        actionUser = int(input("Oops veuillez recommencer    :"))
    if actionUser == 1:
        nom = input ("Entrez votre Nom")
        postnom = input ("Entrez votre prenom")
        prenom = input ("Entrez votre postnom")
        telephone = input ("Entrez votre numero de telephone")
        matricule = input ("Entrez votre matricule")
        specialisation = input ("Entrez votre specialisation")
        docteur(nom,prenom,postnom,telephone,matricule,specialisation)
    elif actionUser == 2:
        nom = input ("Entrez votre Nom")
        prenom = input ("Entrez votre prenom")
        postnom = input ("Entrez votre postnom")
        telephone = input ("Entrez votre numero de telephone")
        poids = input ("Entrez votre poids")
        taille = input ("Entrez votre taille")
        genre = input ("Entrez votre genre")
        age = input ("Entrez votre age")
        print("votre code est",code_dossier)
        patient (nom,prenom,postnom,telephone,poids,taille,genre,code_dossier)    
    elif actionUser == 3:
        recherche()
    elif actionUser == 5:
        afficher_patient()
    elif actionUser == 6:
        afficher_docteur()
    elif actionUser == 7:
        plaints_user=input("Entrez votre plaints")
        plaints(plaints_user)
    elif actionUser == 8:
        lundi=input("Entrez votre programme de lundi")
        mardi=input("Entrez votre programme de mardi")
        mercredi=input("Entrez votre programme de mercredi")
        jeudi=input("Entrez votre programme de jeudi")
        vendredi=input("Entrez votre programme de vendredi")
        samedi=input("Entrez votre programme de samedi")
        horaire (lundi,mardi,mercredi,jeudi,vendredi,samedi)
    elif actionUser == 9:
        verification()
    elif actionUser ==10:
        afficher_plaints()
index()
