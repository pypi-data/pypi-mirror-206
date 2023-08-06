from pathlib import Path

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup
import glob

jaco_module = Pybind11Extension(
    'jaco2',
    [str(fname) for fname in Path('src').glob('*.cpp')],
    include_dirs=['.'],
    library_dirs=['src'],
    extra_compile_args=['/Ox'],
)

setup(
    name='jaco2',
    version=3.4,
    author='Daniel Dharampal',
    description='A binding of simple jaco2 SDK commands for python',
    ext_modules=[jaco_module],
    data_files=[("dll_lib", ['src/CommandLayerEthernet.dll', 'src/CommandLayerWindows.dll', 'src/CommunicationLayerEthernet.dll', 'src/CommunicationLayerWindows.dll'])],
    cmdclass={"build_ext": build_ext},
)