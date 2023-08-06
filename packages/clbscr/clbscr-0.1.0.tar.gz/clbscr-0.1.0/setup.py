from setuptools import setup, find_packages

setup(
    name='clbscr',
    version='0.1.0',
    author='Davide Gimondo',
    author_email='davegimo@example.com',
    description='A package for doing some useful stuff',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/davegimo/clbscr',
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    keywords='my-package, example, demo',
    install_requires=[
        # List your project dependencies here
    ],
    python_requires='>=3.6, <4',
    include_package_data=True
)