from pprint import pprint 
from Scanner import Scanner
import tester

def main():
  testCases = tester.getTestCases()
  pprint(testCases)

#   for batch in testCases:
#       s = Scanner(x)
#       s.scan()
  s = Scanner(testCases[0])
  s.scan()
        
if __name__ == '__main__':
    main()
