from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='jar_manifest',
      version='0.2',
      description='Returns the content of a jar file\'s MANIFEST as dict.',
      long_description=readme(),
      classifiers=[
      	'Development Status :: 4 - Beta',
      	'License :: OSI Approved :: MIT License',
      	'Programming Language :: Python :: 2.7',
      	'Topic :: Software Development :: Libraries :: Java Libraries'
      ],
      keywords='jar file java manifest',
      url='http://github.com/nlohmann/jar_manifest',
      author='Niels Lohmann',
      author_email='mail@nlohmann.me',
      license='MIT',
      scripts=['jar_manifest/bin/read_manifest'],
      packages=['jar_manifest'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
