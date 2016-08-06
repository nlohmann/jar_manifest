jar_manifest
------------

To get a jar file's manifest as dict, just::

    >>> import jar_manifest
    >>> jar_manifest.manifest('junit-4.12.jar')
    {
	  "junit-4.12.jar": [
	    {
	      "Archiver-Version": "Plexus Archiver", 
	      "Build-Jdk": "1.6.0_45", 
	      "Built-By": "jenkins", 
	      "Created-By": "Apache Maven 3.0.4", 
	      "Implementation-Title": "JUnit", 
	      "Implementation-Vendor": "JUnit", 
	      "Implementation-Vendor-Id": "junit", 
	      "Implementation-Version": "4.12", 
	      "Manifest-Version": "1.0"
	    }
	  ]
	}