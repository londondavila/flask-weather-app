import os
import re
import inspect


def get_parser_list(dirname):

    # return list of files in parsers
    files = [file.replace('.py', '')
             for file in os.listdir(dirname)
             if not file.startswith('__')]

    return files

def import_parsers(parserfiles):

    module = re.compile('.+parser$', re.I)

    # import module
    modules = __import__('flask-weather-app.parsers',
                           globals(),
                           locals(),
                           parserfiles,
                           0)

    # return tuples list with two items
    parsers = [(key, value) for key, value in inspect.getmembers(modules)
                if inspect.ismodule(value) and module.match(key)]

    classes = dict()

    # loop and extract parser classes, return dict
    for key, value in parsers:
        classes.update({key: value for key, value in inspect.getmembers(value)
                         if inspect.isclass(value) and module.match(key)})

    return classes

def load(dirname):
    
    parserfiles = get_parser_list(dirname)
    return import_parsers(parserfiles)