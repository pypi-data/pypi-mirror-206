from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
  name = 'wavemix',
  packages = find_packages(exclude=['examples']),
  version = '0.2.4',
  license='MIT',
  description = 'WaveMix - Pytorch',
  long_description=long_description,
  long_description_content_type = 'text/markdown',
  author = 'Pranav Jeevan',
  author_email = 'pranav13phoenix@gmail.com',
  url = 'https://github.com/pranavphoenix/WaveMix',
  keywords = [
    'artificial intelligence',
    'token-mixing',
    'image classification',
    'semantic segmentation',
    'image super-resolution'
  ],
  install_requires=[
    'einops',
    'torch',
    'torchvision',
    'pywavelets',
    'numpy'
  ],
  
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)