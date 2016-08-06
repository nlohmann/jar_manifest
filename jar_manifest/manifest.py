import zipfile


def manifest(jar_filename):
    """
    Returns the content of a jar file's MANIFEST file as dictionary.
    """
    jarfile = zipfile.ZipFile(jar_filename)
    manifest = jarfile.open('META-INF/MANIFEST.MF')

    key = None
    section = {}
    result = []

    for line in [x.rstrip('\n\r') for x in manifest.readlines()]:
        # empty line - end of current section
        if len(line) == 0:
            # store and reset current section
            result.append(section)
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
        result.append(section)

    return result
