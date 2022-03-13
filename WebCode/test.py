import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "face_end.settings")
django.setup()
import glob
from lib import fd_clibrary, fg_clibrary, fa_clibrary, ff_clibrary
from lib.face_detect_sdk_library import *
from lib.face_age_sdk_library import *
from lib.face_gender_sdk_library import *
from lib.face_recognition_sdk_library import *
from util import image_loader
from conf.config import *
import traceback
import time
import base64
import sys
from app.models import UserInfor,sudo,staff
from socket import *
APP_ID = c_char_p(bytes(config.get('arcsoft', 'APP_ID'), encoding='utf-8'))
FD_SDK_KEY = c_char_p(bytes(config.get('arcsoft', 'FD_SDK_KEY'), encoding='utf-8'))
FASE_SDK_KEY = c_char_p(bytes(config.get('arcsoft', 'FASE_SDK_KEY'), encoding='utf-8'))
FSGE_SDK_KEY = c_char_p(bytes(config.get('arcsoft', 'FSGE_SDK_KEY'), encoding='utf-8'))
FAFR_SDK_KEY = c_char_p(bytes(config.get('arcsoft', 'FAFR_SDK_KEY'), encoding='utf-8'))

WORKBUF_SIZE = 50 * 1024 * 1024
MAX_FACE_NUM = 10
bUseYUVFile = False
bUseBGRToEngine = True

fd_engine = None
fa_engine = None
fg_engine = None
ff_engine = None

def init_face_engine():
    global fd_engine
    fd_work_memery = fd_clibrary.malloc(c_size_t(WORKBUF_SIZE))
    fd_engine = c_void_p()
    ret = AFD_FSDK_InitialFaceEngine(APP_ID, FD_SDK_KEY, fd_work_memery, c_int32(WORKBUF_SIZE), byref(fd_engine),
                                     AFD_FSDK_OPF_0_HIGHER_EXT, 32, MAX_FACE_NUM)

    if ret != 0:
        fd_clibrary.free(fd_work_memery)
        print(u'AFD_FSDK_InitialFaceEngine ret 0x{:x}'.format(ret))
        exit(0)


def init_face_age_engine():
    global fa_engine
    fa_work_memery = fa_clibrary.malloc(c_size_t(WORKBUF_SIZE))
    fa_engine = c_void_p()
    ret = ASAE_FSDK_InitAgeEngine(APP_ID, FASE_SDK_KEY, fa_work_memery, c_int32(WORKBUF_SIZE), byref(fa_engine))
    if ret != 0:
        fa_clibrary.free(fa_work_memery)
        print(u'ASAE_FSDK_InitAgeEngine ret 0x{:x}'.format(ret))
        exit(0)


def init_face_gender_engine():
    global fg_engine
    fg_work_memery = fg_clibrary.malloc(c_size_t(WORKBUF_SIZE))
    fg_engine = c_void_p()
    ret = ASGE_FSDK_InitGenderEngine(APP_ID, FSGE_SDK_KEY, fg_work_memery, c_int32(WORKBUF_SIZE), byref(fg_engine))
    if ret != 0:
        fg_clibrary.free(fg_work_memery)
        print(u'ASGE_FSDK_InitGenderEngine ret 0x{:x}'.format(ret))
        exit(0)

def init_face_recognition_engine():
    global ff_engine
    ff_work_memery = ff_clibrary.malloc(c_size_t(WORKBUF_SIZE))
    ff_engine = c_void_p()
    ret = AFR_FSDK_InitialEngine(APP_ID, FAFR_SDK_KEY, ff_work_memery, c_int32(WORKBUF_SIZE), byref(ff_engine))
    if ret != 0:
        ff_clibrary.free(ff_work_memery)
        print(u'AFR_FSDK_InitialEngine ret 0x{:x}'.format(ret))
        exit(0)

def do_face_detection(fd_engine, image):
    face_res = POINTER(AFD_FSDK_FACERES)()
    ret = AFD_FSDK_StillImageFaceDetection(fd_engine, byref(image), byref(face_res))

    if ret != 0:
        print(u'AFD_FSDK_StillImageFaceDetection 0x{0:x}'.format(ret))
        return 0, [], []

    faces = face_res.contents
    face_num = faces.nFace
    #print('{} 个人脸'.format(face_num))
    dan_face = faces.rcFace[0]
    dan_orient = faces.lfaceOrient[0]
    if face_num > 0:
        return face_num, faces.rcFace, faces.lfaceOrient, dan_face, dan_orient


def do_face_age_estimation(fd_engine, fa_engine, image):
    face_num, rect_info, orient_info, dan_face, dan_orient = do_face_detection(fd_engine, image)
    age_face_input = ASAE_FSDK_AGEFACEINPUT()  # 定義臉部信息
    age_face_input.lFaceNumber = face_num
    age_face_input.pFaceRectArray = rect_info
    age_face_input.pFaceOrientArray = orient_info
    age_result = ASAE_FSDK_AGERESULT()  # 定義年齡檢測結果信息
    ret = ASAE_FSDK_AgeEstimation_StaticImage(fa_engine, byref(image), byref(age_face_input),
                                              byref(age_result))

    if ret != 0:
        print(u'ASAE_FSDK_AgeEstimation_StaticImage 0x{0:x}'.format(ret))
        return []

    return age_result


def do_face_gender_estimation(fd_engine, fg_engine, image):
    face_num, rect_info, orient_info, dan_face, dan_orient = do_face_detection(fd_engine, image)
    gender_face_input = ASGE_FSDK_GENDERFACEINPUT()
    gender_face_input.lFaceNumber = face_num
    gender_face_input.pFaceRectArray = rect_info
    gender_face_input.pFaceOrientArray = orient_info
    gender_result = ASGE_FSDK_GENDERRESULT()
    ret = ASGE_FSDK_GenderEstimation_StaticImage(fg_engine, byref(image), byref(gender_face_input),
                                                 byref(gender_result))
    if ret != 0:
        print(u'ASGE_FSDK_GenderEstimation_StaticImage 0x{0:x}'.format(ret))
        return []
    return gender_result

#feature
def do_face_feature(fd_engine,ff_engine, image):
    face_num, rect_info, orient_info, dan_face, dan_orient = do_face_detection(fd_engine, image)
    recognition_face_input = AFR_FSDK_FACEINPUT()
    recognition_face_input.rcFace = dan_face
    recognition_face_input.IOrient = dan_orient
    # print(dan_face.left,'aaa')
    # print(dan_orient,'bbb')

    recognition_feature_result = AFR_FSDK_FACEMODEL()
    ret = AFR_FSDK_ExtractFRFeature(ff_engine, image, recognition_face_input,recognition_feature_result)
    #print(type(recognition_feature_result))
    if ret != 0:
        print(u'AFR_FSDK_ExtractFRFeature 0x{0:x}'.format(ret))
        return []

    try:
        return recognition_feature_result.deepCopy()
    except Exception as e:
        traceback.print_exc()
        print('error')
        return None

#recognition
def do_face_recognition(ff_engine, feature_ku, feature_bi):
    #score = AFR_FSDK_FACE_DUIBI()
    score = c_float()
    ret = AFR_FSDK_FacePairMatching(ff_engine, feature_ku, feature_bi,byref(score))
    if ret != 0:
        print(u'AFR_FSDK_FacePairMatching 0x{0:x}'.format(ret))
        return []
    return score


def main():

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'face_end.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    ##open client
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    tcp_client_socket.connect(("192.168.43.28", 20000))
    ####init sdk
    init_face_engine()
    init_face_age_engine()
    init_face_gender_engine()
    init_face_recognition_engine()



    dir_image_ku = sudo.objects.all()
    num = len(dir_image_ku)
    for i in range(num):
        temp = sudo.objects.values().get(id=i)
        temp_str = temp['photo_ku']
        image_temp = base64.b64decode(temp_str)
        file = open('image_ku/{}.jpg'.format(i+1), 'wb')
        file.write(image_temp)
        file.close()

    # time.sleep(3)
    while True:
        ##jiancha station
        all_object = UserInfor.objects.all()
        num = len(all_object)
        if num == 1:
            sta = UserInfor.objects.values().last()

            station = sta['station']
            if station == 1:
                dir_image = UserInfor.objects.values().last()
                image_str = dir_image['photo']
                image = base64.b64decode(image_str)
                file = open('image/test.jpg', 'wb')
                file.write(image)
                file.close()

                file_path = 'image/test.jpg'
                image = image_loader.load_image(bUseBGRToEngine, file_path)
                image_feature = do_face_feature(fd_engine, ff_engine, image)
                file_ku_path = glob.glob(r"image_ku/*.jpg")
                len_ku = len(file_ku_path)
                image_ku = [0] * len_ku
                for i in range(len_ku):
                    # image_ku[i] = image_loader.load_image(bUseBGRToEngine, file_ku_path[i])
                    image_ku[i] = image_loader.load_image(bUseBGRToEngine, "image_ku/{}.jpg".format(i+1))

                my_score = [0] * len_ku
                zhixingdu = [0] * len_ku
                for i in range(len_ku):
                    temp_feature = do_face_feature(fd_engine, ff_engine, image_ku[i])
                    my_score[i] = do_face_recognition(ff_engine, temp_feature, image_feature)
                    # print(my_score[i].value)
                    zhixingdu[i] = my_score[i].value

                grade = max(zhixingdu)
                weizhi = zhixingdu.index(max(zhixingdu))
                if (grade > 0.7):
                    print('yes')
                    meg = 'y'
                    temp2 = sudo.objects.values('name').get(id=weizhi)
                    name = temp2['name']
                    staff.objects.create(user_name=name)
                    tcp_client_socket.send(meg.encode())
                    UserInfor.objects.all().delete()

                else:
                    print('no')
                    UserInfor.objects.all().delete()

            else:
                pass
        else:
            time.sleep(0.1)

    ASAE_FSDK_UninitAgeEngine(fa_engine)
    ASGE_FSDK_UninitGenderEngine(fg_engine)
    AFD_FSDK_UninitialFaceEngine(fd_engine)
    AFR_FSDK_UninitialEngine(ff_engine)


if __name__ == '__main__':
    main()
