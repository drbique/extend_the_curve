import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='extend_the_curve',  

     version='0.1',

     author="Dr. Stephen Bique",

     author_email="stephenbique@us.af.mil",

     description="A module that provides a function to extend a curve locally",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/drbique/extend_the_curve",

     packages=setuptools.find_packages(),
         
     install_requires=['numpy','sklearn','scipy'],
     
     classifiers=[

         "Programming Language :: Python :: 3",

         "AFLCMC/HNII License",

         "Operating System :: OS Independent",

     ],

 )