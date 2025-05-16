import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The comman
    """


    prompt="(hbnb)"
    
    classes = {
        "BaseModel":BaseModel,
        "User":User,
        "Place":Place,
        "State":State,
        "Review":Review,
        "City":City,
        "Amenity":Amenity
        }
            

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

    def do_create(self, arg):

        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_obj = self.classes[arg]()
            new_obj.save()
            print(f"{new_obj.id}")
    def do_show(self, arg):
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"

            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
            else:
                print(obj)
                    
    def do_destroy(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
    def do_all(self, arg):
        results = []
        objects = storage.all()
        if arg:
            if arg not in self.classes:
                print("** class doesn't exist **")
                return
                
            
            for obj in objects.values():
                results.append(str(obj))
        else:
            for obj in objects.values():
                results.append(str(obj))
        print(results)

    def do_update(self,arg):
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
    
        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                atrr_name = args[2]
                atrr_value = args[3].strip('"')
                try:
                    if '.' in atrr_value:
                        atrr_value = float(trr_value)
                    else:
                        atrr_value = int(atrr_value)
                except ValueError:
                    pass
                setattr(obj, atrr_name, atrr_value)
                obj.save()




if __name__ == '__main__':
    HBNBCommand().cmdloop()



