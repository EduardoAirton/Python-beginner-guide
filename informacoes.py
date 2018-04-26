#---------------------------------------------------------------------------------------
# STRING
myString = "abcdefg"

# Slicing
print(myString[2:]) # Printa todos as letras aparti do indice 2 "CDEFG"
print(myString[::2]) # Printa todos pulando de dois em dois "ACEG"
print(myString[::-1]) # Printar os elementos ao contrario

# Basic Methods
myString.upper() # Deixa maiusculo
myString.capitalize() # Deixa a primeira letra maiuscula

# Print Formatting
"Insert another String here: {}".format("Hello world") # Adiciona a frase na string

# Range

list(range(0,5)) # [0,1,2,3,4]
list(range(0,20,2)) # [0,2,4,6,8,10,12,14,16,18]
range(Start, Stop, Step)

# IN

print('x' in [1,2,3,'x']) # Verifica se 'x' esta na lista "True"

a = "Hiabc"
b = "abc"
# StartWith
a.startwith(b) or b.startwith(a) # Verifica se as primeiras palavras de uma String sao iguais
# EndsWith
b.endswith(a) or a.endswith(b) # Verifica se as ultimas palavras de uma String sao iguais

#---------------------------------------------------------------------------------------
# LIST

myList = [1,2,3]
myList.append(['x','a','c']) # Adicona na lista "[1,2,3,['x','a','c']]"
myList.extend(['x','a','c']) # Adiciona todos os objetos separadamente na lista "[1,2,3,'x','a','c']"
myList.pop() # Retira o ultimo objeto da lista e retorna esse valor
myList.reverse() # Muda os objetos da lista de posição
myList.sort() # Muda os objetos da lista de posição de forma aleatoria

#---------------------------------------------------------------------------------------
# Tuple
myTuple = (1,2,3) # Tupla não pode ser alterada

# DICTIONARIES
myStuff = {"Key1": "value", "Key2":"value"}

# SET
set([1,1,1,1,2,2,2,2,3,3,3,3]) # So adiciona elementos unicos, não repetidos " {1,2,3} "
#---------------------------------------------------------------------------------------
# FOR
seq = [1,2,3,4,5,6]

for item in seq:
    print(item)

#------
carta = "H D S C".split()
naipe = "2 3 4 5 6 7 8 9 10 J Q K A".split()

minhaCarta = []
for i in carta:
    for j in naipe:
        minhaCarta.append((i,j))

# Forma simplificada
minhaCarta = [(i,j) for i in Carta for j in naipe]
#------

out = [num**2 for item in seq] # Apresenta todos os numeros de seq multiplicaos por 2
#---------------------------------------------------------------------------------------
# WHILE
i = 1

while i<5:
    print("i é {}".format(i))
    i += 1
#---------------------------------------------------------------------------------------
# FUNCTIONS

def my_func():
    """Documentação da funcao."""
    print("My function")
#---------------------------------------------------------------------------------------
# FILTER

myList = [1,2,3,4,5,6,7,8,9]

def even_bool(num):
    return num%2 == 0
evens = filter(even_bool, myList)
print(list(evens)) # Aprensetar todos os numeros pares da lista

# LAMBDA

evens = filter(lambda num: num%2 == 0, myList)
print(list(evens))

#---------------------------------------------------------------------------------------
# CLASS

class ClassName():
    # Class Object Attribute
    species = "Human"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Herança
class Animal():
    def __init__(self):
        print("Animal Criado")
    def whoAmI(self):
        print("Animal")
    def comer(self):
        print("Comendo")

pet = Animal()

class Dog(Animal):
    def __init__(self):
        print("DOG Criado")
    def __str__(self):       # Metodo Especial String Representation(ToString)
        print("SomeThing")

    def latir(self):
        print("Au Au")

#---------------------------------------------------------------------------------------
# Arquivo

open("myfile.txt", 'r')
#---------------------------------------------------------------------------------------

# Erros and Exceptions

try:
    f = open("simple.txt", 'w')
    f.write("Teste de um texto simples!")
except IOError: # Nao e necessario colocar o IOError, sem tambem funciona
    print("ERROR: Arquivo nao encontrado")
else:
    print("Arquivo aberto com sucesso")
    f.close()
finally:
    print("Sempre vai rodar") # Sempre vai rodar idependente dos resultados anteriores
#---------------------------------------------------------------------------------------

# Django

Conda create --name virEnv django
conda install django
source activate virEnv
django-admin startproject first_project
python mange.py startapp first_app
python manage.py runserver
