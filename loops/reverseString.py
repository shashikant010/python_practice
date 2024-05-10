string="iamsky"
stringLength=len(string)

newString=""

# for i in range(0,stringLength):
#     newString+=string[stringLength-i-1]          or

for char in string:
    newString=char+newString

print(newString)

