from setuptools import setup, find_packages

setup(
    name='googlegallary',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
    python_requires='>=3.6',
)
