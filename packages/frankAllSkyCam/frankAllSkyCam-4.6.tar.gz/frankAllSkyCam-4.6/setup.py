import os
import shutil
from distutils.core import setup

setup(
  name = 'frankAllSkyCam',         # How you named your package folder (MyLib)
  packages = ['frankAllSkyCam'],   # Chose the same as "name"
  version = '4.6',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'AllSkyCamera with Raspberry Pi and Pi HQ Camera ',   # Give a short description about your library
  author = 'Francesco Sferlazza',                   # Type in your name
  author_email = 'sferlazza@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/sferlix/frankAllSkyCam',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/sferlix/frankAllSkyCam/archive/refs/tags/4.6.tar.gz',    # I explain this later on
  keywords = ['AllSkyCamera', 'Astronomy', 'AllSky'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pytz',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.9',
  ],
)

homepath = os.path.expanduser("~")
print("your homedir is: " + homepath + "\n")
if os.path.exists(homepath+"/frankAllSkyCam") == False:
    os.mkdir(homepath+"/frankAllSkyCam")

if os.path.exists(homepath+"/frankAllSkyCam/img") == False:
    os.mkdir(homepath+"/frankAllSkyCam/img")

if os.path.exists(homepath+"/frankAllSkyCam/log") == False:
    os.mkdir(homepath+"/frankAllSkyCam/log")

if os.path.exists(homepath+"/frankAllSkyCam/sqm") == False:
    os.mkdir(homepath+"/frankAllSkyCam/sqm")

sorg1 = 'frankAllSkyCam/helper/config.txt'
dest1 = homepath +'/frankAllSkyCam/config.txt'
shutil.copy(sorg1, dest1)

sorg2 = 'frankAllSkyCam/helper/index.html'
dest2 = homepath +'/frankAllSkyCam/index.html'
shutil.copy(sorg2, dest2)

