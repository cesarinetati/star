
#creation du triangle
rows = 10
k = 2 * rows - 2
lines = []

#Faire un triangle
for i in range(rows, -1, -1):
    line = ""
    
    for j in range(k-rows, 0, -1):
        line += " "
    k = k + 1
    for j in range(0, i + 1):
        line += "**"
    line += "*"
    lines.append(line.ljust(19, " "))


#On ajoute la pointe du triangle    
line = " " * (2*rows-1) + "*"
lines.append(line.ljust(19, " "))


#Tableau vide qui contiendra l'étoile
pattern = [""] * (len(lines) + rows//2)


#On rempli le tableau depuis le début par la pointe de la pyramide
#et la fin du tableau par la base de la pyramide
#On supperpose les deux pyramides avec un décalage
for i in range(len(lines)):
    pattern[i] = (lines[len(lines)-i-1])
    pattern[len(pattern)-1-i] = fusionneLignes(pattern[len(pattern)-1-i], lines[len(lines)-i-1])
 

#On affiche le tableau
for line in pattern:
    print(line)
    

def fusionneLignes(l1, l2):
    while len(l1) < len(l2):
        l1 += " "
    
    while len(l2) < len(l1):
        l2 += " "
    line = ""
    for mot1, mot2 in zip(l1, l2):
        if (mot1 == "*" or mot2 == "*"):
            line += "*"
        else:
            line += " "
    return line
