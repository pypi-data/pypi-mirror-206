from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='poequora',
    version='1.0.1',
    author='xtekky',
    author_email='',
    description='poe',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://pypi.org/project/poequora/',
    project_urls={
        'Bug Tracker': 'https://pypi.org/project/poequora/',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data = True,
    install_requires = ['pypasser', 'fake_useragent', 'websocket-client', 'tls_client', 'pydantic' , 'selenium'],
    python_requires='>=3.6'
)