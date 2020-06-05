from setuptools import setup, find_packages

setup(name="bioapi",
      version="0.0.1",
      description='Light library to perform request to different bioinformatics APIs',
      author='Kenzo-Hugo Hillion',
      author_email='kehillio@pasteur.fr',
      install_requires=[
          'pydantic==1.5.1',
          'requests==2.23.0',
          'colored==1.4.2'
      ],
      packages=find_packages()
)
