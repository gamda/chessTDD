from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='chess',
      version='1.0',
      description='implementation of the game Chess',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Game :: Chess',
      ],
      url='http://github.com/gamda/chessTDD',
      author='Gamda Software',
      author_email='gamdansoftware@gmail.com',
      license='MIT',
      packages=['checkers'],
      install_requires=[
          'gameboard',
          'pygame'
      ],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],)