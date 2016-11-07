# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    fr = open(file_name,'r')
    text_list = []
    for line in fr:
        text_list.append(line)
    text_list = text_list[::-1]
    text = ''.join(text_list)
    fr.close()
    return(text)
