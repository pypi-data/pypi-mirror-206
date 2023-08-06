from setuptools import setup, find_packages

setup(
    name="packagebinbin",
    version="0.0.4",
    author="Sophat Chhay",
    author_email="<sophat.chhay@gmail.com>",
    description="My demo package with my daughter name",
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    long_description= "Testing",
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.9"
    ]
)