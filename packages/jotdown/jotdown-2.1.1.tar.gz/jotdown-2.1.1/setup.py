from pathlib import Path
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        name="jotdown",
        include_dirs=[
            "include",
            "moonlight/deps",
            "moonlight/include",
            "pybind11/include",
        ],
        sources=[str(src) for src in Path.cwd().glob("src/*.cpp")],
        extra_compile_args=["-O3", "-shared", "-std=c++2a", "-fPIC", "-fpermissive"],
    )
]

# Get the long description from the README file
with open(Path("README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="jotdown",
    version="2.1.1",
    description="Jotdown structrured document language, C++ to python wrapper module.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lainproliant/jotdown",
    author="Lain Musgrove (lainproliant)",
    author_email="lainproliant@gmail.com",
    license="BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="document structure parser query language",
    ext_modules=ext_modules,
    zip_safe=False,
    include_package_data=True,
)
