#!/usr/bin/python3
"""
This module contains the HBNBCommand interpreter
"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """

    prompt = '(hbnb) '

    valid_classes = [
        'BaseModel',
        'User',
        'State',
        'City',
        'Amenity',
        'Place',
        'Review'
    ]

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves to JSON file and prints.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(args[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on class name and id
        Usage: show <class name> <id>
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        obj_dict = storage.all()
        obj = obj_dict.get(key, None)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        Usage: destroy <class name> <id>
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        obj_dict = storage.all()
        obj = obj_dict.get(key, None)
        if obj:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        Usage: all [<class name>]
        """
        args = arg.split()
        obj_list = []

        if not args:
            for obj in HBNBCommand.storage.all().values():
                obj_list.append(str(obj))
        elif args[0] in self.valid_classes:
            for obj in HBNBCommand.storage.all().values():
                if type(obj).__name__ == args[0]:
                    obj_list.append(str(obj))
        else:
            print("** class doesn't exist **")
            return

        print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attributes.
        Usage: update <class name> <id> <attribute name> "attribute value"
        """
        args = arg.split()

        if not args:
            print("** class name missing**")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        obj_dict = HBNBCommand.storage.all()
        obj = obj_dict.get(key, None)

        if not obj:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3].strip('"')

        if hasattr(obj, attribute_name):
            attribute_type = type(getattr(obj), attribute_name)
            setattr(obj, attribute_name, attribute_type(attribute_value))
            storage.save()
        else:
            print("** attribute doesn't exist **")

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
