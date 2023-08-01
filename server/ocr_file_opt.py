import os
import time
import re
from PIL import Image
from google.cloud import vision
import io
from concurrent.futures import ThreadPoolExecutor

# image_path : str = input()

absPath = os.path.dirname(os.getcwd())
image_path = absPath+'/tmp/gen.png'


def extract_text_from_image(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    client = vision.ImageAnnotatorClient.from_service_account_file(
        '/Users/kim-chanok/Desktop/toooooooon/Hackathon_sub_server/server/iron-potion-393208-db8a054e2128.json')

    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)

    texts = response.text_annotations

    if texts:
        extracted_text = texts
        if 'cliping' in image_path:
            for text in extracted_text:
                text_r = text.description.replace("\n", " ")
                break
            return text_r
        elif 'data' in image_path:
            for text in extracted_text:
                text_r = text.description.replace("\n", " ")
                # print(text_r)
                break
            return text_r
        return extracted_text
    else:
        return False


extracted_text = extract_text_from_image(image_path)


def dis(text):
    found_text = False

    for text in extracted_text:
        # print(text.description)
        if '성장곡선' in text.description:
            print("성장곡선")
            return sungjang(image_path)
        elif '부위별근육곡선' and '부위별체지방분석' in text.description:
            print("근육곡선")
            return gen(image_path)
        if not found_text:
            print("인바디 검사지가 아닙니다")
            break


def crop_image(input_image_path, output_image_path, left, top, right, bottom):
    try:
        # 이미지를 엽니다.
        image = Image.open(input_image_path)

        # 지정한 영역을 잘라냅니다.
        cropped_image = image.crop((left, top, right, bottom))

        # 잘라낸 이미지를 저장합니다.
        cropped_image.save(output_image_path)
        print('Image cropped and saved successfully.')
    except Exception as e:
        print(f'Error occurred while cropping the image: {e}')


def sungjang(input_image):
    번호에서성별 = 'data1.png'
    체수분체중 = 'data2.png'
    골격근 = 'data3.png'
    체지방량 = 'data4.png'
    BMI = 'data5.png'
    체지방률 = 'data6.png'
    성장점수 = 'data7.png'
    output_image_path = 'sungjang_cliping.png'
    # 성장곡선 케이스
    left = 0
    top = 150
    right = 1600
    bottom = 1100
    crop_image(input_image, output_image_path, left, top, right, bottom)
    번호에서성별_data: dict = detail_data('sungjang_cliping.png', 번호에서성별, 55, 25, 1560, 65)
    체수분체중_data: dict = detail_data('sungjang_cliping.png', 체수분체중, 690, 140, 130 + 690, 140 + 250)
    골격근_data : str = detail_data('sungjang_cliping.png', 골격근, 250, 595, 250 + 740, 595 + 42)
    체지방량_data : str = detail_data('sungjang_cliping.png', 체지방량, 250, 660, 250 + 740, 660 + 42)
    BMI_data : str= detail_data('sungjang_cliping.png', BMI, 250, 835, 250 + 740, 835 + 42)
    체지방률_data : str= detail_data('sungjang_cliping.png', 체지방률, 250, 900, 250 + 740, 900 + 42)
    체지방률_data : str = re.findall("(\d*\.?\d+)", 체지방률_data)
    성장점수_data : str= detail_data('sungjang_cliping.png', 성장점수, 1170, 205, 1170 + 105, 205 + 50)
    os.remove(output_image_path)
    return {
        "신장": 번호에서성별_data[1],
        "나이": 번호에서성별_data[2],
        "성별": 번호에서성별_data[3],
        "검사일시": 번호에서성별_data[4] + 번호에서성별_data[5],
        "체수분": 체수분체중_data[0],
        "단백질": 체수분체중_data[1],
        "무기질": 체수분체중_data[2],
        "체지방": 체수분체중_data[3],
        "체중": 체수분체중_data[4],
        "골격근": 골격근_data,
        "체지방량": 체지방량_data,
        "BMI": BMI_data,
        "체지방률": 체지방률_data[0],
        "성장점수": 성장점수_data
    }


def gen(input_image):
    output_image_path = 'gen_cliping.png'
    번호에서성별 = 'data1.png'
    체수분체중 = 'data2.png'
    골격근 = 'data3.png'
    체지방량 = 'data4.png'
    BMI = 'data5.png'
    체지방률 = 'data6.png'
    성장점수 = 'data7.png'

    # 근육량 분포 케이스
    left = 0
    top = 150
    right = 1600
    bottom = 1250
    crop_image(input_image, output_image_path, left, top, right, bottom)

    번호에서성별_data: dict = detail_data('gen_cliping.png', 번호에서성별, 40, 25, 1560, 65).split(' ')
    체수분체중_data: dict = detail_data('gen_cliping.png', 체수분체중, 685, 175, 685 + 120, 175 + 250).split(' ')
    골격근_data: str = detail_data('gen_cliping.png', 골격근, 235, 670, 235 + 720, 670 + 42)
    체지방량_data: str = detail_data('gen_cliping.png', 체지방량, 235, 735, 235 + 720, 735 + 42)
    BMI_data: str = detail_data('gen_cliping.png', BMI, 235, 950, 235 + 720, 950 + 42)
    체지방률_data: str = detail_data('gen_cliping.png', 체지방률, 235, 1010, 235 + 720, 1010 + 42)
    체지방률_data: str = re.findall("(\d*\.?\d+)", 체지방률_data)
    성장점수_data: str = detail_data('gen_cliping.png', 성장점수, 1175, 200, 1175 + 105, 200 + 50)
    os.remove(output_image_path)
    return {
        "신장": 번호에서성별_data[1],
        "나이": 번호에서성별_data[2],
        "성별": 번호에서성별_data[3],
        "검사일시": 번호에서성별_data[4] + 번호에서성별_data[5],
        "체수분" : 체수분체중_data[0],
        "단백질": 체수분체중_data[1],
        "무기질": 체수분체중_data[2],
        "체지방": 체수분체중_data[3],
        "체중": 체수분체중_data[4],
        "골격근": 골격근_data,
        "체지방량": 체지방량_data,
        "BMI": BMI_data,
        "체지방률": 체지방률_data[0],
        "성장점수": 성장점수_data
    }


def detail_data(input_image, output_image_path, left, top, right, bottom):
    crop_image(input_image, output_image_path, left, top, right, bottom)
    data_body = extract_text_from_image(output_image_path)
    os.remove(output_image_path)
    print(data_body)
    return data_body


def start(path):
    start_time = time.time()

    # ThreadPoolExecutor 사용하여 각 이미지 처리를 병렬로 실행
    with ThreadPoolExecutor() as executor:
        executor.submit(dis, extracted_text)
    end_time = time.time()
    print(f"실행 시간: {end_time - start_time:.2f}초")
#    json 가공
