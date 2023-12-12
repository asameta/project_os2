from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


setup(
  name='krohne',
  ext_modules=[Extension('krohne', ['krohne.py'],)],
  cmdclass={'build_ext': build_ext},
)
