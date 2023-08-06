from setuptools import setup, find_packages


setup(
    name="ExpdLoggerService",
    version="0.5.0",
    license='MIT',
    author="greg he",
    author_email='greg.he@expeditors.com',
    description="Python Module for customize logger",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='logger service',
    install_requires=[
        'loguru', 'pendulum', 'pytzdata'
    ],
)