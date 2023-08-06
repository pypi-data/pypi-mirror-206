from setuptools import find_packages, setup
import os

with open("app/Readme.md", "r") as f:
    long_description = f.read()

about = {}
with open("app/vizmetrics/src/_version.py") as f:
    exec(f.read(), about)
os.environ["PBR_VERSION"] = about["__version__"]

setup(
    name="vizmetrics",
    setup_requires=["pbr"],
    pbr=False,
    version=about["__version__"],
    # version="0.0.10",
    description="A package to plot AI/ML metrics at ease",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/somexgupta/vizmetrics",
    author="SomexGupta",
    author_email="gupta.somex@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["seaborn>= 0.11.2",
                      "matplotlib>= 3.3.4",
                      "numpy>= 1.19.2",
                      "scikit-learn",
                      "pandas",
                    #   "itertools",
                      "scipy>= 1.6.0",
                      ],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.7",
)
