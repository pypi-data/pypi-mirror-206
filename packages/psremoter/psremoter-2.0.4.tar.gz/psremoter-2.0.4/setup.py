import setuptools

setuptools.setup(
    name = "psremoter",
    version = "2.0.4",
    author = "Daniel Mandelblat",
    author_email = "danielmande@gmail.com",
    description = "Powershell remote client tool for Python",
    long_description_content_type = "text/markdown",
    url = "https://github.com/danielMandelblat/psremoter",
    project_urls = {
        "Bug Tracker": "https://github.com/danielMandelblat/psremoter",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.8"
)