
import bpy

class LIGHT_OT_createPoint(bpy.types.Operator):
    bl_idname = "obj.createpointlight"
    bl_label = "创建点光源"
    bl_description = "创建点光源"

    def execute(self, context):
        bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        return {"FINISHED"}

#创建点光源


class LIGHT_OT_brighter(bpy.types.Operator):
    bl_idname = "obj.pointlightbrighter"
    bl_label = "变亮"
    bl_description = "选中光源之后点击这个可以使其变亮"

    def execute(self, context):
        if (bpy.context.object.data.energy<=10000):
            bpy.context.object.data.energy *= 10
        return {"FINISHED"}

#点光源变亮

class LIGHT_OT_darker(bpy.types.Operator):
    bl_idname = "obj.pointlightdarker"
    bl_label = "变亮"
    bl_description = "选中光源之后点击这个可以使其变亮"

    def execute(self, context):
        if (bpy.context.object.data.energy>=1):
            bpy.context.object.data.energy /= 10
        return {"FINISHED"}

#点光源变暗

class LIGHT_OT_createParallel(bpy.types.Operator):
    bl_idname = "obj.createparallellight"
    bl_label = "创建平行光"
    bl_description = "创建平行光"
    
    def execute(self, context):
        bpy.ops.object.light_add(type='SUN', radius=1, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        return {"FINISHED"}

#创造平行光

#点光源亮暗相较于平行光亮暗变化比较大

class LIGHT_OT_parallelBrighter(bpy.types.Operator):
    bl_idname = "obj.parallellightbrighter"
    bl_label = "变亮"
    bl_description = "选中平行光之后点击这个可以使其变亮"

    def execute(self, context):
        if (bpy.context.object.data.energy<=16):
            bpy.context.object.data.energy *= 2
        return {"FINISHED"}

class LIGHT_OT_parallelDarker(bpy.types.Operator):
    bl_idname = "obj.parallellightdarker"
    bl_label = "变暗"
    bl_description = "选中平行光之后点击这个可以使其变暗"

    def execute(self, context):
        if (bpy.context.object.data.energy>=1):
            bpy.context.object.data.energy /= 2
        return {"FINISHED"}

#点光源光色改变
class LIGHT_OT_lightColorChange(bpy.types.Operator):
    bl_idname = "obj.lightcolorchange"
    bl_label = "改变光色"
    bl_description = "选中光之后点击"
    
    def execute(self, context):
        if(bpy.context.object.data.type == 'SUN'or'POINT'or'SPOT'or'AREA'):#如果选中的是光
            #bpy.context.scene.light_color != (0,0,0,1)不起作用
            if (bpy.context.scene.light_color[0]!=0 and bpy.context.scene.light_color[1]!=0 and bpy.context.scene.light_color[2]!=0):#如果指定了自定义光色
                for i in range(3):
                    bpy.context.object.data.color[i] = bpy.context.scene.light_color[i]
            else:
                if bpy.context.object.data.type == 'SUN':
                    i = bpy.context.scene.light_color_parallelpersets
                    if   i==1:
                        bpy.context.object.data.color = (0.75, 1, 0.65)#清晨
                    elif i==2:
                        bpy.context.object.data.color = (1, 0.8, 0.25)#中午
                    elif i==3:
                        bpy.context.object.data.color = (1, 0.3, 0.05)#黄昏
                    elif i==4:
                        bpy.context.object.data.color = (0.1, 0.25, 1)#夜晚
                elif bpy.context.object.data.type == 'POINT':
                    j = bpy.context.scene.light_color_pointpersets
                    if   j==1:
                        bpy.context.object.data.color = (1, 0.6, 0)#黄光，白炽灯
                    elif j==2:
                        bpy.context.object.data.color = (1, 1, 1)#白光
                    elif j==3:
                        bpy.context.object.data.color = (0, 0.1, 1)#蓝光
            
        #scene.color里面有个透明度预设，里面有4个数据，但是object.data.color里面只有3个数据
        return {"FINISHED"}

class Light_OT_BlueSky(bpy.types.Operator):
    bl_idname = "obj.bluesky"
    bl_label = "添加天光"
    bl_description = "天光是蓝天反射的光，也是平行光"

    def execute(self, context):
        bpy.ops.object.light_add(type='SUN', radius=1, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.object.name = "天光"
        bpy.context.object.data.color = (0.1, 0.4, 1)
        return {"FINISHED"}

class Light_OT_returnZero(bpy.types.Operator):
    bl_idname = "obj.lightcolorreturnzero"
    bl_label = "取消自定义"
    bl_description = "取消后才能使用光色预设"

    def execute(self, context):
        bpy.context.scene.light_color = (0, 0, 0, 1)
        return {"FINISHED"}


#光色预设
"""
class LIGHT_OT_pointLightColor1(bpy.types.Operator):
    bl_idname = "obj.pointlightcoloryellow"
    bl_label = "黄光"
    
    def execute(self, context):
        if(bpy.context.scene.light_color_persets==1):
            bpy.context.object.data.color = (1, 0.8, 0.5)
        return {"FINISHED"}
"""