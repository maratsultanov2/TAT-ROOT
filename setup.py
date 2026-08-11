from setuptools import setup, find_packages
setup(
    name='tat-public',
    version='0.1.0',
    description='TAT — Thermodynamic Adaptive Transformer (public modules)',
    author='Marat Sultanov',
    author_email='maratsultanov2@gmail.com',
    url='https://github.com/maratsultanov2/TAT-ROOT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['numpy>=1.24.0', 'scipy>=1.10.0', 'matplotlib>=3.7.0', 'pandas>=1.5.0'],
    python_requires='>=3.10',
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering',
    ],
)
