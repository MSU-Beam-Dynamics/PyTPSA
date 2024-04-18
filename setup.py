from distutils.core import setup, Extension
from Cython.Build import cythonize
 
ext = Extension('PyTPSA.cython.tpsalib',
                sources=["cython_src/tpsalib.pyx", "src/polymap.cpp", "src/mathfunc.cpp"],  # additional source fi$
                language="c++",             # generate C++ code
                extra_compile_args=["-O3", "-std=c++11"],
                )
 
setup (name='PyTPSA', ext_modules=cythonize(ext),
       package_dir={'PyTPSA': 'pkg', 'PyTPSA.cython': 'cython_src'},
       packages=['PyTPSA', 'PyTPSA.cython'],
       zip_safe=False)