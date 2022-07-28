#!/usr/bin/python3
""" creates function inherits_from """


def inherits_from(obj, a_class):
    """ returns True if the object in an instance of a class
    that inherited (directly or indirectly) from a specified class """
    return issubclass(type(obj), a_class) and type(obj) != a_class
