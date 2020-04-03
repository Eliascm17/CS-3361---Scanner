from typing import List

class Scanner:

    def __init__(self, a: List):
        #array of lines segmented into an array that is parsed
        self.a = a
        # variable to keep track of if you're in the middle of a comment or not
        self.commentOpen = False
        # array of tokens that will be returned when Scanner.scan() runs
        # that hold the list of tokens in a batch
        self.tokens = []

    def scan(self):
        #for each line that is in a batch
        for k in range(len(self.a)):
            # print('loop: {0}'.format(k+1))
            #one liner comment
            if '/*' in self.a[k] and '*/' in self.a[k]:
                continue

            #beginning of a multi-line comment
            #if /* is contained in the line then declare it as the beginning of a comment
            if '/*' in self.a[k]:
                self.commentOpen = True
            
            #end of a multi-line comment
            #if */ is contained in the line then declare it as the end of a comment
            elif '*/' in self.a[k]:
                self.commentOpen = False

            #no white spaces EX's: "five" or "3.14159"
            elif (' ' not in self.a[k]) and self.commentOpen == False:
                if self.a[k] == 'read':
                    self.tokens.append('read')
                elif self.a[k] == 'write':
                    self.tokens.append('write')
                else:
                     for i in range(len(self.a[k])):
                            if self.a[k][i] == '(':
                                self.tokens.append('lparen')
                                print('here')
                            elif self.a[k][i] == ')':
                                self.tokens.append('rparen')
                            elif self.a[k][i] == '+':
                                self.tokens.append('plus')
                            elif self.a[k][i] == '-':
                                self.tokens.append('minue')
                            elif self.a[k][i] == '/':
                                self.tokens.append('div')
                            elif self.a[k][i] == '*':
                                self.tokens.append('mult')
                            elif self.a[k][i] == ':' and self.a[k][i+1] == '=':
                                self.tokens.append('assignment')
                            elif self.a[k][i].isnumeric():
                                #throw error for '1.2.3'
                                if self.a[k].count('.') > 1:
                                    raise ValueError('error')
                                # '123', '-10', '2.34', etc
                                elif self.a[k].isnumeric():
                                    self.tokens.append('number')
                                    break
                                #do something here if element is a number ex 3.13)
                                else:
                                    #indexing from '3.13)' 
                                    for j in range(i, len(self.a[k])):
                                        #going through to determine where the end
                                        # of 3.13 is in the index
                                        if self.a[k][j] == '.' or self.a[k][j].isnumeric():
                                            #validate that dec point isn't last element i.e. '56.'
                                            if self.a[k][j+1] == '.' or self.a[k][j+1].isnumeric():
                                                #go to next loop
                                                continue
                                        #seeing that ')' is not numeric thus
                                        #update i to a new index and going to the next loop
                                        else:
                                            self.tokens.append('number')
                                            i = j
                            # to identify if token is a valid id
                            elif self.a[k][i].isalpha():
                                #do something here if element is a letter (A-Z,a-z,1-9)
                                if self.a[k].isalnum():
                                    self.tokens.append('id')
                                    break
                                else: 
                                    raise ValueError('error')
                            else:
                                raise ValueError('error sdfsdf')

                # print('tokens for {0}: {1}'.format(self.a[k], self.tokens))  
        # print('tokens: {0}'.format(self.tokens))                 
            #check to see if there are multiple possible tokens such as "five 5"
            #if the line has multiple possible tokens and is not a comment
            elif (' ' in self.a[k]) and (self.commentOpen == False):
                tokens = self.a[k].split()
                for token in tokens:
                    if token == 'read':
                        self.tokens.append('read')
                    elif token == 'write':
                        self.tokens.append('write')
                    #identify what the a specific index in the token is
                    else:
                        for i in range(len(token)):
                            if token[i] == '(':
                                self.tokens.append('lparen')
                            elif token[i] == ')':
                                self.tokens.append('rparen')
                            elif token[i] == '+':
                                self.tokens.append('plus')
                            elif token[i] == '-':
                                self.tokens.append('minue')
                            elif token[i] == '/':
                                self.tokens.append('div')
                            elif token[i] == '*':
                                self.tokens.append('mult')
                            elif token[i] == ':' and token[i+1] == '=':
                                self.tokens.append('assignment')
                            elif token[i].isnumeric():
                                #throw error for '1.2.3'
                                if token.count('.') > 1:
                                    raise ValueError('error')
                                # '123', '-10', '2.34', etc
                                elif token.isnumeric():
                                    self.tokens.append('number')
                                    break
                                #do something here if element is a number ex 3.13)
                                else:
                                    #indexing from '.13)' NOT '3.13)'
                                    for j in range(i+1, len(token)):
                                        #going through to determine where the end
                                        # of 3.13 is in the index
                                        if token[j] == '.' or token[j].isnumeric():
                                            #validate that dec point isn't last element i.e. '56.'
                                            if token[j] == '.' and token[j+1].isnumeric():
                                                continue
                                            else:
                                                raise ValueError('error')
                                        #seeing that ')' is not numeric thus
                                        #update i to a new index and going to the next loop
                                        else:
                                            self.tokens.append('number')
                                            i = j
                            # to identify if token is a valid id
                            elif token[i].isalpha():
                                #do something here if element is a letter (A-Z,a-z,1-9)
                                if token.isalnum():
                                    self.tokens.append('id')
                                    break
                                else: 
                                    raise ValueError('error')
        print(self.tokens)
                    