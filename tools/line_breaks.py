import sys, getopt

def main(argv):
    txt_file = ''
    chars = 65
    out_file = 'out_lines.txt'
    try:
        opts, args = getopt.getopt(argv,"hc:o:",['chars=','output='])
    except getopt.GetoptError:
        print('USAGE: line_breaks.py -c <character_length> -o <output_file> <txt_file>')
        print(' Type line_breaks.py --help for more details.')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h','--help'):
            print('USAGE: line_breaks.py -c <character_length> -o <output_file> <txt_file>')
            print('\nTakes a .txt file as input and outputs a new .txt file with the new line lengths. See the possible options below.\n')
            print('OPTIONS:\n -c, --chars INT\n  Set the number of characters for line length. Default 65')
            print(' -o, --output <PATH>\n  Set the output file. Default out_lines.txt')
            sys.exit()
        elif opt in ('-c','--chars'):
            chars = int(arg)
        elif opt in ('-o','--output'):
            out_file = arg
    for arg in args:
        txt_file = arg
        
        inFile = open(txt_file)
        rawText = inFile.read()
        inFile.close()

        paragraphs = rawText.split('\n')
        newText = []

        for paragraph in paragraphs:
            newPara = ""
            tokens = paragraph.split(' ')
            for token in tokens:
                newPara = newPara + ' ' + token
                if len(newPara.split('\n')[-1]) > chars:
                    newPara = newPara + '\n'
            newPara = newPara.strip().replace('\n ','\n')

            newText.append(newPara)

        print("Separated into lines of",chars,"characters. Saving results to",out_file+".")

        outFile = open(out_file,'w')
        outFile.write("\n".join(newText))
        outFile.close()
    
if __name__ == "__main__":
   main(sys.argv[1:])
