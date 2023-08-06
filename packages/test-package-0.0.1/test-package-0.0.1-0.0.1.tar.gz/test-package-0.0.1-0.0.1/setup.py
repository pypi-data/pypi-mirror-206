from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'My Sample Python package'
LONG_DESCRIPTION = 'My Sample Python package for Display'

# Setting up
setup(
       # the name must match the folder name 'testpackage0.0.1'
        name="test-package-0.0.1", 
        version=VERSION,
        author="sachin",
        author_email="reachsachinquick@gmail.com",
        description="Setting up a sample python package",
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'sample package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)