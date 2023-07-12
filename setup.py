from distutils.core import setup

setup(
    name='ColabPlugin',
    version='1.0',
    author='Michael Canesche',
    author_email='michael.canesche@gmail.com',
    py_modules=['plugin', 'cuda.cuda', 'c.c', 'cpp.cpp', 'verilog.verilog', 'java.java', 'gem5.gem5', 'valgrind.valgrind', 'llvm.llvm', 'rust.rust', 'common.helper', 'common.tool'],
    url='https://github.com/menotti/cad4u',
    license='LICENSE',
    description='Jupyter notebook plugin to run CUDA, C/C++, GCC code, Verilog, LLVM, Gem5',
    # long_description=open('README.md').read(),
)
