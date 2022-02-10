"""Summarization"""

from gensim.summarization import summarize, keywords

LINE = 30 * '--'


def summer(file_name, ratio, save_dir):
    """
    Summerizes and provides keywords
    """
    sumSign = "┌─┐┬ ┬┌┬┐┌┬┐┌─┐┬─┐┬ ┬ \n└─┐│ │││││││├─┤├┬┘└┬┘ \n└─┘└─┘┴ ┴┴ ┴┴ ┴┴└─ ┴ "
    kwSign = "┬┌─┌─┐┬ ┬┬ ┬┌─┐┬─┐┌┬┐┌─┐ \n├┴┐├┤ └┬┘││││ │├┬┘ ││└─┐ \n┴ ┴└─┘ ┴ └┴┘└─┘┴└──┴┘└─┘ "
    print('____Opening File_____')
    with open(file_name, "r") as f:
        text = f.read()
    print('____File Succesfully Opened____')

    if __name__ == "__main__":
        print(summarize(text, ratio=ratio))
        print(keywords(text, ratio=ratio))

    # output
    with open(save_dir, 'w+', encoding="utf-8") as output:
        output.write(f"{LINE}\nFILENAME: {file_name}\n{LINE}\n")
        output.write(sumSign + '\n')
        output.write(summarize(text, ratio=ratio) + '\n')
        output.write(kwSign + '\n')
        output.write(keywords(text, ratio=ratio) + '\n')


def dirty_summer(text, ratio, save_dir):
    """
    Summerizes and provides keywords in a dirty way (?)
    """
    sumSign = "┌─┐┬ ┬┌┬┐┌┬┐┌─┐┬─┐┬ ┬ \n└─┐│ │││││││├─┤├┬┘└┬┘ \n└─┘└─┘┴ ┴┴ ┴┴ ┴┴└─ ┴ "
    kwSign = "┬┌─┌─┐┬ ┬┬ ┬┌─┐┬─┐┌┬┐┌─┐ \n├┴┐├┤ └┬┘││││ │├┬┘ ││└─┐ \n┴ ┴└─┘ ┴ └┴┘└─┘┴└──┴┘└─┘ "
    print('____Opening File_____')
    print('____File Succesfully Opened____')

    if __name__ == "__main__":
        print(summarize(text, ratio=ratio))
        print(keywords(text, ratio=ratio))

    # output
    with open(save_dir, 'w+', encoding="utf-8") as output:
        output.write(f"{LINE}\nFILETYPE: User Input\n{LINE}\n")
        output.write(sumSign + '\n')
        output.write(summarize(text, ratio=ratio) + '\n')
        output.write(kwSign + '\n')
        output.write(keywords(text, ratio=ratio) + '\n')
