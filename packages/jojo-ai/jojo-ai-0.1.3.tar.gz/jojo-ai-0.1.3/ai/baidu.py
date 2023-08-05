#!/usr/bin/python
# coding:utf-8
#
# Baidu class is to access AI APIs of Baidu
#
# Author: JoStudio

import sys
import requests
import base64
import os

try:
    import playsound
except ImportError:
    playsound = None


IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    import urllib2
    from urllib import quote_plus
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import URLError
    from urllib import urlencode


class Utils:
    @staticmethod
    def read_file(file_name, is_base64=False):
        """
        读取文件，返回文件内容

        :param file_name: 文件名
        :param is_base64: （可选)是否 base64编码，默认为False
        :return: 返回一个元组(文件长度, 文件内容数据)
        """
        with open(file_name, 'rb') as file1:
            data = file1.read()
            length = len(data)
            if is_base64:
                return length, base64.b64encode(data)
            else:
                return length, data

    @staticmethod
    def save_file(file_name, content):
        """
        保存文件
        :param file_name: 文件名
        :param content: 文件内容数据
        :return: None
        """
        with open(file_name, 'wb') as of:
            of.write(content)

    @staticmethod
    def is_url(url):
        url = url.lower()
        if url[0:7] == 'http://' or url[0:8] == 'https://':
            return True
        return False


class BaiduAI:
    """
    百度AI APIs

    """

    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.token = ''
        self.raw_result = False  # 返回值是否百度原始数据结果
        self.cuid = '123456PYTHON'  # 用户唯一标识，用来区分用户
        self.temp_audio_file = 'temp.wav'  # 语音临时文件

    def _get_token(self, api_key, secret_key):
        """
        获取 access token

        :param api_key:   平台提供的 API_KEY
        :param secret_key: 平台提供的 SECRET_KEY
        :return:
        """
        self.token = ''  # 将当前token清空

        # 请求 access_token 的 url 和 参数
        url = 'https://aip.baidubce.com/oauth/2.0/token'
        params = {
            'grant_type': 'client_credentials',
            'client_id': api_key,
            'client_secret': secret_key
        }

        # 发起请求
        response = requests.get(url, params=params)
        if response:
            self.token = response.json()['access_token']
            return self.token
        raise ConnectionError('Baidu AI 获取 token 失败')

    def _update_token(self):
        """ 更新access token，确保其有效 """
        self._get_token(self.api_key, self.secret_key)

    def _correct_keys(self, err):
        """ 纠正Key名 """
        if type(err) == dict:
            if 'err_no' in err:
                err['error_code'] = err['err_no']
                del err['err_no']
            if 'err_msg' in err:
                err['error_msg'] = err['err_msg']
                del err['err_msg']
        return err

    def _error(self, err, err_msg=''):
        """ 返回错误值 """
        if type(err) != dict:
            err = {'error_code': err, 'error_msg': err_msg}
        else:
            err = self._correct_keys(err)

        if self.raw_result:
            return err
        else:
            raise RuntimeError(str(err['error_code']) + ' ' + err['error_msg'])

    def _result(self, response_json, key):
        """ 从响应JSON值中取得返回结果 """
        if self.raw_result or type(response_json) != dict:
            return response_json
        else:
            response_json = self._correct_keys(response_json)
            if 'error_code' not in response_json or response_json['error_code'] == 0:
                if key in response_json:
                    return response_json[key]
                else:
                    return response_json
            else:
                return self._error(response_json)

    def asr(self, audio_filename):
        """
        语音转文字

        API文档: https://ai.baidu.com/ai-doc/SPEECH/Vk38lxily

        :param audio_filename: 语音文件名，格式可以是 .wav, .mp3, .amr, .m4a.
                    必须是16000采样率、单声道
        :return: 返回文字结果
        """
        self._update_token()  # 首先，检查access token

        # 读取语音文件数据
        file_length, file_content = Utils.read_file(audio_filename, True)
        file_content = str(file_content, 'utf-8')

        # 请求参数
        params = {
            'dev_pid': 1537,  # 输入法模型 1537表示识别普通话
            'format': audio_filename[-3:],  # 语音格式: 文件后缀名3个字符，pcm/wav/amr/m4a
            'rate': 16000,  # 采样率，16000、8000，固定值
            'token': self.token,  # 获取到的 access_token
            'cuid': self.cuid,  # 用户唯一标识，用来区分用户，计算UV值。建议填写能区分用户的机器 MAC 地址或 IMEI
            'channel': 1,  # 声道数，仅支持单声道，请填写固定值 1
            'speech': file_content,  # 语音文件的二进制语音数据 ，需要进行base64 编码
            'len': file_length  # 语音文件的的字节数
        }

        # 发起请求
        asr_url = 'http://vop.baidu.com/server_api'
        response = requests.post(asr_url, json=params)
        if response:
            return self._result(response.json(), 'result')
        return self._error(500, 'error request Baidu ASR')

    def tts(self, text, save_filename='', person=0, speed=5, volume=5, pitch=5):
        """
        文字转语音

        API文档: https://cloud.baidu.com/doc/SPEECH/s/Gk38y8lzk

        :param text: 文字
        :param save_filename: 存盘文件名。如文件名为空，则直接播放声音。
        :param person: (可选) 说话人， 可以是：‘小美’，'小宇’，‘逍遥’，‘丫丫’, '小鹿', '博文', '小童', '小萌', '米朵', '小娇'
        :param speed: (可选)语速，取值0-15，默认为5中语速
        :param volume: (可选) 音量，取值0-15，默认为5中音量（取值为0时为音量最小值，并非为无声）
        :param pitch:  (可选) 音调，取值0-15，默认为5中语调
        :return: 返回存盘文件名. 如该文件名为空，则直接播放声音。
        """
        self._update_token()  # 首先，检查access token

        if not save_filename:
            save_filename = self.temp_audio_file

        # 支持的音频格式， 3为mp3格式(默认)； 4为pcm-16k；5为pcm-8k；6为wav
        formats = {"mp3": 3, "pcm": 4, "wav": 6}
        # 根据存盘文件扩展名判断音频格式
        file_ext = save_filename[-3:].lower()
        if file_ext in formats:
            audio_format = formats[file_ext]
        else:
            return self._error(501, f'音频格式 {file_ext} 不支持')

        # 讲话人
        persons = {"小美": 3, "小宇": 4, "逍遥": 3, "丫丫": 4, "小鹿": 5118,
                   "博文": 106, "小童": 110, "小萌": 111, "米朵": 103, "小娇": 5}
        if type(person) == int:
            pass
        elif person == '':
            person = 0
        else:
            # 去掉首字“度"
            if type(person) == str and person[0:1] == '度':
                person = person[1:]
            if person in persons:
                person = persons[person]
            else:
                return self._error(502, f'讲话人 {person} 不存在')

        # TEXT需要quote_plus
        text = quote_plus(text)

        # 请求参数
        params = {
            'tok': self.token,
            'tex': text,  # 合成的文本，文本长度必须小于1024GBK字节
            'per': person,  # 说话人, 度小宇=1，度小美=0，度逍遥（基础）=3，度丫丫=4
            'spd': speed,  # 语速，取值0-15，默认为5中语速
            'pit': pitch,  # 音调，取值0-15，默认为5中语调
            'vol': volume,  # 音量，取值0-15，默认为5中音量（取值为0时为音量最小值，并非为无声）
            'aue': audio_format,  # 音频格式， 3为mp3格式(默认)； 4为pcm-16k；5为pcm-8k；6为wav
            'cuid': self.cuid,
            'lan': 'zh',  # 语言选择,目前只有中英文混合模式，填写固定值zh
            'ctp': 1  # 客户端类型选择，web端填写固定值1
        }

        # 发起请求
        tts_url = 'http://tsn.baidu.com/text2audio'
        data = urlencode(params)
        response = requests.post(tts_url, data=data.encode('utf-8'))

        if response:
            content_type = response.headers['Content-Type']
            # 如果响应内容的类型为 audio
            if content_type.find('audio/') >= 0:
                # 则存盘为文件
                Utils.save_file(save_filename, response.content)
                if save_filename == self.temp_audio_file and playsound is not None:
                    # noinspection PyBroadException
                    try:
                        playsound.playsound(save_filename)
                        os.remove(self.temp_audio_file)
                    except Exception:
                        pass
                return save_filename
            else:
                return self._error(response.json())
        return self._error(500, '请求 Baidu TTS 失败')

    def _ocr_api(self, image_file, api_url, add_params=None, result_key=''):
        """
        文字识别

        :param image_file: 图片文件名或URL
        :param api_url: API 所在 URL
        :param add_params: 添加的查询参数
        :param result_key: 结果只取返回dict中指定的Key（为空则返回整个dict)
        :return: 返回识别结果
        """
        self._update_token()  # 首先，检查access token

        if Utils.is_url(image_file):
            # image_file 是一个URL
            params = {"url": image_file}
        else:
            # image_file 是一个文件, 读取图片文件
            file_length, file_content = Utils.read_file(image_file, True)
            params = {"image": file_content}

        if type(add_params) == dict:
            for k in add_params:
                params[k] = add_params[k]

        request_url = api_url + "?access_token=" + self.token
        headers = {'content-type': 'application/x-www-form-urlencoded'}

        # 请求
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            return self._result(response.json(), result_key)

        return self._error(500, 'error request Baidu OCR')

    def ocr(self, image_file):
        """
        通用文字识别

        API文档: https://ai.baidu.com/ai-doc/OCR/zk3h7xz52

        :param image_file: 图片文件名或URL
        :return: 返回文字识别结果
        """
        return self._ocr_api(image_file, "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic",
                             None, 'words_result')

    def ocr_id_card(self, image_file):
        """
        身份证识别

        API文档: https://ai.baidu.com/ai-doc/OCR/rk3h7xzck

        :param image_file: 身份证图片文件名或URL
        :return: 返回识别结果
        """
        params = {'id_card_side': 'front', 'detect_photo': 'true'}
        return self._ocr_api(image_file, "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard",
                             params)

    def ocr_bank_card(self, image_file):
        """
        银行卡识别

        API文档: https://ai.baidu.com/ai-doc/OCR/ak3h7xxg3

        :param image_file: 图片文件名或URL
        :return: 返回识别结果
        """
        return self._ocr_api(image_file, "https://aip.baidubce.com/rest/2.0/ocr/v1/bankcard",
                             None, 'result')

    def _get_image(self, image_file):
        """返回一张图片数据"""
        if Utils.is_url(image_file):
            # 当 image_file 是一个URL
            params = {"url": image_file, 'image_type': 'URL'}
        elif image_file.find('.') >= 0:
            # 当 image_file 是一个文件, 读取图片文件
            file_length, file_content = Utils.read_file(image_file, True)
            params = {"image": file_content, 'image_type': 'BASE64'}
        else:
            # image_file 是一个 FACE_TOKEN
            params = {"image": image_file, 'image_type': 'FACE_TOKEN'}
        return params

    def face_detect(self, image_file, face_field='', corp_image=True, max_faces=4):
        """
        人脸检测

        API文档: https://ai.baidu.com/ai-doc/FACE/yk37c1u4t

        :param image_file: 图片文件名或URL
        :param face_field: (可选)脸部信息，逗号分隔, 包括age,expression,face_shape,gender,glasses,
            landmark,landmark150,quality,eye_status,emotion,face_type,mask,spoofing信息
        :param corp_image: (可选)是否显示检测人脸的裁剪图
        :param max_faces:  (可选)最多处理人脸的数目，最大值120

        :return:  返回检测结果
        """
        self._update_token()  # 首先，检查access token

        # API DOC:
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
        request_url = request_url + "?access_token=" + self.token

        params = self._get_image(image_file)
        if face_field:
            params['face_field'] = face_field
        params['max_face_num'] = max_faces
        params['face_sort_type'] = 1
        params['display_corp_image'] = 1 if corp_image else 0

        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            return self._result(response.json(), 'result')
        return self._error(500, 'error request Baidu face detect')

    def face_match(self, image1, image2):
        """
        人脸比对

        API文档: https://ai.baidu.com/ai-doc/FACE/Lk37c1tpf

        :param image1: 图片1(文件名或 URL 或 FACE_TOKEN)
        :param image2: 图片2(文件名或 URL 或 FACE_TOKEN)
        :return: 返回比对结果
        """
        self._update_token()  # 首先，检查access token

        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
        request_url = request_url + "?access_token=" + self.token

        params = list()
        params.append(self._get_image(image1))
        params.append(self._get_image(image2))

        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, json=params, headers=headers)
        if response:
            return self._result(response.json(), 'result')

        return self._error(500, 'error request Baidu face match')

    def save_image(self, base64_data, save_filename):
        """
        将base64编码的图像数据，还原，存盘为文件。

        :param base64_data: base64编码的图像数据
        :param save_filename: 存盘文件名
        :return: None
        """
        img = base64.b64decode(base64_data)
        Utils.save_file(save_filename, img)
        return save_filename

    def face_merge(self, face_image, template_image, save_filename, alpha=0):
        """
        人脸融合

        API文档: https://ai.baidu.com/ai-doc/FACE/5k37c1ti0

        :param face_image: 目标人脸图片文件名或URL
        :param template_image: 模板图片文件名或URL
        :param save_filename: 存盘文件名
        :param alpha: （可选)融合参数，可选范围 0-1浮点数，保留两位小数，默认(0),
            0代表与目标图人脸最大程度相似（完全换脸），1 代表完全不换脸保留模版图，
            中间值（如0.5）为进行一般的换脸效果。该参数主要用于连续使用制作一组换脸渐变图片
        :return: 返回存盘文件名.
        """
        self._update_token()  # 首先，检查access token

        request_url = "https://aip.baidubce.com/rest/2.0/face/v1/merge"
        request_url = request_url + "?access_token=" + self.token

        params = {
            'image_template': self._get_image(template_image),
            'image_target': self._get_image(face_image),
            'version': '2.0'
        }

        if alpha != 0:
            params['version'] = '4.0'
            params['alpha'] = alpha

        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, json=params, headers=headers)
        if response:
            ret = response.json()
            if 'error_code' in ret and ret['error_code'] == 0:
                img_b64 = ret['result']['merge_image']
                img = base64.b64decode(img_b64)
                Utils.save_file(save_filename, img)
                return save_filename
            return ret

        return self._error(500, 'error request Baidu face match')

    def _image_api(self, image_file, api_url, result_key=''):
        """
        通用图像API
        :param image_file: 图片文件
        :return: 返回检测结果
        """
        self._update_token()  # 首先，检查access token

        request_url = api_url + "?access_token=" + self.token

        # file_length, file_content = Utils.read_file(image_file, True)
        # params = {"image": file_content}
        params = self._get_image(image_file)

        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            return self._result(response.json(), result_key)

        return self._error(500, 'error request Baidu API')

    def body_count(self, image_file):
        """
        人流量统计.

        适用于3米以上的中远距离俯拍，以头部为主要识别目标统计人数，无需正脸、全身照，
        适应各类人流密集场景（如：机场、车展、景区、广场等）；

        API文档: https://ai.baidu.com/ai-doc/BODY/7k3cpyy1t

        :param image_file: 图片文件
        :return: 返回检测结果
        """
        api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_num"
        return self._image_api(image_file, api_url, 'person_num')

    def body_detect(self, image_file):
        """
        人体检测

        API文档: https://ai.baidu.com/ai-doc/BODY/Ak3cpyx6v

        :param image_file: 图像文件
        :return: 返回检测结果
        """
        api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"
        return self._image_api(image_file, api_url)

    def body_anlysis(self, image_file):
        """
        人体关键点识别.

        API文档: https://ai.baidu.com/ai-doc/BODY/0k3cpyxme

        :param image_file: 图像文件
        :return: 返回检测结果
        """
        api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis"
        return self._image_api(image_file, api_url)

    def gesture(self, image_file):
        """
        手势识别

        API文档: https://ai.baidu.com/ai-doc/BODY/Ak3cpyx6v

        :param image_file: 图像文件
        :return: 返回检测结果
        """
        api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/gesture"
        return self._image_api(image_file, api_url)

    def classify(self, image_file):
        """
        通用物体和场景识别、分类

        API文档: https://ai.baidu.com/ai-doc/IMAGERECOGNITION/Xk3bcxe21

        :param image_file: 图像文件
        :return: 返回检测结果
        """
        api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
        return self._image_api(image_file, api_url)

    def classify_plant(self, image_file):
        """
        植物识别

        API文档: https://ai.baidu.com/ai-doc/IMAGERECOGNITION/Mk3bcxe9i

        :param image_file: 图像文件
        :return: 返回检测结果
        """
        api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"
        return self._image_api(image_file, api_url)

    def classify_animal(self, image_file):
        """
        动物识别

        API文档: https://ai.baidu.com/ai-doc/IMAGERECOGNITION/Zk3bcxdfr

        :param image_file: 图像文件
        :return: 返回检测结果
        """
        api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
        return self._image_api(image_file, api_url)

    def classify_car(self, image_file):
        """
        车型识别

        API文档: https://ai.baidu.com/ai-doc/VEHICLE/tk3hb3eiv

        :param image_file: 图像文件
        :return: 返回检测结果
        """
        api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"
        return self._image_api(image_file, api_url)

    def car_detect(self, image_file):
        """
        车辆检测

        API文档: https://ai.baidu.com/ai-doc/VEHICLE/rk3hb3flg

        :param image_file: 图像文件
        :return: 返回检测结果
        """
        api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
        return self._image_api(image_file, api_url)

    def car_attribute(self, image_file):
        """
        车辆属性识别

        API文档: https://ai.baidu.com/ai-doc/VEHICLE/mk3hb3fde

        :param image_file: 图像文件
        :return: 返回检测结果
        """
        api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/vehicle_attr"
        return self._image_api(image_file, api_url)

    def car_damage(self, image_file):
        """
        车辆外观损伤识别

        API文档: https://ai.baidu.com/ai-doc/VEHICLE/fk3hb3f5w

        :param image_file: 图像文件
        :return: 返回检测结果
        """
        api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_damage"
        return self._image_api(image_file, api_url)

    def classify_wine(self, image_file):
        """
        红酒识别

        API文档: https://ai.baidu.com/ai-doc/IMAGERECOGNITION/Tk3bcxctf

        :param image_file: 图像文件
        :return: 返回检测结果
        """
        api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/redwine"
        return self._image_api(image_file, api_url)

    def classify_objects(self, image_file):
        """
        图像主体检测

        API文档: https://ai.baidu.com/ai-doc/IMAGERECOGNITION/Wk7em3moi

        :param image_file: 图像文件
        :return: 返回检测结果
        """
        api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/multi_object_detect"
        return self._image_api(image_file, api_url)

    def classify_dish(self, image_file):
        """
        菜品识别

        API文档: https://ai.baidu.com/ai-doc/IMAGERECOGNITION/tk3bcxbb0

        :param image_file: 图像文件
        :return: 返回检测结果
        """
        api_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"
        return self._image_api(image_file, api_url)

    def _text_api(self, text, api_url, add_params=None, result_key='', add_url=''):
        """
        通用文字API
        :param text: 文字
        :return: 返回检测结果
        """
        self._update_token()  # 首先，检查access token

        request_url = api_url + "?access_token=" + self.token + add_url

        if text is None:
            params = dict()
        else:
            params = {"text": text}

        if type(add_params) == dict:
            for k in add_params:
                params[k] = add_params[k]

        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, json=params, headers=headers)
        if response:
            ret = response.json()
            if result_key in ret:
                return ret[result_key]
            else:
                return ret

        return self._error(500, 'error request Baidu API')

    def nlp_poem(self, topic, index=0):
        """
        智能写诗(七言绝句)

        API文档: https://ai.baidu.com/ai-doc/NLP/ak53wc3o3

        :param topic: 主题
        :param index: 数值为0，即第一幅。每换一次，数值加1即可，一定数量后会返回之前的结果。
        :return: 返回结果
        """
        api_url = "https://aip.baidubce.com/rpc/2.0/creation/v1/poem"
        return self._text_api(topic, api_url, {'index': index}, 'poem')

    def nlp_couplets(self, topic, index=0):
        """
        智能春联

        API文档: https://ai.baidu.com/ai-doc/NLP/Ok53wb6dh

        :param topic: 主题
        :param index: 数值为0，即第一幅。每换一次，数值加1即可，一定数量后会返回之前的结果。
        :return: 返回结果
        """
        api_url = "https://aip.baidubce.com/rpc/2.0/creation/v1/couplets"
        return self._text_api(topic, api_url, {'index': index}, 'couplets')

    def nlp_bless(self, topic):
        """
        节日祝福语生成

        API文档: https://cloud.baidu.com/doc/NLP/s/sl4cg75jk

        :param topic: 主题, 节日关键词，目前支持生成祝福语的关键词如下：平安夜 圣诞节 情人节
            元旦 除夕 春节 新年 元宵节 妇女节 清明节 劳动节 端午节 国庆节 中秋节 重阳节 立春
            雨水 惊蛰 春分 清明 谷雨 立夏 小满 芒种 夏至 小暑 大暑 立秋 处暑 白露 秋分 寒露
            霜降 立冬 小雪 大雪 冬至 小寒 大寒 高考
        :return: 返回结果
        """
        api_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/bless_creation"
        return self._text_api(topic, api_url, None, '')

    def nlp_address(self, address_text):
        """
        地址识别

        API文档: https://cloud.baidu.com/doc/NLP/s/vk6z52h5n

        :param address_text: 地址文字
        :return: 返回结果
        """
        api_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/address"
        return self._text_api(address_text, api_url, None, '')

    def nlp_sentiment(self, text):
        """
        情感倾向分析: 对包含主体主观信息的文本，进行自动情感倾向性判断

        API文档: https://cloud.baidu.com/doc/NLP/s/zk6z52hds

        :param text: 文字
        :return: 返回结果
        """
        api_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify"
        return self._text_api(text, api_url, None, '')

    def nlp_comment(self, text, industry=8):
        """
        评论观点抽取

        API文档: https://cloud.baidu.com/doc/NLP/s/ok6z52g8q

        :param text: 评论文字
        :param industry: 行业: 酒店, KTV, 丽人, 美食, 餐饮, 旅游, 健康, 教育, 商业, 房产, 汽车, 生活, 购物, 3C
        :return: 返回结果
        """
        industries = {'酒店': 1, 'KTV': 2, '丽人': 3, '美容': 3, '美食': 4, '餐饮': 4,
                      '旅游': 5, '健康': 6, '教育': 7, '商业': 8, '房产': 9,
                      '汽车': 10, '生活': 11, '购物': 12, '3C': 13}
        if type(industry) == str:
            if industry in industries:
                industry = industries[industry]
            else:
                industry = 4
        api_url = "https://aip.baidubce.com/rpc/2.0/nlp/v2/comment_tag"
        return self._text_api(text, api_url, {'type': industry},
                              '', add_url='&charset=UTF-8')

    def nlp_lexer(self, text):
        """
        词法分析
        
        API文档: https://cloud.baidu.com/doc/NLP/s/fk6z52f2u
        
        :param text:  文字
        :return: 返回分析结果
        """
        api_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer"
        ret = self._text_api(text, api_url, None, '', add_url='&charset=UTF-8')
        if 'items' in ret:
            words = list()
            for item in ret['items']:
                ws = item['basic_words']
                for word in ws:
                    words.append(word)
            ret['words'] = words
        return ret

    def nlp_keywords(self, text):
        """
        关键词提取

        API文档: https://cloud.baidu.com/doc/NLP/s/rl9zkamiq

        :param text:  文字
        :return: 返回分析结果
        """
        api_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/txt_keywords_extraction"
        ret = self._text_api([text], api_url, None, '', add_url='&charset=UTF-8')
        if 'results' in ret:
            words = list()
            for item in ret['results']:
                words.append(item['word'])
            ret['keywords'] = words
        return ret

    def nlp_summary(self, title, content, summary_len):
        """
        新闻摘要

        API文档: https://cloud.baidu.com/doc/NLP/s/Gk6z52hu3

        :param title:  新闻标题
        :param content:  新闻内容
        :param summary_len:  摘要结果的最大长度
        :return: 返回分析结果
        """
        api_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/news_summary"
        return self._text_api(None, api_url,
                              {'title': title, 'content': content, 'max_summary_len': summary_len},
                              'summary', add_url='&charset=UTF-8')

    def nlp_tags(self, title, content):
        """
        文章标签

        API文档: https://cloud.baidu.com/doc/NLP/s/7k6z52ggx

        :param title:  文章标题
        :param content:  文章内容
        :return: 返回分析结果
        """
        api_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/keyword"
        return self._text_api(None, api_url,
                              {'title': title, 'content': content},
                              'items', add_url='&charset=UTF-8')

    def nlp_topic(self, title, content):
        """
        文章分类

        API文档: https://cloud.baidu.com/doc/NLP/s/wk6z52gxe

        :param title:  文章标题
        :param content:  文章内容
        :return: 返回分析结果
        """
        api_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/topic"
        return self._text_api(None, api_url,
                              {'title': title, 'content': content},
                              'item', add_url='&charset=UTF-8')

