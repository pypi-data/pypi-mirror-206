from setuptools import find_packages, setup


setup(
    name='vnpy_askshare',
    version='1.0',
    description='vnpy_akshare数据服务',
    long_description=open('README.rst').read(),
    author='<lpf6;jan>',
    author_email='<298092154@qq.com>',
    maintainer='<jan>',
    maintainer_email='<298092154@qq.com>',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/bthuntergg/vnpy_akshare',
    license='BSD License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
