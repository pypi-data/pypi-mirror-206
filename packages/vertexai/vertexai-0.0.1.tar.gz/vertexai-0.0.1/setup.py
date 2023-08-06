
import logging
import setuptools
import sys

from setuptools.command.install import install


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        sys.stderr.write("WARNING: To use the Vertex AI SDK, install the google-cloud-aiplatform package.")

setuptools.setup(
    cmdclass={
        'install': PostInstallCommand,
    },
)
