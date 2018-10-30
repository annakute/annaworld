import math
import subprocess as sp
import webbrowser

def main():
    #comment 1
    webbrowser.get('windows-default').open('google.com')

    #math fun
    print("5^2 = " + str(5^2))
    print("5^2 is really: " + str(math.pow(5,2)))

    import subprocess as sp
    proc = sp.check_output("ipconfig").decode('utf-8')
    print(proc)
main()