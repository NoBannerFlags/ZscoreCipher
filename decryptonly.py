import statistics

print("Decrypt mode")
key1 = float(input("stdev "))
key2 = float(input("mean "))

#This code was made by Malokai Persoff, please do not redistribute without permission.

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
