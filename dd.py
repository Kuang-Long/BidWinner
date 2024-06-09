import ddddocr

# 创建一个 OCR 识别器对象
ocr = ddddocr.DdddOcr()
ocr.set_ranges("0123456789")
# 读取要识别的图像文件
image_path = "C:/Users/IT_manager/Desktop/1.jpg"
with open(image_path, 'rb') as f:
    img_bytes = f.read()

# 使用 ddddocr 进行识别
result = ocr.classification(img_bytes)

# 打印识别结果
print("识别结果:", result)
