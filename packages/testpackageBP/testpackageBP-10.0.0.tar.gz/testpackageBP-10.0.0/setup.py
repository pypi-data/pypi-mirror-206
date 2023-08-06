from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()
    
setup(
    name='testpackageBP',
    version='10.0.0',
    description='A script that uploads environment variables to a Jenkins server',
    author='Your Name',
    author_email='vanhoorenvictor@gmail.com',
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'upload-env-variables=upload_env_variables:main'
        ]
    }
)
