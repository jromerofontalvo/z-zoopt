import setuptools
import os

readme_path = os.path.join("..", "README.md")
with open(readme_path, "r") as f:
    long_description = f.read()

setuptools.setup(
    name="z-zoopt",
    version="0.1.0",
    author="JRF",
    author_email="jromerofontalvo@zapatacomputing.com",
    description="Example Zoopt integration.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jromerofontalvo/z-zoopt.git",
    packages=setuptools.find_namespace_packages(include=['zzoopt.*']),
    package_dir={'' : 'python'},
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'z-quantum-core',
        'pytest==5.3.5',
        'zoopt==0.4.0'
    ]
)
