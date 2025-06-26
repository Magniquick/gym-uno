from setuptools import setup

setup(name='gym_uno',
      version='0.0.1',
      install_requires=['gymnasium>=1.1.1'],
      data_files=[('envs',['gym_uno/envs/uno.jar'])],
      include_package_data=True
)
