from setuptools import setup, find_packages

setup(
    name='LbReleaseDoxy',
    packages=find_packages(),
    version='0.1.0',    
    description='LbRelease. Here only used for creating doxygen configuration',
    url='https://gitlab.cern.ch/pinogga/lbutils_doxy',
    author='Piet Nogga',
    author_email='piet.nogga@cern.ch',
    install_requires=[                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.9',
    ],
)
