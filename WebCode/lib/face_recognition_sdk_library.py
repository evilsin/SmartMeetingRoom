# -*- encoding=utf-8 -*-
from . import MRECT, ASVLOFFSCREEN
from . import fr_clibrary
from .fr_clibrary import *
# 定义臉部信息
class AFR_FSDK_FACEINPUT(Structure):
    _fields_ = [(u'rcFace', MRECT), (u'IOrient', c_int32)]


# 定义脸部feature信息
class AFR_FSDK_FACEMODEL(Structure):
    _fields_ = [(u'pbFeature', c_void_p), (u'IFeatureSize', c_int32)]

    def __init__(self):
        self.bAllocByMalloc = False
        Structure.__init__(self)

    def deepCopy(self):
        if (self.pbFeature == 0):
            raise Exception(u'invalid feature')
        feature = AFR_FSDK_FACEMODEL()
        feature.bAllocByMalloc = True
        feature.IFeatureSize = self.IFeatureSize
        feature.pbFeature = fr_clibrary.malloc(feature.IFeatureSize)
        fr_clibrary.memcpy(feature.pbFeature, self.pbFeature, feature.IFeatureSize)
        return feature

    def freeUnmanaged(self):
        if self.bAllocByMalloc and (self.pbFeature != 0):
            fr_clibrary.free(self.pbFeature)
            self.pbFeature = 0

    def __del__(self):
        self.freeUnmanaged()
        # print(u'gc feature freeUnmanaged')

    @staticmethod
    def fromByteArray(byteArrayFeature):
        if byteArrayFeature == None:
            raise Exception(u'invalid byteArray')
        feature = AFR_FSDK_FACEMODEL()
        feature.lFeatureSize = len(byteArrayFeature)
        feature.bAllocByMalloc = True
        featureData = create_string_buffer(byteArrayFeature)
        feature.pbFeature = fr_clibrary.malloc(feature.lFeatureSize)
        fr_clibrary.memcpy(feature.pbFeature, cast(featureData, c_void_p), feature.lFeatureSize)
        return feature

    def toByteArray(self):
        if (self.pbFeature == 0):
            raise Exception(u'invalid feature')
        featureData = create_string_buffer(self.lFeatureSize)
        fr_clibrary.memcpy(cast(featureData, c_void_p), self.pbFeature, self.lFeatureSize)
        return bytes(bytearray(featureData))

#my result
#class AFR_FSDK_FACE_DUIBI(Structure):
#    _fields_ = [(u'pfSimiScore',POINTER(c_void_p))]

# 定义版本信息
class AFR_FSDK_VERSION(Structure):
    _fields_ = [(u'lCodebase', c_int32), (u'lMajor', c_int32), (u'lMinor', c_int32), (u'lBuild', c_int32),
                (u'Version', c_char_p), (u'BuildDate', c_char_p), (u'CopyRight', c_char_p)]


# 定义脸部角度的检测范围
AFR_FSDK_OPF_0_ONLY = 0x1  # 0; 0; ...
AFR_FSDK_OPF_90_ONLY = 0x2  # 90; 90; ...
AFR_FSDK_OPF_270_ONLY = 0x3  # 270; 270; ...
AFR_FSDK_OPF_180_ONLY = 0x4  # 180; 180; ...
AFR_FSDK_OPF_0_HIGHER_EXT = 0x5  # 0; 90; 270; 180; 0; 90; 270; 180; ...

# 定义人脸检测结果中的人脸角度
AFR_FSDK_FOC_0 = 0x1  # 0 degree
AFR_FSDK_FOC_90 = 0x2  # 90 degree
AFR_FSDK_FOC_270 = 0x3  # 270 degree
AFR_FSDK_FOC_180 = 0x4  # 180 degree
AFR_FSDK_FOC_30 = 0x5  # 30 degree
AFR_FSDK_FOC_60 = 0x6  # 60 degree
AFR_FSDK_FOC_120 = 0x7  # 120 degree
AFR_FSDK_FOC_150 = 0x8  # 150 degree
AFR_FSDK_FOC_210 = 0x9  # 210 degree
AFR_FSDK_FOC_240 = 0xa  # 240 degree
AFR_FSDK_FOC_300 = 0xb  # 300 degree
AFR_FSDK_FOC_330 = 0xc  # 330 degree


AFR_FSDK_InitialEngine = internal_library.AFR_FSDK_InitialEngine
AFR_FSDK_UninitialEngine = internal_library.AFR_FSDK_UninitialEngine
AFR_FSDK_ExtractFRFeature = internal_library.AFR_FSDK_ExtractFRFeature
AFR_FSDK_FacePairMatching = internal_library.AFR_FSDK_FacePairMatching
AFR_FSDK_GetVersion = internal_library.AFR_FSDK_GetVersion

AFR_FSDK_InitialEngine.restype = c_long
AFR_FSDK_InitialEngine.argtypes = (c_char_p, c_char_p, c_void_p, c_int32, POINTER(c_void_p))
AFR_FSDK_UninitialEngine.restype = c_long
AFR_FSDK_UninitialEngine.argtypes = (c_void_p,)
AFR_FSDK_ExtractFRFeature.restype = c_long
AFR_FSDK_ExtractFRFeature.argtypes = (
    c_void_p,POINTER(ASVLOFFSCREEN), POINTER(AFR_FSDK_FACEINPUT), POINTER(AFR_FSDK_FACEMODEL))
AFR_FSDK_FacePairMatching.restype = c_long
AFR_FSDK_FacePairMatching.argtypes = (
    c_void_p, POINTER(AFR_FSDK_FACEMODEL), POINTER(AFR_FSDK_FACEMODEL),POINTER(c_float))
AFR_FSDK_GetVersion.restype = POINTER(AFR_FSDK_VERSION)
AFR_FSDK_GetVersion.argtypes = (c_void_p,)