import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='aws-ami-delete',
    version='0.0.0',
    author='Gunter Grodotzki',
    author_email='gunter@grodotzki.co.za',
    description='Delete AMIs - optionally from a packer manifest.json.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lifeofguenter/aws-ami-delete',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3',
    install_requires=[
        'boto3',
    ],
    entry_points={
        'console_scripts': [
            'aws-ami-delete = aws_ami_delete.__main__:cli',
        ],
    },
)
