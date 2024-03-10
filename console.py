#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
import sys

class HBNBCommand(cmd.Cmd):
    """
    This is the colsole class
    """
    prompt = "(hbnb) "


    def do_quit(self, line):
        """This is the quit method"""
        return True

    def do_EOF(self, line):
        """This is the end of file method"""
        print("")
        return True

    def emptyline(self):
        """Tis is the empty line method"""
        pass

    def do_create(self, class_name):
        """ Creates a new instance of BaseModel """
        if not class_name:
            print("** class name missing **")
            return
        try:
            cls = getattr(sys.modules["models.base_model"], class_name)
        except AttributeError:
            print("** class doesn't exist **")
            return
        instance = cls()
        filename = instance.save()
        print(instance.id)

    def do_show(class_name, class_id):
        """shows the class instance with id"""
        if not class_name:
            print("** class name missing **")
            return
        try:
            att = str(sys.modules["models.base_model"])
            cls = getattr(att, class_name)
        except AttributeError:
            print("** class doesn't exist **")
            return
        if not class_id:
            print("** instance id missing **")
            return
        instance = cls._BaseModel__object.get(class_id)
        if instance:
            print(instance)
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
