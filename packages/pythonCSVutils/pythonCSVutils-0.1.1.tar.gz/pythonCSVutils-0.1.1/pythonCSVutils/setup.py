from setuptools import setup
with open('README.md', 'r') as f:
    long_description = f.read()
setup(
    name='pythonCSVutils',
    version='0.1.1',
    description='A Python module for processing CSV files efficiently',
    packages=['pythonCSVutils'],
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
