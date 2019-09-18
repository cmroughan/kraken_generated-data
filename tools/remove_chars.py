import sys, getopt

def main(argv):
    txt_file = ''
    out_file = 'out.txt'
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["input=","output="])
    except getopt.GetoptError:
        print('USAGE: remove_chars.py -i <txt_file> -o <output_file> <characters to remove>')
        print(' Type remove_chars.py --help for more details.')
        sys.exit(2)
    if len(args) == 0:
        print('ERROR: no arguments detected for characters to remove.')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h','--help'):
            print('USAGE: remove_chars.py -i <txt_file> -o <output_file> <characters to remove>')
            print('\nTakes a .txt file as input and outputs a new .txt file with desired characters removed. Each character to remove must be separated by a space. You may use Unicode escape codes for characters if desired.\n')
            print('OPTIONS:\n -i, --input <PATH>\n  Select the input .txt file.')
            print(' -o, --output <PATH>\n  Set the output file. Default out.txt')
            sys.exit()
        elif opt in ('-i','--input'):
            txt_file = arg
        elif opt in ('-o','--output'):
            out_file = arg
        
    inFile = open(txt_file)
    rawText = inFile.read()
    inFile.close()
    
    for arg in args:
        if len(arg) == 1:
            print("Removing",arg,"from",txt_file + "...")
            rawText = rawText.replace(arg,'')
        elif len(('\\'+arg).encode('utf-8').decode('unicode-escape')) == 1:
            arg2 = ('\\'+arg).encode('utf-8').decode('unicode-escape')
            print("Removing",arg2,"(\\" + arg + ") from",txt_file + "...")
            rawText = rawText.replace(arg2,'')
        else:
            print('ERROR: argument',arg,'is not a valid character.')
            sys.exit(2)
            
    print("Done. Saving results to",out_file+".")
    
    outFile = open(out_file,'w')
    outFile.write(rawText)
    outFile.close()

    
if __name__ == "__main__":
   main(sys.argv[1:])
