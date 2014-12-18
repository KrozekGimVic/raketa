import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyglet',
]

setup(
    name='game',
    version='0.1dev',
    description='Our game',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='game',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['game'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points='',
)
