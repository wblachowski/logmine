import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='logmine',
     version='0.3.0',
     scripts=['logmine'],
     author="Tony Dinh",
     author_email="trungdq88@gmail.com",
     description="Log pattern analyzer",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/trungdq88/logmine",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
