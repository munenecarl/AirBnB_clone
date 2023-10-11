#!/usr/bin/env python3

import cmd
import sys

from models.base_model import BaseModel

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
        if line == "":
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

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

        if line == "":
            objs = storage.all()
        else:
            try:
                cls = eval(line)
                objs = storage.all(cls)
            except:
                print("** class doesn't exist **")
                return

        print("[{}]".format(", ".join(str(obj) for obj in objs.values())))

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
