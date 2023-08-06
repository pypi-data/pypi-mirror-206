from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='twity',
    version='0.0.2',
    author='Sanuja Methmal',
    author_email='methmal66@gmail.com',
    url='https://github.com/methmal66/twity.git',
    description='A simple twitter bot to create and delete your tweets from the terminal',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=required_packages,
    python_requires='>=3.6',
    entry_points={
        'console_scripts':[
            'twity=twity.twity:__main__'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)