# -*- coding: utf-8 -*-
import sys
from distutils.core import setup
import py2exe
sys.argv.append("py2exe")
# Change the path in the following line for webdriver.xpi
data_files = [('selenium/webdriver', ['C:/Python27/Lib/site-packages/selenium/webdriver/firefox/webdriver.xpi'])]

setup(
    name='ikariam',
    version='0.1',
    description='ikariam (web_script_tools)',
    author='lxq',
    author_email='email',
    url='',
    console=[{'script': 'ikariam.py'}],   # the main py file
    data_files=data_files,
    options={
        'py2exe':
            {
                'skip_archive': True,
                'optimize': 2,
            }
    }
)