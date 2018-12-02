from setuptools import setup, find_packages

long_description = '''
Recursively compare dicts.
Designed for Web API test.
'''


setup(
    name='chabie',
    version='0.3.3',
    description='Comparison utility',
    long_description=long_description,
    author='TatchNicolas',
    author_email='TatchNicolas@users.noreply.github.com',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/TatchNicolas/chabie'
)
