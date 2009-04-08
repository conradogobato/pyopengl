'''OpenGL extension SUNX.constant_data

This module customises the behaviour of the 
OpenGL.raw.GL.SUNX.constant_data to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.SUNX.constant_data import *
### END AUTOGENERATED SECTION