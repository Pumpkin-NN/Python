import matplotlib.pyplot as plt
from collections import OrderedDict





def file_handle():
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

# Use Dictionary
def frequence(contents, n):
    frequence = {}
    for items in contents:
        frequence[items] = contents.count(items)
    
    frequence = OrderedDict(sorted(frequence.items(), key=lambda x: x[1]))
    
    # The total length of the dictionary
    Length = len(frequence.keys())
    
    Key = []
    Value = []
    count = 0
    for key, value in frequence.items():
        if count < Length - n:
            count = count + 1
        else:
            Key.append(key)
            Value.append(value)
            
    '''
    # Another approach:
    #Key = Key[::-1]
    #Key = Key[:n]
    
    #Value = Value[::-1]
    #Value = Value[:n]
    print(Key, Value)
    '''
    
    return Key, Value
        
def plot(l1, l2):
    plt.figure(figsize=(9, 6))
    plt.bar(l1, l2)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.show()
    
# Main function
if __name__ == "__main__":
    contents = file_handle()
    Key, Value = frequence(contents, 20)
    plot(Key, Value)