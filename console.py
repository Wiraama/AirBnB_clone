#!/usr/bin/python3
"""
module to interpreate for an application
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ class """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit thr program"""
        print()
        return True

    def emptyline(self):
        """Do nothing empty input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
