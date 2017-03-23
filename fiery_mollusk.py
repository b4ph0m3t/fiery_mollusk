#usare python2
import string
inputname=""
outputname=""
if (inputname == "" or outputname == ""):
    print("please define input/output in script file")
    exit()
intero = str(filehandle.read())
vect = intero.split("\n>")
coppie = 0
coppiebuone = 0
ve2 = []
for item in vect:
    temp=list(item.split("\n"))
    if (len(temp) == 3) and ('' not in temp):
        coppie +=1
        if ("at" in temp[1]): # la percentuale scritta di fianco al primo elemento della coppia
            score = float(temp[1].split("at ")[1].translate(None,"%"))
            if (score < 95.00):
                coppiebuone +=1
                ve2.append(temp)
        else: # la percentuale scritta a fianco al secondo elemento della coppia (credo, in realta si, in uno dei due sta scritto)
            score = float(temp[2].split("at ")[1].translate(None,"%"))
            if (score < 95.00):
                coppiebuone +=1
                ve2.append(temp)
        '''if ("100.00%" not in temp[1]) and ("100.00%" not in temp[2]):
            coppiebuone +=1
            ve2.append(temp)'''

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

