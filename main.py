from pprint import pprint 
from Scanner import Scanner
import tester

def main():
  testCases = tester.getTestCases()
  # pprint(testCases)

  # for i in range(len(testCases)):
  #     print('Batch {0}: {1}'.format(i+1, testCases[i]))
  #     s = Scanner(testCases[i])
  #     s.scan()
  #     print('Batch {0}: {1}'.format(i+1, s.scan()))
        
  s = Scanner(testCases[2])
  print(testCases[2])
  # print('tokens: {0}'.format(s.scan()))
  s.scan()

if __name__ == '__main__':
    main()
