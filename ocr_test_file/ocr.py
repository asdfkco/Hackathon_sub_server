import io
from google.cloud import vision
import json

image_path = 'asdf.png'
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


for text in extracted_text:
    # print(text.description)
    if '성장곡선' in text.description :
        # sungjang()
        print("성장곡선")
        break
    elif '부위별근육곡선' and '부위별체지방분석' in  text.description  :
        print("근육곡선")
        break
    else :
        print("인바디 검사지가 아닙니다")
        break


# print(extracted_text)

# if extracted_text :
#     print('추출된 텍스트:')
#
#     print(type(extracted_text))
#     print('성장' in extracted_text)
# else:
#     print('텍스트를 추출할 수 없습니다.')