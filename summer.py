def summer(filename,ratio):
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
    output = open('output.txt','w+')
    output.write(30 * '--' + '\n' + 'FILENAME:' + filename + '\n' + 30 * '--'  + '\n')
    output.write(sumSign + '\n')
    output.write(summarize(text,ratio = ratio) + '\n')
    output.write(kwSign + '\n')
    output.write(keywords(text,ratio = ratio) + '\n')
