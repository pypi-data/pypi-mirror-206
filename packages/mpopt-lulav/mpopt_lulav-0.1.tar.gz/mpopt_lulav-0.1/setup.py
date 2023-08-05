from distutils.core import setup
setup(
  name = 'mpopt_lulav',   
  packages = ['mpopt_lulav'], 
  version = '0.1', 
  license='MIT',   
  description = 'Optimal control lib modified by Lulav Space', 
  author = 'gtep',   
  author_email = 'gleb@lulav.space', 
  url = 'https://github.com/lulav/mpopt_lulav',
  download_url = 'https://github.com/lulav/mpopt_lulav/archive/refs/tags/v0.1.tar.gz', 
  keywords = ['Optimal', 'Control', 'Lulav'],  
  install_requires=[           
          'numpy',
          'casadi',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',    
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)