from passlib.utils import pbkdf2
import binascii, sys, fileinput

arguments_counter = len(sys.argv) - 1

if arguments_counter != 3:
    if arguments_counter != 4:
        raise TypeError("The function takes exactly 3 or 4 arguments (%d passed)" % arguments_counter)

count = 0
length = 0
wordlist = sys.argv[1]
ssid = sys.argv[2]
pskInput = sys.argv[3]
verbose = None

try:
    verbose = sys.argv[4]
    print("Verbose switch used, warning this may take some extra time to run, but you will see the status")
except:
    print("Verbose switch NOT used, you will not see the status until the word list completes or the encrypted password is found")

# Opening file using ISO-8859-1 due to limits with default utf-8 unable to read large files, like wordlists
file1 = fileinput.input(wordlist,encoding="ISO-8859-1")

print ("Reading wordlist", wordlist)
for line1 in file1:
    length += 1

# Closing files
file1.close()

print(length ," passwords to try to decrypt encrypted PSK: ", pskInput, " using SSID: ", ssid)

# Opening file using ISO-8859-1 due to limits with default utf-8 unable to read large files
file1 = fileinput.input(wordlist,encoding="ISO-8859-1")

for line in file1:
    count += 1   

    password = line.strip()
    var = pbkdf2.pbkdf2(str.encode(password), str.encode(ssid), 4096, 32)

    pskString = (binascii.hexlify(var).decode("utf-8"))
    
    if pskString == pskInput:        
        print("Attempt #", count, " out of ", length)
        print(line + " is the password for SSID: ", ssid," using encrypted PSK: ", pskInput) 
        break

    if verbose != None:        
        print("Attempt #", count, " out of ", length)
        print(line)

# Closing files
file1.close()




