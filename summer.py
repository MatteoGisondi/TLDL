from gensim.summarization import summarize, keywords
sumSign = "┌─┐┬ ┬┌┬┐┌┬┐┌─┐┬─┐┬ ┬ \n└─┐│ │││││││├─┤├┬┘└┬┘ \n└─┘└─┘┴ ┴┴ ┴┴ ┴┴└─ ┴ "
kwSign = "┬┌─┌─┐┬ ┬┬ ┬┌─┐┬─┐┌┬┐┌─┐ \n├┴┐├┤ └┬┘││││ │├┬┘ ││└─┐ \n┴ ┴└─┘ ┴ └┴┘└─┘┴└──┴┘└─┘ "
filename = input('Enter file name + .extension: ')
print('____Opening File_____')
text = open(filename).read()
print('____File Succesfully Opened____')
ratio = int(input('Please enter the keyword/summary to text ratio (number between 1 and 99): ')) / 100

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
