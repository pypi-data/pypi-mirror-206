from setuptools import setup, find_packages

setup(

    name='imagefx',
    version='1.0.2',
    description='Python library for performing image processing operations',
    author='Photon',
    author_email='electrify0608@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'Pillow>=8.2.0',
        'numpy>=1.20.3',
        'opencv-python-headless>=4.5.2.52'
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'flake8'
        ]
    },
    entry_points={
        'console_scripts': [
            'imagefx=imagefx.cli:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',  
        'Programming Language :: Python :: 3.7',  
        'Programming Language :: Python :: 3.8', 
        'Programming Language :: Python :: 3.9',
    ],
)
