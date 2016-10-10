from setuptools import setup, find_packages

version = '1.0'

LONG_DESCRIPTION = """
Thin wrapper for Solve360 API.
"""

setup(
    name='python-solve-threesixty',
    version=version,
    description="python-solve-threesixty",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django (optional)",
        "Environment :: Web Environment",
    ],
    keywords='solve360,django',
    author='Alvin Mites',
    author_email='alvin@mitesdesign.com',
    license='BSD',
    packages=find_packages(),
    package_data={
        'solve_threesixty': [
            '*'
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
