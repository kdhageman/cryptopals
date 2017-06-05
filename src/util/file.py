from pkg_resources import resource_string

def read(fname):
    """
    Reads the specified file name split up in lines
    :param fname: name of the file
    :return: array of line values
    """
    f = resource_string('resources', fname)
    return f.splitlines()

def readfull(fname):
    """
    Reads the specified file name
    :param fname: name of the file
    :return: content of file
    """
    return resource_string('resources', fname)