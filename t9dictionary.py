import time

class Trie:
    def __init__(self, char):
        self.character = char
        self.mapping = {}

#Function to print the different contacts that are possible with the given input in the keypad
def printpossibilities(word,dictionary):
    if not dictionary.mapping:
        print(''.join(char for char in word))
    
    else:
        for letter in dictionary.mapping:
            word.append(letter)
            printpossibilities(word,dictionary.mapping[letter])
            word.pop()

#Function to search for contact names based on keypad input
def search(number,keypad,curr,end,word,dictionary):
    if(curr == end):
        printpossibilities(word,dictionary)
        
    else:
        possible_letters = keypad[number[curr]]
        for character in possible_letters:
            if(character in dictionary.mapping):
                word.append(character)
                search(number,keypad,curr+1,end,word,dictionary.mapping[character])
                word.pop()
    

# Main function to enumerate the possible contact names given the keypad input
def t9dictionary(number,keypad,dictionary):
  start = 0
  end = len(number)
  words = []

  search(number,keypad,start,end,words,dictionary)

# Function to insert a contact into the dictionary
def insertcontact(root,contact):
    length = len(contact)
    i = 0

    curr_map = root.mapping
    while i < length:
        if contact[i] not in curr_map:
            temp = Trie(contact[i])
            curr_map[contact[i]] = temp
            curr_map = temp.mapping
        
        else:
            curr_map = curr_map[contact[i]].mapping

        i += 1

#Function to create a dictionary
def createdictionary(contacts):
    root = Trie('+')

    for contact in contacts:
        insertcontact(root,contact)
    
    return root

#Function to print a dictionary
def printdictionary(dictionary,result):
    root = dictionary.mapping
    if not root:
        print(result)
    
    else:
        for letter in root:
            result.append(letter)
            printdictionary(root[letter],result)
            result.pop()
        
def getcontacts(filename):
    f = open(filename,'r')
    contacts = []
    for line in f:
        contacts.append(line.rstrip('\n'))
    return contacts

def main():
    number = [5,3,7]
    keypad = {0: [], 1: [], 2: ['a','b','c'], 3: ['d','e','f'], 4:['g','h','i'] , 5: ['j','k','l'], 6: ['m','n','o'], 7: ['p','q','r','s'], 8: ['t','u','v'], 9: ['w','x','y','z']}
    contacts = getcontacts("contacts.txt")
    # start_time = time.time()
    dictionary = createdictionary(contacts)
    t9dictionary(number,keypad,dictionary)
    # print(" %s seconds " % (time.time() - start_time))


if __name__ == "__main__":
    main()
