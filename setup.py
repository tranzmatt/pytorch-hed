from setuptools import setup, find_packages

# Load long description from README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='pytorch-hed',
    version='0.1',
    description='A personal reimplementation of Holistically-Nested Edge Detection using PyTorch.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Simon Niklaus',
    author_email='mail@sniklaus.com",
    url='https://github.com/sniklaus/pytorch-hed',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.15.0',
        'Pillow>=5.0.0',
        'torch>=1.6.0',
    ],
    entry_points={
        'console_scripts': [
            'pytorch-hed=run:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.12',
    ],
)

