string="iamsky"
stringLength=len(string)

newString=""

for i in range(0,stringLength):
    print(string[stringLength-i-1] ,end="" ) 
        # or
print("")
for char in string:
    newString=char+newString

print(newString)

