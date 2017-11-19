from setuptools import setup, find_packages

with open('dragon/__init__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")

setup(
    name='dragon',
    version=version,
    description='A place where dragons are born',
    url='',
    author='Elvarg21',
    author_email='',
    packages=find_packages(),
    install_requires=[
    ],
    dependency_links=[
    ],
    zip_safe=False
)
