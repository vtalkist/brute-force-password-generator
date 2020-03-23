"""
Bruteforce Password Generator
Use: python BrutePWGen.py --merge-words --h4x0r keywords.txt
"""

import sys
from time import time

class wgen:

    # Construct for class.
    def __init__(self):
        self.argument = { '--merge-words':False, '--h4x0r':False }
        self.argument_list = { '--merge-words':[], '--h4x0r':[] }
        self.leetdict = {
            'a':['4','@'],
            'e':['3'],
            'g':['6'],
            'i':['1','!'],
            'l':['1','!'],
            'o':['0'],
            's':['5','$'],
            't':['7']
        }


    # Read the keyword file from file system.
    #
    # @param string filename
    # @return list
    def read_file(self, filename):
        f = open(filename, 'r')
        lines = f.read().splitlines()
        f.close()

        return lines

    # Save the output to file system.
    #
    # @param string filename
    # @param list data
    # @return void
    def save_file(self, filename, data):
        f = open(filename, 'a')
        for passwd in data:
            f.write("%s\n" % passwd)
        f.close()

        return

    # Add a prefix to the word list.
    #
    # @param string word
    # @param list wordlist
    # @return list
    def add_prefix(self, prefix, wordlist):
        return [prefix+word for word in wordlist if prefix != word]


    # Merge the wordlist keywords.
    def merge_words(self, wordlist):
        mlist = []
        for word in wordlist:
            mlist.append(self.add_prefix(word, wordlist))

        return self.merge_lists(mlist)


    # Convert letters to numbers, for example admin to 4dm1n.
    # Taken from: http://ptscripts.googlecode.com/svn/trunk/leet.py
    #
    # @param list wordlist
    # @return list
    def h4x0r(self, wordlist):
        mlist = wordlist
        for word in wordlist:
            for i in range(len(word)):
                chars = list(word)
                if chars[i].lower() in self.leetdict.keys():
                    for x in self.leetdict[chars[i].lower()]:
                        chars[i] = x
                        neword = ''.join(chars)
                        if not neword in wordlist:
                            mlist.append(neword)
        
        return mlist

    # Swap case of all letters.
    # Taken from: http://ptscripts.googlecode.com/svn/trunk/leet.py
    #
    # @param list wordlist
    # @return list
    def case(self, wordlist):
        mlist = wordlist
        for word in wordlist:
            for i in range(len(word)):
                chars = list(word)
                chars[i] = chars[i].swapcase()
                neword = ''.join(chars)
                if not neword in wordlist:
                    mlist.append(neword)
        
        return mlist


    # Instructions to use the program.
    #
    # @return string
    def banner(self):
        return """
    Use the program follows: 
    python3 wgen.py [[--merge-words] [--h4x0r]] wordlist 
        """


    # Merge the lists of different arguments to a main list.
    #
    # @param mixed object 
    # @return string
    def merge_lists(self, object):
        main_list = []
        if type(object) is list:
            for sublist in object:
                for word in sublist:
                    main_list.append(word)
        
        return main_list


    # Generate the list for all methods selected on the arguments.
    def gen_argument_list(self):
        output = []
        # --h4x0r applied to --merge-words.
        argv = '--h4x0r'
        if self.argument[argv] is True:
            mlist = self.h4x0r(self.argument_list['--merge-words'])
            output.append(mlist)

        
        return output
            

    # The main function.
    def main(self):
        if len(sys.argv) < 3:
            print(self.banner())
            exit()

        output = []
        wordlist = self.read_file(sys.argv[-1])
        output.append(wordlist)
        for argv in sys.argv[1::]:
            if argv == '--merge-words':
                list_merge_words = self.merge_words(wordlist)
                output.append(list_merge_words)
                self.argument[argv] = True
                self.argument_list[argv] = list_merge_words

            if argv == '--h4x0r':
                list_h4x0r = self.h4x0r(wordlist)
                output.append(list_h4x0r)
                self.argument[argv] = True
                self.argument_list[argv] = list_h4x0r

        # Generate the list for all methods selected on the arguments.
        gen_argument_list = self.merge_lists(self.gen_argument_list())
        output.append(gen_argument_list)

        # Save output to file system.
        self.save_file('wgen.passwd.txt', self.merge_lists(output))

if __name__ == "__main__":
    start_time = time()
    wgen = wgen()
    wgen.main()
    print("--- %d seconds, %d minutes ---" % (int(time()-start_time), int(time()-start_time)/60))
