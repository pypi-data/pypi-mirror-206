import setuptools

setuptools.setup(
    name='letipy',
    version='0.1.5',
    description='A Powerful scientific strings-processing library',
    install_requires=['numpy', 'nltk', 'afinn', 'gmpy2'],
    author='Khalid Aghrini',
    author_email='kwaaghrini@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)