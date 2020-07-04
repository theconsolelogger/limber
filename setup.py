from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='limber',
    version='0.1.0',
    description='A python web application framework built using FastAPI.',
    long_description=readme,
    keywords="python FastAPI",
    author='Jonathan Staniforth',
    author_email='jonathanstaniforth@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests')),
    url='https://github.com/limber-project/limber',
    project_urls={
        "Bug Tracker": "https://github.com/limber-project/limber/issues",
        "Documentation": "https://github.com/limber-project/limber/wiki",
        "Source Code": "https://github.com/limber-project/limber",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Development Status :: 1 - Planning"
    ]
)