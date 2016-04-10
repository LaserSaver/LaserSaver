from setuptools import setup, find_packages

setup(  name = "Lasersaver",
        version = "0.1",
        description = "A high level python framework for implementing the Lasersaver project to reuse scrap material",
        author = "LaserCutter Group",
        author_email = "acordero1532@gmail.com",
        license = "BSD",
        packages = find_packages(),
        install_requires = ['numpy', 'decimal', 'json', 'logging', 'configparser', 'imutils', 'Pillow']
)
