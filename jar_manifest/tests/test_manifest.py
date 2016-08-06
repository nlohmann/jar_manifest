from unittest import TestCase
import urllib2
import os
import jar_manifest

class TestManifest(TestCase):
	def test_manifest(self):
		junit_url = 'http://search.maven.org/remotecontent?filepath=junit/junit/4.12/junit-4.12.jar'
		junit_jarfile = open('junit.jar', 'wb')
		junit_jarfile.write(urllib2.urlopen(junit_url).read())
		junit_jarfile.close()

		junit_manifest = jar_manifest.manifest('junit.jar')
		self.assertEqual(junit_manifest[0]['Created-By'], 'Apache Maven 3.0.4')
		self.assertEqual(junit_manifest[0]['Implementation-Title'], 'JUnit')
		os.remove('junit.jar')
