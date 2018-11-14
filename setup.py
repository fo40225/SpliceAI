import io
from setuptools import setup

setup(name='spliceai',
      description='SpliceAI: A deep learning-based tool to identify splice variants',
      long_description=io.open('README.md', encoding='utf-8').read(),
      long_description_content_type='text/markdown',
      version='0.3',
      author='Kishore Jaganathan',
      author_email='kishorejaganathan@gmail.com',
      license='GPLv3',
      url='https://github.com/illumina/SpliceAI',
      packages=['spliceai'],
      install_requires=['keras>=2.0.5',
                        'tensorflow>=1.1.0',
                        'pyfasta>=0.5.2',
                        'pysam>=0.10.0',
                        'numpy>=1.14.0',
                        'pandas>=0.23.0'],
      extras_require={'gpu': ['tensorflow-gpu>=1.1.0']},
      package_data={'spliceai': ['annotations/GENCODE.v24lift37',
                                 'models/spliceai1.h5',
                                 'models/spliceai2.h5',
                                 'models/spliceai3.h5',
                                 'models/spliceai4.h5',
                                 'models/spliceai5.h5']},
      entry_points={'console_scripts': ['spliceai=spliceai.__main__:main']})
