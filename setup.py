from setuptools import setup, find_packages
 
setup(name='movarm',
      version='0.1',
      url='https://github.com/shazaum/movarm',
      license='MIT',
      author='Renato dos Santos',
      author_email='shazaum@gmail.com',
      description='Para movimentar um braço robotico',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)