import sys
import pyfiglet

if __name__ == '__main__':
  f = pyfiglet.Figlet(font='ANSI Shadow')
  lines = f.renderText(sys.argv[1]).replace(' ', '-').split('\n')
  for l in lines[:-1]:
    print('// ' + l)

