#!/usr/bin/python
# coding:utf-8

import ai
from pprint import pprint  # pprint() 用于将dict打印得好看些


# 以下请写入百度云中创建应用后提供的API Key、Secret Key
api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
secret_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
api_key = '8IGsGGa2nQaf8nn47zGnN4Mi'
secret_key = 'G5NY2NU3WVwzTWIb6EFQ1pVFsc8buy6u'

# 创建 BaiduAI 对象， 代入 api_key, secret_key 两个参数
b = ai.BaiduAI(api_key, secret_key)

# 调用各个API
print('====语音转文本')
texts = b.asr('images/16k.wav')
print(texts)

print('====文本转语音')
b.tts('我是北京人')

print('====文字识别')
print(b.ocr("https://www.baidu.com/img/flexible/logo/pc/result.png"))

print('====身份证识别')
pprint(b.ocr_id_card("images/idcard2.jpg"))

print('====银行卡识别')
pprint(b.ocr_bank_card("images/bank_card.jpg"))

print('====人脸检测')
pprint(b.face_detect("images/face1.jpg", "age,expression"))

print('====人脸比对')
pprint(b.face_match("images/face1.jpg", "images/face2.jpg"))

print('====人脸融合')
pprint(b.face_merge("images/face2.jpg", "images/template.jpg", "images/merge_face.jpg"))

print('====人流量统计')
pprint(b.body_count("images/bodys.jpg"))

print('====人体检测')
pprint(b.body_detect("images/bodys2.jpg"))

print('====人体关键点识别')
pprint(b.body_anlysis("images/body_ana.jpg"))

print('====通用物体和场景识别')
pprint(b.classify("images/notebook.jpg"))

print('====植物识别')
pprint(b.classify_plant("images/plant3.jpg"))

print('====动物识别')
pprint(b.classify_animal("images/animal3.jpg"))

print('====车型识别')
pprint(b.classify_car("images/car1.jpg"))

print('====车辆检测')
pprint(b.car_detect("images/cars2.jpg"))

print('====车辆属性识别')
pprint(b.car_attribute("images/car4.jpg"))

print('====车辆外观损伤识别')
pprint(b.car_damage("images/car_damage1.jpg"))

print('====红酒识别')
pprint(b.classify_wine("images/wine1.jpg"))

print('====图像主体检测')
pprint(b.classify_objects("images/objects1.jpg"))

print('====菜品识别')
pprint(b.classify_dish("images/dish1.jpg"))

print('====智能写诗(七言绝句)')
pprint(b.nlp_poem("长江望月"))

print('====智能春联')
pprint(b.nlp_couplets("长江"))

print('====节日祝福语生成')
pprint(b.nlp_bless("情人节"))

print('====地址识别')
pprint(b.nlp_address("上海市浦东新区纳贤路701号百度上海研发中心 F4A000 张三"))

print('====情感倾向分析')
pprint(b.nlp_sentiment("实在不怎么样"))

print('====评论观点抽取')
pprint(b.nlp_comment("三星电脑电池不给力", "3C"))

print('====词法分析')
pprint(b.nlp_lexer("百度是一家高科技公司"))

print('====关键词提取')
pprint(b.nlp_keywords("学习书法，就选唐颜真卿《颜勤礼碑》原碑与对临「第1节」"))

print('====新闻摘要')
title = "麻省理工仓库货物管理"
content = '麻省理工学院的研究团队为无人机在仓库中使用RFID技术进行库存查找等工作，创造了一种聪明的新方式。它允许公司使用更小，更安全的无人机在巨型建筑物中找到之前无法找到的东西。使用RFID标签更换仓库中的条形码，将帮助提升自动化并提高库存管理的准确性。与条形码不同，RFID标签不需要对准扫描，标签上包含的信息可以更广泛和更容易地更改。它们也可以很便宜，尽管有优点，但是它具有局限性，对于跟踪商品没有设定RFID标准，“标签冲突”可能会阻止读卡器同时从多个标签上拾取信号。扫描RFID标签的方式也会在大型仓库内引起尴尬的问题。固定的RFID阅读器和阅读器天线只能扫描通过设定阈值的标签，手持式读取器需要人员出去手动扫描物品。'
pprint(b.nlp_summary(title, content, 80))

print('====文章标签')
title = "麻省理工仓库货物管理"
content = '麻省理工学院的研究团队为无人机在仓库中使用RFID技术进行库存查找等工作，创造了一种聪明的新方式。它允许公司使用更小，更安全的无人机在巨型建筑物中找到之前无法找到的东西。使用RFID标签更换仓库中的条形码，将帮助提升自动化并提高库存管理的准确性。与条形码不同，RFID标签不需要对准扫描，标签上包含的信息可以更广泛和更容易地更改。它们也可以很便宜，尽管有优点，但是它具有局限性，对于跟踪商品没有设定RFID标准，“标签冲突”可能会阻止读卡器同时从多个标签上拾取信号。扫描RFID标签的方式也会在大型仓库内引起尴尬的问题。固定的RFID阅读器和阅读器天线只能扫描通过设定阈值的标签，手持式读取器需要人员出去手动扫描物品。'
pprint(b.nlp_tags(title, content))

print('====文章分类')
title = "麻省理工仓库货物管理"
content = '麻省理工学院的研究团队为无人机在仓库中使用RFID技术进行库存查找等工作，创造了一种聪明的新方式。它允许公司使用更小，更安全的无人机在巨型建筑物中找到之前无法找到的东西。使用RFID标签更换仓库中的条形码，将帮助提升自动化并提高库存管理的准确性。与条形码不同，RFID标签不需要对准扫描，标签上包含的信息可以更广泛和更容易地更改。它们也可以很便宜，尽管有优点，但是它具有局限性，对于跟踪商品没有设定RFID标准，“标签冲突”可能会阻止读卡器同时从多个标签上拾取信号。扫描RFID标签的方式也会在大型仓库内引起尴尬的问题。固定的RFID阅读器和阅读器天线只能扫描通过设定阈值的标签，手持式读取器需要人员出去手动扫描物品。'
pprint(b.nlp_topic(title, content))


