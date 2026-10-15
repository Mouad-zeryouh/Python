Prénom = input("Entrez votre prénom : ") 
Age = input("Entrez votre age : ")
Taille_cm = input("Entrez votre taille en cm : ")
age = int(Age) + 5  
taille_m = int(Taille_cm) / 100
print("Bonjour", Prénom)
print("Dans 5 ans vous aurez", age,"ans")
print("Votre taille est de", taille_m, "mètres." )