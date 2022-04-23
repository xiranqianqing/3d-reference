import bpy
from random import randint

global trigger1,trigger2,trigger3
trigger1=False
trigger2=False
trigger3=False
#按一次确定，按两次取消

class OTHER_OT_shadow(bpy.types.Operator):
    bl_idname = "obj.shadow"
    bl_label = "优化阴影"
    bl_description = "Eevee优化阴影"

    def execute(self, context):
        global trigger1
        trigger1 = not trigger1
        if(trigger1 == True):
            bpy.context.scene.eevee.use_gtao = True
            bpy.context.scene.eevee.shadow_cube_size = '4096'
            bpy.context.scene.eevee.shadow_cascade_size = '4096'
            bpy.context.scene.eevee.use_shadow_high_bitdepth = True
            bpy.context.scene.eevee.use_soft_shadows = True
        else:
            bpy.context.scene.eevee.use_gtao = False
            bpy.context.scene.eevee.shadow_cube_size = '512'
            bpy.context.scene.eevee.shadow_cascade_size = '1024'
            bpy.context.scene.eevee.use_shadow_high_bitdepth = False
            bpy.context.scene.eevee.use_soft_shadows = False

        #环境光遮蔽，
        return {"FINISHED"}

class OTHER_OT_floodlight(bpy.types.Operator):
    bl_idname = "obj.floodlight"
    bl_label = "辉光"
    bl_description = "Eevee辉光"

    def execute(self, context):
        global trigger2
        trigger2 = not trigger2
        if(trigger2 == True):
            bpy.context.scene.eevee.use_bloom = True
            bpy.context.object.data.dof.aperture_fstop = 0.1
        else:
            bpy.context.scene.eevee.use_bloom = False
            bpy.context.object.data.dof.aperture_fstop = 2.8
        return {"FINISHED"}

class OTHER_OT_cameraOutOfFocus(bpy.types.Operator):
    bl_idname = "obj.cameraoutoffocus"
    bl_label = "相机失焦"
    bl_description = "请选中相机后使用"

    def execute(self, context):
        global trigger3
        trigger3 = not trigger3
        if(trigger3 == True):
            bpy.context.object.data.dof.use_dof = True
        else:
            bpy.context.object.data.dof.use_dof = False
        return {"FINISHED"}

class OTHER_OT_flyingProps(bpy.types.Operator):
    bl_idname = "obj.flyingprops"
    bl_label = "随机空中球"
    bl_description = "飞行道具"

    def execute(self, context):
        number = 10
        for i in range(0,number):
            x=randint(-10,10)
            y=randint(-10,10)
            z=randint(0,20)
            size=randint(20,100)/50    
            bpy.ops.mesh.primitive_uv_sphere_add(location=(x,y,z),scale=(size,size,size))
        return {"FINISHED"}
"""
class OTHER_OT_grainEffect(bpy.types.Operator):
    bl_idname = "obj.graineffect"
    bl_label = "萤火虫"
    bl_description = "粒子特效"

    def execute(self, context):
        ...
        return {"FINISHED"}
"""
#目前没有解决的问题：褶皱和头发是比较难画的部分，还需要头发和裙子的碰撞和布料设定。