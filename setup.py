try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = 'wddd'
__version__ = '0.1.0'

packages = [
    'weibo_cn_api',
    'weibo_com_api',
    'simple_captcha',
    'util'
]

setup(
    name='weibo_api',
    version=__version__,
    author=__author__,
    license='MIT',
    url='',
    install_requires=['cookiejar', 'mxnet==1.3.1', 'numpy==1.14.6', 'peewee', 'pickledb',
                      'pillow', 'requests', 'requests_toolbelt', 'rsa'],
    include_package_data=True,
    keywords='Weibo api',
    description='An api for posting weibo (text, image, and video).',
    packages=packages,
    package_dir={'weibo_cn_api': 'weibo_cn_api', 'weibo_com_api': 'weibo_com_api'},
    package_data={'simple_captcha': ['*.params', '*.json', '*.pkl']},
    classifiers=[
        'Development Status :: Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
)
