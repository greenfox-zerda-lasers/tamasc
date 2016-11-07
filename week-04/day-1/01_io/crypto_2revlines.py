# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    fr = open(file_name, 'r')
    text = ''
    for line in fr:
        text = text + line[::-1]
    text = text + '\n'
    fr.close()
    return text[1:]
