'''OpenGL extension ARB.gpu_shader_fp64

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_gpu_shader_fp64'
_DEPRECATED = False
GL_DOUBLE_VEC2 = constant.Constant( 'GL_DOUBLE_VEC2', 0x8FFC )
GL_DOUBLE_VEC3 = constant.Constant( 'GL_DOUBLE_VEC3', 0x8FFD )
GL_DOUBLE_VEC4 = constant.Constant( 'GL_DOUBLE_VEC4', 0x8FFE )
GL_DOUBLE_MAT2 = constant.Constant( 'GL_DOUBLE_MAT2', 0x8F46 )
GL_DOUBLE_MAT3 = constant.Constant( 'GL_DOUBLE_MAT3', 0x8F47 )
GL_DOUBLE_MAT4 = constant.Constant( 'GL_DOUBLE_MAT4', 0x8F48 )
GL_DOUBLE_MAT2x3 = constant.Constant( 'GL_DOUBLE_MAT2x3', 0x8F49 )
GL_DOUBLE_MAT2x4 = constant.Constant( 'GL_DOUBLE_MAT2x4', 0x8F4A )
GL_DOUBLE_MAT3x2 = constant.Constant( 'GL_DOUBLE_MAT3x2', 0x8F4B )
GL_DOUBLE_MAT3x4 = constant.Constant( 'GL_DOUBLE_MAT3x4', 0x8F4C )
GL_DOUBLE_MAT4x2 = constant.Constant( 'GL_DOUBLE_MAT4x2', 0x8F4D )
GL_DOUBLE_MAT4x3 = constant.Constant( 'GL_DOUBLE_MAT4x3', 0x8F4E )
glUniform1d = platform.createExtensionFunction( 
'glUniform1d',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLdouble,),
doc='glUniform1d(GLint(location), GLdouble(x)) -> None',
argNames=('location','x',),
deprecated=_DEPRECATED,
)

glUniform2d = platform.createExtensionFunction( 
'glUniform2d',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLdouble,constants.GLdouble,),
doc='glUniform2d(GLint(location), GLdouble(x), GLdouble(y)) -> None',
argNames=('location','x','y',),
deprecated=_DEPRECATED,
)

glUniform3d = platform.createExtensionFunction( 
'glUniform3d',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLdouble,constants.GLdouble,constants.GLdouble,),
doc='glUniform3d(GLint(location), GLdouble(x), GLdouble(y), GLdouble(z)) -> None',
argNames=('location','x','y','z',),
deprecated=_DEPRECATED,
)

glUniform4d = platform.createExtensionFunction( 
'glUniform4d',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLdouble,constants.GLdouble,constants.GLdouble,constants.GLdouble,),
doc='glUniform4d(GLint(location), GLdouble(x), GLdouble(y), GLdouble(z), GLdouble(w)) -> None',
argNames=('location','x','y','z','w',),
deprecated=_DEPRECATED,
)

glUniform1dv = platform.createExtensionFunction( 
'glUniform1dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,arrays.GLdoubleArray,),
doc='glUniform1dv(GLint(location), GLsizei(count), GLdoubleArray(value)) -> None',
argNames=('location','count','value',),
deprecated=_DEPRECATED,
)

glUniform2dv = platform.createExtensionFunction( 
'glUniform2dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,arrays.GLdoubleArray,),
doc='glUniform2dv(GLint(location), GLsizei(count), GLdoubleArray(value)) -> None',
argNames=('location','count','value',),
deprecated=_DEPRECATED,
)

glUniform3dv = platform.createExtensionFunction( 
'glUniform3dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,arrays.GLdoubleArray,),
doc='glUniform3dv(GLint(location), GLsizei(count), GLdoubleArray(value)) -> None',
argNames=('location','count','value',),
deprecated=_DEPRECATED,
)

glUniform4dv = platform.createExtensionFunction( 
'glUniform4dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,arrays.GLdoubleArray,),
doc='glUniform4dv(GLint(location), GLsizei(count), GLdoubleArray(value)) -> None',
argNames=('location','count','value',),
deprecated=_DEPRECATED,
)

glUniformMatrix2dv = platform.createExtensionFunction( 
'glUniformMatrix2dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glUniformMatrix2dv(GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glUniformMatrix3dv = platform.createExtensionFunction( 
'glUniformMatrix3dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glUniformMatrix3dv(GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glUniformMatrix4dv = platform.createExtensionFunction( 
'glUniformMatrix4dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glUniformMatrix4dv(GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glUniformMatrix2x3dv = platform.createExtensionFunction( 
'glUniformMatrix2x3dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glUniformMatrix2x3dv(GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glUniformMatrix2x4dv = platform.createExtensionFunction( 
'glUniformMatrix2x4dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glUniformMatrix2x4dv(GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glUniformMatrix3x2dv = platform.createExtensionFunction( 
'glUniformMatrix3x2dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glUniformMatrix3x2dv(GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glUniformMatrix3x4dv = platform.createExtensionFunction( 
'glUniformMatrix3x4dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glUniformMatrix3x4dv(GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glUniformMatrix4x2dv = platform.createExtensionFunction( 
'glUniformMatrix4x2dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glUniformMatrix4x2dv(GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glUniformMatrix4x3dv = platform.createExtensionFunction( 
'glUniformMatrix4x3dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glUniformMatrix4x3dv(GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glGetUniformdv = platform.createExtensionFunction( 
'glGetUniformdv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,arrays.GLdoubleArray,),
doc='glGetUniformdv(GLuint(program), GLint(location), GLdoubleArray(params)) -> None',
argNames=('program','location','params',),
deprecated=_DEPRECATED,
)

glProgramUniform1dEXT = platform.createExtensionFunction( 
'glProgramUniform1dEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLdouble,),
doc='glProgramUniform1dEXT(GLuint(program), GLint(location), GLdouble(x)) -> None',
argNames=('program','location','x',),
deprecated=_DEPRECATED,
)

glProgramUniform2dEXT = platform.createExtensionFunction( 
'glProgramUniform2dEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLdouble,constants.GLdouble,),
doc='glProgramUniform2dEXT(GLuint(program), GLint(location), GLdouble(x), GLdouble(y)) -> None',
argNames=('program','location','x','y',),
deprecated=_DEPRECATED,
)

glProgramUniform3dEXT = platform.createExtensionFunction( 
'glProgramUniform3dEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLdouble,constants.GLdouble,constants.GLdouble,),
doc='glProgramUniform3dEXT(GLuint(program), GLint(location), GLdouble(x), GLdouble(y), GLdouble(z)) -> None',
argNames=('program','location','x','y','z',),
deprecated=_DEPRECATED,
)

glProgramUniform4dEXT = platform.createExtensionFunction( 
'glProgramUniform4dEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLdouble,constants.GLdouble,constants.GLdouble,constants.GLdouble,),
doc='glProgramUniform4dEXT(GLuint(program), GLint(location), GLdouble(x), GLdouble(y), GLdouble(z), GLdouble(w)) -> None',
argNames=('program','location','x','y','z','w',),
deprecated=_DEPRECATED,
)

glProgramUniform1dvEXT = platform.createExtensionFunction( 
'glProgramUniform1dvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLsizei,arrays.GLdoubleArray,),
doc='glProgramUniform1dvEXT(GLuint(program), GLint(location), GLsizei(count), GLdoubleArray(value)) -> None',
argNames=('program','location','count','value',),
deprecated=_DEPRECATED,
)

glProgramUniform2dvEXT = platform.createExtensionFunction( 
'glProgramUniform2dvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLsizei,arrays.GLdoubleArray,),
doc='glProgramUniform2dvEXT(GLuint(program), GLint(location), GLsizei(count), GLdoubleArray(value)) -> None',
argNames=('program','location','count','value',),
deprecated=_DEPRECATED,
)

glProgramUniform3dvEXT = platform.createExtensionFunction( 
'glProgramUniform3dvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLsizei,arrays.GLdoubleArray,),
doc='glProgramUniform3dvEXT(GLuint(program), GLint(location), GLsizei(count), GLdoubleArray(value)) -> None',
argNames=('program','location','count','value',),
deprecated=_DEPRECATED,
)

glProgramUniform4dvEXT = platform.createExtensionFunction( 
'glProgramUniform4dvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLsizei,arrays.GLdoubleArray,),
doc='glProgramUniform4dvEXT(GLuint(program), GLint(location), GLsizei(count), GLdoubleArray(value)) -> None',
argNames=('program','location','count','value',),
deprecated=_DEPRECATED,
)

glProgramUniformMatrix2dvEXT = platform.createExtensionFunction( 
'glProgramUniformMatrix2dvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glProgramUniformMatrix2dvEXT(GLuint(program), GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('program','location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glProgramUniformMatrix3dvEXT = platform.createExtensionFunction( 
'glProgramUniformMatrix3dvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glProgramUniformMatrix3dvEXT(GLuint(program), GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('program','location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glProgramUniformMatrix4dvEXT = platform.createExtensionFunction( 
'glProgramUniformMatrix4dvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glProgramUniformMatrix4dvEXT(GLuint(program), GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('program','location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glProgramUniformMatrix2x3dvEXT = platform.createExtensionFunction( 
'glProgramUniformMatrix2x3dvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glProgramUniformMatrix2x3dvEXT(GLuint(program), GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('program','location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glProgramUniformMatrix2x4dvEXT = platform.createExtensionFunction( 
'glProgramUniformMatrix2x4dvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glProgramUniformMatrix2x4dvEXT(GLuint(program), GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('program','location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glProgramUniformMatrix3x2dvEXT = platform.createExtensionFunction( 
'glProgramUniformMatrix3x2dvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glProgramUniformMatrix3x2dvEXT(GLuint(program), GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('program','location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glProgramUniformMatrix3x4dvEXT = platform.createExtensionFunction( 
'glProgramUniformMatrix3x4dvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glProgramUniformMatrix3x4dvEXT(GLuint(program), GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('program','location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glProgramUniformMatrix4x2dvEXT = platform.createExtensionFunction( 
'glProgramUniformMatrix4x2dvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glProgramUniformMatrix4x2dvEXT(GLuint(program), GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('program','location','count','transpose','value',),
deprecated=_DEPRECATED,
)

glProgramUniformMatrix4x3dvEXT = platform.createExtensionFunction( 
'glProgramUniformMatrix4x3dvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLsizei,constants.GLboolean,arrays.GLdoubleArray,),
doc='glProgramUniformMatrix4x3dvEXT(GLuint(program), GLint(location), GLsizei(count), GLboolean(transpose), GLdoubleArray(value)) -> None',
argNames=('program','location','count','transpose','value',),
deprecated=_DEPRECATED,
)


def glInitGpuShaderFp64ARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )