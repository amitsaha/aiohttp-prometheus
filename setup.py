from setuptools import setup
import os


install_requires = ['aiohttp>=1.0.2']
extras_require = {
    'prometheus_client': ['prometheus_client>=0.0.19'],
}


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()

version = 0.1
setup(name='aiohttp_prometheus',
      version=version,
      description=("prometheus middleware for aiohttp.web"),
      long_description='\n\n'.join((read('README.rst'), read('CHANGES.rst'))),
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Internet :: WWW/HTTP'],
      author='Amit Saha',
      author_email='amitsaha.in@gmail.com',
      url='https://github.com/amitsaha/aiohttp-prometheus/',
      license='Apache 2',
      packages=['aiohttp_prometheus'],
      install_requires=install_requires,
      include_package_data=True,
      extras_require=extras_require)
