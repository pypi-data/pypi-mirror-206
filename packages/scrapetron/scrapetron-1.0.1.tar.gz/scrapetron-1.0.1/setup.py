from setuptools import setup, find_packages

setup(
    name='scrapetron',
    version='1.0.1',
    description='A library for web scraping in Python. Provides a simple and intuitive API for extracting data from websites. With Scrapetron, you can easily scrape web pages and extract information such as text, images, links, and more.',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'beautifulsoup4',
        'requests',
    ],
    author='Rohan',
    author_email='rohan.mbox@gmail.com',
    url='https://github.com/rohzzn/scrapetron',
)
