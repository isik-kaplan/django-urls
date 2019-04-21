from setuptools import setup


with open('README.md') as f:
    long_description = f.read()


setup(
    name='django_urls',
    version='1.0.6',
    packages=['django_urls'],
    url='https://github.com/isik-kaplan/django_urls',
    description="URL decorator for django views",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='APGL-3.0',
    author='isik-kaplan',
    author_email='',
    python_requires=">=3.5",
    install_requires=['django>=2.0']
)
