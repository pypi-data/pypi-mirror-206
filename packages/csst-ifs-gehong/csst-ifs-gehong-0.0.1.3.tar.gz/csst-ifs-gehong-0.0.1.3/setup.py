from setuptools import setup, find_packages


setup(
    name='csst-ifs-gehong',
    version='0.0.1.3',
    license='MIT',
    author="Shuai Feng",
    author_email='sfeng@hebtu.edu.cn',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='CSST-IFS',
    install_requires=[
          'astropy',
      ],

)