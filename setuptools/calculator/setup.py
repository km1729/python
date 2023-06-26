import setuptools

setuptools.setup(
    include_package_data=True,
    name='km',
    version='0.0.1',
    description='python module',
    url=' ',
    author='km',
    author_email='abcd@abcd.com',
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'pytest'
    ],
    long_description='python module',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)