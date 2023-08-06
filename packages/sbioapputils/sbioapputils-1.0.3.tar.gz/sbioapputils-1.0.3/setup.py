from setuptools import setup

setup(name="sbioapputils",
      version="1.0.5",
      description="Superbio app runner utils",
      author="Superbio AI",
      author_email="smorgan@superbio.ai",
      url='https://github.com/Superbio-ai/app-sbioutils',
      install_requires=['requests==2.22.0', 'urllib3>=1.26', 'boto3==1.21.27','pandas==1.2.5', 'anndata==0.8.0', 'scanpy==1.9.1', 'numpy==1.21'],
      packages=['sbioapputils']
)
