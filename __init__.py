# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Autoretopo",
    "author" : "Sphinx",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "view3D",
    "warning" : "",
    "category" : "Object"
}


import bpy
from bpy.props import *

from . SPX_op import SPX_OT_Apply_All_Op
from . SPX_panel import SPX_PT_Panel

#Scene properties

bpy.types.Scene.voxel_size = bpy.props.FloatProperty(
    name="Voxel Size",
    description="Size of the voxels for the remesh operation",
    default=0.1,
    min=0.01,
    max=10.0
)

bpy.types.Scene.quad_enabled = bpy.props.BoolProperty(
    name="Quad faces",
    description="Enable quad remeshing",
    default=True
)

bpy.types.Scene.face_number = bpy.props.IntProperty(
    name="Faces",
    description="Number of faces for quad remeshing",
    default=1000,
    min=1,
    max=50000
)

bpy.types.Scene.diffuse_texture = bpy.props.BoolProperty(
    name="Diffuse",
    description="",
    default=True
)

bpy.types.Scene.normal_texture = bpy.props.BoolProperty(
    name="Normal",
    description="",
    default=True
)

bpy.types.Scene.tex_size = bpy.props.IntProperty(
    name="Texture Size",
    description="Texture size",
    default=2048,
    min=1,
    max=50000
)

bpy.types.Scene.bakeFolder = bpy.props.StringProperty(
    name="",
    description="Choose a directory to save the output file",
    default="Output path",
    maxlen=1023,
    subtype='DIR_PATH'
)



classes = (SPX_OT_Apply_All_Op, SPX_PT_Panel)

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()