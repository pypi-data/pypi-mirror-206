from setuptools import setup

setup(
    name="simulateIRAS",
    version = '0.0.0',
    description="A python package for simulating Infrared Reflection Absorption Spectroscopy(IRAS) measurements",
    py_modules = ["simulateIRAS"],
    package_dir = {'':'src'},
    
    author="coconnor24",
    author_email="coconnor@g.harvard.edu",
    
    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",
    
    url="https://github.com/coconnor24/simulateIRAS",
    include_package_data=True,
    
    license="GPLv3",
    
    classifiers  = [
        'Development Status :: 4 - Beta',
        
        'Programming Language :: Python',
        
        "License :: OSI Approved :: BSD License",
        
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
        
        'Operating System :: Microsoft :: Windows',
        ],
        
    install_requires=['numpy', 'scipy'],
    keywords = ["IRAS", "Surface Science", "FTIR", "doi:"]
)
