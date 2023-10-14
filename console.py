#!/usr/bin/env python3

import cmd
import sys

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place

my_classes = {
    "BaseModel",
    "User",
    "State",
    "City",
    "Amenity",
    "Place",
    "Review",
}

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that contains the entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def help(self):
        """help command that displays the help"""
        print("help")

    def emptyline(self):
        """emptyline method that does nothing"""
        pass

    def default(self, line):
        """default method that does nothing"""
        pass

    def do_create(self, line):
        """create command that creates a new instance of BaseModel"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif line not in my_classes:
            print("** class doesn't exist **")
        else:
            from models import storage
            cls = eval(args[0])
            new_instance = cls()
            new_instance.save()
            print(new_instance.id)
            storage.save()

    def do_show(self, line):
        """show command that prints the string representation of an instance"""
        from models import storage

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objs = storage.all(cls)
        key = "{}.{}".format(args[0], args[1])
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """destroy command that deletes an instance based on the class name and id"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                from models import storage
                # Test whether arg[0] is in my_classes dictionary
                if args[0] not in my_classes:
                    print("** class doesn't exist **")
                    return
                elif len(args) == 1:
                    print("** instance id missing **")
                    return
                else:
                    key = args[0] + "." + args[1]

                    if key not in storage.all():
                        print("** no instance found **")
                        return
                    else:
                        del storage.all()[key]
                        storage.save()
            except KeyError:
                print("** class doesn't exist **")


    def do_all(self, line):
        """all command that prints all string representation of all instances"""
        from models import storage

        if line:
            try:
                cls = eval(line)
            except:
                print("** class doesn't exist **")
                return
            objs = storage.all(cls)
        else:
            objs = storage.all()
        if len(objs) == 0:
            print("[]")
        for obj in objs.values():
            print(obj)

    def do_update(self, line):
        """update command that updates an instance based on the class name and id"""
        from models import storage

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objs = storage.all(cls)
        key = "{}.{}".format(args[0], args[1])
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(objs[key], args[2], args[3])
        objs[key].save()

    def do_count(self, line):
        """count command that retrieves the number of instances of a class"""
        from models import storage

        args = line.split('.')
        if len(args) == 1:
            class_name = args[0]
            if class_name not in my_classes:
                print("** class doesn't exist **")
                return
            else:
                count = 0
                objects = storage.all()
                for obj in objects.values():
                    if class_name == obj.__class__.__name__:
                        count += 1
                print(count)
        elif len(args) == 2:
            class_name = args[0]
            method_name = args[1]
            if class_name not in my_classes:
                print("** class doesn't exist **")
                return
            try:
                cls = eval(class_name)
            except:
                print("** class doesn't exist **")
                return
            try:
                method = getattr(cls, method_name)
            except AttributeError:
                print("** method doesn't exist **")
                return
            print(method())
        else:
            print("** invalid syntax **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
