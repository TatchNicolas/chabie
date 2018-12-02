import os
import sys

from setuptools import setup, find_packages
from setuptools.command.install import install


VERSION = '0.3.6'


def readme():
    """print long description"""
    with open('README.md') as f:
        return f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'
    error_message = "Git tag: {0} does not match the version of this app: {1}"

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = self.error_message.format(
                tag, VERSION
            )
            sys.exit(info)


setup(
    name='chabie',
    version=VERSION,
    description='Comparison utility',
    long_description=readme(),
    author='TatchNicolas',
    author_email='TatchNicolas@users.noreply.github.com',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/TatchNicolas/chabie',
    cmdclass={
        'verify': VerifyVersionCommand,
    },
)
