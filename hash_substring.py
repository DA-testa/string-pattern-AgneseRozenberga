#Agnese Rozenberga 11. grupa 221RDB117
# python3
import random
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    izvelne = input().strip()
    if izvelne == "F":
        filename = input().strip()
        with open(filename, 'r') as f:
            pattern =f.readLine().strip()
            text = f.readLine().strip()
            return  pattern, text

    else:
       
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
        return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(str(x) for x in output))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    p =10 ** 9 + 7
    x = random.randint(1,p - 1)
    lengthp = len(pattern)
    lengtht = len(text)

    if lengthp>lengtht:
        return[]
    
    ash =0
    hash = 0

    for i in range (lengthp):
        ash = (ash * x + ord(pattern[i])) % p
        hash = (hash* x + ord(text[i]))%p

    powofx = 1
    for i in range(lengthp - 1):
        powofx = (powofx * x) % p
    
    occurances = []
    for i in range(lengtht - lengthp+1):
        if ash == hash:
            if pattern == text[i:i+lengthp]:
                occurances.append(i)
        if i < lengtht - lengthp:
            hash = ((hash - powofx * ord(text[i]))* x + ord(text[i + lengthp])) % p
            hash = (hash + p) % p

    return occurances


# this part launches the functions
if __name__ == '__main__':
    pattern, text = read_input()
    occurances = get_occurrences(pattern, text)
    print_occurrences(occurances)

