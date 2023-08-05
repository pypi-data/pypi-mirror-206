from pathlib import Path

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

jaco_module = Pybind11Extension(
    'jaco2',
    [str(fname) for fname in Path('robotControl').glob('*.cpp')],
    include_dirs=['./lib'],
    extra_compile_args=['/std:c++11', '/MT', '/arch:amd64'],
    extra_link_args=['-Wl,-rpath,$ORIGIN/../lib']
)

setup(
    name='jaco2',
    version=2.0,
    author='Daniel Dharampal',
    description='A binding of simple jaco2 SDK commands for python',
    ext_modules=[jaco_module],
    cmdclass={"build_ext": build_ext},
)