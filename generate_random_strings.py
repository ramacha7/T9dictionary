import string
import random

def main():
    f = open("contacts.txt","w")
    for i in range(1000):
        length = random.randint(1,10)
        word = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
        f.write(word + "\n")
    
    f.close()


if __name__ == "__main__":
    main()