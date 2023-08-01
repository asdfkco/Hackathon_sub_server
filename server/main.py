from fastapi import FastAPI
from pydantic import BaseModel

# import ocr_file_opt
from concurrent.futures import ThreadPoolExecutor
import time

app = FastAPI()

# ocr = ocr_file_opt

class Item(BaseModel):
    file_name:str

@app.post("/ocr_file")
async def ocr_send_data(item:Item):
    print(item.file_name)
    # asdf = None
    # start_time = time.time()
    # with ThreadPoolExecutor() as executor:
    #     asdf = executor.submit(ocr.dis, ocr.extracted_text).result()
    # end_time = time.time()
    # print(f"실행 시간: {end_time - start_time:.2f}초")
    return item
