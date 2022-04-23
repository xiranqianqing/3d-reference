import bpy
import math

global angle
global heightangle
global focal
radianConversion = 0.01745329

class CAMERA_OT_createCamera(bpy.types.Operator):
    bl_idname = "obj.createcamera"
    bl_label = "创建摄像机"
    bl_description = "完成后请在物体约束属性中添加指向目标"

    def execute(self, context):
        global angle
        global heightangle
        global focal
        focal = 100
        angle = -90
        heightangle = 0
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.object.location[1] = -50
        bpy.context.object.location[2] = 16#初始高度
        bpy.context.object.rotation_euler[0] = 1.5708
        bpy.context.object.rotation_euler[2] = 1.5708
        bpy.context.object.data.lens = focal

        #创建一个摄像机，模型通常是真实比例的10倍，所以初始高度为16m，初始距离为50m
        bpy.ops.object.constraint_add(type='TRACK_TO')
        #需要用户鼠标点击摄像机指定的物体
        return {"FINISHED"}

class CAMERA_OT_latitudeLeft(bpy.types.Operator):
    bl_idname = "obj.latitudeleft"
    bl_label = "摄像机角度右转"
    bl_description = "摄像机角度右转"

    def execute(self, context):
        global angle
        angle += 22.5
        bpy.context.object.location[0] = 50*math.cos(angle*radianConversion)
        bpy.context.object.location[1] = 50*math.sin(angle*radianConversion)
        return {"FINISHED"}

class CAMERA_OT_latitudeRight(bpy.types.Operator):
    bl_idname = "obj.latituderight"
    bl_label = "摄像机角度左转"
    bl_description = "摄像机角度左转"

    def execute(self, context):
        global angle
        angle -= 22.5
        bpy.context.object.location[0] = 50*math.cos(angle*radianConversion)
        bpy.context.object.location[1] = 50*math.sin(angle*radianConversion)
        return {"FINISHED"}

class CAMERA_OT_littleLatitudeRight(bpy.types.Operator):
    bl_idname = "obj.litlatituderight"
    bl_label = "摄像机小角度右转"
    bl_description = "摄像机小角度右转"

    def execute(self, context):
        global angle
        angle += 10
        bpy.context.object.location[0] = 50*math.cos(angle*radianConversion)
        bpy.context.object.location[1] = 50*math.sin(angle*radianConversion)
        return {"FINISHED"}

class CAMERA_OT_littleLatitudeLeft(bpy.types.Operator):
    bl_idname = "obj.litlatitudeleft"
    bl_label = "摄像机小角度左转"
    bl_description = "摄像机小角度左转"

    def execute(self, context):
        global angle
        angle -= 10
        bpy.context.object.location[0] = 50*math.cos(angle*radianConversion)
        bpy.context.object.location[1] = 50*math.sin(angle*radianConversion)
        return {"FINISHED"}

class CAMERA_OT_cameraHeightUp(bpy.types.Operator):
    bl_idname = "obj.cameraheightup"
    bl_label = "摄像机抬高"
    bl_description = "摄像机抬高"

    def execute(self, context):
        global heightangle
        if heightangle<80:
            heightangle += 10
            bpy.context.object.location[2] = 16 + 50*math.tan(heightangle*radianConversion)
            if (abs(heightangle * 6) >3):
                bpy.context.object.data.lens = abs(heightangle * 6)
            else:
                bpy.context.object.data.lens = 50
        else:
            print('太高了')
        return {"FINISHED"}
        
class CAMERA_OT_cameraHeightDown(bpy.types.Operator):
    bl_idname = "obj.cameraheightdown"
    bl_label = "摄像机降低"
    bl_description = "摄像机降低"

    def execute(self, context):
        global heightangle
        if heightangle>-80:
            heightangle -= 10
            bpy.context.object.location[2] = 16 + 50*math.tan(heightangle*radianConversion)
            if (abs(heightangle * 6) >3):
                bpy.context.object.data.lens = abs(heightangle * 6)
            else:
                bpy.context.object.data.lens = 50
        else:
            print('太低了')
        return {"FINISHED"}

class CAMERA_OT_distanceCloser(bpy.types.Operator):
    bl_idname = "obj.distancecloser"
    bl_label = "摄像机接近"
    bl_description = "摄像机接近"

    def execute(self, context):
        global focal
        if(focal<500):
            focal += 20
            bpy.context.object.data.lens = focal
        return {"FINISHED"}

class CAMERA_OT_distanceFarther(bpy.types.Operator):
    bl_idname = "obj.distancefarther"
    bl_label = "摄像机远离"
    bl_description = "摄像机远离"

    def execute(self, context):
        global focal
        if(focal>20):
            focal -= 20
            bpy.context.object.data.lens = focal
        return {"FINISHED"}

#



