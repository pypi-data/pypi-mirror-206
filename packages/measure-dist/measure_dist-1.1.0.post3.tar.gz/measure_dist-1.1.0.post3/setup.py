from setuptools import setup
setup(
    name = "measure_dist",
    version = "1.1.0-3",
    packages = ["measure_dist"],
    package_dir = {"measure_dist": "src/measure_dist"},
    include_package_data = True,
    description = "Measurement helper functions",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    readme = "README.md",
    author = "Gegeco",
    author_email = "gegeco06@gmail.com" ,
    license_files = ["LICENSE"],
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords = ["Measure", "Measurement", "Distance"],
    setup_requires = [
        "setuptools>=59.0.0",
        "wheel"
    ],
    install_requires = [
        "pybindgen",
    ],
    python_requires = "==3.6.*"
)
