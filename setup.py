import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='extend_the_curve',  

     version='1.0',

     scripts=['extend_the_curve'] ,

     author="Stephen Bique",

     author_email="stephenbique@us.af.mil",

     description="A module to extend a curve locally",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/drbique/extend_the_curve",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: AFLCMC/HNII License",

         "Operating System :: OS Independent",

     ],

 )