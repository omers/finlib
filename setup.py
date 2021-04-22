from distutils.core import setup

setup(
    name="FinLib",
    version="0.3",
    author="Omer Segev",
    author_email="omersegev@gmail.com",
    description="Python package for getting Financial data from data sources",
    llong_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/omerse",
    keywords=["finance", "models", "technical"],
    packages=["finlib"],
    install_requires=[
        "pandas==1.2.4",
        "pandas-datareader==0.9.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
)
