from setuptools import setup, find_packages

setup(
    name='googlegallary',
    version='0.3.0',
    author='Rahul chauhan',
    packages=['googlegallary'],
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
    python_requires='>=3.6'
)

# twine register --repository-url https://github.com/Rjchauhan18/google-gallary.git --username Rjchauhan18 --password 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
