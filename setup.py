from setuptools import setup

setup(name='gym_uno',
      version='0.0.1',
      install_requires=['gym>=0.2.3'],
      data_files=[('envs',['gym_uno/envs/uno.jar'])],
      include_package_data=True
)
