from typing import List

class Scanner:

    def __init__(self, a: List):
        self.a = a
        self.assign = ':='
        self.plus = '+'
        self.minus = '-'
        self.times = '*'
        self.div = '/'
        self.lparen = '('
        self.rparen = ')'
        self.openCom = '/*'
        self.closeCom = '*/'
        # variable to keep track of if you're in the middle of a comment
        self.commentOpen = False
        self.tokens = []

    def scan(self):
        for line in self.a:
            # length = len(line)
            for i in line:
                if i == self.assign and self.commentOpen == False:
                    self.tokens.append('assign')
                elif i == self.plus and self.commentOpen == False:
                    self.tokens.append('plus')
                elif i == self.minus and self.commentOpen == False:
                    self.tokens.append('minus')
                elif i == self.times and self.commentOpen == False:
                    self.tokens.append('times')
                elif i == self.div and self.commentOpen == False:
                    self.tokens.append('divs')
                elif i == self.lparen and self.commentOpen == False:
                    self.tokens.append('lparen')
                elif i == self.rparen and self.commentOpen == False:
                    self.tokens.append('rparen')
                # elif i == self.openCom:
                #     self.commentOpen = True
                # elif i == self.closeCom:
                #     self.closeCom = False

                
