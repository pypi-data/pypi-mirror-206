from setuptools import setup, find_packages

setup(
    name='vectorGPTBot',
    version='0.1.4',
    author='wstart',
    description='A sample vectorGPTBot',
    long_description='A sample vectorGPTBot',
    long_description_content_type="text/markdown",
    packages=find_packages('vectorGPTBot'),
    package_dir={'': 'vectorGPTBot'},
    install_requires=[
        'chromadb',
        'modelscope',
        'transformers'
    ],
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
    keywords='vectorGPTBot',
    license='Apache License 2.0',
)
