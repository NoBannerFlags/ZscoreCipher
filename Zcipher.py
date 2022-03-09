import statistics

data = []

t = input("Words to use:")

for achr in t:
    data.append(ord(achr))
    print(achr)
    print(ord(achr))

#This code was made by Malokai Persoff, please do not redistribute without permission.
# Get the ASCII number of a character
#number = ord(char)

# Get the character given by an ASCII number
#char = chr(number)



#data = [11, 22, 33, 44, 41, 51, 55]

x = statistics.mean(data)
y = statistics.median(data)
#b = statistics.mode(data)
a = statistics.stdev(data)
print("Mean = {}".format(x))
print("Median = {}".format(y))
#print("Mode = {}".format(b))
print("Standard dev = {}".format(a))


data2 = []
for p in data:
    print("using data:{}".format(p))

    z = ((p-x)/a)
    print("Standard = {}".format(z))
    data2.append(z)



for p in data2:
    print("using data:{}".format(p))

    z = (p*a)
    z += x
    z = int(z)
    print("Non standard = {}".format(z))
    print("chr = "+chr(z))

encr = ""
nencr = ""
for p in data2:
    encr+="{}".format(p)
    encr+=" "
for p in data:
    nencr+="{}".format(p)
    nencr+=" "
print(encr)
#print(nencr) -- used for debug
print("Keys:")
print("(stdev):{}".format(a))
print(" (mean):{}".format(x))


print("Decrypt mode")
key1 = float(input("stdev "))
key2 = float(input("mean "))



decryptme2 = input("All chrs to decrypt")
decryptme2 = decryptme2.split(' ')
complete = ""
for wd in decryptme2:
    dec = float(wd)*key1
    dec += key2
    dec = int(dec)
    print(chr(dec))
    complete+=chr(dec)
print("Completed string: ")
print(complete)

decs = input("Press enter to close.")


#old code - do not use, archived because I want to remember it
#decryptme = input("Chr to decrypt?")
#dec = float(decryptme)*key1
#dec += key2
#dec = int(dec)
#print(chr(dec))

#while True:
    #decryptme = input("Chr to decrypt?")
    #dec = float(decryptme)*key1
    #dec += key2
    #dec = int(dec)
    #print(chr(dec)) 
#while True
#dataRe = []
#print("add character num vals, end with \'n\'")
#d = ""
#while(d!="n"):
#    d=input("val")
#    if(d!="n"):
#        dataRe.append(d)
    

#for p in dataRe:
#    print("using data:{}".format(p))
#
#    z = (float(p)*key1)
#    z += key2
#    z = int(z)
#    print("Non standard = {}".format(z))
#    print("chr = "+chr(z))
