from pkg_resources import resource_string

def read_lines(fname):
    """
    Reads the specified file name split up in lines
    :param fname: name of the file
    :return: array of line values
    """
    return read(fname).splitlines()

def read(fname):
    """
    Reads the specified file name
    :param fname: name of the file
    :return: content of file
    """
    return resource_string('resources', fname)