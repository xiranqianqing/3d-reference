
import bpy

class READY_OT_bindBones(bpy.types.Operator):
    bl_idname = "obj.bindbones"
    bl_label = "绑定骨骼"
    bl_description = "将骨骼和模型绑定在一起"

    def execute(self, context):
        bpy.ops.mmd_tools.morph_slider_setup(type='BIND')
        return {"FINISHED"}

class READY_OT_colorNormal(bpy.types.Operator):
    bl_idname = "obj.colornormal"
    bl_label = "颜色正常"
    bl_description = "解决颜色变紫"

    def execute(self, context):
        bpy.context.object.mmd_root.use_toon_texture = False
        return {"FINISHED"}

#bpy.context.space_data.overlay.show_bones = False

