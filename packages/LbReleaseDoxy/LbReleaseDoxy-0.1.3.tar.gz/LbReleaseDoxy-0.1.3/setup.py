from setuptools import setup, find_packages
import os
#config_path = os.path.join(os.path.dirname(__file__), "LbRelease/_LHCbDocResources")
setup(
    name='LbReleaseDoxy',
    packages=find_packages(),
    package_data={"":['class.php','layout.xml-1.7.2','layout.xml-1.8.2','layout.xml-1.8.9.1','layout.xml-1.8.11']},
    version='0.1.3',    
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
