def split_text(string):
    '''default to 10 words per line'''
    string = string.split()
    sentences = (len(string) // 10) + 1
    lst = []
    for i in range(sentences):
        if i != sentences:
            lst.append(' '.join(string[(i * 10):(i * 10) + 10]))
        else:
            lst.append(' '.join(string[(i * 10):]))
    return lst

def max_file_number(PATH):
    import os
    folder = os.listdir(os.fsencode(PATH))
    print(folder)
    fnumbers = [str(file) for file in folder]
    print(fnumbers)
    if fnumbers:
        return max(fnumbers + 1)
    return '1'

def write(text):
    if isinstance(text, str):
        text = split_text(text)
    wfname, ext = 'whole_text', '.txt'
    PATH = '.\\whole_texts\\'
    write_file = open(PATH + wfname + '_' + max_file_number(PATH) + ext, 'w')
    for line in text:
        write_file.write(line + '\n')
    write_file.close()
