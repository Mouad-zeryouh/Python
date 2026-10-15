#Partie 1:
#exercice 1:

#on demande a l'utilisateur de renseigner son code pin 
"""code_pin = int(input("Entrer le code PIN : ")) 

#on vérifie si le code est correct 
if code_pin == 4567 :
    print("code correct")
else : 
    print("code incorrect")"""

#Exercice 2 :
#on demande à l'utilisateur un nombre entier
"""nmbr_entier= int(input("Saisir un nombre entier : "))
#affiche “Positif” si ce nombre est supérieur à 0
if nmbr_entier > 0 :
    print("Positif")
# affiche “Négatif” si ce nombre est inférieur à 0
elif nmbr_entier < 0 :
    print("Négatif")
#affiche "Nul" si ce nombre vaut 0
else :
    nmbr_entier == 0
    print("Nul")"""

#Exercice 3 :
#on demande à l'utilisateur un nombre entier
"""nombre_entier= int(input("Saisir un nombre entier : "))
# affiche “pair” si ce nombre est divisible par 2 et que son reste est de 0
if nombre_entier % 2 == 0:
    print(nombre_entier, "est un nombre pair")
# affiche “impair” si ce nombre divisé par 2 donne un reste
else:
    print(nombre_entier, "est un nombre impair")"""

#Exercice 4 : 
#on demande a l'utilisatuer d'entrer son age 
"""age= int(input("Entrer votre age : "))
#affiche (A "N" ans, vous êtes un enfant.) si l'age est inférieur a 12 ans 
if age < 12 :
    print("A", age,", vous etes un enfant.")
#affiche (A "N" ans, vous êtes un adolescent.) si l'age est entre 12ans et 18 ans 
elif age < 18  :
    print("A", age,", vous etes un adolescent.")
#affiche (A "N" ans, vous êtes un adulte.) si l'age est supérieur ou égal a 18 ans 
else :
    age >= 18
    print("A", age,", vous etes un adulte.")"""

#Exercice 5 :
# On demande le prix de fabrication et le prix de vente 
"""
prix_fabrication = float(input("Prix de fabrication : "))
prix_vente = float(input("Prix de vente : "))

# On compare les deux prix
if prix_vente < prix_fabrication:
    print("perte")
else:
    print("profit")
    """

#Exercice 6:

# On demande a l'utilisateur les 3 nombres :
"""
nombre1 = float(input("Saisir le premier nombre : "))
nombre2 = float(input("Saisir le second nombre : "))
nombre3 = float(input("Saisir le troisième nombre : "))

# On détermine le maximum entre ces 3 nombres :
if nombre1 >= nombre2 and nombre1 >= nombre3:
    print("Le maximum est le premier nombre", nombre1)
elif nombre2 >= nombre1 and nombre2 >= nombre3:
    print("Le maximum est le second nombre", nombre2)
else:
    print("Le maximum est le troisième nombre", nombre3)
"""

#Exercice 7:
#on demande a l'utilisateur de renseigner la longueur des cotés du trianlge:
"""
print("Veuiller entrer les longueurs dans l’ordre croissant s'il vous plait !")
cote1 = float(input("côté 1 : "))
cote2 = float(input("côté 2 : "))
cote3 = float(input("côté 3 : "))

# On vérifie l'ordre des côtés
if cote1 <= cote2 and cote2 <= cote3:

    # On applique le théorème de Pythagore:
    #si le théorème est validé afficher (triangle rectangle)5
    if cote3 ** 2 == cote1 ** 2 + cote2 ** 2:
        print("triangle rectangle")
    #si le théorème n'est pas validé afficher (triangle non rectangle)
    else:
        print("triangle non rectangle")
#si l'ordre des coté n'est pas croissant on affiche (Les longueurs des côtés n’ont pas été saisies dans l’ordre croissant.)
else:
    print("Les longueurs des côtés n’ont pas été saisies dans l’ordre croissant.")
    """

#Partie 2 :

#Exercice 1:
#on demande a l'utilisateur de saisir une année :
"""
annee= int(input("Saisir l'année : "))
#on calcule si l'année saisit est bisextile ou non:
if (annee % 4 == 0 and annee % 100 !=0) or annee % 400==0 :
   #si elle l'est on affiche (Année bissextile):
    print("Année bissextile")
#sinon on affiche (Année non bissextile):
else :
    print("Année non bissextile")
    """

#Exercice 2:
"""
age = int(input("Saisir votre âge: "))

# On teste les tranches d'âge une par une du plus petit au plus grand (sans and/or)
if age <= 5:
   # Gratuit pour les enfants de 5 ans et moins
   prix = 0  
elif age < 16:
    # Moitié du tarif plein pour les mineurs dont l'âge est de plus de 5 ans et de strictement moins de 16 ans (10€ / 2)
    prix = 5  
elif age <= 21:
    # 40% de réduction pour les jeunes ayant entre 16 ans et 21 ans compris (10 - 4) 
    prix = 6  
elif age < 51:
    # Plein tarif pour les passagers ayant strictement plus de 21 ans et moins de 51 ans
    prix = 10  
else:
    # 10% de réduction pour les passagers ayant 51 ans et plus (10 - 1)
    prix = 9  

# Affiche le résultat final
print("Le prix du transport est de", prix, "euros.")
"""

#Exercice 3:
#on demande a l'utilisateur de renssigner le nombre d'élèves, la durée du voyage
"""
nmbr_eleves= int(input("Nombre d'élèves : "))
duree_voyage= int(input("Durée du voyage en jours : "))
#on calcule ensuite le prix de la nourriture par élève pour la durée du voyage
prix_nourriture= 3.50*duree_voyage
#Le coût du transport est de 110 € par élève jusqu’à 25 élèves et de 100 € au-delà.
if nmbr_eleves <=25 :
    prix_transport= 110
else : 
    prix_transport= 100

#le cout de L’hébergement est de 4,20 € par jour et par élève si le nombre d’élèves est strictement inférieur à 20
if nmbr_eleves <20 :
    prix_hébergement= 4.20*duree_voyage
#le cout de L’hébergement est de 3,80 € par jour et par élève si le nombre d’élèves est compris entre 20 et 35 élèves
elif nmbr_eleves <35 :
    prix_hébergement= 3.80*duree_voyage
#le cout de L’hébergement est de 4,00 € par jour et par élève si le nombre d’élèves est strictement supérieur à 35
else :
    prix_hébergement=4.0*duree_voyage
#on calcule le prix total du voyage par élève:
prix_voyage= prix_hébergement + prix_transport + prix_nourriture
#on affiche la phrase suivante (Le prix du voyage revient à prix_voyage euros par élève.)
print("Le prix du voyage revient à",prix_voyage,"par élève.")
"""
#Exercice 4 :
"""
vehiule=input("Quel est le type de véhicule ? : ")
carburant= input("Quel est le type de véhicule ? : ")
duree= int(input("Quelle est la durée de location ? : "))
"""
#Partie 3:

#Exercice 1:
"""
seance = int(input("Nombre de séances : "))
tarif_a= 145+(10.5*seance)
tarif_b= 15.5*seance

if tarif_a < tarif_b :
    print("Pour", seance, "séances,le tarif A est le plus avantageux.")
elif tarif_b < tarif_a :
    print("Pour", seance, "séances,le tarif B est le plus avantageux.")
else :
    print("Pour", seance, "séances,aucun tarif n'est le plus avantageux.")
detail= input("Souhaitez-vous plus de détails? (yes/no) : ")
if detail== "yes" or "Yes" :
    print("Tarif A : ",tarif_a," euros")
    print("Tarif B : ",tarif_b," euros")
"""
#Exercice 2:
"""
caractere= input("Saisir un caractère : ")
if caractere == "a" or caractere == "e" or caractere == "i" or caractere == "o" or caractere == "u" or caractere == "y" or caractere == "A" or caractere =="E" or caractere =="I" or caractere =="O" or caractere =="U" or caractere =="Y" :
    print(caractere,": voyelle")
# elif caractere == "b" or "c" or "d" or "f" or "g" or "h" or "j" or "k" or "l" or "m" or "n" or "p" or "q" or "r" or "s" or "t" or "v" or "w" or "x" or "z" or "B" or "C" or "D" or "F" or "G" or "H" or "J" or "K" or "L" or "M" or "N" or "P" "Q" or "R" or "S" or "T" or "V" or "W" or "X" or "Z" :
elif caractere >= "a" and caractere <= "z" or caractere >= "A" and caractere <= "Z":
    print(caractere,": consonne")
else :
    print(caractere,": caractère spécial")
"""
#Exercice 3:
"""
prix_ht = float(input("Saisir le prix hors taxe : "))


TVA = 19.6
prix_ttc = prix_ht * (1 + TVA / 100)

if prix_ttc < 1000:
    taux_remise = 0
elif prix_ttc < 2000:
    taux_remise = 1
elif prix_ttc < 5000:
    taux_remise = 3
else:
    taux_remise = 5

remise = prix_ttc * taux_remise / 100
prix_net = prix_ttc - remise

print("Prix HT :", round(prix_ht, 2), "euros")
print("Prix TTC :", round(prix_ttc, 2), "euros")
print("Remise :", round(remise, 2), "euros")
print("Prix Net à payer :", round(prix_net, 2), "euros")
"""
#Exercice 4:
"""
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

operation = input("Entrez l'opération (addition, soustraction, multiplication, division) : ")

if operation == "addition":
    resultat = nombre1 + nombre2
    print("> ", nombre1, " + ", nombre2, " = ",resultat)

elif operation == "soustraction":
    resultat = nombre1 - nombre2
    print("> ", nombre1, " - ", nombre2, " = ", resultat)

elif operation == "multiplication":
    resultat = nombre1 * nombre2
    print("> ", nombre1, " * ", nombre2, " = ",resultat)

elif operation == "division":
    if nombre2 == 0:
        print("> Erreur : Division par zéro !")
    else:
        resultat = nombre1 / nombre2
        print("> ", nombre1, " / ", nombre2, " = ",resultat)

else:
    print("> Opération non valide.")
"""
#Exercice 5:





    













