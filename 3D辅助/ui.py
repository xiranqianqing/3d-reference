from pydoc import describe
import bpy

class TDR_Panel_Base(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "3D辅助"
    bl_context = "objectmode"
    #总UI类

    def draw(self, context):
        layout = self.layout
    #Panel好像一定要有这个attribute

class TDR_PT_Ready(TDR_Panel_Base):
    
    bl_idname = "TDR_PT_Ready"
    bl_label = "准备工作"

    def draw(self, context):
        layout = self.layout
        layout.operator("obj.bindbones",text="绑定骨骼",icon="CONSTRAINT")
        layout.operator("obj.colornormal",text="颜色正常",icon="CONSTRAINT")
    #准备工作UI类


class TDR_PT_Light(TDR_Panel_Base):
    bl_idname = "TDR_PT_Light"
    bl_label = "光影调整"

    def draw(self, context):
        layout = self.layout
        layout.label(text="请先切换至渲染视图",icon="OUTLINER_OB_LIGHT")


        layout.operator("obj.createpointlight",text="创建点光源",icon="LIGHT_POINT")
        row = layout.row()
        row.operator("obj.pointlightbrighter",text="点光源变亮")
        row.operator("obj.pointlightdarker",text="点光源变暗")
        #点光源光色预设
        row = layout.row()
        row.prop(context.scene,'light_color_pointpersets')


        layout.operator("obj.createparallellight",text="创建平行光",icon="LIGHT_SUN")
        row = layout.row()
        row.operator("obj.parallellightbrighter",text="平行光变亮")
        row.operator("obj.parallellightdarker",text="平行光变暗")
        #平行光光色预设
        
        layout.prop(context.scene,'light_color_parallelpersets')
        layout.operator("obj.bluesky",text = "添加天光")

        #光色自定义
        col = layout.column()
        layout.label(text="光色自定义",icon="OUTLINER_OB_LIGHT")
        layout.prop(context.scene, 'light_color')
        row = layout.row()
        row.operator("obj.lightcolorchange",text = "改变光色")
        row.operator("obj.lightcolorreturnzero",text = "取消自定义")
        



        #光影调整UI类
    

class TDR_PT_Camera(TDR_Panel_Base):
    bl_idname = "TDR_PT_Camera"
    bl_label = "摄像机调整"
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="调整选中的摄像机",icon="CAMERA_DATA")

        layout.operator("obj.createcamera",text = "创建摄像机")

        layout.label(text="角度调整")
        row = layout.row()
        row.operator("obj.latituderight",text="角度右转")
        row.operator("obj.latitudeleft",text="角度左转")
        row = layout.row()
        row.operator("obj.litlatituderight",text="角度小右转")
        row.operator("obj.litlatitudeleft",text="角度小左转")
        
        layout.label(text="相机高度调整")
        layout.operator("obj.cameraheightup",text="抬升相机高度")
        layout.operator("obj.cameraheightdown",text="降低相机高度")

        layout.label(text="距离调整")
        layout.operator("obj.distancecloser",text="缩短距离")
        layout.operator("obj.distancefarther",text="增长距离")
        #并非真的在调整距离，而是在调整相机焦距
        #摄像机调整UI类


class TDR_PT_Other(TDR_Panel_Base):
    bl_idname = "TDR_PT_Other"
    bl_label = "其他功能"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator("obj.shadow",text="阴影优化")
        col.operator("obj.floodlight",text="辉光")
        col.operator("obj.cameraoutoffocus",text="相机失焦")
        layout.label(text="请设置物体数据属性-景深-聚焦到物体")
        col = layout.column()
        col.operator("obj.flyingprops",text="随机空中球")
        #col.operator("obj.graineffect",text="萤火虫")
        
        

