
import io
from setuptools import setup, find_packages

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='pddsdk',
    version='0.1.12',
    description='an open source api for pingduoduo',
    long_description=readme,
    url='https://github.com/linzhiming0826/pddsdk',
    author='TuoX',
    author_email='120549827@qq.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='pddsdk pingduoduo api extend',
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),
    install_requires=['requests'],
    # List additional groups of dependencies here
    extras_require={}
)
