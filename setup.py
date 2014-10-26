from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

# Cython extensions
sources = ["FastxIO/fastx.pyx", "FastxIO/reverse_complement.c"]
extensions = [Extension("FastxIO.fastx", sources, extra_compile_args=['-O3'])]

setup(
    name = "FastxIO",
    version = '0.0.0',
    packages = find_packages(exclude=['tests']),
    ext_modules = cythonize(extensions),
    description = "Read FASTA and FASTQ files.",
    author = "Marcus Kinsella",
    license = "MIT",
    install_requires = [
        'cython'
        ],
)


