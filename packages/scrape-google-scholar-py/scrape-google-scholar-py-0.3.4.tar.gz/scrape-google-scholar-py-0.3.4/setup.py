from setuptools import setup

README = ''
with open('README.md', 'r', encoding='utf-8') as readme_file:
    README = readme_file.read()

setup(
    name='scrape-google-scholar-py',
    description = 'Extract data from all Google Scholar pages in Python. Sponsored by SerpApi.',
    url='https://github.com/dimitryzub/scrape-google-scholar',
    version='0.3.4',
    license='MIT',
    author='Dmitiry Zub',
    author_email='dimitryzub@gmail.com',
    maintainer='Dmitiry Zub',
    maintainer_email='dimitryzub@gmail.com',
    long_description_content_type='text/markdown',
    long_description=README,
    include_package_data=True,
    python_requires='>=3.10',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Topic :: Internet',
        'Natural Language :: English',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords=[
            'google scholar',
            'serpapi',
            'scraper',
            'python',
            'python google scholar',
            'python google scholar api',
            'web scraping',
            'python web scraping',
            'research',
            'lexbor',
            'selectolax',
            'selenium',
            'selenium-stealth',
            'pandas',
        ],
    install_requires=[
          'google-search-results>=2.4.2',
          'selectolax>=0.3.12',
          'parsel>=1.7.0',
          'selenium-stealth>=1.0.6',
          'pandas>=1.5.3',
          'webdriver-manager>=3.8.5' 
    ],
    project_urls={
        'Documentation': 'https://github.com/dimitryzub/scrape-google-scholar#example-usage-custom-backend',
        'Source': 'https://github.com/dimitryzub/scrape-google-scholar',
        'Tracker': 'https://github.com/dimitryzub/scrape-google-scholar/issues',
    },
)