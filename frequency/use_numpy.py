import numpy as np
import matplotlib.pyplot as plt




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
    frequence = []
    y = []
    for i in contents:
        if i not in frequence:
            frequence.append(i)
            x = np.array([i, contents.count(i)])
            #print(x)
            y = np.append([y],[x])
    print(y)
    
    #for element in y:
    #    print(element)
    
    
def plot(n):
    plt.plot(n)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    contents = file()
    n = frequence(contents, 10)
    # plot(n)