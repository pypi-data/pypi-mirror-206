from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='maxeqx-dc-webhook.py',
  version='1.1.0',
  description='This is simple webhook sender in discord.',
  long_description="Long description and usage is on my github: https://github.com/makseksowny/maxeqx-dc-webhook.",
  url='',  
  author='maxeqx',
  author_email='maxeqxmail@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='discord webhook sender',
  packages=find_packages(),
  install_requires=['requests'] 
)
