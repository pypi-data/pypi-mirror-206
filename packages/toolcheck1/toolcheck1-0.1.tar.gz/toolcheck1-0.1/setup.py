from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig
from setuptools import find_packages
import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toolcheck1",                
    version="0.1",                        
    author="Bhanuja",  
    author_email="abhanuja@presidio.com",
    license= 'MIT',              
    description="Data And Analytics Audit Tool",
    long_description=long_description,     
    long_description_content_type="text/markdown",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={
        'dna_audit_tool': ['common/templates/*.html']
    },
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'toolcheck11=dna_audit_tool.main:__main__'
        ]
    },
    include_package_data=True,
    python_requires='>=3.6',                
    install_requires=["boto3==1.26.85","nose==1.3.7","Jinja2==3.1.2","moto==4.1.4","docker==6.0.1","pyparsing==3.0.9","openapi_spec_validator==0.5.6"]                    
)