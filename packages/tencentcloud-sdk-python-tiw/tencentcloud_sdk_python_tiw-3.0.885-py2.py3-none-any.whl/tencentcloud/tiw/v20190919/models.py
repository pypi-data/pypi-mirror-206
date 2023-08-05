# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class ApplicationItem(AbstractModel):
    """白板应用

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用SdkAppId
        :type SdkAppId: int
        :param AppName: 应用名
        :type AppName: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param TagList: 标签列表
        :type TagList: list of Tag
        """
        self.SdkAppId = None
        self.AppName = None
        self.CreateTime = None
        self.TagList = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.AppName = params.get("AppName")
        self.CreateTime = params.get("CreateTime")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyTiwTrialRequest(AbstractModel):
    """ApplyTiwTrial请求参数结构体

    """


class ApplyTiwTrialResponse(AbstractModel):
    """ApplyTiwTrial返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AuthParam(AbstractModel):
    """鉴权参数

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用SdkAppId
        :type SdkAppId: int
        :param UserId: 用户ID
        :type UserId: str
        :param UserSig: 用户ID对应的签名
        :type UserSig: str
        """
        self.SdkAppId = None
        self.UserId = None
        self.UserSig = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.UserId = params.get("UserId")
        self.UserSig = params.get("UserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Canvas(AbstractModel):
    """混流画布参数

    """

    def __init__(self):
        r"""
        :param LayoutParams: 混流画布宽高配置
        :type LayoutParams: :class:`tencentcloud.tiw.v20190919.models.LayoutParams`
        :param BackgroundColor: 背景颜色，默认为黑色，格式为RGB格式，如红色为"#FF0000"
        :type BackgroundColor: str
        """
        self.LayoutParams = None
        self.BackgroundColor = None


    def _deserialize(self, params):
        if params.get("LayoutParams") is not None:
            self.LayoutParams = LayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        self.BackgroundColor = params.get("BackgroundColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Concat(AbstractModel):
    """实时录制视频拼接参数

    """

    def __init__(self):
        r"""
        :param Enabled: 是否开启拼接功能
在开启了视频拼接功能的情况下，实时录制服务会把同一个用户因为暂停导致的多段视频拼接成一个视频
        :type Enabled: bool
        :param Image: 视频拼接时使用的垫片图片下载地址，不填默认用全黑的图片进行视频垫片
        :type Image: str
        """
        self.Enabled = None
        self.Image = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationRequest(AbstractModel):
    """CreateApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用SdkAppId
        :type SdkAppId: int
        :param AppName: App名字
        :type AppName: str
        :param SKey: 创建IM应用需要的SKey
        :type SKey: str
        :param TinyId: 创建IM应用需要的TinyId
        :type TinyId: str
        :param TagList: 需要绑定的标签列表
        :type TagList: list of Tag
        """
        self.SdkAppId = None
        self.AppName = None
        self.SKey = None
        self.TinyId = None
        self.TagList = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.AppName = params.get("AppName")
        self.SKey = params.get("SKey")
        self.TinyId = params.get("TinyId")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationResponse(AbstractModel):
    """CreateApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param AppId: 客户的AppId
        :type AppId: int
        :param AppName: App名字
        :type AppName: str
        :param SdkAppId: 应用SdkAppId
        :type SdkAppId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppId = None
        self.AppName = None
        self.SdkAppId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.AppName = params.get("AppName")
        self.SdkAppId = params.get("SdkAppId")
        self.RequestId = params.get("RequestId")


class CreateOfflineRecordRequest(AbstractModel):
    """CreateOfflineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param RoomId: 录制任务对应的房间号
        :type RoomId: int
        :param GroupId: 录制任务对应的群组Id
        :type GroupId: str
        :param MixStream: 混流参数配置
目前课后录制暂未支持自定义混流布局Custom参数
        :type MixStream: :class:`tencentcloud.tiw.v20190919.models.MixStream`
        :param Whiteboard: 白板参数配置
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        """
        self.SdkAppId = None
        self.RoomId = None
        self.GroupId = None
        self.MixStream = None
        self.Whiteboard = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.GroupId = params.get("GroupId")
        if params.get("MixStream") is not None:
            self.MixStream = MixStream()
            self.MixStream._deserialize(params.get("MixStream"))
        if params.get("Whiteboard") is not None:
            self.Whiteboard = Whiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOfflineRecordResponse(AbstractModel):
    """CreateOfflineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePPTCheckTaskRequest(AbstractModel):
    """CreatePPTCheckTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Url: 经过URL编码后的PPT文件地址。URL 编码会将字符转换为可通过因特网传输的格式，例如文档地址为http://example.com/测试.pptx，经过URL编码之后为http://example.com/%E6%B5%8B%E8%AF%95.pptx。为了提高URL解析的成功率，请对URL进行编码。
        :type Url: str
        :param AutoHandleUnsupportedElement: 是否对不支持元素开启自动处理的功能。默认不开启。

在开启自动处理的情况下，会自动进行如下处理：
1. 墨迹：移除不支持的墨迹（比如使用WPS画的）
2. 自动翻页：移除PPT上所有的自动翻页设置，并设置为单击鼠标翻页
3. 已损坏音视频：移除PPT上对损坏音视频的引用
        :type AutoHandleUnsupportedElement: bool
        """
        self.SdkAppId = None
        self.Url = None
        self.AutoHandleUnsupportedElement = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Url = params.get("Url")
        self.AutoHandleUnsupportedElement = params.get("AutoHandleUnsupportedElement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePPTCheckTaskResponse(AbstractModel):
    """CreatePPTCheckTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 检测任务的唯一标识Id，用于查询该任务的进度以及检测结果
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateSnapshotTaskRequest(AbstractModel):
    """CreateSnapshotTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param Whiteboard: 白板相关参数
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.SnapshotWhiteboard`
        :param SdkAppId: 白板房间 `SdkAppId`
        :type SdkAppId: int
        :param RoomId: 白板房间号
        :type RoomId: int
        :param CallbackURL: 白板板书生成结果通知回调地址
        :type CallbackURL: str
        :param COS: 白板板书文件 `COS` 存储参数， 不填默认存储在公共存储桶，公共存储桶的数据仅保存3天
        :type COS: :class:`tencentcloud.tiw.v20190919.models.SnapshotCOS`
        :param SnapshotMode: 白板板书生成模式，默认为 `AllMarks`。取值说明如下：

`AllMarks` - 全量模式，即对于客户端每一次调用 `addSnapshotMark` 接口打上的白板板书生成标志全部都会生成对应的白板板书图片。

`LatestMarksOnly` - 单页去重模式，即对于客户端在同一页白板上多次调用 `addSnapshotMark` 打上的白板板书生成标志仅保留最新一次标志来生成对应白板页的白板板书图片。

（**注意：`LatestMarksOnly` 模式只有客户端使用v2.6.8及以上版本的白板SDK调用 `addSnapshotMark` 时才生效，否则即使在调用本API是指定了 `LatestMarksOnly` 模式，服务后台会使用默认的 `AllMarks` 模式生成白板板书**）
        :type SnapshotMode: str
        """
        self.Whiteboard = None
        self.SdkAppId = None
        self.RoomId = None
        self.CallbackURL = None
        self.COS = None
        self.SnapshotMode = None


    def _deserialize(self, params):
        if params.get("Whiteboard") is not None:
            self.Whiteboard = SnapshotWhiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.CallbackURL = params.get("CallbackURL")
        if params.get("COS") is not None:
            self.COS = SnapshotCOS()
            self.COS._deserialize(params.get("COS"))
        self.SnapshotMode = params.get("SnapshotMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotTaskResponse(AbstractModel):
    """CreateSnapshotTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 白板板书生成任务ID，只有任务创建成功的时候才会返回此字段
        :type TaskID: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.RequestId = params.get("RequestId")


class CreateTranscodeRequest(AbstractModel):
    """CreateTranscode请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Url: 经过URL编码后的转码文件地址。URL 编码会将字符转换为可通过因特网传输的格式，比如文档地址为http://example.com/测试.pdf，经过URL编码之后为http://example.com/%E6%B5%8B%E8%AF%95.pdf。为了提高URL解析的成功率，请对URL进行编码。
        :type Url: str
        :param IsStaticPPT: 是否为静态PPT，默认为False；
如果IsStaticPPT为False，后缀名为.ppt或.pptx的文档会动态转码成HTML5页面，其他格式的文档会静态转码成图片；如果IsStaticPPT为True，所有格式的文档会静态转码成图片；
        :type IsStaticPPT: bool
        :param MinResolution: 注意: 该参数已废弃, 请使用最新的 [云API SDK](https://cloud.tencent.com/document/api/1137/40060#SDK) ，使用 MinScaleResolution字段传递分辨率

转码后文档的最小分辨率，不传、传空字符串或分辨率格式错误则使用文档原分辨率

示例：1280x720，注意分辨率宽高中间为英文字母"xyz"的"x"
        :type MinResolution: str
        :param ThumbnailResolution: 动态PPT转码可以为文件生成该分辨率的缩略图，不传、传空字符串或分辨率格式错误则不生成缩略图，分辨率格式同MinResolution
        :type ThumbnailResolution: str
        :param CompressFileType: 转码文件压缩格式，不传、传空字符串或不是指定的格式则不生成压缩文件，目前支持如下压缩格式：

zip： 生成`.zip`压缩包
tar.gz： 生成`.tar.gz`压缩包
        :type CompressFileType: str
        :param ExtraData: 内部参数
        :type ExtraData: str
        :param Priority: 文档转码优先级， 只有对于PPT动态转码生效，支持填入以下值：<br/>
- low: 低优先级转码，对于动态转码，能支持500MB（下载超时时间10分钟）以及2000页文档，但资源有限可能会有比较长时间的排队，请酌情使用该功能。<br/>
- 不填表示正常优先级转码，支持200MB文件（下载超时时间2分钟），500页以内的文档进行转码
<br/>
注意：对于PDF等静态文件转码，无论是正常优先级或者低优先级，最大只能支持200MB
        :type Priority: str
        :param MinScaleResolution: 转码后文档的最小分辨率，不传、传空字符串或分辨率格式错误则使用文档原分辨率。
分辨率越高，效果越清晰，转出来的图片资源体积会越大，课件加载耗时会变长，请根据实际使用场景配置此参数。

示例：1280x720，注意分辨率宽高中间为英文字母"xyz"的"x"
        :type MinScaleResolution: str
        :param AutoHandleUnsupportedElement: 是否对不支持元素开启自动处理的功能。默认不开启。

在开启自动处理的情况下，会自动进行如下处理：
1. 墨迹：移除不支持的墨迹（比如使用WPS画的）
2. 自动翻页：移除PPT上所有的自动翻页设置，并设置为单击鼠标翻页
3. 已损坏音视频：移除PPT上对损坏音视频的引用
        :type AutoHandleUnsupportedElement: bool
        """
        self.SdkAppId = None
        self.Url = None
        self.IsStaticPPT = None
        self.MinResolution = None
        self.ThumbnailResolution = None
        self.CompressFileType = None
        self.ExtraData = None
        self.Priority = None
        self.MinScaleResolution = None
        self.AutoHandleUnsupportedElement = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Url = params.get("Url")
        self.IsStaticPPT = params.get("IsStaticPPT")
        self.MinResolution = params.get("MinResolution")
        self.ThumbnailResolution = params.get("ThumbnailResolution")
        self.CompressFileType = params.get("CompressFileType")
        self.ExtraData = params.get("ExtraData")
        self.Priority = params.get("Priority")
        self.MinScaleResolution = params.get("MinScaleResolution")
        self.AutoHandleUnsupportedElement = params.get("AutoHandleUnsupportedElement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTranscodeResponse(AbstractModel):
    """CreateTranscode返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 文档转码任务的唯一标识Id，用于查询该任务的进度以及转码结果
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateVideoGenerationTaskRequest(AbstractModel):
    """CreateVideoGenerationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param OnlineRecordTaskId: 录制任务的TaskId
        :type OnlineRecordTaskId: str
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Whiteboard: 视频生成的白板参数，例如白板宽高等。

此参数与开始录制接口提供的Whiteboard参数互斥，在本接口与开始录制接口都提供了Whiteboard参数时，优先使用本接口指定的Whiteboard参数进行视频生成，否则使用开始录制接口提供的Whiteboard参数进行视频生成。
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param Concat: 视频拼接参数

此参数与开始录制接口提供的Concat参数互斥，在本接口与开始录制接口都提供了Concat参数时，优先使用本接口指定的Concat参数进行视频拼接，否则使用开始录制接口提供的Concat参数进行视频拼接。
        :type Concat: :class:`tencentcloud.tiw.v20190919.models.Concat`
        :param MixStream: 视频生成混流参数

此参数与开始录制接口提供的MixStream参数互斥，在本接口与开始录制接口都提供了MixStream参数时，优先使用本接口指定的MixStream参数进行视频混流，否则使用开始录制接口提供的MixStream参数进行视频拼混流。
        :type MixStream: :class:`tencentcloud.tiw.v20190919.models.MixStream`
        :param RecordControl: 视频生成控制参数，用于更精细地指定需要生成哪些流，某一路流是否禁用音频，是否只录制小画面等

此参数与开始录制接口提供的RecordControl参数互斥，在本接口与开始录制接口都提供了RecordControl参数时，优先使用本接口指定的RecordControl参数进行视频生成控制，否则使用开始录制接口提供的RecordControl参数进行视频拼生成控制。
        :type RecordControl: :class:`tencentcloud.tiw.v20190919.models.RecordControl`
        :param ExtraData: 内部参数
        :type ExtraData: str
        """
        self.OnlineRecordTaskId = None
        self.SdkAppId = None
        self.Whiteboard = None
        self.Concat = None
        self.MixStream = None
        self.RecordControl = None
        self.ExtraData = None


    def _deserialize(self, params):
        self.OnlineRecordTaskId = params.get("OnlineRecordTaskId")
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Whiteboard") is not None:
            self.Whiteboard = Whiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        if params.get("Concat") is not None:
            self.Concat = Concat()
            self.Concat._deserialize(params.get("Concat"))
        if params.get("MixStream") is not None:
            self.MixStream = MixStream()
            self.MixStream._deserialize(params.get("MixStream"))
        if params.get("RecordControl") is not None:
            self.RecordControl = RecordControl()
            self.RecordControl._deserialize(params.get("RecordControl"))
        self.ExtraData = params.get("ExtraData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoGenerationTaskResponse(AbstractModel):
    """CreateVideoGenerationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 视频生成的任务Id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CustomLayout(AbstractModel):
    """自定义混流布局参数

    """

    def __init__(self):
        r"""
        :param Canvas: 混流画布参数
        :type Canvas: :class:`tencentcloud.tiw.v20190919.models.Canvas`
        :param InputStreamList: 流布局参数，每路流的布局不能超出画布区域
        :type InputStreamList: list of StreamLayout
        """
        self.Canvas = None
        self.InputStreamList = None


    def _deserialize(self, params):
        if params.get("Canvas") is not None:
            self.Canvas = Canvas()
            self.Canvas._deserialize(params.get("Canvas"))
        if params.get("InputStreamList") is not None:
            self.InputStreamList = []
            for item in params.get("InputStreamList"):
                obj = StreamLayout()
                obj._deserialize(item)
                self.InputStreamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataItem(AbstractModel):
    """画图数据，Time/Value/Details

    """

    def __init__(self):
        r"""
        :param Time: 时间
按月格式yyyy-mm
按天格式yyyy-mm-dd
按分钟格式 yyyy-mm-dd HH:MM:SS
        :type Time: str
        :param Value: 画图所需要的值
        :type Value: int
        :param Details: 各个具体指标的详情
        :type Details: list of Detail
        """
        self.Time = None
        self.Value = None
        self.Details = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = Detail()
                obj._deserialize(item)
                self.Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIServiceRequest(AbstractModel):
    """DescribeAPIService请求参数结构体

    """

    def __init__(self):
        r"""
        :param Service: 目前支持的Service为cos:GetService，cdn:DescribeDomainsConfig
        :type Service: str
        :param Data: JSON格式的请求参数
        :type Data: str
        """
        self.Service = None
        self.Data = None


    def _deserialize(self, params):
        self.Service = params.get("Service")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIServiceResponse(AbstractModel):
    """DescribeAPIService返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResponseData: Json格式的响应数据
        :type ResponseData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResponseData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResponseData = params.get("ResponseData")
        self.RequestId = params.get("RequestId")


class DescribeApplicationInfosRequest(AbstractModel):
    """DescribeApplicationInfos请求参数结构体

    """


class DescribeApplicationInfosResponse(AbstractModel):
    """DescribeApplicationInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationInfos: 应用列表
        :type ApplicationInfos: list of ApplicationItem
        :param AllOption: 是否包含所有的应用，0-不包含，1-包含
        :type AllOption: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplicationInfos = None
        self.AllOption = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ApplicationInfos") is not None:
            self.ApplicationInfos = []
            for item in params.get("ApplicationInfos"):
                obj = ApplicationItem()
                obj._deserialize(item)
                self.ApplicationInfos.append(obj)
        self.AllOption = params.get("AllOption")
        self.RequestId = params.get("RequestId")


class DescribeApplicationUsageRequest(AbstractModel):
    """DescribeApplicationUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param BeginTime: 用量开始时间（包括该时间点）
        :type BeginTime: str
        :param EndTime: 用量结束时间（不包括该时间点）
        :type EndTime: str
        :param SubProduct: 白板子产品名
        :type SubProduct: str
        :param TimeLevel: 时间跨度单位
- MONTHLY：月
- DAILY：天
- MINUTELY：分钟
        :type TimeLevel: str
        :param SdkAppId: 白板应用的SdkAppId
        :type SdkAppId: int
        :param IsWeighted: true: 返回加权求和后的用量数据
false: 返回原始用量数据
        :type IsWeighted: bool
        """
        self.BeginTime = None
        self.EndTime = None
        self.SubProduct = None
        self.TimeLevel = None
        self.SdkAppId = None
        self.IsWeighted = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.SubProduct = params.get("SubProduct")
        self.TimeLevel = params.get("TimeLevel")
        self.SdkAppId = params.get("SdkAppId")
        self.IsWeighted = params.get("IsWeighted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationUsageResponse(AbstractModel):
    """DescribeApplicationUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 画图所需的用量数据
        :type Data: list of DataItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBoardSDKLogRequest(AbstractModel):
    """DescribeBoardSDKLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 白板应用的SdkAppId
        :type SdkAppId: int
        :param RoomId: 需要查询日志的白板房间号
        :type RoomId: str
        :param UserId: 需要查询日志的用户ID
        :type UserId: str
        :param TimeRange: 查询时间段，Unix时间戳，单位毫秒，第一个值为开始时间戳，第二个值为结束时间
        :type TimeRange: list of int
        :param AggregationInterval: 聚合日志条数查询的桶的时间范围，如5m, 1h, 4h等
        :type AggregationInterval: str
        :param Query: 额外的查询条件
        :type Query: str
        :param Ascending: 是否按时间升序排列
        :type Ascending: bool
        :param Context: 用于递归拉取的上下文Key，在上一次请求中返回
        :type Context: str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserId = None
        self.TimeRange = None
        self.AggregationInterval = None
        self.Query = None
        self.Ascending = None
        self.Context = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserId = params.get("UserId")
        self.TimeRange = params.get("TimeRange")
        self.AggregationInterval = params.get("AggregationInterval")
        self.Query = params.get("Query")
        self.Ascending = params.get("Ascending")
        self.Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBoardSDKLogResponse(AbstractModel):
    """DescribeBoardSDKLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总共能查到日志条数
        :type Total: int
        :param Sources: 日志详细内容
        :type Sources: list of str
        :param Buckets: 按时间段聚合后每个时间段的日志条数
        :type Buckets: list of str
        :param Context: 用于递归拉取的上下文Key，下一次请求的时候带上
        :type Context: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Sources = None
        self.Buckets = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Sources = params.get("Sources")
        self.Buckets = params.get("Buckets")
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")


class DescribeIMApplicationsRequest(AbstractModel):
    """DescribeIMApplications请求参数结构体

    """


class DescribeIMApplicationsResponse(AbstractModel):
    """DescribeIMApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeOfflineRecordCallbackRequest(AbstractModel):
    """DescribeOfflineRecordCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfflineRecordCallbackResponse(AbstractModel):
    """DescribeOfflineRecordCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeOfflineRecordRequest(AbstractModel):
    """DescribeOfflineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 课后录制任务的Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfflineRecordResponse(AbstractModel):
    """DescribeOfflineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeOnlineRecordCallbackRequest(AbstractModel):
    """DescribeOnlineRecordCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOnlineRecordCallbackResponse(AbstractModel):
    """DescribeOnlineRecordCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param Callback: 实时录制事件回调地址，如果未设置回调地址，该字段为空字符串
        :type Callback: str
        :param CallbackKey: 实时录制回调鉴权密钥
        :type CallbackKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Callback = None
        self.CallbackKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        self.RequestId = params.get("RequestId")


class DescribeOnlineRecordRequest(AbstractModel):
    """DescribeOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 实时录制任务Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOnlineRecordResponse(AbstractModel):
    """DescribeOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param FinishReason: 录制结束原因，
- AUTO: 房间内长时间没有音视频上行及白板操作导致自动停止录制
- USER_CALL: 主动调用了停止录制接口
- EXCEPTION: 录制异常结束
- FORCE_STOP: 强制停止录制，一般是因为暂停超过90分钟或者录制总时长超过24小时。
        :type FinishReason: str
        :param TaskId: 需要查询结果的录制任务Id
        :type TaskId: str
        :param Status: 录制任务状态
- PREPARED: 表示录制正在准备中（进房/启动录制服务等操作）
- RECORDING: 表示录制已开始
- PAUSED: 表示录制已暂停
- STOPPED: 表示录制已停止，正在处理并上传视频
- FINISHED: 表示视频处理并上传完成，成功生成录制结果
        :type Status: str
        :param RoomId: 房间号
        :type RoomId: int
        :param GroupId: 白板的群组 Id
        :type GroupId: str
        :param RecordUserId: 录制用户Id
        :type RecordUserId: str
        :param RecordStartTime: 实际开始录制时间，Unix 时间戳，单位秒
        :type RecordStartTime: int
        :param RecordStopTime: 实际停止录制时间，Unix 时间戳，单位秒
        :type RecordStopTime: int
        :param TotalTime: 回放视频总时长（单位：毫秒）
        :type TotalTime: int
        :param ExceptionCnt: 录制过程中出现异常的次数
        :type ExceptionCnt: int
        :param OmittedDurations: 拼接视频中被忽略的时间段，只有开启视频拼接功能的时候，这个参数才是有效的
        :type OmittedDurations: list of OmittedDuration
        :param VideoInfos: 录制视频列表
        :type VideoInfos: list of VideoInfo
        :param ReplayUrl: 回放URL，需配合信令播放器使用。此字段仅适用于`视频生成模式`
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplayUrl: str
        :param Interrupts: 视频流在录制过程中断流次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Interrupts: list of Interrupt
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FinishReason = None
        self.TaskId = None
        self.Status = None
        self.RoomId = None
        self.GroupId = None
        self.RecordUserId = None
        self.RecordStartTime = None
        self.RecordStopTime = None
        self.TotalTime = None
        self.ExceptionCnt = None
        self.OmittedDurations = None
        self.VideoInfos = None
        self.ReplayUrl = None
        self.Interrupts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FinishReason = params.get("FinishReason")
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.RoomId = params.get("RoomId")
        self.GroupId = params.get("GroupId")
        self.RecordUserId = params.get("RecordUserId")
        self.RecordStartTime = params.get("RecordStartTime")
        self.RecordStopTime = params.get("RecordStopTime")
        self.TotalTime = params.get("TotalTime")
        self.ExceptionCnt = params.get("ExceptionCnt")
        if params.get("OmittedDurations") is not None:
            self.OmittedDurations = []
            for item in params.get("OmittedDurations"):
                obj = OmittedDuration()
                obj._deserialize(item)
                self.OmittedDurations.append(obj)
        if params.get("VideoInfos") is not None:
            self.VideoInfos = []
            for item in params.get("VideoInfos"):
                obj = VideoInfo()
                obj._deserialize(item)
                self.VideoInfos.append(obj)
        self.ReplayUrl = params.get("ReplayUrl")
        if params.get("Interrupts") is not None:
            self.Interrupts = []
            for item in params.get("Interrupts"):
                obj = Interrupt()
                obj._deserialize(item)
                self.Interrupts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePPTCheckCallbackRequest(AbstractModel):
    """DescribePPTCheckCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePPTCheckCallbackResponse(AbstractModel):
    """DescribePPTCheckCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param Callback: 回调地址
        :type Callback: str
        :param CallbackKey: 回调鉴权密钥
        :type CallbackKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Callback = None
        self.CallbackKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        self.RequestId = params.get("RequestId")


class DescribePPTCheckRequest(AbstractModel):
    """DescribePPTCheck请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 任务的唯一标识Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePPTCheckResponse(AbstractModel):
    """DescribePPTCheck返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务的唯一标识Id
        :type TaskId: str
        :param IsOK: PPT文件是否正常
        :type IsOK: bool
        :param ResultUrl: 修复后的PPT URL，只有创建任务时参数AutoHandleUnsupportedElement=true，才返回此参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultUrl: str
        :param Slides: 错误PPT页面列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Slides: list of PPTErrSlide
        :param Status: 任务的当前状态 - QUEUED: 正在排队等待 - PROCESSING: 执行中 - FINISHED: 执行完成	
        :type Status: str
        :param Progress: 当前进度,取值范围为0~100
        :type Progress: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.IsOK = None
        self.ResultUrl = None
        self.Slides = None
        self.Status = None
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.IsOK = params.get("IsOK")
        self.ResultUrl = params.get("ResultUrl")
        if params.get("Slides") is not None:
            self.Slides = []
            for item in params.get("Slides"):
                obj = PPTErrSlide()
                obj._deserialize(item)
                self.Slides.append(obj)
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DescribePostpaidUsageRequest(AbstractModel):
    """DescribePostpaidUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param BeginTime: 开始时间
        :type BeginTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePostpaidUsageResponse(AbstractModel):
    """DescribePostpaidUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeQualityMetricsRequest(AbstractModel):
    """DescribeQualityMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 白板应用的SdkAppId
        :type SdkAppId: int
        :param StartTime: 开始时间，Unix时间戳，单位秒，时间跨度不能超过7天
        :type StartTime: int
        :param EndTime: 结束时间，Unix时间戳，单位秒，时间跨度不能超过7天
        :type EndTime: int
        :param Metric: 查询的指标，目前支持以下值
  - image_load_total_count: 图片加载总数（单位，次）
  - image_load_fail_count: 图片加载失败数量（单位，次）
  - image_load_success_rate: 图片加载成功率（百分比）
  - ppt_load_total_count: PPT加载总数（单位，次）
  - ppt_load_fail_count: PPT加载失败总数（单位，次）
  - ppt_load_success_rate: PPT加载成功率（单位，百分比）
  - verify_sdk_total_count: 白板鉴权总次数（单位，次）
  - verify_sdk_fail_count: 白板鉴权失败次数（单位，次）
  - verify_sdk_success_rate: 白板鉴权成功率（单位，百分比）
  - verify_sdk_in_one_second_rate: 白板鉴权秒开率（单位，百分比）
  - verify_sdk_cost_avg: 白板鉴权耗时平均时间（单位，毫秒）
        :type Metric: str
        :param Interval: 聚合的时间维度，目前只支持1小时，输入值为"1h"
        :type Interval: str
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Interval = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQualityMetricsResponse(AbstractModel):
    """DescribeQualityMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Metric: 输入的查询指标
        :type Metric: str
        :param Content: 时间序列
        :type Content: list of TimeValue
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Metric = None
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRecordSearchRequest(AbstractModel):
    """DescribeRecordSearch请求参数结构体

    """


class DescribeRecordSearchResponse(AbstractModel):
    """DescribeRecordSearch返回参数结构体

    """

    def __init__(self):
        r"""
        :param RecordTaskSet: 录制任务搜索结果集合
        :type RecordTaskSet: list of RecordTaskSearchResult
        :param TotalCount: 录制总任务数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordTaskSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RecordTaskSet") is not None:
            self.RecordTaskSet = []
            for item in params.get("RecordTaskSet"):
                obj = RecordTaskSearchResult()
                obj._deserialize(item)
                self.RecordTaskSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRoomListRequest(AbstractModel):
    """DescribeRoomList请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 白板应用的SdkAppId
        :type SdkAppId: int
        :param TimeRange: 查询时间段，Unix时间戳，单位毫秒，第一个值为开始时间戳，第二个值为结束时间
        :type TimeRange: list of int
        :param Query: 额外的查询条件
        :type Query: str
        :param MaxSize: 返回最大的数据条数，默认1000
        :type MaxSize: int
        """
        self.SdkAppId = None
        self.TimeRange = None
        self.Query = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TimeRange = params.get("TimeRange")
        self.Query = params.get("Query")
        self.MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomListResponse(AbstractModel):
    """DescribeRoomList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RoomList: 白板房间列表
        :type RoomList: list of RoomListItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RoomList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RoomList") is not None:
            self.RoomList = []
            for item in params.get("RoomList"):
                obj = RoomListItem()
                obj._deserialize(item)
                self.RoomList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRunningTasksRequest(AbstractModel):
    """DescribeRunningTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppID: 应用的SdkAppID
        :type SdkAppID: int
        :param TaskType: 指定需要获取的任务类型。
有效取值如下：
- TranscodeH5: 动态转码任务，文档转HTML5页面
- TranscodeJPG: 静态转码任务，文档转图片
- WhiteboardPush: 白板推流任务
- OnlineRecord: 实时录制任务
        :type TaskType: str
        :param Offset: 分页获取时的任务偏移量，默认为0。
        :type Offset: int
        :param Limit: 每次获取任务列表时最大获取任务数，默认值为100。
有效取值范围：[1, 500]
        :type Limit: int
        """
        self.SdkAppID = None
        self.TaskType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SdkAppID = params.get("SdkAppID")
        self.TaskType = params.get("TaskType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRunningTasksResponse(AbstractModel):
    """DescribeRunningTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 当前正在执行中的任务总数
        :type Total: int
        :param Tasks: 任务信息列表
        :type Tasks: list of RunningTaskItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = RunningTaskItem()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotTaskRequest(AbstractModel):
    """DescribeSnapshotTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 查询任务ID
        :type TaskID: str
        :param SdkAppId: 任务SdkAppId
        :type SdkAppId: int
        """
        self.TaskID = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotTaskResponse(AbstractModel):
    """DescribeSnapshotTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskID: str
        :param Status: 任务状态
Running - 任务执行中
Finished - 任务已结束
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param CreateTime: 任务创建时间，单位s
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param FinishTime: 任务完成时间，单位s
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishTime: int
        :param Result: 任务结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tiw.v20190919.models.SnapshotResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskID = None
        self.Status = None
        self.CreateTime = None
        self.FinishTime = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.FinishTime = params.get("FinishTime")
        if params.get("Result") is not None:
            self.Result = SnapshotResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTIWDailyUsageRequest(AbstractModel):
    """DescribeTIWDailyUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 互动白板应用SdkAppId
        :type SdkAppId: int
        :param SubProduct: 需要查询的子产品用量，支持传入以下值
- sp_tiw_board: 互动白板时长，单位为分钟
- sp_tiw_dt: 动态转码页数，单位页
- sp_tiw_st: 静态转码页数，单位页
- sp_tiw_ric: 实时录制时长，单位分钟

注意：动态转码以1:8的比例计算文档转码页数，静态转码以1:1的比例计算文档转码页数
        :type SubProduct: str
        :param StartTime: 开始时间，格式YYYY-MM-DD，查询结果里包括该天数据
        :type StartTime: str
        :param EndTime: 结束时间，格式YYYY-MM-DD，查询结果里包括该天数据，单次查询统计区间最多不能超过31天。
        :type EndTime: str
        """
        self.SdkAppId = None
        self.SubProduct = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.SubProduct = params.get("SubProduct")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTIWDailyUsageResponse(AbstractModel):
    """DescribeTIWDailyUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Usages: 指定区间指定产品的用量汇总
        :type Usages: list of UsageDataItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Usages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self.Usages = []
            for item in params.get("Usages"):
                obj = UsageDataItem()
                obj._deserialize(item)
                self.Usages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTIWRoomDailyUsageRequest(AbstractModel):
    """DescribeTIWRoomDailyUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 互动白板应用SdkAppId
        :type SdkAppId: int
        :param SubProduct: 需要查询的子产品用量，支持传入以下值
- sp_tiw_board: 互动白板时长，单位为分钟
- sp_tiw_ric: 实时录制时长，单位分钟
        :type SubProduct: str
        :param StartTime: 开始时间，格式YYYY-MM-DD，查询结果里包括该天数据
        :type StartTime: str
        :param EndTime: 结束时间，格式YYYY-MM-DD，查询结果里包括该天数据，单次查询统计区间最多不能超过31天。
        :type EndTime: str
        :param RoomIDs: 需要查询的房间ID列表，不填默认查询全部房间
        :type RoomIDs: list of int non-negative
        :param Offset: 查询偏移量，默认为0
        :type Offset: int
        :param Limit: 每次查询返回条目限制，默认为20
        :type Limit: int
        """
        self.SdkAppId = None
        self.SubProduct = None
        self.StartTime = None
        self.EndTime = None
        self.RoomIDs = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.SubProduct = params.get("SubProduct")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RoomIDs = params.get("RoomIDs")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTIWRoomDailyUsageResponse(AbstractModel):
    """DescribeTIWRoomDailyUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Usages: 指定区间指定产品的房间用量列表
        :type Usages: list of RoomUsageDataItem
        :param Total: 用量列表总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Usages = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self.Usages = []
            for item in params.get("Usages"):
                obj = RoomUsageDataItem()
                obj._deserialize(item)
                self.Usages.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeTranscodeCallbackRequest(AbstractModel):
    """DescribeTranscodeCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeCallbackResponse(AbstractModel):
    """DescribeTranscodeCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param Callback: 文档转码回调地址
        :type Callback: str
        :param CallbackKey: 文档转码回调鉴权密钥
        :type CallbackKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Callback = None
        self.CallbackKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        self.RequestId = params.get("RequestId")


class DescribeTranscodeRequest(AbstractModel):
    """DescribeTranscode请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 文档转码任务的唯一标识Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeResponse(AbstractModel):
    """DescribeTranscode返回参数结构体

    """

    def __init__(self):
        r"""
        :param Pages: 文档的总页数
        :type Pages: int
        :param Progress: 转码的当前进度,取值范围为0~100
        :type Progress: int
        :param Resolution: 文档的分辨率
        :type Resolution: str
        :param ResultUrl: 转码完成后结果的URL
动态转码：PPT转动态H5的链接
静态转码：文档每一页的图片URL前缀，比如，该URL前缀为`http://example.com/g0jb42ps49vtebjshilb/`，那么文档第1页的图片URL为
`http://example.com/g0jb42ps49vtebjshilb/1.jpg`，其它页以此类推
        :type ResultUrl: str
        :param Status: 任务的当前状态
- QUEUED: 正在排队等待转换
- PROCESSING: 转换中
- FINISHED: 转换完成
        :type Status: str
        :param TaskId: 转码任务的唯一标识Id
        :type TaskId: str
        :param Title: 文档的文件名
        :type Title: str
        :param ThumbnailUrl: 缩略图URL前缀，比如，该URL前缀为`http://example.com/g0jb42ps49vtebjshilb/ `，那么动态PPT第1页的缩略图URL为
`http://example.com/g0jb42ps49vtebjshilb/1.jpg`，其它页以此类推

如果发起文档转码请求参数中带了ThumbnailResolution参数，并且转码类型为动态转码，该参数不为空，其余情况该参数为空字符串
        :type ThumbnailUrl: str
        :param ThumbnailResolution: 动态转码缩略图生成分辨率
        :type ThumbnailResolution: str
        :param CompressFileUrl: 转码压缩文件下载的URL，如果发起文档转码请求参数中`CompressFileType`为空或者不是支持的压缩格式，该参数为空字符串
        :type CompressFileUrl: str
        :param ResourceListUrl: 资源清单文件下载URL(内测体验)
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceListUrl: str
        :param Ext: 文档制作方式(内测体验)
注意：此字段可能返回 null，表示取不到有效值。
        :type Ext: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Pages = None
        self.Progress = None
        self.Resolution = None
        self.ResultUrl = None
        self.Status = None
        self.TaskId = None
        self.Title = None
        self.ThumbnailUrl = None
        self.ThumbnailResolution = None
        self.CompressFileUrl = None
        self.ResourceListUrl = None
        self.Ext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Pages = params.get("Pages")
        self.Progress = params.get("Progress")
        self.Resolution = params.get("Resolution")
        self.ResultUrl = params.get("ResultUrl")
        self.Status = params.get("Status")
        self.TaskId = params.get("TaskId")
        self.Title = params.get("Title")
        self.ThumbnailUrl = params.get("ThumbnailUrl")
        self.ThumbnailResolution = params.get("ThumbnailResolution")
        self.CompressFileUrl = params.get("CompressFileUrl")
        self.ResourceListUrl = params.get("ResourceListUrl")
        self.Ext = params.get("Ext")
        self.RequestId = params.get("RequestId")


class DescribeTranscodeSearchRequest(AbstractModel):
    """DescribeTranscodeSearch请求参数结构体

    """


class DescribeTranscodeSearchResponse(AbstractModel):
    """DescribeTranscodeSearch返回参数结构体

    """

    def __init__(self):
        r"""
        :param TranscodeTaskSet: 转码任务搜索结果集合
        :type TranscodeTaskSet: list of TranscodeTaskSearchResult
        :param TotalCount: 转码总任务数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TranscodeTaskSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TranscodeTaskSet") is not None:
            self.TranscodeTaskSet = []
            for item in params.get("TranscodeTaskSet"):
                obj = TranscodeTaskSearchResult()
                obj._deserialize(item)
                self.TranscodeTaskSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeUsageSummaryRequest(AbstractModel):
    """DescribeUsageSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param BeginTime: 统计时间段的开始时间
        :type BeginTime: str
        :param EndTime: 统计时间段的结束时间
        :type EndTime: str
        :param SubProducts: 需要获取用量的子产品列表
        :type SubProducts: list of str
        :param IsWeighted: true: 返回加权后的数据
false: 返回原始数据
        :type IsWeighted: bool
        """
        self.BeginTime = None
        self.EndTime = None
        self.SubProducts = None
        self.IsWeighted = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.SubProducts = params.get("SubProducts")
        self.IsWeighted = params.get("IsWeighted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsageSummaryResponse(AbstractModel):
    """DescribeUsageSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeUserListRequest(AbstractModel):
    """DescribeUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 白板应用的SdkAppId
        :type SdkAppId: int
        :param RoomId: 需要查询用户列表的白板房间号
        :type RoomId: str
        :param TimeRange: 查询时间段，Unix时间戳，单位毫秒，第一个值为开始时间戳，第二个值为结束时间
        :type TimeRange: list of int
        :param Query: 额外的查询条件
        :type Query: str
        :param MaxSize: 返回最大的数据条数，默认1000
        :type MaxSize: int
        """
        self.SdkAppId = None
        self.RoomId = None
        self.TimeRange = None
        self.Query = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.TimeRange = params.get("TimeRange")
        self.Query = params.get("Query")
        self.MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserListResponse(AbstractModel):
    """DescribeUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserList: 房间内的用户列表
        :type UserList: list of UserListItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = UserListItem()
                obj._deserialize(item)
                self.UserList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserResourcesRequest(AbstractModel):
    """DescribeUserResources请求参数结构体

    """


class DescribeUserResourcesResponse(AbstractModel):
    """DescribeUserResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeUserStatusRequest(AbstractModel):
    """DescribeUserStatus请求参数结构体

    """


class DescribeUserStatusResponse(AbstractModel):
    """DescribeUserStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param AppId: 客户的AppId
        :type AppId: int
        :param IsTiwUser: 是否开通过白板（试用或正式）

0: 从未开通过白板服务
1: 已经开通过白板服务
        :type IsTiwUser: int
        :param IsSaaSUser: 是否开通过互动课堂（试用或正式）
        :type IsSaaSUser: int
        :param IsTiwOfflineRecordUser: 是否使用白板的课后录制
        :type IsTiwOfflineRecordUser: int
        :param IsAuthenticated: 用户是否实名认证
        :type IsAuthenticated: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppId = None
        self.IsTiwUser = None
        self.IsSaaSUser = None
        self.IsTiwOfflineRecordUser = None
        self.IsAuthenticated = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.IsTiwUser = params.get("IsTiwUser")
        self.IsSaaSUser = params.get("IsSaaSUser")
        self.IsTiwOfflineRecordUser = params.get("IsTiwOfflineRecordUser")
        self.IsAuthenticated = params.get("IsAuthenticated")
        self.RequestId = params.get("RequestId")


class DescribeVideoGenerationTaskCallbackRequest(AbstractModel):
    """DescribeVideoGenerationTaskCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoGenerationTaskCallbackResponse(AbstractModel):
    """DescribeVideoGenerationTaskCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param Callback: 录制视频生成回调地址
        :type Callback: str
        :param CallbackKey: 录制视频生成回调鉴权密钥
        :type CallbackKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Callback = None
        self.CallbackKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        self.RequestId = params.get("RequestId")


class DescribeVideoGenerationTaskRequest(AbstractModel):
    """DescribeVideoGenerationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 录制视频生成的任务Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoGenerationTaskResponse(AbstractModel):
    """DescribeVideoGenerationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 任务对应的群组Id
        :type GroupId: str
        :param RoomId: 任务对应的房间号
        :type RoomId: int
        :param TaskId: 任务的Id
        :type TaskId: str
        :param Progress: 已废弃
        :type Progress: int
        :param Status: 录制视频生成任务状态
- QUEUED: 正在排队
- PROCESSING: 正在生成视频
- FINISHED: 生成视频结束（成功完成或失败结束，可以通过错误码和错误信息进一步判断）
        :type Status: str
        :param TotalTime: 回放视频总时长,单位：毫秒
        :type TotalTime: int
        :param VideoInfos: 已废弃，请使用`VideoInfoList`参数
        :type VideoInfos: :class:`tencentcloud.tiw.v20190919.models.VideoInfo`
        :param VideoInfoList: 录制视频生成视频列表
        :type VideoInfoList: list of VideoInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RoomId = None
        self.TaskId = None
        self.Progress = None
        self.Status = None
        self.TotalTime = None
        self.VideoInfos = None
        self.VideoInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RoomId = params.get("RoomId")
        self.TaskId = params.get("TaskId")
        self.Progress = params.get("Progress")
        self.Status = params.get("Status")
        self.TotalTime = params.get("TotalTime")
        if params.get("VideoInfos") is not None:
            self.VideoInfos = VideoInfo()
            self.VideoInfos._deserialize(params.get("VideoInfos"))
        if params.get("VideoInfoList") is not None:
            self.VideoInfoList = []
            for item in params.get("VideoInfoList"):
                obj = VideoInfo()
                obj._deserialize(item)
                self.VideoInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWarningCallbackRequest(AbstractModel):
    """DescribeWarningCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWarningCallbackResponse(AbstractModel):
    """DescribeWarningCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param Callback: 告警事件回调地址，如果未设置回调地址，该字段为空字符串
        :type Callback: str
        :param CallbackKey: 告警回调鉴权密钥
        :type CallbackKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Callback = None
        self.CallbackKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        self.RequestId = params.get("RequestId")


class DescribeWhiteboardApplicationConfigRequest(AbstractModel):
    """DescribeWhiteboardApplicationConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskTypes: 需要查询的任务类型
recording: 实时录制
transcode: 文档转码
        :type TaskTypes: list of str
        :param SdkAppIds: 需要查询配置的SdkAppId列表
        :type SdkAppIds: list of int
        """
        self.SdkAppId = None
        self.TaskTypes = None
        self.SdkAppIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskTypes = params.get("TaskTypes")
        self.SdkAppIds = params.get("SdkAppIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardApplicationConfigResponse(AbstractModel):
    """DescribeWhiteboardApplicationConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Configs: 白板应用任务相关配置
        :type Configs: list of WhiteboardApplicationConfig
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SdkAppId = None
        self.Configs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Configs") is not None:
            self.Configs = []
            for item in params.get("Configs"):
                obj = WhiteboardApplicationConfig()
                obj._deserialize(item)
                self.Configs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWhiteboardBucketConfigRequest(AbstractModel):
    """DescribeWhiteboardBucketConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskType: 需要查询的任务类型
recording: 实时录制
transcode: 文档转码
        :type TaskType: str
        """
        self.SdkAppId = None
        self.TaskType = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardBucketConfigResponse(AbstractModel):
    """DescribeWhiteboardBucketConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeWhiteboardPushCallbackRequest(AbstractModel):
    """DescribeWhiteboardPushCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardPushCallbackResponse(AbstractModel):
    """DescribeWhiteboardPushCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param Callback: 白板推流事件回调地址，如果未设置回调地址，该字段为空字符串
        :type Callback: str
        :param CallbackKey: 白板推流回调鉴权密钥
        :type CallbackKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Callback = None
        self.CallbackKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        self.RequestId = params.get("RequestId")


class DescribeWhiteboardPushRequest(AbstractModel):
    """DescribeWhiteboardPush请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 白板推流任务Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardPushResponse(AbstractModel):
    """DescribeWhiteboardPush返回参数结构体

    """

    def __init__(self):
        r"""
        :param FinishReason: 推流结束原因，
- AUTO: 房间内长时间没有音视频上行及白板操作导致自动停止推流
- USER_CALL: 主动调用了停止推流接口
- EXCEPTION: 推流异常结束
        :type FinishReason: str
        :param TaskId: 需要查询结果的白板推流任务Id
        :type TaskId: str
        :param Status: 推流任务状态
- PREPARED: 表示推流正在准备中（进房/启动推流服务等操作）
- PUSHING: 表示推流已开始
- STOPPED: 表示推流已停止
        :type Status: str
        :param RoomId: 房间号
        :type RoomId: int
        :param GroupId: 白板的群组 Id
        :type GroupId: str
        :param PushUserId: 推流用户Id
        :type PushUserId: str
        :param PushStartTime: 实际开始推流时间，Unix 时间戳，单位秒
        :type PushStartTime: int
        :param PushStopTime: 实际停止推流时间，Unix 时间戳，单位秒
        :type PushStopTime: int
        :param ExceptionCnt: 推流过程中出现异常的次数
        :type ExceptionCnt: int
        :param IMSyncTime: 白板推流首帧对应的IM时间戳，可用于录制回放时IM聊天消息与白板推流视频进行同步对时。
        :type IMSyncTime: int
        :param Backup: 备份推流任务结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Backup: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FinishReason = None
        self.TaskId = None
        self.Status = None
        self.RoomId = None
        self.GroupId = None
        self.PushUserId = None
        self.PushStartTime = None
        self.PushStopTime = None
        self.ExceptionCnt = None
        self.IMSyncTime = None
        self.Backup = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FinishReason = params.get("FinishReason")
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.RoomId = params.get("RoomId")
        self.GroupId = params.get("GroupId")
        self.PushUserId = params.get("PushUserId")
        self.PushStartTime = params.get("PushStartTime")
        self.PushStopTime = params.get("PushStopTime")
        self.ExceptionCnt = params.get("ExceptionCnt")
        self.IMSyncTime = params.get("IMSyncTime")
        self.Backup = params.get("Backup")
        self.RequestId = params.get("RequestId")


class DescribeWhiteboardPushSearchRequest(AbstractModel):
    """DescribeWhiteboardPushSearch请求参数结构体

    """


class DescribeWhiteboardPushSearchResponse(AbstractModel):
    """DescribeWhiteboardPushSearch返回参数结构体

    """

    def __init__(self):
        r"""
        :param WhiteboardPushTaskSet: 推流任务搜索结果集合
        :type WhiteboardPushTaskSet: list of WhiteboardPushTaskSearchResult
        :param TotalCount: 推流总任务数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WhiteboardPushTaskSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WhiteboardPushTaskSet") is not None:
            self.WhiteboardPushTaskSet = []
            for item in params.get("WhiteboardPushTaskSet"):
                obj = WhiteboardPushTaskSearchResult()
                obj._deserialize(item)
                self.WhiteboardPushTaskSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class Detail(AbstractModel):
    """计费用量数据里，带不同指标Tag的详情

    """

    def __init__(self):
        r"""
        :param TagName: 用量指标
        :type TagName: str
        :param Weight: 用量权重
        :type Weight: float
        :param Value: 用量的值
        :type Value: float
        """
        self.TagName = None
        self.Weight = None
        self.Value = None


    def _deserialize(self, params):
        self.TagName = params.get("TagName")
        self.Weight = params.get("Weight")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Interrupt(AbstractModel):
    """实时录制中出现的用户视频流断流次数统计

    """

    def __init__(self):
        r"""
        :param UserId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param Count: 视频流断流次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self.UserId = None
        self.Count = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LayoutParams(AbstractModel):
    """自定义混流配置布局参数

    """

    def __init__(self):
        r"""
        :param Width: 流画面宽，取值范围[2,3000]
        :type Width: int
        :param Height: 流画面高，取值范围[2,3000]
        :type Height: int
        :param X: 当前画面左上角顶点相对于Canvas左上角顶点的x轴偏移量，默认为0，取值范围[0,3000]
        :type X: int
        :param Y: 当前画面左上角顶点相对于Canvas左上角顶点的y轴偏移量，默认为0， 取值范围[0,3000]
        :type Y: int
        :param ZOrder: 画面z轴位置，默认为0
z轴确定了重叠画面的遮盖顺序，z轴值大的画面处于顶层
        :type ZOrder: int
        """
        self.Width = None
        self.Height = None
        self.X = None
        self.Y = None
        self.ZOrder = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.ZOrder = params.get("ZOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixStream(AbstractModel):
    """混流配置

    """

    def __init__(self):
        r"""
        :param Enabled: 是否开启混流
        :type Enabled: bool
        :param DisableAudio: 是否禁用音频混流
        :type DisableAudio: bool
        :param ModelId: 内置混流布局模板ID, 取值 [1, 2], 区别见内置混流布局模板样式示例说明
在没有填Custom字段时候，ModelId是必填的
        :type ModelId: int
        :param TeacherId: 老师用户ID
此字段只有在ModelId填了的情况下生效
填写TeacherId的效果是把指定为TeacherId的用户视频流显示在内置模板的第一个小画面中
        :type TeacherId: str
        :param Custom: 自定义混流布局参数
当此字段存在时，ModelId 及 TeacherId 字段将被忽略
        :type Custom: :class:`tencentcloud.tiw.v20190919.models.CustomLayout`
        """
        self.Enabled = None
        self.DisableAudio = None
        self.ModelId = None
        self.TeacherId = None
        self.Custom = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.DisableAudio = params.get("DisableAudio")
        self.ModelId = params.get("ModelId")
        self.TeacherId = params.get("TeacherId")
        if params.get("Custom") is not None:
            self.Custom = CustomLayout()
            self.Custom._deserialize(params.get("Custom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationRequest(AbstractModel):
    """ModifyApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用SdkAppId
        :type SdkAppId: int
        :param AppName: App名字
        :type AppName: str
        """
        self.SdkAppId = None
        self.AppName = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationResponse(AbstractModel):
    """ModifyApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAutoRenewFlagRequest(AbstractModel):
    """ModifyAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param SubProduct: 资源Id，从DescribeUserResources接口中获取Level=1的正式月功能费的SubProduct，一般为sp_tiw_package
        :type SubProduct: str
        :param ResourceId: 资源Id，从DescribeUserResources接口中获取Level=1的正式月功能费资源Id
        :type ResourceId: str
        :param AutoRenewFlag: 自动续费标记，0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费(用户设置)，若业务无续费概念或无需自动续 费，需要设置为0
        :type AutoRenewFlag: int
        """
        self.SubProduct = None
        self.ResourceId = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.SubProduct = params.get("SubProduct")
        self.ResourceId = params.get("ResourceId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoRenewFlagResponse(AbstractModel):
    """ModifyAutoRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWhiteboardApplicationConfigRequest(AbstractModel):
    """ModifyWhiteboardApplicationConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Configs: 白板应用任务相关配置
        :type Configs: list of WhiteboardApplicationConfig
        """
        self.SdkAppId = None
        self.Configs = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Configs") is not None:
            self.Configs = []
            for item in params.get("Configs"):
                obj = WhiteboardApplicationConfig()
                obj._deserialize(item)
                self.Configs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWhiteboardApplicationConfigResponse(AbstractModel):
    """ModifyWhiteboardApplicationConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWhiteboardBucketConfigRequest(AbstractModel):
    """ModifyWhiteboardBucketConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskType: 需要查询的任务类型
recording: 实时录制
transcode: 文档转码
        :type TaskType: str
        :param BucketName: COS存储桶名字
        :type BucketName: str
        :param BucketLocation: COS存储桶地域
        :type BucketLocation: str
        :param BucketPrefix: 存储桶里资源前缀
        :type BucketPrefix: str
        :param ResultDomain: 返回Url域名
        :type ResultDomain: str
        """
        self.SdkAppId = None
        self.TaskType = None
        self.BucketName = None
        self.BucketLocation = None
        self.BucketPrefix = None
        self.ResultDomain = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskType = params.get("TaskType")
        self.BucketName = params.get("BucketName")
        self.BucketLocation = params.get("BucketLocation")
        self.BucketPrefix = params.get("BucketPrefix")
        self.ResultDomain = params.get("ResultDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWhiteboardBucketConfigResponse(AbstractModel):
    """ModifyWhiteboardBucketConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OmittedDuration(AbstractModel):
    """拼接视频中被忽略的时间段

    """

    def __init__(self):
        r"""
        :param VideoTime: 录制暂停时间戳对应的视频播放时间(单位: 毫秒)
        :type VideoTime: int
        :param PauseTime: 录制暂停时间戳(单位: 毫秒)
        :type PauseTime: int
        :param ResumeTime: 录制恢复时间戳(单位: 毫秒)
        :type ResumeTime: int
        """
        self.VideoTime = None
        self.PauseTime = None
        self.ResumeTime = None


    def _deserialize(self, params):
        self.VideoTime = params.get("VideoTime")
        self.PauseTime = params.get("PauseTime")
        self.ResumeTime = params.get("ResumeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PPTErr(AbstractModel):
    """PPT错误元素

    """

    def __init__(self):
        r"""
        :param Name: 元素名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Type: 0: 不支持的墨迹类型，1: 不支持自动翻页，2: 存在已损坏音视频，3: 存在不可访问资源，4: 只读文件
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param Detail: 错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: str
        """
        self.Name = None
        self.Type = None
        self.Detail = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Detail = params.get("Detail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PPTErrSlide(AbstractModel):
    """PPT错误页面列表

    """

    def __init__(self):
        r"""
        :param Page: 异常元素存在的页面，由页面类型+页码组成，页码类型包括：幻灯片、幻灯片母版、幻灯片布局等
注意：此字段可能返回 null，表示取不到有效值。
        :type Page: str
        :param Errs: 错误元素列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Errs: list of PPTErr
        """
        self.Page = None
        self.Errs = None


    def _deserialize(self, params):
        self.Page = params.get("Page")
        if params.get("Errs") is not None:
            self.Errs = []
            for item in params.get("Errs"):
                obj = PPTErr()
                obj._deserialize(item)
                self.Errs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseOnlineRecordRequest(AbstractModel):
    """PauseOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 实时录制任务 Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseOnlineRecordResponse(AbstractModel):
    """PauseOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RecordControl(AbstractModel):
    """录制控制参数， 用于指定全局录制控制及具体流录制控制参数，比如设置需要对哪些流进行录制，是否只录制小画面等

    """

    def __init__(self):
        r"""
        :param Enabled: 设置是否开启录制控制参数，只有设置为true的时候，录制控制参数才生效。
        :type Enabled: bool
        :param DisableRecord: 设置是否禁用录制的全局控制参数。一般与`StreamControls`参数配合使用。

true - 所有流都不录制。
false - 所有流都录制。默认为false。

这里的设置对所有流都生效，如果同时在 `StreamControls` 列表中针对指定流设置了控制参数，则优先采用`StreamControls`中设置的控制参数。
        :type DisableRecord: bool
        :param DisableAudio: 设置是否禁用所有流的音频录制的全局控制参数。一般与`StreamControls`参数配合使用。

true - 所有流的录制都不对音频进行录制。
false - 所有流的录制都需要对音频进行录制。默认为false。

这里的设置对所有流都生效，如果同时在 `StreamControls` 列表中针对指定流设置了控制参数，则优先采用`StreamControls`中设置的控制参数。
        :type DisableAudio: bool
        :param PullSmallVideo: 设置是否所有流都只录制小画面的全局控制参数。一般与`StreamControls`参数配合使用。

true - 所有流都只录制小画面。设置为true时，请确保上行端在推流的时候同时上行了小画面，否则录制视频可能是黑屏。
false - 所有流都录制大画面，默认为false。

这里的设置对所有流都生效，如果同时在 `StreamControls` 列表中针对指定流设置了控制参数，则优先采用`StreamControls`中设置的控制参数。
        :type PullSmallVideo: bool
        :param StreamControls: 针对具体流指定控制参数，如果列表为空，则所有流采用全局配置的控制参数进行录制。列表不为空，则列表中指定的流将优先按此列表指定的控制参数进行录制。
        :type StreamControls: list of StreamControl
        """
        self.Enabled = None
        self.DisableRecord = None
        self.DisableAudio = None
        self.PullSmallVideo = None
        self.StreamControls = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.DisableRecord = params.get("DisableRecord")
        self.DisableAudio = params.get("DisableAudio")
        self.PullSmallVideo = params.get("PullSmallVideo")
        if params.get("StreamControls") is not None:
            self.StreamControls = []
            for item in params.get("StreamControls"):
                obj = StreamControl()
                obj._deserialize(item)
                self.StreamControls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTaskResult(AbstractModel):
    """实时录制结果

    """

    def __init__(self):
        r"""
        :param FinishReason: AUTO - 自动停止录制， USER_CALL - 用户主动调用停止录制
        :type FinishReason: str
        :param ExceptionCnt: 异常数
        :type ExceptionCnt: int
        :param RoomId: 房间号
        :type RoomId: int
        :param GroupId: 分组
        :type GroupId: str
        :param RecordStartTime: 录制真实开始时间
        :type RecordStartTime: int
        :param RecordStopTime: 录制结束时间
        :type RecordStopTime: int
        :param TotalTime: 录制总时长
        :type TotalTime: int
        :param VideoInfos: 视频信息列表
        :type VideoInfos: list of VideoInfo
        :param OmittedDurations: 被忽略的视频时间段
        :type OmittedDurations: list of OmittedDuration
        :param Details: 详情
        :type Details: str
        :param ErrorCode: 任务失败错误码
        :type ErrorCode: int
        :param ErrorMsg: 错误信息
        :type ErrorMsg: str
        """
        self.FinishReason = None
        self.ExceptionCnt = None
        self.RoomId = None
        self.GroupId = None
        self.RecordStartTime = None
        self.RecordStopTime = None
        self.TotalTime = None
        self.VideoInfos = None
        self.OmittedDurations = None
        self.Details = None
        self.ErrorCode = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.FinishReason = params.get("FinishReason")
        self.ExceptionCnt = params.get("ExceptionCnt")
        self.RoomId = params.get("RoomId")
        self.GroupId = params.get("GroupId")
        self.RecordStartTime = params.get("RecordStartTime")
        self.RecordStopTime = params.get("RecordStopTime")
        self.TotalTime = params.get("TotalTime")
        if params.get("VideoInfos") is not None:
            self.VideoInfos = []
            for item in params.get("VideoInfos"):
                obj = VideoInfo()
                obj._deserialize(item)
                self.VideoInfos.append(obj)
        if params.get("OmittedDurations") is not None:
            self.OmittedDurations = []
            for item in params.get("OmittedDurations"):
                obj = OmittedDuration()
                obj._deserialize(item)
                self.OmittedDurations.append(obj)
        self.Details = params.get("Details")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTaskSearchResult(AbstractModel):
    """实时录制任务搜索结果

    """

    def __init__(self):
        r"""
        :param TaskId: 任务唯一ID
        :type TaskId: str
        :param Status: 实时录制任务状态
- PAUSED: 录制已暂停
- PREPARED: 录制在准备阶段
- RECORDING: 正在录制
- STOPPED：录制已停止
- FINISHED: 录制已结束
        :type Status: str
        :param RoomId: 实时录制房间号
        :type RoomId: int
        :param CreateTime: 任务创建时间
        :type CreateTime: str
        :param SdkAppId: 用户应用SdkAppId
        :type SdkAppId: int
        :param Result: 实时录制结果
        :type Result: :class:`tencentcloud.tiw.v20190919.models.RecordTaskResult`
        """
        self.TaskId = None
        self.Status = None
        self.RoomId = None
        self.CreateTime = None
        self.SdkAppId = None
        self.Result = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.RoomId = params.get("RoomId")
        self.CreateTime = params.get("CreateTime")
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Result") is not None:
            self.Result = RecordTaskResult()
            self.Result._deserialize(params.get("Result"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeOnlineRecordRequest(AbstractModel):
    """ResumeOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 恢复录制的实时录制任务 Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeOnlineRecordResponse(AbstractModel):
    """ResumeOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RoomListItem(AbstractModel):
    """日志查询里返回的白板房间数据

    """

    def __init__(self):
        r"""
        :param RoomId: 房间ID
        :type RoomId: str
        :param StartTime: 房间在查询时间段内最早出现的时间，Unix时间戳，单位毫秒
        :type StartTime: int
        :param EndTime: 房间在查询时间段内最晚出现的时间，Unix时间戳，单位毫秒
        :type EndTime: int
        :param UserNumber: 房间里成员数
        :type UserNumber: int
        """
        self.RoomId = None
        self.StartTime = None
        self.EndTime = None
        self.UserNumber = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.UserNumber = params.get("UserNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoomUsageDataItem(AbstractModel):
    """互动白板房间用量信息

    """

    def __init__(self):
        r"""
        :param Time: 日期，格式为YYYY-MM-DD
        :type Time: str
        :param SdkAppId: 白板应用SDKAppID
        :type SdkAppId: int
        :param SubProduct: 互动白板子产品，请求参数传入的一致
- sp_tiw_board: 互动白板时长
- sp_tiw_ric: 实时录制时长
        :type SubProduct: str
        :param Value: 用量值
- 白板时长、实时录制时长单位为分钟
        :type Value: float
        :param RoomID: 互动白板房间号
        :type RoomID: int
        """
        self.Time = None
        self.SdkAppId = None
        self.SubProduct = None
        self.Value = None
        self.RoomID = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.SdkAppId = params.get("SdkAppId")
        self.SubProduct = params.get("SubProduct")
        self.Value = params.get("Value")
        self.RoomID = params.get("RoomID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunningTaskItem(AbstractModel):
    """正在运行的任务列表项

    """

    def __init__(self):
        r"""
        :param SdkAppID: 应用SdkAppID
        :type SdkAppID: int
        :param TaskID: 任务ID
        :type TaskID: str
        :param TaskType: 任务类型
- TranscodeH5: 动态转码任务，文档转HTML5页面
- TranscodeJPG: 静态转码任务，文档转图片
- WhiteboardPush: 白板推流任务
- OnlineRecord: 实时录制任务
        :type TaskType: str
        :param CreateTime: 任务创建时间
        :type CreateTime: str
        :param CancelTime: 任务取消时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CancelTime: str
        :param Status: 任务状态
- QUEUED: 任务正在排队等待执行中
- PROCESSING: 任务正在执行中 
- FINISHED: 任务已完成
        :type Status: str
        :param Progress: 任务当前进度
        :type Progress: int
        :param FileURL: 转码任务中转码文件的原始URL
此参数只有任务类型为TranscodeH5、TranscodeJPG类型时才会有有效值。其他任务类型为空字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileURL: str
        :param RoomID: 房间号

当任务类型为TranscodeH5、TranscodeJPG时，房间号为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomID: int
        """
        self.SdkAppID = None
        self.TaskID = None
        self.TaskType = None
        self.CreateTime = None
        self.CancelTime = None
        self.Status = None
        self.Progress = None
        self.FileURL = None
        self.RoomID = None


    def _deserialize(self, params):
        self.SdkAppID = params.get("SdkAppID")
        self.TaskID = params.get("TaskID")
        self.TaskType = params.get("TaskType")
        self.CreateTime = params.get("CreateTime")
        self.CancelTime = params.get("CancelTime")
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.FileURL = params.get("FileURL")
        self.RoomID = params.get("RoomID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOfflineRecordCallbackRequest(AbstractModel):
    """SetOfflineRecordCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Callback: 课后录制任务结果回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持 http或https协议，即回调地址以http://或https://开头
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOfflineRecordCallbackResponse(AbstractModel):
    """SetOfflineRecordCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetOnlineRecordCallbackKeyRequest(AbstractModel):
    """SetOnlineRecordCallbackKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        :param CallbackKey: 设置实时录制回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥。回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        :type CallbackKey: str
        """
        self.SdkAppId = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOnlineRecordCallbackKeyResponse(AbstractModel):
    """SetOnlineRecordCallbackKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetOnlineRecordCallbackRequest(AbstractModel):
    """SetOnlineRecordCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Callback: 实时录制任务结果回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持 http或https协议，即回调地址以http://或https://开头。回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40258
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOnlineRecordCallbackResponse(AbstractModel):
    """SetOnlineRecordCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetPPTCheckCallbackKeyRequest(AbstractModel):
    """SetPPTCheckCallbackKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        :param CallbackKey: 设置回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257	
        :type CallbackKey: str
        """
        self.SdkAppId = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPPTCheckCallbackKeyResponse(AbstractModel):
    """SetPPTCheckCallbackKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetPPTCheckCallbackRequest(AbstractModel):
    """SetPPTCheckCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId	
        :type SdkAppId: int
        :param Callback: 进度回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持http或https协议，即回调地址以http://或https://开头。 回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40260#c9cbe05f-fe1a-4410-b4dc-40cc301c7b81	
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPPTCheckCallbackResponse(AbstractModel):
    """SetPPTCheckCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetTranscodeCallbackKeyRequest(AbstractModel):
    """SetTranscodeCallbackKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        :param CallbackKey: 设置文档转码回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        :type CallbackKey: str
        """
        self.SdkAppId = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTranscodeCallbackKeyResponse(AbstractModel):
    """SetTranscodeCallbackKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetTranscodeCallbackRequest(AbstractModel):
    """SetTranscodeCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Callback: 文档转码进度回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持http或https协议，即回调地址以http://或https://开头。
回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40260
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTranscodeCallbackResponse(AbstractModel):
    """SetTranscodeCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetVideoGenerationTaskCallbackKeyRequest(AbstractModel):
    """SetVideoGenerationTaskCallbackKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        :param CallbackKey: 设置视频生成回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥
        :type CallbackKey: str
        """
        self.SdkAppId = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetVideoGenerationTaskCallbackKeyResponse(AbstractModel):
    """SetVideoGenerationTaskCallbackKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetVideoGenerationTaskCallbackRequest(AbstractModel):
    """SetVideoGenerationTaskCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Callback: 课后录制任务结果回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持 http或https协议，即回调地址以http://或https://开头
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetVideoGenerationTaskCallbackResponse(AbstractModel):
    """SetVideoGenerationTaskCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetWarningCallbackRequest(AbstractModel):
    """SetWarningCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Callback: 告警回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持http或https协议，即回调地址以http://或https://开头。
回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/90112
        :type Callback: str
        :param CallbackKey: 设置告警回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        :type CallbackKey: str
        """
        self.SdkAppId = None
        self.Callback = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetWarningCallbackResponse(AbstractModel):
    """SetWarningCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetWhiteboardPushCallbackKeyRequest(AbstractModel):
    """SetWhiteboardPushCallbackKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        :param CallbackKey: 设置白板推流回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥。回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        :type CallbackKey: str
        """
        self.SdkAppId = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetWhiteboardPushCallbackKeyResponse(AbstractModel):
    """SetWhiteboardPushCallbackKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetWhiteboardPushCallbackRequest(AbstractModel):
    """SetWhiteboardPushCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param Callback: 白板推流任务结果回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持 http或https协议，即回调地址以http://或https://开头。回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetWhiteboardPushCallbackResponse(AbstractModel):
    """SetWhiteboardPushCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SnapshotCOS(AbstractModel):
    """板书文件存储cos参数

    """

    def __init__(self):
        r"""
        :param Uin: cos所在腾讯云帐号uin
        :type Uin: int
        :param Region: cos所在地区
        :type Region: str
        :param Bucket: cos存储桶名称
        :type Bucket: str
        :param TargetDir: 板书文件存储根目录
        :type TargetDir: str
        :param Domain: CDN加速域名
        :type Domain: str
        """
        self.Uin = None
        self.Region = None
        self.Bucket = None
        self.TargetDir = None
        self.Domain = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.TargetDir = params.get("TargetDir")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotResult(AbstractModel):
    """白板板书结果

    """

    def __init__(self):
        r"""
        :param ErrorCode: 任务执行错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCode: str
        :param ErrorMessage: 任务执行错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param Total: 快照生成图片总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Snapshots: 快照图片链接列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Snapshots: list of str
        """
        self.ErrorCode = None
        self.ErrorMessage = None
        self.Total = None
        self.Snapshots = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMessage = params.get("ErrorMessage")
        self.Total = params.get("Total")
        self.Snapshots = params.get("Snapshots")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotWhiteboard(AbstractModel):
    """生成白板板书时的白板参数，例如白板宽高等

    """

    def __init__(self):
        r"""
        :param Width: 白板宽度大小，默认为1280，有效取值范围[0，2560]
        :type Width: int
        :param Height: 白板高度大小，默认为720，有效取值范围[0，2560]
        :type Height: int
        :param InitParams: 白板初始化参数的JSON转义字符串，透传到白板 SDK
        :type InitParams: str
        """
        self.Width = None
        self.Height = None
        self.InitParams = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.InitParams = params.get("InitParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartOnlineRecordRequest(AbstractModel):
    """StartOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param RoomId: 需要录制的房间号，取值范围: (1, 4294967295)
        :type RoomId: int
        :param RecordUserId: 用于录制服务进房的用户ID，最大长度不能大于60个字节，格式为`tic_record_user_${RoomId}_${Random}`，其中 `${RoomId} `与录制房间号对应，`${Random}`为一个随机字符串。
该ID必须是一个单独的未在SDK中使用的ID，录制服务使用这个用户ID进入房间进行音视频与白板录制，若该ID和SDK中使用的ID重复，会导致SDK和录制服务互踢，影响正常录制。
        :type RecordUserId: str
        :param RecordUserSig: 与RecordUserId对应的签名
        :type RecordUserSig: str
        :param GroupId: （已废弃，设置无效）白板的 IM 群组 Id，默认同房间号
        :type GroupId: str
        :param Concat: 录制视频拼接参数
        :type Concat: :class:`tencentcloud.tiw.v20190919.models.Concat`
        :param Whiteboard: 录制白板参数，例如白板宽高等
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param MixStream: 录制混流参数
特别说明：
1. 混流功能需要根据额外开通， 请联系腾讯云互动白板客服人员
2. 使用混流功能，必须提供 Extras 参数，且 Extras 参数中必须包含 "MIX_STREAM"
        :type MixStream: :class:`tencentcloud.tiw.v20190919.models.MixStream`
        :param Extras: 使用到的高级功能列表
可以选值列表：
MIX_STREAM - 混流功能
        :type Extras: list of str
        :param AudioFileNeeded: 是否需要在结果回调中返回各路流的纯音频录制文件，文件格式为mp3
        :type AudioFileNeeded: bool
        :param RecordControl: 录制控制参数，用于更精细地指定需要录制哪些流，某一路流是否禁用音频，是否只录制小画面等
        :type RecordControl: :class:`tencentcloud.tiw.v20190919.models.RecordControl`
        :param RecordMode: 录制模式

REALTIME_MODE - 实时录制模式（默认）
VIDEO_GENERATION_MODE - 视频生成模式（内测中，需邮件申请开通）
        :type RecordMode: str
        :param ChatGroupId: 聊天群组ID，此字段仅适用于`视频生成模式`

在`视频生成模式`下，默认会记录白板群组内的非白板信令消息，如果指定了`ChatGroupId`，则会记录指定群ID的聊天消息。
        :type ChatGroupId: str
        :param AutoStopTimeout: 自动停止录制超时时间，单位秒，取值范围[300, 86400], 默认值为300秒。

当超过设定时间房间内没有音视频上行且没有白板操作的时候，录制服务会自动停止当前录制任务。
        :type AutoStopTimeout: int
        :param ExtraData: 内部参数，可忽略
        :type ExtraData: str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.RecordUserId = None
        self.RecordUserSig = None
        self.GroupId = None
        self.Concat = None
        self.Whiteboard = None
        self.MixStream = None
        self.Extras = None
        self.AudioFileNeeded = None
        self.RecordControl = None
        self.RecordMode = None
        self.ChatGroupId = None
        self.AutoStopTimeout = None
        self.ExtraData = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.RecordUserId = params.get("RecordUserId")
        self.RecordUserSig = params.get("RecordUserSig")
        self.GroupId = params.get("GroupId")
        if params.get("Concat") is not None:
            self.Concat = Concat()
            self.Concat._deserialize(params.get("Concat"))
        if params.get("Whiteboard") is not None:
            self.Whiteboard = Whiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        if params.get("MixStream") is not None:
            self.MixStream = MixStream()
            self.MixStream._deserialize(params.get("MixStream"))
        self.Extras = params.get("Extras")
        self.AudioFileNeeded = params.get("AudioFileNeeded")
        if params.get("RecordControl") is not None:
            self.RecordControl = RecordControl()
            self.RecordControl._deserialize(params.get("RecordControl"))
        self.RecordMode = params.get("RecordMode")
        self.ChatGroupId = params.get("ChatGroupId")
        self.AutoStopTimeout = params.get("AutoStopTimeout")
        self.ExtraData = params.get("ExtraData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartOnlineRecordResponse(AbstractModel):
    """StartOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 录制任务Id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class StartWhiteboardPushRequest(AbstractModel):
    """StartWhiteboardPush请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param RoomId: 需要推流的白板房间号，取值范围: (1, 4294967295)。

1. 白板推流默认以RoomId的字符串表达形式作为IM群组的GroupID（比如RoomId为1234，则IM群组的GroupID为"1234"）加群进行信令同步，请在开始推流前确保相应IM群组已创建完成，否则会导致推流失败。
2. 在没有指定TRTCRoomId和TRTCRoomIdStr的情况下，默认会以RoomId作为白板流进行推流的TRTC房间号。
        :type RoomId: int
        :param PushUserId: 用于白板推流服务进入白板房间的用户ID。在没有额外指定`IMAuthParam`和`TRTCAuthParam`的情况下，这个用户ID同时会用于IM登录、IM加群、TRTC进房推流等操作。
用户ID最大长度不能大于60个字节，该用户ID必须是一个单独的未同时在其他地方使用的用户ID，白板推流服务使用这个用户ID进入房间进行白板音视频推流，若该用户ID和其他地方同时在使用的用户ID重复，会导致白板推流服务与其他使用场景帐号互踢，影响正常推流。
        :type PushUserId: str
        :param PushUserSig: 与PushUserId对应的IM签名(usersig)。
        :type PushUserSig: str
        :param Whiteboard: 白板参数，例如白板宽高、背景颜色等
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param AutoStopTimeout: 自动停止推流超时时间，单位秒，取值范围[300, 259200], 默认值为1800秒。

当白板超过设定时间没有操作的时候，白板推流服务会自动停止白板推流。
        :type AutoStopTimeout: int
        :param AutoManageBackup: 对主白板推流任务进行操作时，是否同时同步操作备份任务
        :type AutoManageBackup: bool
        :param Backup: 备份白板推流相关参数。

指定了备份参数的情况下，白板推流服务会在房间内新增一路白板画面视频流，即同一个房间内会有两路白板画面推流。
        :type Backup: :class:`tencentcloud.tiw.v20190919.models.WhiteboardPushBackupParam`
        :param PrivateMapKey: TRTC高级权限控制参数，如果在实时音视频开启了高级权限控制功能，必须提供PrivateMapKey才能保证正常推流。
        :type PrivateMapKey: str
        :param VideoFPS: 白板推流视频帧率，取值范围[0, 30]，默认20fps
        :type VideoFPS: int
        :param VideoBitrate: 白板推流码率， 取值范围[0, 2000]，默认1200kbps。

这里的码率设置是一个参考值，实际推流的时候使用的是动态码率，所以真实码率不会固定为指定值，会在指定值附近波动。
        :type VideoBitrate: int
        :param AutoRecord: 在实时音视频云端录制模式选择为 `指定用户录制` 模式的时候是否自动录制白板推流。

默认在实时音视频的云端录制模式选择为 `指定用户录制` 模式的情况下，不会自动进行白板推流录制，如果希望进行白板推流录制，请将此参数设置为true。

如果实时音视频的云端录制模式选择为 `全局自动录制` 模式，可忽略此参数。
        :type AutoRecord: bool
        :param UserDefinedRecordId: 指定白板推流录制的RecordID，指定的RecordID会用于填充实时音视频云端录制完成后的回调消息中的 "userdefinerecordid" 字段内容，便于您更方便的识别录制回调，以及在点播媒体资源管理中查找相应的录制视频文件。

限制长度为64字节，只允许包含大小写英文字母（a-zA-Z）、数字（0-9）及下划线和连词符。

此字段设置后，不管`AutoRecord`字段取值如何，都将自动进行白板推流录制。

默认RecordId生成规则如下：
urlencode(SdkAppID_RoomID_PushUserID)

例如：
SdkAppID = 12345678，RoomID = 12345，PushUserID = push_user_1
那么：RecordId = 12345678_12345_push_user_1
        :type UserDefinedRecordId: str
        :param AutoPublish: 在实时音视频旁路推流模式选择为`指定用户旁路`模式的时候，是否自动旁路白板推流。

默认在实时音视频的旁路推流模式选择为 `指定用户旁路` 模式的情况下，不会自动旁路白板推流，如果希望旁路白板推流，请将此参数设置为true。

如果实时音视频的旁路推流模式选择为 `全局自动旁路` 模式，可忽略此参数。
        :type AutoPublish: bool
        :param UserDefinedStreamId: 指定实时音视频在旁路白板推流时的StreamID，设置之后，您就可以在腾讯云直播 CDN 上通过标准直播方案（FLV或HLS）播放该用户的音视频流。

限制长度为64字节，只允许包含大小写英文字母（a-zA-Z）、数字（0-9）及下划线和连词符。

此字段设置后，不管`AutoPublish`字段取值如何，都将自动旁路白板推流。

默认StreamID生成规则如下：
urlencode(SdkAppID_RoomID_PushUserID_main)

例如：
SdkAppID = 12345678，RoomID = 12345，PushUserID = push_user_1
那么：StreamID = 12345678_12345_push_user_1_main
        :type UserDefinedStreamId: str
        :param ExtraData: 内部参数，不需要关注此参数
        :type ExtraData: str
        :param TRTCRoomId: TRTC数字类型房间号，取值范围: (1, 4294967295)。

在同时指定了RoomId与TRTCRoomId的情况下，优先使用TRTCRoomId作为白板流进行推流的TRTC房间号。

当指定了TRTCRoomIdStr的情况下，此字段将被忽略。
        :type TRTCRoomId: int
        :param TRTCRoomIdStr: TRTC字符串类型房间号。

在指定了TRTCRoomIdStr的情况下，会优先使用TRTCRoomIdStr作为白板流进行推流的TRTC房间号。
        :type TRTCRoomIdStr: str
        :param IMAuthParam: IM鉴权信息参数，用于IM鉴权。
当白板信令所使用的IM应用与白板应用的SdkAppId不一致时，可以通过此参数提供对应IM应用鉴权信息。

如果提供了此参数，白板推流服务会优先使用此参数指定的SdkAppId作为白板信令的传输通道，否则使用公共参数中的SdkAppId作为白板信令的传输通道。
        :type IMAuthParam: :class:`tencentcloud.tiw.v20190919.models.AuthParam`
        :param TRTCAuthParam: TRTC鉴权信息参数，用于TRTC进房推流鉴权。
当需要推流到的TRTC房间所对应的TRTC应用与白板应用的SdkAppId不一致时，可以通过此参数提供对应的TRTC应用鉴权信息。

如果提供了此参数，白板推流服务会优先使用此参数指定的SdkAppId作为白板推流的目标TRTC应用，否则使用公共参数中的SdkAppId作为白板推流的目标TRTC应用。
        :type TRTCAuthParam: :class:`tencentcloud.tiw.v20190919.models.AuthParam`
        :param TRTCEnterRoomMode: 内测参数，需要提前申请白名单进行体验。

指定白板推流时推流用户进TRTC房间的进房模式。默认为 TRTCAppSceneVideoCall

TRTCAppSceneVideoCall - 视频通话场景，即绝大多数时间都是两人或两人以上视频通话的场景，内部编码器和网络协议优化侧重流畅性，降低通话延迟和卡顿率。
TRTCAppSceneLIVE - 直播场景，即绝大多数时间都是一人直播，偶尔有多人视频互动的场景，内部编码器和网络协议优化侧重性能和兼容性，性能和清晰度表现更佳。
        :type TRTCEnterRoomMode: str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.PushUserId = None
        self.PushUserSig = None
        self.Whiteboard = None
        self.AutoStopTimeout = None
        self.AutoManageBackup = None
        self.Backup = None
        self.PrivateMapKey = None
        self.VideoFPS = None
        self.VideoBitrate = None
        self.AutoRecord = None
        self.UserDefinedRecordId = None
        self.AutoPublish = None
        self.UserDefinedStreamId = None
        self.ExtraData = None
        self.TRTCRoomId = None
        self.TRTCRoomIdStr = None
        self.IMAuthParam = None
        self.TRTCAuthParam = None
        self.TRTCEnterRoomMode = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.PushUserId = params.get("PushUserId")
        self.PushUserSig = params.get("PushUserSig")
        if params.get("Whiteboard") is not None:
            self.Whiteboard = Whiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        self.AutoStopTimeout = params.get("AutoStopTimeout")
        self.AutoManageBackup = params.get("AutoManageBackup")
        if params.get("Backup") is not None:
            self.Backup = WhiteboardPushBackupParam()
            self.Backup._deserialize(params.get("Backup"))
        self.PrivateMapKey = params.get("PrivateMapKey")
        self.VideoFPS = params.get("VideoFPS")
        self.VideoBitrate = params.get("VideoBitrate")
        self.AutoRecord = params.get("AutoRecord")
        self.UserDefinedRecordId = params.get("UserDefinedRecordId")
        self.AutoPublish = params.get("AutoPublish")
        self.UserDefinedStreamId = params.get("UserDefinedStreamId")
        self.ExtraData = params.get("ExtraData")
        self.TRTCRoomId = params.get("TRTCRoomId")
        self.TRTCRoomIdStr = params.get("TRTCRoomIdStr")
        if params.get("IMAuthParam") is not None:
            self.IMAuthParam = AuthParam()
            self.IMAuthParam._deserialize(params.get("IMAuthParam"))
        if params.get("TRTCAuthParam") is not None:
            self.TRTCAuthParam = AuthParam()
            self.TRTCAuthParam._deserialize(params.get("TRTCAuthParam"))
        self.TRTCEnterRoomMode = params.get("TRTCEnterRoomMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartWhiteboardPushResponse(AbstractModel):
    """StartWhiteboardPush返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 推流任务Id
        :type TaskId: str
        :param Backup: 备份任务结果参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Backup: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Backup = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Backup = params.get("Backup")
        self.RequestId = params.get("RequestId")


class StopOnlineRecordRequest(AbstractModel):
    """StopOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 需要停止录制的任务 Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopOnlineRecordResponse(AbstractModel):
    """StopOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopWhiteboardPushRequest(AbstractModel):
    """StopWhiteboardPush请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param TaskId: 需要停止的白板推流任务 Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopWhiteboardPushResponse(AbstractModel):
    """StopWhiteboardPush返回参数结构体

    """

    def __init__(self):
        r"""
        :param Backup: 备份任务相关参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Backup: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Backup = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Backup = params.get("Backup")
        self.RequestId = params.get("RequestId")


class StreamControl(AbstractModel):
    """指定流录制的控制参数，比如是否禁用音频、视频是录制大画面还是录制小画面等

    """

    def __init__(self):
        r"""
        :param StreamId: 视频流ID
视频流ID的取值含义如下：
1. tic_record_user - 表示白板视频流
2. tic_substream - 表示辅路视频流
3. 特定用户ID - 表示指定用户的视频流

在实际录制过程中，视频流ID的匹配规则为前缀匹配，只要真实流ID的前缀与指定的流ID一致就认为匹配成功。
        :type StreamId: str
        :param DisableRecord: 设置是否对此路流开启录制。

true - 表示不对这路流进行录制，录制结果将不包含这路流的视频。
false - 表示需要对这路流进行录制，录制结果会包含这路流的视频。

默认为 false。
        :type DisableRecord: bool
        :param DisableAudio: 设置是否禁用这路流的音频录制。

true - 表示不对这路流的音频进行录制，录制结果里这路流的视频将会没有声音。
false - 录制视频会保留音频，如果设置为true，则录制视频会丢弃这路流的音频。

默认为 false。
        :type DisableAudio: bool
        :param PullSmallVideo: 设置当前流录制视频是否只录制小画面。

true - 录制小画面。设置为true时，请确保上行端同时上行了小画面，否则录制视频可能是黑屏。
false - 录制大画面。

默认为 false。
        :type PullSmallVideo: bool
        """
        self.StreamId = None
        self.DisableRecord = None
        self.DisableAudio = None
        self.PullSmallVideo = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.DisableRecord = params.get("DisableRecord")
        self.DisableAudio = params.get("DisableAudio")
        self.PullSmallVideo = params.get("PullSmallVideo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamLayout(AbstractModel):
    """流布局参数

    """

    def __init__(self):
        r"""
        :param LayoutParams: 流布局配置参数
        :type LayoutParams: :class:`tencentcloud.tiw.v20190919.models.LayoutParams`
        :param InputStreamId: 视频流ID
流ID的取值含义如下：
1. tic_record_user - 表示当前画面用于显示白板视频流
2. tic_substream - 表示当前画面用于显示辅路视频流
3. 特定用户ID - 表示当前画面用于显示指定用户的视频流
4. 不填 - 表示当前画面用于备选，当有新的视频流加入时，会从这些备选的空位中选择一个没有被占用的位置来显示新的视频流画面
        :type InputStreamId: str
        :param BackgroundColor: 背景颜色，默认为黑色，格式为RGB格式，如红色为"#FF0000"
        :type BackgroundColor: str
        :param FillMode: 视频画面填充模式。

0 - 自适应模式，对视频画面进行等比例缩放，在指定区域内显示完整的画面。此模式可能存在黑边。
1 - 全屏模式，对视频画面进行等比例缩放，让画面填充满整个指定区域。此模式不会存在黑边，但会将超出区域的那一部分画面裁剪掉。
        :type FillMode: int
        """
        self.LayoutParams = None
        self.InputStreamId = None
        self.BackgroundColor = None
        self.FillMode = None


    def _deserialize(self, params):
        if params.get("LayoutParams") is not None:
            self.LayoutParams = LayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        self.InputStreamId = params.get("InputStreamId")
        self.BackgroundColor = params.get("BackgroundColor")
        self.FillMode = params.get("FillMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeValue(AbstractModel):
    """查询指标返回的时间序列

    """

    def __init__(self):
        r"""
        :param Time: Unix时间戳，单位秒
        :type Time: int
        :param Value: 查询指标对应当前时间的值
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTaskResult(AbstractModel):
    """转码任务结果

    """

    def __init__(self):
        r"""
        :param ResultUrl: 转码结果地址
        :type ResultUrl: str
        :param Resolution: 分辨率
        :type Resolution: str
        :param Title: 标题（一般为文件名）
        :type Title: str
        :param Pages: 转码页数
        :type Pages: int
        :param ThumbnailUrl: 缩略图URL前缀，比如，该URL前缀为http://example.com/g0jb42ps49vtebjshilb/，那么动态PPT第1页的缩略图URL为
http://example.com/g0jb42ps49vtebjshilb/1.jpg，其它页以此类推

如果发起文档转码请求参数中带了ThumbnailResolution参数，并且转码类型为动态转码，该参数不为空，其余情况该参数为空字符串
        :type ThumbnailUrl: str
        :param ThumbnailResolution: 动态转码缩略图生成分辨率
        :type ThumbnailResolution: str
        :param CompressFileUrl: 转码压缩文件下载的URL，如果发起文档转码请求参数中CompressFileType为空或者不是支持的压缩格式，该参数为空字符串
        :type CompressFileUrl: str
        :param ErrorCode: 任务失败错误码
        :type ErrorCode: int
        :param ErrorMsg: 任务失败错误信息
        :type ErrorMsg: str
        """
        self.ResultUrl = None
        self.Resolution = None
        self.Title = None
        self.Pages = None
        self.ThumbnailUrl = None
        self.ThumbnailResolution = None
        self.CompressFileUrl = None
        self.ErrorCode = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.ResultUrl = params.get("ResultUrl")
        self.Resolution = params.get("Resolution")
        self.Title = params.get("Title")
        self.Pages = params.get("Pages")
        self.ThumbnailUrl = params.get("ThumbnailUrl")
        self.ThumbnailResolution = params.get("ThumbnailResolution")
        self.CompressFileUrl = params.get("CompressFileUrl")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTaskSearchResult(AbstractModel):
    """转码任务搜索结果

    """

    def __init__(self):
        r"""
        :param CreateTime: 任务创建时间
        :type CreateTime: str
        :param TaskId: 任务唯一ID
        :type TaskId: str
        :param Status: 任务的当前状态
- QUEUED: 正在排队等待转换
- PROCESSING: 转换中
- FINISHED: 转换完成
        :type Status: str
        :param OriginalFilename: 转码文件原始名称
        :type OriginalFilename: str
        :param SdkAppId: 用户应用SdkAppId
        :type SdkAppId: int
        :param Result: 转码任务结果
        :type Result: :class:`tencentcloud.tiw.v20190919.models.TranscodeTaskResult`
        :param IsStatic: 是否静态转码
        :type IsStatic: bool
        """
        self.CreateTime = None
        self.TaskId = None
        self.Status = None
        self.OriginalFilename = None
        self.SdkAppId = None
        self.Result = None
        self.IsStatic = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.OriginalFilename = params.get("OriginalFilename")
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Result") is not None:
            self.Result = TranscodeTaskResult()
            self.Result._deserialize(params.get("Result"))
        self.IsStatic = params.get("IsStatic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageDataItem(AbstractModel):
    """互动白板用量信息

    """

    def __init__(self):
        r"""
        :param Time: 日期，格式为YYYY-MM-DD
        :type Time: str
        :param SdkAppId: 白板应用SDKAppID
        :type SdkAppId: int
        :param SubProduct: 互动白板子产品，请求参数传入的一致
- sp_tiw_board: 互动白板时长
- sp_tiw_dt: 动态转码页数
- sp_tiw_st: 静态转码页数
- sp_tiw_ric: 实时录制时长
        :type SubProduct: str
        :param Value: 用量值
- 静态转码、动态转码单位为页
- 白板时长、实时录制时长单位为分钟
        :type Value: float
        """
        self.Time = None
        self.SdkAppId = None
        self.SubProduct = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.SdkAppId = params.get("SdkAppId")
        self.SubProduct = params.get("SubProduct")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserListItem(AbstractModel):
    """日志查询里返回的白板用户数据

    """

    def __init__(self):
        r"""
        :param UserId: 房间内的用户ID
        :type UserId: str
        :param StartTime: 用户在查询时间段内最早出现的时间，Unix时间戳，单位毫秒
        :type StartTime: int
        :param EndTime: 用户在查询时间段内最晚出现的时间，Unix时间戳，单位毫秒
        :type EndTime: int
        """
        self.UserId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoInfo(AbstractModel):
    """视频信息

    """

    def __init__(self):
        r"""
        :param VideoPlayTime: 视频开始播放的时间（单位：毫秒）
        :type VideoPlayTime: int
        :param VideoSize: 视频大小（字节）
        :type VideoSize: int
        :param VideoFormat: 视频格式
        :type VideoFormat: str
        :param VideoDuration: 视频播放时长（单位：毫秒）
        :type VideoDuration: int
        :param VideoUrl: 视频文件URL
        :type VideoUrl: str
        :param VideoId: 视频文件Id
        :type VideoId: str
        :param VideoType: 视频流类型 
- 0：摄像头视频 
- 1：屏幕分享视频
- 2：白板视频 
- 3：混流视频
- 4：纯音频（mp3)
        :type VideoType: int
        :param UserId: 摄像头/屏幕分享视频所属用户的 Id（白板视频为空、混流视频tic_mixstream_房间号_混流布局类型、辅路视频tic_substream_用户Id）
        :type UserId: str
        :param Width: 视频分辨率的宽
        :type Width: int
        :param Height: 视频分辨率的高
        :type Height: int
        """
        self.VideoPlayTime = None
        self.VideoSize = None
        self.VideoFormat = None
        self.VideoDuration = None
        self.VideoUrl = None
        self.VideoId = None
        self.VideoType = None
        self.UserId = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.VideoPlayTime = params.get("VideoPlayTime")
        self.VideoSize = params.get("VideoSize")
        self.VideoFormat = params.get("VideoFormat")
        self.VideoDuration = params.get("VideoDuration")
        self.VideoUrl = params.get("VideoUrl")
        self.VideoId = params.get("VideoId")
        self.VideoType = params.get("VideoType")
        self.UserId = params.get("UserId")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Whiteboard(AbstractModel):
    """实时录制白板参数，例如白板宽高等

    """

    def __init__(self):
        r"""
        :param Width: 实时录制结果里白板视频宽，取值必须大于等于2，默认为1280
        :type Width: int
        :param Height: 实时录制结果里白板视频高，取值必须大于等于2，默认为960
        :type Height: int
        :param InitParam: 白板初始化参数，透传到白板 SDK
        :type InitParam: str
        """
        self.Width = None
        self.Height = None
        self.InitParam = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.InitParam = params.get("InitParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardApplicationConfig(AbstractModel):
    """白板应用配置，包括资源存储桶，域名，回调地址，回调密钥等

    """

    def __init__(self):
        r"""
        :param TaskType: 任务类型

recording: 实时录制
transcode: 文档转码
        :type TaskType: str
        :param BucketName: 存储桶名字
        :type BucketName: str
        :param BucketLocation: 存储桶地域
        :type BucketLocation: str
        :param BucketPrefix: 资源在存储桶中的前缀
        :type BucketPrefix: str
        :param ResultDomain: 目标CDN域名
        :type ResultDomain: str
        :param Callback: 回调地址
        :type Callback: str
        :param CallbackKey: 回调鉴权密钥
        :type CallbackKey: str
        :param SdkAppId: 配置的应用SdkAppId
        :type SdkAppId: int
        :param AdminUserId: IM管理员UserId
        :type AdminUserId: str
        :param AdminUserSig: IM管理员UserSig
        :type AdminUserSig: str
        """
        self.TaskType = None
        self.BucketName = None
        self.BucketLocation = None
        self.BucketPrefix = None
        self.ResultDomain = None
        self.Callback = None
        self.CallbackKey = None
        self.SdkAppId = None
        self.AdminUserId = None
        self.AdminUserSig = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.BucketName = params.get("BucketName")
        self.BucketLocation = params.get("BucketLocation")
        self.BucketPrefix = params.get("BucketPrefix")
        self.ResultDomain = params.get("ResultDomain")
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
        self.SdkAppId = params.get("SdkAppId")
        self.AdminUserId = params.get("AdminUserId")
        self.AdminUserSig = params.get("AdminUserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardPushBackupParam(AbstractModel):
    """白板推流备份相关请求参数

    """

    def __init__(self):
        r"""
        :param PushUserId: 用于白板推流服务进房的用户ID，
该ID必须是一个单独的未在SDK中使用的ID，白板推流服务将使用这个用户ID进入房间进行白板推流，若该ID和SDK中使用的ID重复，会导致SDK和录制服务互踢，影响正常推流。
        :type PushUserId: str
        :param PushUserSig: 与PushUserId对应的签名
        :type PushUserSig: str
        """
        self.PushUserId = None
        self.PushUserSig = None


    def _deserialize(self, params):
        self.PushUserId = params.get("PushUserId")
        self.PushUserSig = params.get("PushUserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardPushResult(AbstractModel):
    """白板推流任务结果

    """

    def __init__(self):
        r"""
        :param FinishReason: AUTO - 自动停止推流， USER_CALL - 用户主动调用停止推流
        :type FinishReason: str
        :param ExceptionCnt: 异常数
        :type ExceptionCnt: int
        :param RoomId: 房间号
        :type RoomId: int
        :param GroupId: IM群组ID
        :type GroupId: str
        :param PushStartTime: 推流真实开始时间
        :type PushStartTime: int
        :param PushStopTime: 推流结束时间
        :type PushStopTime: int
        :param IMSyncTime: 白板推流首帧对应的IM时间戳，可用于录制回放时IM聊天消息与白板推流视频进行同步对时。
        :type IMSyncTime: int
        :param ErrorCode: 任务失败错误码
        :type ErrorCode: int
        :param ErrorMsg: 错误信息
        :type ErrorMsg: str
        """
        self.FinishReason = None
        self.ExceptionCnt = None
        self.RoomId = None
        self.GroupId = None
        self.PushStartTime = None
        self.PushStopTime = None
        self.IMSyncTime = None
        self.ErrorCode = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.FinishReason = params.get("FinishReason")
        self.ExceptionCnt = params.get("ExceptionCnt")
        self.RoomId = params.get("RoomId")
        self.GroupId = params.get("GroupId")
        self.PushStartTime = params.get("PushStartTime")
        self.PushStopTime = params.get("PushStopTime")
        self.IMSyncTime = params.get("IMSyncTime")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardPushTaskSearchResult(AbstractModel):
    """实时录制任务搜索结果

    """

    def __init__(self):
        r"""
        :param TaskId: 任务唯一ID
        :type TaskId: str
        :param Status: 白板推流任务状态
- PREPARED: 推流在准备阶段
- PUSHING: 正在推流
- STOPPED：推流已停止
        :type Status: str
        :param RoomId: 白板推流房间号
        :type RoomId: int
        :param CreateTime: 任务创建时间
        :type CreateTime: str
        :param SdkAppId: 用户应用SdkAppId
        :type SdkAppId: int
        :param Result: 白板推流结果
        :type Result: :class:`tencentcloud.tiw.v20190919.models.WhiteboardPushResult`
        :param PushUserId: 白板推流用户ID
        :type PushUserId: str
        """
        self.TaskId = None
        self.Status = None
        self.RoomId = None
        self.CreateTime = None
        self.SdkAppId = None
        self.Result = None
        self.PushUserId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.RoomId = params.get("RoomId")
        self.CreateTime = params.get("CreateTime")
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Result") is not None:
            self.Result = WhiteboardPushResult()
            self.Result._deserialize(params.get("Result"))
        self.PushUserId = params.get("PushUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        