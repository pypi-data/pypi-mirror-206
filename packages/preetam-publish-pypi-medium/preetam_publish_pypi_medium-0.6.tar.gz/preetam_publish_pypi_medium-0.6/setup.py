from setuptools import setup, find_packages


setup(
    name='preetam_publish_pypi_medium',
    version='0.6',
    license='MIT',
    author="Giorgos Myrianthous",
    author_email='preetam@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)
