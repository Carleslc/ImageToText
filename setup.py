from setuptools import setup, find_packages

with open('README.md', 'r') as readme_f:
  readme = readme_f.read()

setup(
  name='ImageToText',
  version='1.1',
  author='Carlos Lázaro Costa',
  author_email='lazaro.costa.carles@gmail.com',
  url='https://github.com/Carleslc/ImageToText',
  description="OCR with Google's AI technology (Cloud Vision API)",
  long_description=readme,
  long_description_content_type='text/markdown',
  python_requires='>=3.6',
  packages=find_packages(),
  install_requires=['google-cloud-vision'],
  entry_points={
    'console_scripts': [
      'img2txt = ImageToText.img2txt:main',
    ]
  },
)
