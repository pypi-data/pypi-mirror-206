from setuptools import setup


setup(
    name='foggyday',
    packages=['foggyday'],
    version='1.0.0',
    description='Weather Forcast Data',
    license="MIT",
    author='Zakhar Sotnichenko',
    author_email='zakhar.sotnichenko@mail.ru',
    url="http://jinkosiz.pythonanywhere.com/",
    keywords=['weather', 'forecast', 'openweather'],
    install_requires=['requests'],  # external packages as dependencies
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ]
)
