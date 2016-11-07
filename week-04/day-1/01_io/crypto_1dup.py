# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    fr = open(file_name, 'r')
    text = ''
    for line in fr:
        i = 0
        while i < len(line) - 1:
            text = text + line[i]
            if line[i] == line[i+1]:
                i += 1
            else:
                pass
            i += 1
        text = text + '\n'
    fr.close()
    return text
