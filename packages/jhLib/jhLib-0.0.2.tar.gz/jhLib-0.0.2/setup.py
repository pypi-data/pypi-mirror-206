import setuptools as setuptools
from setuptools import setup
import setuptools

setup(
    name='jhLib',
    version='0.0.2',
    description='This program processes an OMR image of specific format. Then it identifies correct answers and scores the script',
    author='Md Nur Kutubul Alam',
    #url='https://github.com/alamjhilam/OMR_KUET.git',
    packages=setuptools.find_packages(),
    keywords=['OMR'],
    #classifiers=["Programming Language :: Python::3",
    #             "License :: OSI Approved :: MIT License",
    #             "Operating System :: OS Independent"],
   # python_requires='>=2.0',
   # py_modules=['OMRUtils'],
   # package_dir={'':'src'},
    install_requires=['opencv-python','numpy']
)