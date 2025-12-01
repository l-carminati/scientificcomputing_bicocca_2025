from setuptools import setup, find_packages

setup(name='pip_test_ids_bicocca2025',
      description='simple test for pip',
      author='Carminati Leonardo',
      author_email='davide.gerosa@unimib.it',
      license='MIT',
      version='0.0.3',
      packages=find_packages(),
      install_requires=['numpy', 'tqdm', 'pathos'])

