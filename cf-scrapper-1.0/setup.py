# coding:utf-8

from setuptools import setup
import setuptools
# or
# from distutils.core import setup  

setup(
        name='cf-scrapper',     # 包名字
        version='1.0',   # 包版本
        scripts=['cf-scrapper.py'],
        description="A tool to check user's info on Codeforces",   # 简单描述
        author='jayinnn',  # 作者
        author_email='jayin920805@gmail.com',  # 作者邮箱
        url='https://github.com/jayin92/cf-scrapper',      # 包的主页
        packages=setuptools.find_packages()               # 包
)