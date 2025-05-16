import cmd

class HBNBCommand(cmd.Cmd):
            """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
        commands:
            `quit` and `EOF`
            together with `help so that `help quit`
            emptylines 
    """

    prompt="(hbnb)"
    def emptyline(self):
        """overriding defaul`emptyline` method 
        so that an empty line + ENTER shouldn’t execute anything"""
        pass
    def do_quit(self, arg):
        """quit: to exit the program when user writes `quit` command"""
        return True
    def do_EOF(self, arg):
        """EOF to exit the program when user writes `EOF` command"""
        return True
    def help_quit(self):
        print("Usage:it exit the program when user writes `quit` command")
        print(" write `quit` to exit the commandline ")
    def help_EOF(self):
        print("Usage:it exit the program when user writes `EOF` command")
        print(" write `EOF` to exit the commandline ")

if __name__ == '__main__':
    HBNBCommand().cmdloop()



