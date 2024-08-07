# print(object(s), sep=separator, end=end, file=file, flush=flush)



print("hello world !!")
with open("first.py","w") as f:
    print("print('hello')",file=f)
print("Hello", "how are you?", sep="---",end="hii")