import statistics

data = []

t = input("Words to use:")

for achr in t:
    data.append(ord(achr))
    print(achr)
    print(ord(achr))

#This code was made by Malokai Persoff, please do not redistribute without permission.


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
decs = input("Press enter to close.")
