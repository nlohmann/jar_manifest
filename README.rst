jar_manifest
------------

To get a jar file's manifest as dict, just::

    >>> import jar_manifest
    >>> jar_manifest.manifest('junit-4.12.jar')
    [{'Created-By': 'Apache Maven 3.0.4', 'Archiver-Version': 'Plexus Archiver', 'Manifest-Version': '1.0', 'Implementation-Title': 'JUnit', 'Implementation-Version': '4.12', 'Build-Jdk': '1.6.0_45', 'Implementation-Vendor': 'JUnit', 'Implementation-Vendor-Id': 'junit', 'Built-By': 'jenkins'}]
