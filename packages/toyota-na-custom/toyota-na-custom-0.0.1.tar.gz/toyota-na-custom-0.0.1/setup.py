from setuptools import setup

setup(
    name='toyota-na-custom',
    version='0.0.1',
    description='Customized Toyota NA that support refresh token',
    author='Tony',
    author_email='waddle-years-0f@icloud.com',
    # url='https://github.com/your-username/your-package',
    packages=['toyota-na-custom'],
    install_requires=[
        'aiohttp',
        'cryptography',
        'PyJWT',
        'pytz',
    ],
)