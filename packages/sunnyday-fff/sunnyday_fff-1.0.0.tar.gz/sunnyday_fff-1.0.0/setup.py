
from setuptools import setup

setup(
    name='sunnyday_fff',
    packages=['sunnyday'],
    version='1.0.0',
    license='MIT',
    description='Weather forecast data',
    author='FrostFireFalcon',
    author_email='i.simac.8@gmail.com',
    url='https://github.com/FrostFireFalcon',
    keywords=['weather', 'forecast', 'openweather'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)
