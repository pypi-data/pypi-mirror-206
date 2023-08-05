from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable', 
    'Intended Audience :: Education',
    'Operating System :: MacOS',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='goodbyeworld',
    version='0.0.1',
    description='I want to die',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Ur mom',
    author_email='fakeemail@gmail.com',
    License='MIT',
    classifiers=classifiers,
    keywords='',
    packages=find_packages(),
    install_requires=['']
)