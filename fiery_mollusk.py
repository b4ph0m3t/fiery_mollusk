#usare python2
import string

filehandle = open("proteine_mitilo_nr.clstr", 'r')
outputhandle = open("ptroteine_mitilo_coppie.csv", 'w')
intero = str(filehandle.read())
vect = intero.split("\n>")
coppie = 0
coppiebuone = 0
ve2 = []
for item in vect:
    temp=list(item.split("\n"))
    if (len(temp) == 3) and ('' not in temp):
        coppie +=1
        if ("100.00%" not in temp[1]) and ("100.00%" not in temp[2]):
            coppiebuone +=1
            ve2.append(temp)

for item in ve2:
    print(item)
print("%d coppie trovate in totale, di cui %d non identiche" %(coppie, coppiebuone))
filehandle.close()

for item in ve2:
    cluster = str(item[0]).translate(None,">.")
    nome1 = str(item[1].split(" ")[1]).translate(None,">.")
    nome2 = str(item[2].split(" ")[1]).translate(None,">.")
    outputhandle.write("%s,%s,%s\n" %(cluster, nome1, nome2))
outputhandle.close()
