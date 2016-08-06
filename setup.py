from setuptools import setup

setup(name='jar_manifest',
      version='0.1',
      description='Returns the content of a jar file\'s MANIFEST as dict.',
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
      packages=['jar_manifest'],
      include_package_data=True,
      zip_safe=False)
