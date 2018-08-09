from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='handyspark',
      version='0.0.1dev1',
      install_requires=['matplotlib', 'numpy', 'seaborn', 'pandas', 'scikit-learn'],
      description='"Handy Spark',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/dvgodoy/handyspark',
      author='Daniel Voigt Godoy',
      author_email='datagnosis@gmail.com',
      keywords=['spark', 'big data', 'data cleaning', 'plot', 'chart'],
      license='MIT',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Scientific/Engineering :: Visualization',
          'Topic :: System :: Distributed Computing',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
      packages=find_packages(),
      zip_safe=False)
