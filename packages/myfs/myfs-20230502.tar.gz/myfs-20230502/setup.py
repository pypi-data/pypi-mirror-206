import time
from distutils.core import setup

setup(
  name = 'myfs',
  packages = ['myfs'],
  version = time.strftime('%Y%m%d'),
  description = 'My File Store - GET/PUT/DELETE operations over HTTPS.',
  long_description = 'Fault tolerant and highly available. Uses mTLS for auth.',
  author = 'Bhupendra Singh',
  author_email = 'bhsingh@gmail.com',
  url = 'https://github.com/magicray/myfs'
)
