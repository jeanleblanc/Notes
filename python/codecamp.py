from importlib.abc import Traversable
from math import *

# Free code camp : python in 4h

    # Hello World & draw a shape

print("Hello World") #print va "imprimer" ce que l'on va ecrire"

print("   /|")
print("  / |")
print(" /  |")
print("/___|")
# Python execute les lignes dans l'ordre
print("___________________________________________________________________")

    # variable & data type

print("There once was a man named George, ")
print("he was 70 years old. ")
print("He really liked the name George, ")
print("but didn't like being 70.")
#une variable est un conteneur de donées
#changeons le nom et l'age du personnage -->
print("------------------------------------------")
name = "John"
age = "35"
print("There once was a man named "+ name+ ", ") # ajouter une variable entre deux "+"
print("he was "+age+ " years old. ") # attention de bien remmetre des guillemets
print("He really liked the name "+ name+" , ") #attention aux espaces
print("but didn't like being "+age+".")#pour changer le nom du personnage il 
#faut juste changer ce qui se trouve apres la variable ("john" --> "tom")
print("------------------------------------------")
name = "John"
age = "35"
print("There once was a man named "+ name+ ", ") 
print("he was "+age+" years old. ")
age = "78"
name = "tom"
print("He really liked the name "+ name+" , ") 
print("but didn't like being "+age+".")

#autres types de données
name = "tom" #chaine de charactere toujours entre "xx"
age = 50.5 #nombre
isMale = True  #boolean repondre True or False  

print("___________________________________________________________________")

    #Working with strings 

#string sont des chaine de caractere
print("giraffe academy")
print("giraffe \nacademy") #\n va passer dans la string à la ligne 
print("giraffe \"academy") # \" va litteralement ecire le guillemet
phrase = "Giraffe Academy"
print(phrase) 
print(phrase +" is cool")# concaténation : prend une chaine et en 
#ajoute une autre
print("------------------------------------------")
print(phrase.lower())#on peut ajouter une fonction à une string
# en locurence lower met tout en minuscule
print(phrase.upper()) #a l'inverse met tout en maj
print(phrase.isupper()) #verifie si la phrase est en majuscule
print(phrase.upper().isupper()) #on peut mettre une fonction apres une autre
print(len(phrase)) #pour savoir cb il y a de characteres
print(phrase[0]) #pour savoir quel est le caractere x de la phrase (ici 0)
#en python on commence a compter par 0
print(phrase.index("i")) #pour savoir en quelle position se trouve la lettre x
print(phrase.index("Aca")) #nous dis en quelle position commence xxx
#si on met dans index qq chose qui n'existe pas --> message d'erreur
print(phrase.replace("Giraffe", "Elephant")) #on remplace giraffe par (,) elephant

print("___________________________________________________________________")

# Working with numbers

print(2)#pour imprimer un nbrs 
print(3.643)#pour imprimer un nbrs decimal 
print(-535)#pour imprimer un nbrs negatif

print("------------------------------------------")
#on peut aussi faie des operations
print(4 + 4 - 7 * 2 / 2) #plus moins fois diviser
print(3 * (4 + 5))#PEMIMDAS
print(10 % 3)#10 mode 3 premier nbrs / deuxieme et renvoie le reste
print("------------------------------------------")
Num = 45
print (Num)#variable avec un num
print (str(Num) + " it's my age")#pour convertir num en 
#une string (pour pouvoir ajouter apres une string) ==> erreur si on le fait pas
Num = -5
print (abs(Num))#donne la valeure absolue
print (pow(5, 3))#x^y
print (max(5, 13))#renvoie le numero le plus grand
print (min(5, 13))#renvoie le numero le plus petit
print (round(3.7)) #arrondis ton nombre
#pour utiliser plus de fonction math il faut declarer <<from math import *>> en haut
print(floor(6.795139))#arrondi au nbrs le plus bas
print(ceil(1.2))#arrondi au plus grand
print(sqrt(9))#fait la racine carré

    #Getting input from users 

print("___________________________________________________________________")

#permetre à un utilisateur d'entrer des infos dans notre porgramme
#input("Enter your name : ") #input dis qu'on demande a l'user une info ("info: ")
#name = input("Enter your name : ")
#age = input("Enter your age : ")
#print ("Hello my name is "+name+" and i have "+age+" years old.") #pour 
#utiliser les données reçus

    #Building a basic calculator
    
print("___________________________________________________________________")

#premiere chose à faire est crée deux variable dans lequels on veut stocker
#les deux nombres que l'user veut additioner
#num1 = input("Enter a number : ") 
#num2 = input("Enter another number : ") 
#result_badexemle = num1 + num2 # ici il va faire comme si les var. etaient des 
#string donc va afficher 58 au lieu de 13
#result_int = int(num1) + int(num2) #int()va transformer ce qu'il y a dans la parenthese
# en nombre entier, on ne peut pas avoir de decimales...
#result = float(num1) + float(num2)
#print("Result : " +str(result))

    #Mad libs game
    
print("___________________________________________________________________")
#crée une mad libs en python (txt a trous remplis avec des mots aleatoires)
#color = input("Enter a color : ")
#plural_noun= input("Enter a plural noun : ")
#celebrity = input("Enter a celebrity : ")


#print("Rose are " + color)
#print(plural_noun+" are blue ")
#print("I love "+celebrity )

        #LIST
# structure utilisable a l'interieur de python
# on crée une liste pour mettre un tas de valeures liées   
friends = ["Kevin", "Karen", "Jim"] #[]pour dire qu'on va entrer des valeurs
#a notre liste
# variable = 1 value / List = xValue
friends = ["Kevin", 2, False] # on peut aussi mettre nbrs et bolean
friends = ["Kevin", "Karen", "Jim"] 
print(friends)
# pour avoir acces a un seul ca marche comme un index (0, 1, 2...)
print(friends[1]) #ca marche avec des nbrs negatif
print(friends[-1])#va renvoyer vers le dernier > ici le 2e
# [-2] l'avant dernier etc.
print(friends[1:]) #va donner l'element 1 et tout ce qu'il y a apres
friends = ["Kevin", "Karen", "Jim", "Oscar", "Jean", "Toby"]
print(friends[2:4]) # de l'element 2 a (:) 4 exclu
print(friends[:3]) # jusqu'a 3
friends[1] = "Mike" # pour changer la valeur de l'index 1
print(friends[1]) #ce sera mis a jour 
print("______________________________________________________________________")

# List function

lucky_nbrs = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.extend(lucky_nbrs)#fonction extension :  prend une liste et 
#ajoute une autre liste a la fin
friends.append("Creed") # ajoute qq a la fin de la liste
friends.insert(1, "Kelly") # ajoute en position 1 kelly
friends.remove("Jim") #suprimme un element de la liste
friends.pop() #enleve  le dernier element de la liste
friends.clear() #efface tout ce qu'il y a dans la liste

lucky_nbrs = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#on veut savoir si qq est dans cette liste
print(friends.index("Kevin")) #nous renvoi l'index (pos) de Kevin dans la liste
#si on met un nom qui n'est pas dans la liste > erreur
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
#on veut savoir si qq est dans cette liste
print(friends.count("Jim")) #nous renvoi le nbrs de Jim dans la liste
#si on met un nom qui n'est pas dans la liste > erreur

friends.sort() #va trier "" ordre alphabetique, 4 ordre croissant.
print(friends)

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends.reverse() #va donner la liste dans le sens inverse
print(friends)

friends2 = friends.copy() #crée une copy de la liste 

print("______________________________________________________________________")


    # Tuples
#type de data structur containeur ou on peut stocker differente valeurs
#ressemble a une liste
coordinates = (4, 5) #pour crée un tuple on utilise () et on met les values qu'on veut stock
#particularité il est immuable : on pt pas le modif
print(coordinates[0]) #index ici est entre []
# on utilise les tuples pour des données qui ne vont jamais changer
coordinates = [(1, 5), (265,4), (2,3)] #on peut aussi crée des listes de tuple

print("______________________________________________________________________")

    #Fonctions
#collection de code qui acompli une tache particuliere

def say_hi(): #ça dit que tout le code qui va venir après c'est notre fonction
    #il faut forcement l'indenté (tab)
    print("Hello User") # mais en mettant jusque ça il ne le fait pas

say_hi() # il faut appeler la fonction
# python execute la fonction là ou elle est appelée

def sayhi(name):
    print("Hello " + name)
    
sayhi("Mike")
sayhi("Steve")

def SayHi(name, age):
    print("Hello " + name + " you are " + age) #si on veut mettre un int il faut 
    #rajouter str(age) et il va convertir en nbrs
    
    
SayHi("Tom", "45")
SayHi("John", "90")

print("______________________________________________________________________")

#return statement 

def cube(num):
   return num*num*num #return va renvoyer tout les valeur inseré après
    #sans le return la fonction renvoi "none"
    
print(cube(3)) #si on ne print pas rien ne se passe

def cube(num):
   return num*num*num   
   print("code") 
    
#on peut crée une variable qui va stocker la valeur retourné par la fonction cube
result = cube(4)   
print(result) #comme on imprime la fonction ça ne va pas executer le "print"


print("______________________________________________________________________")

#if statements
    #c'est une structure special en python où on peut aider notre programme a 
    #prendre des desisons, en utilisant if on peut utiliser un certain code quand
    #certaine conditions sont vraies et inversement.
    #ça permet à notre programme de repondre à ce qu'on peut lui envoyer
   
is_male = True
if is_male:
    print("you are a male") #ce qui est indenté va etre executé si la c'est est vraie
    
is_male = False
if is_male:
    print("you are a male") #Ne va rien faire quand c'est faux
else: # quand le if est faux alors il va executer le else
    print("you are not a male")
    
    #FAISONS PLUS COMPLEXE
    
is_male = False
is_tall = False

if is_male and is_tall: # si les deux sont vrais
    print("you are a big man")
elif is_male and not(is_tall): #si le 1e est vrai et pas le 2e
    print("your are a short male")
elif not(is_male) and is_tall: #si le 2e est vrai mais pas le 1e
    print("You are a big girl")
else: # seulement si aucun des deux est vrai
    print("you are a short girl")
    
















































