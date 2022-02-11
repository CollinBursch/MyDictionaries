def main():
    infile = open('AI.txt', 'r') #read the Al.txt file object assigned to infile variable
    
    word_frequency = {}
    for line in infile:
        # Each line as a big string in the infile
        for word in line.split():
            # Each word as a string in the lines
            if word_frequency.get(word): #if the word is a key in the dictionary, incriment the key's value 
                word_frequency[word] += 1
            else: #if the word is not a key in our dict, then create a key for that string, and set its value to 1
                word_frequency[word] = 1

    print(word_frequency)
    
    infile.close()

main()