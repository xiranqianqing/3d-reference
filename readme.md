# 使用说明书

3D辅助插件by夕染浅青

链接: https://pan.baidu.com/s/1lIiAf7tIyv4zZWHv1YQC2Q?pwd=ktaf 提取码: ktaf 

这是一个blender插件，功能是3D辅助，它需要同时安装cats插件by dtupper。

我使用这个插件的blender的版本为2.92，我试过的是，3.1版本也可以正常使用



适合用户：画画的

## 功能和命名

这个插件用于3D辅助作图，原理是**用blender渲染mmd模型**

PT是用户交互界面，OT是方法，

其中有大量中文描述

有以下模块：前期准备模块ready，灯光模块light，摄像机模块camera，动作模块pose（还在开发），二次元渲染模块animeRender（还在开发）。

方法在__ init __.py中的classes中有详细的解释。

```python
classes = [
    #属性类
    TDR_property,#特殊属性

    #UI类
    TDR_PT_Ready,
    TDR_PT_Light,
    TDR_PT_Camera,
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
    
    #二次元渲染类
]
```

可以随便改代码，使其更好用。



## 如何安装

下载安装blender

[Download — blender.org](https://www.blender.org/download/)

将解压后的文件夹（3D辅助）移动到这个文件夹里面

C:\Users\你的电脑用户名\AppData\Roaming\Blender Foundation\Blender\版本\scripts\addons



打开blender

点击左上角的：编辑-偏好设置

在界面-显示中勾选：使用工具提示

在插件中点击安装

<img src="C:\Users\夕染浅青\AppData\Roaming\Typora\typora-user-images\image-20220317144617434.png" alt="image-20220317144617434"  />

打开addons\3D辅助

点击init.py文件，安装插件



在插件列表中看见 Add Mesh: 3D辅助就说明安装成功了。



另外还需要安装cats插件

[Blender——安装MMD插件教程 - 哔哩哔哩 (bilibili.com)](https://www.bilibili.com/read/cv12680972/)

github上不去就直接用我文件夹里面的



## 如何使用

##### 导入模型和动作

![image-20220317151036106](C:\Users\夕染浅青\AppData\Roaming\Typora\typora-user-images\image-20220317151036106.png)

这样可以导入模型

点击模型后

（推荐修改动作方法）在侧边栏-MMD-Motion那里可以导入舞蹈动作

（其他方法一是用3D辅助里面的动作模式，二，在姿态Pose那里导入姿态，（自定义）三，点击骨骼-姿态模式-自己慢慢调）

物理Physics效果请在一开始没有任何动作的时候建立，如果不介意穿模也可以不建立

在绑定骨骼之后，通过在下面调节动画帧，就可以有不同动作了。

##### 调整光照

创建光照后，可以移动点光的位置和旋转平行光的角度

创建点光源，可以模拟蜡烛，灯泡，萤火虫，星星等自发光点光源，光色预设是黄光，白光和蓝光

创建平行光，可以模拟阳光，环境光（较弱），地面反光（较弱），光色预设是一天中早上，中午，下午，晚上的光色。

光源强度都可以调节，请注意：平行光光强远大于点光源

太阳光是从上往下照的

光源颜色都可以自定义，点击“改变光色”生效，如果觉得自定义效果不好，可以取消自定义后继续使用预设

天光是指蓝天的反光，如果是室外场景请添加天光。

##### 调整摄像机

可以创建多个摄像机进行比对，按小键盘的0转入摄像机视图

##### 二次元渲染

随后将继续开发二次元渲染模块

二次元渲染有以下特点：

明暗二分，勾边，脸部是平面的，很明显的光衰减



##### 其他：

随机粒子特效，随机飞行道具





调整好光照和摄像机之后，按f12进行渲染（渲染器有eevee和cycle，推荐使用前者，后者很卡而且会过于真实），保存图片后就能作为参考图使用，随便描图

![image-20220317154006214](C:\Users\夕染浅青\AppData\Roaming\Typora\typora-user-images\image-20220317154006214.png)

例子







