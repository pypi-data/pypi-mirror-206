from setuptools import setup , find_packages
setup(name='SiteScraper',
      version='0.2.1',
      description='Scraping high intensity content sites',
      author='Ibrahim',
        packages=find_packages(),
        zip=False,
        author_email='string2025@gmail.com',
      install_requires=[
        'selenium',
        ],)