import setuptools

# see https://setuptools.pypa.io/en/latest/references/keywords.html
setuptools.setup(
    name="open-pyxl-sql",
    version='0.13',
    author="Fabien BATTINI",                    # noqa
    author_email="fabien.battini@gmail.com",
    description="A tiny SQL engine for Excel files, moved to excel-sql-engine",
    long_description='moved to excel-sql-engine',
    long_description_content_type="text/markdown",
    url="https://gitlab.com/fabien.battini/pyxlsql",
    license_files=["LICENCE"],
    keywords='excel sql',
    packages=setuptools.find_packages(),
    classifiers=[
        # see https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",  # noqa
        "Operating System :: OS Independent",
        "Development Status :: 7 - Inactive",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business :: Office Suites",
    ],
    python_requires='>=3.6',
)