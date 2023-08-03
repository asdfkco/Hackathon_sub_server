from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import os
import ocr_file_opt
from concurrent.futures import ThreadPoolExecutor
import time
from fastapi import FastAPI, HTTPException
from fastapi.logger import logger

app = FastAPI()

ocr = ocr_file_opt

class Item(BaseModel):
    file_name:str

@app.post("/ocr_file")
def ocr_send_data(item:Item,request:Request):
    print(item.file_name)
    print(os.path.dirname(os.getcwd())+"/tmp/"+item.file_name)
    body_info = None
    start_time = time.time()
    path = os.path.dirname(os.getcwd())+"/tmp/"+item.file_name
    try:
        ocr.image_size(os.path.dirname(os.getcwd())+"/tmp/"+item.file_name)
        with (ThreadPoolExecutor(4) as executor):
            body_info = executor.submit(ocr.dis,path).result()


        print(request.client.host,body_info)
        end_time = time.time()
        print(f"실행 시간: {end_time - start_time:.2f}초")
        return body_info
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400 , detail="사진이 알맞지 않습니다")
