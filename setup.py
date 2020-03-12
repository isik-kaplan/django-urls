from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='django_urls',
    version='1.1.0',
    packages=['django_urls'],
    url='https://github.com/isik-kaplan/django_urls',
    description="URL decorator for django views",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='AGPL-3.0-only',
    author='isik-kaplan',
    author_email='',
    python_requires=">=3.5",
    install_requires=['django>=2.0'],
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3'
    ],
)
