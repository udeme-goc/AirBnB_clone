#!/usr/bin/python3
"""HBNBCommand module"""
import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    file_path = "file.json"
    storage = FileStorage()
    storage.reload()

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            key = "{}.{}".format(args[0], args[1])
            print(HBNBCommand.storage.all()[key])
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            key = "{}.{}".format(args[0], args[1])
            del HBNBCommand.storage.all()[key]
            HBNBCommand.storage.save()
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        obj_list = []
        try:
            if len(args) == 0:
                for obj in HBNBCommand.storage.all().values():
                    obj_list.append(str(obj))
            else:
                for obj in HBNBCommand.storage.all().values():
                    if type(obj).__name__ == args[0]:
                        obj_list.append(str(obj))
            print(obj_list)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        try:
            key = "{}.{}".format(args[0], args[1])
            obj = HBNBCommand.storage.all()[key]
            setattr(obj, args[2], args[3])
            HBNBCommand.storage.save()
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        raise SystemExit

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        raise SystemExit

    def do_exit(self, arg):
        """Exit command to exit the program"""
        raise SystemExit

    def do_help(self, arg):
        """Help command to display all available commands"""
        cmd.Cmd.do_help(self, arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

