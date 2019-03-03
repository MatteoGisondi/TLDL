def summer(filename,ratio,savedir):
    """
    Summerizes and provides keywords and fucking heck I dont know ffs
    """
    from gensim.summarization import summarize, keywords
    sumSign = "┌─┐┬ ┬┌┬┐┌┬┐┌─┐┬─┐┬ ┬ \n└─┐│ │││││││├─┤├┬┘└┬┘ \n└─┘└─┘┴ ┴┴ ┴┴ ┴┴└─ ┴ "
    kwSign = "┬┌─┌─┐┬ ┬┬ ┬┌─┐┬─┐┌┬┐┌─┐ \n├┴┐├┤ └┬┘││││ │├┬┘ ││└─┐ \n┴ ┴└─┘ ┴ └┴┘└─┘┴└──┴┘└─┘ "
    print('____Opening File_____')
    text = open(filename).read()
    print('____File Succesfully Opened____')

    if __name__ == "__main__":
        print(summarize(text,ratio = ratio))
        print(keywords(text, ratio= ratio))

    # output
    output = open(savedir,'w+')
    output.write(30 * '--' + '\n' + 'FILENAME:' + filename + '\n' + 30 * '--'  + '\n')
    output.write(sumSign + '\n')
    output.write(summarize(text,ratio = ratio) + '\n')
    output.write(kwSign + '\n')
    output.write(keywords(text,ratio = ratio) + '\n')

def dirty_summer(text,ratio,savedir):
    """
    Summerizes and provides keywords and fucking heck I dont know ffs
    """
    from gensim.summarization import summarize, keywords
    sumSign = "┌─┐┬ ┬┌┬┐┌┬┐┌─┐┬─┐┬ ┬ \n└─┐│ │││││││├─┤├┬┘└┬┘ \n└─┘└─┘┴ ┴┴ ┴┴ ┴┴└─ ┴ "
    kwSign = "┬┌─┌─┐┬ ┬┬ ┬┌─┐┬─┐┌┬┐┌─┐ \n├┴┐├┤ └┬┘││││ │├┬┘ ││└─┐ \n┴ ┴└─┘ ┴ └┴┘└─┘┴└──┴┘└─┘ "
    print('____Opening File_____')
    print('____File Succesfully Opened____')

    if __name__ == "__main__":
        print(summarize(text,ratio = ratio))
        print(keywords(text, ratio= ratio))

    # output
    output = open(savedir,'w+')
    output.write(30 * '--' + '\n' + 'FILETYPE:' + ' User Input' + '\n' + 30 * '--'  + '\n')
    output.write(sumSign + '\n')
    output.write(summarize(text,ratio = ratio) + '\n')
    output.write(kwSign + '\n')
    output.write(keywords(text,ratio = ratio) + '\n')
