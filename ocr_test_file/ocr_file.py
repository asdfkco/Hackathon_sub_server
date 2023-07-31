from PIL import Image
from google.cloud import vision
import io

image_path : str = input()
#
def extract_text_from_image(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    client = vision.ImageAnnotatorClient.from_service_account_file('iron-potion-393208-29d8e7c7deed.json')

    image = vision.Image(content=content)
    response = client.text_detection(image=image)

    texts = response.text_annotations
    image_file
    if texts:
        extracted_text = texts
        return extracted_text
    else:
        return False

extracted_text = extract_text_from_image(image_path)

def dis(text):
    for text in extracted_text:
        # print(text.description)
        if '성장곡선' in text.description :
            sungjang()
            print("성장곡선")
            break
        elif '부위별근육곡선' and '부위별체지방분석' in  text.description :
            gen()
            print("근육곡선")
            break
        else :
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


def sungjang():
    input_image_path = 'sungjang.png'
    output_image_path = 'sungjang_cliping.png'
    # 성장곡선 케이스
    left = 0
    top = 150
    right = 1600
    bottom = 1100
    crop_image(input_image_path, output_image_path, left, top, right, bottom)

def gen():
    input_image_path = 'gen.png'
    output_image_path = 'gen_cliping.png'
    # 근육량 분포 케이스
    left = 0
    top = 150
    right = 1600
    bottom = 1250
    crop_image(input_image_path, output_image_path, left, top, right, bottom)


if __name__ == "__main__":
    dis(extract_text_from_image(image_path))

