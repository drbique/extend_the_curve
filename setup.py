import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='extend_the_curve',  

     version='1.0',

     scripts=['extend_the_curve'] ,

     author="Stephen Bique",

     author_email="stephenbique@us.af.mil",

     description="A module that provides a function to extend a curve locally",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/drbique/extend_the_curve",

     packages=['extend_the_curve'],
     
     install_requires=['numpy','sklearn','scipy','re'],
     
     classifiers=[

         "Programming Language :: Python :: 3",

         "AFLCMC/HNII License",

         "Operating System :: OS Independent",

     ],

 )