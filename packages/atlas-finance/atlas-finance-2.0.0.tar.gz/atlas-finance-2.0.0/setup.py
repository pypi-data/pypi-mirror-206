# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup
from pathlib import Path
from sys import platform

__version__ = "2.0.0"

BASE_DIR = Path(__file__).absolute().parent.resolve()

include_dirs = []
library_dirs = []
libraries = []
if platform == "win32":
    LIB_DIR = Path('C:/Users/jmelo/Desktop/Desarrollo/c++/builds/release')   
    include_dirs += [str(LIB_DIR / 'include'), str(LIB_DIR / 'boost')]
    library_dirs += [str(LIB_DIR / 'lib')]

    libraries += ['QuantLib-x64-mt',  'Atlas', 'xad64_vc142_md']

else:
    if platform == "linux" or platform == "linux2":
        LIB_DIR = Path('/usr/local')
    else:
        LIB_DIR = Path('/Users/josemelo/Desktop/dev/builds')
        include_dirs += ['/opt/homebrew/opt/boost/include']
        include_dirs += ['/Users/josemelo/Desktop/dev/builds/include/eigen3']
        library_dirs += ['/opt/homebrew/opt/boost/lib']

    include_dirs += [str(LIB_DIR / 'include')]
    library_dirs += [str(LIB_DIR / 'lib')]

    libraries += ['QuantLib', 'Atlas','xad']

extra_compile_args = ['-std=c++17','/std:c++17']

ext_modules = [
    Pybind11Extension("Atlas",
                      ["module.cpp"],
                      include_dirs=include_dirs,
                      library_dirs=library_dirs,
                      libraries=libraries,
                      define_macros=[('VERSION_INFO', __version__)],
                      extra_compile_args=extra_compile_args
                      ),
]

setup(
    name="atlas-finance",
    version=__version__,
    author="Jose Melo",
    author_email="jmelo@live.cl",
    description="Pricing library for Python",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
