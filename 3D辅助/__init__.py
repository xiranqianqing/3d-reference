bl_info = {
    "name": "3D辅助",
    "author": "夕染浅青",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "借助MMD模型和blender渲染器以及Cats插件快速生产一个具有正确透视,结构,光影的参考图",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}


import bpy
#id名全部小写，类名按照blender类的命名规范

from .ui import TDR_PT_Ready,TDR_PT_Light,TDR_PT_Camera,TDR_PT_Other#,TDR_PT_Pose
from .operator.ready import READY_OT_bindBones,READY_OT_colorNormal
from .operator.light import LIGHT_OT_brighter,LIGHT_OT_createPoint,LIGHT_OT_darker,LIGHT_OT_createParallel,LIGHT_OT_parallelBrighter,LIGHT_OT_parallelDarker,LIGHT_OT_lightColorChange,Light_OT_returnZero,Light_OT_BlueSky
from .operator.camera import CAMERA_OT_createCamera,CAMERA_OT_latitudeLeft,CAMERA_OT_latitudeRight,CAMERA_OT_littleLatitudeRight,CAMERA_OT_littleLatitudeLeft,CAMERA_OT_cameraHeightUp,CAMERA_OT_cameraHeightDown,CAMERA_OT_distanceCloser,CAMERA_OT_distanceFarther
from .operator.other import OTHER_OT_shadow,OTHER_OT_floodlight,OTHER_OT_cameraOutOfFocus,OTHER_OT_flyingProps#,OTHER_OT_grainEffect


class TDR_property(bpy.types.PropertyGroup):
    bpy.types.Scene.light_color = bpy.props.FloatVectorProperty(name = "光色",description="光的颜色",   default=[0,0,0,1],    min=0.0,    max=1.0,    subtype='COLOR',    size=4)
    bpy.types.Scene.light_color_pointpersets = bpy.props.IntProperty(name = "点光色预设" ,description="1=黄光,2=白光,3=蓝光",            default=0,          min=0,      max=3)
    bpy.types.Scene.light_color_parallelpersets = bpy.props.IntProperty(name = "平行光色预设" ,description="1=清晨,2=中午,3=黄昏,4=夜晚" ,            default=0,          min=0,      max=4)
#特殊的属性
        

classes = [
    #属性类
    TDR_property,#特殊属性

    #UI类
    TDR_PT_Ready,
    TDR_PT_Light,
    TDR_PT_Camera,
    TDR_PT_Other,
    #TDR_PT_Pose,
    #TDR_PT_AnimeRender
    
    #准备工作类
    READY_OT_bindBones,#绑定骨骼
    READY_OT_colorNormal,#解决颜色变紫
                        #隐藏骨骼，我不会

    #光照类
    #点光
    LIGHT_OT_createPoint,
    LIGHT_OT_darker,
    LIGHT_OT_brighter,
    #平行光
    LIGHT_OT_createParallel,
    LIGHT_OT_parallelBrighter,
    LIGHT_OT_parallelDarker,
    LIGHT_OT_lightColorChange,#光色改变
    Light_OT_returnZero,#取消自定义光色
    Light_OT_BlueSky,#添加天光

    #摄像机类
    CAMERA_OT_createCamera,
    #水平角度变换
    CAMERA_OT_latitudeLeft,
    CAMERA_OT_latitudeRight,
    CAMERA_OT_littleLatitudeRight,
    CAMERA_OT_littleLatitudeLeft,
    #垂直角度变化
    CAMERA_OT_cameraHeightUp,
    CAMERA_OT_cameraHeightDown,
    #焦距变化
    CAMERA_OT_distanceCloser,
    CAMERA_OT_distanceFarther,
    
    #其他功能
    OTHER_OT_shadow,
    OTHER_OT_floodlight,
    OTHER_OT_cameraOutOfFocus,
    OTHER_OT_flyingProps,
    #OTHER_OT_grainEffect
]
#批量注册


def register():
    for clas in classes:
        bpy.utils.register_class(clas)
    print('register')


def unregister():
    for clas in classes:
        bpy.utils.unregister_class(clas)
    print('unregister')
#注册与注销


if __name__ == "__main__":
    register()
