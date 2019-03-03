def split_text(string):
    '''default to 10 words per line'''
    string = string.split()
    sentences = len((string) // 10) + 1)
    lst = []
    for i in range(sentences):
        if i != sentences:
            lst.append(' '.join(string[(i * 10):(i * 10) + 10]))
        else:
            lst.append(' '.join(string[(i * 10):]))
    return lst

def write(text):
    if text.isinstance(str):
        text = split_text(text)
    wfname = 'whole_text.txt'
    write_file = open(wfname, 'w')
    for line in text:
        write_file.write(line)
    write_file.close()

if __name__ == '__main__':
    print(split_text('The quick brown fox jumped over the lazy dog The quick brown fox jumped over the lazy dog The quick brown fox jumped over the lazy dog The quick brown fox jumped over the lazy dog'))
