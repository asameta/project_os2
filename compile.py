from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
  name='etki',
  ext_modules=[Extension('etki', ['etki.py'],)],
  cmdclass={'build_ext': build_ext},
)
