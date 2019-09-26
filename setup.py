from setuptools import setup, find_packages

setup(name='lefs',
      description='Program translates words from subtitles or whole .srt file.',
      author='Miłosz Hoć',
      author_email='miloszhoc@gmail.com',
      version=str(0.1),
      packages=find_packages(exclude=['tests', 'venv']),

      py_modules=['lefs'],
      install_requires=['requests'],
      entry_points={'console_scripts': ['lefs = lefs:main', ]},
      )
