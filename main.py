from pprint import pprint 
from Scanner import Scanner
import tester

def main():
  testCases = tester.getTestCases()
  pprint(testCases)
  print('\n')

  for i in range(len(testCases)):
      print('Batch {0}: {1}'.format(i+1, testCases[i]))
      s = Scanner(testCases[i])
      s.scan()
      print('\n')

if __name__ == '__main__':
    main()
