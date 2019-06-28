from setuptools import setup, find_packages

setup(
    name='subword_nmt',
    version='0.3.6',
    description='Unsupervised Word Segmentation for Neural Machine Translation and Text Generation',
    url='https://github.com/tanbro/subword-nmt',
    author='liu xue yan',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Text Processing',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    entry_points={
        'console_scripts': ['subword-nmt=subword_nmt.subword_nmt:main'],
    },
)
