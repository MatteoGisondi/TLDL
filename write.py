def split_text(string):
    '''default to 10 words per line'''
    string = string.split()
    sentences = (len(string) // 10) + 1
    lst = []
    for i in range(sentences):
        if i != sentences:
            lst.append(' '.join(string[(i * 10) : (i * 10) + 10]))
        else:
            lst.append(' '.join(string[(i * 10) :]))
    return lst


def max_file_number(PATH):
    from os import listdir

    folder = listdir(PATH)
    fnumbers = []
    for file in folder:
        try:
            start = file.rindex('_')
            end = file.rindex('.')
            fnumbers.append(int(file[start + 1 : end]))
        except:
            pass
    try:
        return str(max(fnumbers) + 1)
    except:
        return '1'


def writeS(text, path):
    if isinstance(text, str):
        text = split_text(text)
    # wfname, ext = 'text', '.txt'
    #    PATH = '.\\whole_texts\\'
    # PATH + wfname + '_' + max_file_number(PATH) + ext
    write_file = open(path, 'w')
    for line in text:
        write_file.write(line + '\n')
    write_file.close()
