from setuptools import setup, find_packages


setup(
    name='fastapi-modelrouter',
    version='0.0',
    license='MIT',
    author="Uwe Windt",
    author_email='uwe.windt@windisoft.de',
    packages=find_packages('modelrouter'),
    package_dir={'': 'modelrouter'},
    url='https://github.com/UweWindt/fastapi-modelrouter',
    keywords='fastapi router sqlalchemy',
    install_requires=[
          'sqlalchemy',
      ],

)