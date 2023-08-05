from setuptools import setup, find_packages


setup(
    name='MediaLib',
    version='3.0.1.6',
    license='MIT',
    author="Jingyun Wang",
    author_email='jingyun.wang@durham.ac.uk',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='http://medialib.club',
    keywords='Multimedia',
    install_requires=[
          'pygame',
      ],

)
