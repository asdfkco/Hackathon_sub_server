import os
import re
from PIL import Image
from google.cloud import vision
import io
import uuid
from concurrent.futures import ProcessPoolExecutor


def image_size(path):
    im = Image.open(path)
    width,height = im.size
    if width != 1600 and height != 2255:
        raise Exception('사진크기가 알맞지 않습니다')


def extract_text_from_image(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    client = vision.ImageAnnotatorClient.from_service_account_file(
        os.getcwd()+'/iron-potion-393208-db8a054e2128.json')

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

def data(image_path):
    output_image_path = '../tmp/'+random()+'.png'
    crop_image(image_path, output_image_path, 30, 1120, 30+300, 1120+360)
    extracted_text = extract_text_from_image(output_image_path)
    os.remove(output_image_path)
    return extracted_text

# dis(data(path),path)

def dis(path):
    found_text = False

    for text in data(path):
        # print(text.description)
        if '성장곡선' in text.description:
            print("성장곡선")
            return sungjang(path)
        elif '부위별근육분석' in text.description:
            print("근육분석")
            return gen(path)
        if not found_text:
            raise Exception('사진이 알맞지 않습니다')
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


def random():
    return uuid.uuid1().hex

def sungjang(input_image):
    번호에서성별= '../tmp/1_data_'+random()+'.png'
    체수분체중 = '../tmp/2_data_'+random()+'.png'
    골격근 = '../tmp/3_data_'+random()+'.png'
    BMI = '../tmp/4_data_'+random()+'.png'
    체지방률 = '../tmp/5_data_'+random()+'.png'
    성장점수 = '../tmp/6_data_'+random()+'.png'
    output_image_path = '../tmp/cliping_img_'+random()+'.png'
    # 성장곡선 케이스
    left, top, right, bottom = 0, 150, 1600, 1100
    # print(번호에서성별,체수분체중,골격근,BMI,체지방률,성장점수,output_image_path)

    crop_image(input_image, output_image_path, left, top, right, bottom)
    with ProcessPoolExecutor(max_workers=6) as exe:
            번호에서성별_data: dict = detail_data(output_image_path, 번호에서성별, 55, 25, 1560, 65).split(' ')
            체수분체중_data: dict = detail_data(output_image_path, 체수분체중, 690, 140, 130 + 690, 140 + 250).split(' ')
            골격근_data : str = detail_data(output_image_path, 골격근, 250, 595, 250 + 740, 595 + 42)
            BMI_data : str= detail_data(output_image_path, BMI, 250, 835, 250 + 740, 835 + 42)
            체지방률_data : str= detail_data(output_image_path, 체지방률, 250, 900, 250 + 740, 900 + 42)
            체지방률_data : str = re.findall("(\d*\.?\d+)", 체지방률_data)
            성장점수_data : str= detail_data(output_image_path, 성장점수, 1170, 205, 1170 + 105, 205 + 50)
    exe.shutdown(wait=True)
    os.remove(output_image_path)
    return {
        "height": 번호에서성별_data[1].replace('cm',''),
        "ages": 번호에서성별_data[2],
        "inspection_date": 번호에서성별_data[4] + 번호에서성별_data[5],
        "body_water": 체수분체중_data[0],
        "protein": 체수분체중_data[1],
        "minerals": 체수분체중_data[2],
        "body_fat": 체수분체중_data[3],
        "weight": 체수분체중_data[4],
        "skeletal_muscle_mass": 골격근_data,
        "bmi": BMI_data,
        "body_fat_percentage": 체지방률_data[0],
        "inbody_score": 성장점수_data
    }


def gen(input_image):
    번호에서성별= '../tmp/1_data_'+random()+'.png'
    체수분체중 = '../tmp/2_data_'+random()+'.png'
    골격근 = '../tmp/3_data_'+random()+'.png'
    BMI = '../tmp/4_data_'+random()+'.png'
    체지방률 = '../tmp/5_data_'+random()+'.png'
    성장점수 = '../tmp/6_data_'+random()+'.png'
    output_image_path = '../tmp/cliping_img_'+random()+'.png'

    # 근육량 분포 케이스
    left, top, right, bottom = 0, 150, 1600, 1250
    crop_image(input_image, output_image_path, left, top, right, bottom)
    with ProcessPoolExecutor(max_workers=6) as exe:
        번호에서성별_data: dict = detail_data(output_image_path, 번호에서성별, 40, 25, 1560, 65).split(' ')
        체수분체중_data: dict = detail_data(output_image_path, 체수분체중, 685, 175, 685 + 120, 175 + 250).split(' ')
        골격근_data: str = detail_data(output_image_path, 골격근, 235, 670, 235 + 720, 670 + 42)
        BMI_data: str = detail_data(output_image_path, BMI, 235, 950, 235 + 720, 950 + 42)
        체지방률_data: str = detail_data(output_image_path, 체지방률, 235, 1010, 235 + 720, 1010 + 42)
        체지방률_data: str = re.findall("(\d*\.?\d+)", 체지방률_data)
        성장점수_data: str = detail_data(output_image_path, 성장점수, 1175, 200, 1175 + 105, 200 + 50)
    exe.shutdown(wait=True)
    os.remove(output_image_path)
    return {
        "height": 번호에서성별_data[1].replace('cm',''),
        "ages": 번호에서성별_data[2],
        "inspection_date": 번호에서성별_data[4] + 번호에서성별_data[5],
        "body_water": 체수분체중_data[0],
        "protein": 체수분체중_data[1],
        "minerals": 체수분체중_data[2],
        "body_fat": 체수분체중_data[3],
        "weight": 체수분체중_data[4],
        "skeletal_muscle_mass": 골격근_data,
        "bmi": BMI_data,
        "body_fat_percentage": 체지방률_data[0],
        "inbody_score": 성장점수_data

    }


def detail_data(input_image, output_image_path, left, top, right, bottom):
    crop_image(input_image, output_image_path, left, top, right, bottom)
    data_body = extract_text_from_image(output_image_path)
    # print(input_image,output_image_path)
    os.remove(output_image_path)
    # print("지워지지않는다.")
    print(data_body)
    return data_body