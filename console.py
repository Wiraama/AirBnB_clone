#!/usr/bin/python3
"""
module to interpreate for an application
"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return true

    def do_EoF(self, arg):
        """ end of fucking file """
        print()
        return True

    def emptyline(self):
        """ Do nothing just pass """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
