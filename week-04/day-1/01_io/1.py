# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    encr = open(file_name,'r')
    text = ''
    for line in encr:
        for chars in line:
            if chars == ' ' or chars == '\n':
                text += chars
            else:
                text += str(chr(ord(chars) - 1))
    encr.close()
    return text

print(decrypt('texts/encoded_zen_lines.txt'))
