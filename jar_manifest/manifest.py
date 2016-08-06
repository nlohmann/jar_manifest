from zipfile import ZipFile
from os.path import splitext
from cStringIO import StringIO


def manifest_internal(jarfile, jar_filename, data, recursive):
    manifest = jarfile.open('META-INF/MANIFEST.MF')

    key = None
    section = {}
    data[jar_filename] = []

    for line in [x.rstrip('\n\r') for x in manifest.readlines()]:
        # empty line - end of current section
        if len(line) == 0:
            # store and reset current section
            data[jar_filename].append(section)
            section = {}

        # line begins with a space: continuation of value
        elif line[0] == ' ':
            section[key] += line[1:]

        # new key/value pair
        else:
            # key and value are separated by ': ' (colon space)
            [key, value] = line.split(': ', 1)
            section[key] = value

    # if manifest does not end with empty line, store last section
    if len(section.keys()) != 0:
        data[jar_filename].append(section)

    # recurse into embedded jar files
    if recursive:
        embedded_jarfiles = [x for x in jarfile.namelist() if splitext(x)[1] == '.jar']
        for j in embedded_jarfiles:
            zfiledata = StringIO(jarfile.read(j))
            manifest_internal(ZipFile(zfiledata), jar_filename + '/' + j, data, recursive)


def manifest(jar_filename, recursive=True):
    """
    Returns the content of a jar file's MANIFEST file as dictionary.
    """
    data = dict()
    manifest_internal(ZipFile(jar_filename), jar_filename, data, recursive)
    return data
