from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import os
import ocr_file_opt
from concurrent.futures import ThreadPoolExecutor
import time

app = FastAPI()

ocr = ocr_file_opt

class Item(BaseModel):
    file_name:str

@app.post("/ocr_file")
def ocr_send_data(item:Item):
    # print(item.file_name)

    print(os.path.dirname(os.getcwd())+"/tmp/"+item.file_name)
    body_info = None
    start_time = time.time()
    ocr.image_size(os.path.dirname(os.getcwd())+"/tmp/"+item.file_name)
    with ThreadPoolExecutor() as executor:
        body_info = executor.submit(ocr.dis,executor.submit(executor.submit(ocr.data,os.path.dirname(os.getcwd())+"/tmp/"+item.file_name),os.path.dirname(os.getcwd())+"/tmp/"+item.file_name),os.path.dirname(os.getcwd())+"/tmp/"+item.file_name).result()
    end_time = time.time()
    print(f"실행 시간: {end_time - start_time:.2f}초")
    return body_info

# from fastapi import FastAPI
# from pydantic import BaseModel
# import os
# import ocr_file_opt
# from concurrent.futures import ThreadPoolExecutor
# import time
#
# app = FastAPI()
#
# ocr = ocr_file_opt
#
# class Item(BaseModel):
#     file_name:str
#
# @app.post("/ocr_file")
# async def ocr_send_data(item:Item):
#     print(item.file_name)
#     asdf = None
#     start_time = time.time()
#     with ThreadPoolExecutor() as executor:
#         asdf = executor.submit(ocr.dis,executor.submit(ocr.extracted_text,os.path.dirname(os.getcwd())+item.file_name),os.path.dirname(os.getcwd())+item.file_name).result()
#     end_time = time.time()
#     print(f"실행 시간: {end_time - start_time:.2f}초")
#     return asdf
