from setuptools import setup

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='shify',
    version='0.0.1',
    author='Sharavsambuu Gunchinish',
    author_email='sharavsambuu@gmail.com',
    description='Multi asset, multi universe and multi strategy backtester',
    long_description= long_description,
    url='https://github.com/sharavsambuu/shify-backtester',
    license='MIT',
    packages=[
        'shify',
        'shify.utilities'
        ],
    install_requires=[
        'pandas',
        'numpy',
        'TA-Lib',
        'selenium',
        'beautifulsoup4',
        'webdriver-manager'
        ],
    entry_points = {
        'console_scripts': [
            'binance-download=shify.utilities.data_tools:binance_download'
        ],
    }

)