from pathlib import Path

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup
import glob

jaco_module = Pybind11Extension(
    'jaco2',
    [str(fname) for fname in Path('robotControl').glob('*.cpp')],
    include_dirs=['.'],
    extra_compile_args=['/Ox'],
    extra_link_args=['-Wl,-rpath,$ORIGIN/../lib'],
    data_files=[('.', ['CommandLayerEthernet.dll', 'CommandLayerWindows.dll', 'CommunicationLayerEthernet.dll', 'CommunicationLayerWindows.dll'])],
)

setup(
    name='jaco2',
    version=2.7,
    author='Daniel Dharampal',
    description='A binding of simple jaco2 SDK commands for python',
    ext_modules=[jaco_module],
    cmdclass={"build_ext": build_ext},
)