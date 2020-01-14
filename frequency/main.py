from collections import OrderedDict





def file():
    f=open("text.txt","r")
    contents =f.read()
    contents = contents.lower()
    contents = contents.replace(",", " ")
    contents = contents.replace(".", " ")
    contents = contents.replace("?", " ")
    contents = contents.replace("!", " ")
    contents = contents.split()
    return contents
    print(contents)

def frequence(contents, n):
    frequence = {}
    for items in contents:
        frequence[items] = contents.count(items)
    
    frequence = OrderedDict(sorted(frequence.items(), key=lambda x: x[1]))
    for key, value in frequence.items():
        print("{}: {}".format(key, value))
    

if __name__ == "__main__":
    contents = file()
    frequence(contents, 10)