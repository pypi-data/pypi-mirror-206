from setuptools import setup, find_packages

setup(
    name='zoomlet',
    version='0.1',
    description='Box plot visualization library',
    author='Vinil',
    author_email='vinilharsh123@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
