# coding:utf-8

from setuptools import setup
import setuptools

setup(
        name='cf-scrapper',
        version='1.0',
        scripts=['cf-scrapper'],
        description="A tool to check user's info on Codeforces",
        author='jayinnn',
        author_email='jayin920805@gmail.com',
        url='https://github.com/jayin92/cf-scrapper',
        packages=setuptools.find_packages(),
        # package_data={"cf-scrapper": ['favicon.png']}
)