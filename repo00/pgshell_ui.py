import cmd, sys, winsound
from test_funcs import add_2_func, open_csv

class PShell(cmd.Cmd):
    intro = 'Welcome to the pshell.   Type help or ? to list commands.\n'
    prompt = '(PShell) > '
    file = None

    # ----- basic commands -----

    def do_close(self, arg):
        'Stop , close the pshell window, and exit:  BYE'
        print('Thank you for using PShell')
        self.close()
        return True
    def do_mymeth(self, arg):
        'My method I added 2019/feb: MYMETH'
        print("YES I DID IT!")
    def do_add(self, arg):
        'add 1 + 3'
        print(add_2_func())
    def do_open_csv(self, arg):
        'open testdata.csv'
        open_csv()

    # ----- record and playback -----

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    PShell().cmdloop()
