from setuptools import setup, find_packages

# Read the content of the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
  name = 'repvgg-pytorch',
  packages = find_packages(exclude=['examples']),
  version = '1.0.1',
  license='MIT',
  description = 'RepVGG - Pytorch',
  long_description=long_description,  # Add the long_description parameter
  long_description_content_type = 'text/markdown',
  author = 'Asad Ismail',
  author_email = 'asadismaeel@gmail.com',
  url = 'https://github.com/Asad-Ismail/repvgg-packaged',
  keywords = [
    'artificial intelligence',
    'attention mechanism',
    'image recognition'
  ],
  install_requires=[
    'einops>=0.6.0',
    'torch>=1.10',
    'torchvision'
  ],
  setup_requires=[
    'pytest-runner',
  ],
  tests_require=[
    'pytest',
    'torch==1.12.1',
    'torchvision==0.13.1'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
  ],
)
