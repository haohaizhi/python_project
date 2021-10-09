# 导入所有必须的python库
# pip install opencv-python
import cv2
import numpy as np
import types


# 将任意类型数据转换成二进制
def messageToBinary(message):
    if type(message) == str:
        return ''.join([ format(ord(i), "016b") for i in message ])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [ format(i, "016b") for i in message ]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "016b")
    else:
        raise TypeError("不支持的数据类型！")

# 改变图像最低有效位（LSB）从而将秘密信息隐藏
def hideData(image, secret_message):
    # 计算需要编码的最大字节数
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    print("最大字节数为:", n_bytes)

    # 确定需要加密的信息是否字节数过长
    if len(secret_message) > n_bytes:
        raise ValueError("加密数据错误, 需要更大像素的图像或者更短的加密信息 !!")

    secret_message += "#####"

    data_index = 0

    binary_secret_msg = messageToBinary(secret_message)

    data_len = len(binary_secret_msg)
    for values in image:
        for pixel in values:
            # 转换RGB值为二进制格式
            r, g, b = messageToBinary(pixel)
            # 只有当仍然有数据要存储时，才修改最低有效位
            if data_index < data_len:
                # 将数据隐藏到红色像素的最低有效位
                pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # 将数据隐藏到绿色像素的最低有效位
                pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # 将数据隐藏到蓝色像素的最低有效位
                pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            # 如果数据都被加密完成，就跳出循环
            if data_index >= data_len:
                break
    return image

# 解码隐藏图像中的隐藏消息
def showData(image):
    binary_data = ""
    for values in image:
      for pixel in values:
          r, g, b = messageToBinary(pixel)
          binary_data += r[-1]  # 从红色像素的最低有效位提取数据
          binary_data += g[-1]  # 从绿色像素的最低有效位提取数据
          binary_data += b[-1]  # 从蓝色像素的最低有效位提取数据

    # 每16位进行分割,考虑到中文占两个字节
    all_bytes = [ binary_data[i: i+16] for i in range(0, len(binary_data), 16) ]

    # 从位转换为字符
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####":  # 检查我们是否已经到达结束标志，它是#####
            break
    # print(decoded_data)
    return decoded_data[:-5]  # 移除结束标志以显示原始的隐藏消息

# 将信息隐藏到图像
def encode_text():
    image_name = input("输入图像名称(带扩展名): ")
    image = cv2.imread(image_name)  # 使用OpenCV-Python读取输入图像。
    # 它是一个Python绑定库，旨在解决计算机视觉问题。

    print("计算图像字节数: ", image.shape)  # 检查图像的形状以计算其中的字节数

    # print("原始图像如下图所示: ")
    # resized_image = cv2.resize(image, (500, 500))  # 根据要求调整图像的大小
    # cv2.imshow(image_name ,resized_image)

    data = input("输入需要隐藏的信息 : ")
    if (len(data) == 0):
        raise ValueError('信息为空！')

    filename = input("输入新编码图像的名称(带扩展名): ")
    encoded_image = hideData(image, data)

    cv2.imwrite(filename, encoded_image)

# 将加密信息进行显示
def decode_text():
    image_name = input("输入要解码的隐写图像的名称(带有扩展名) :")
    image = cv2.imread(image_name)

    # print("隐写图像如下图所示: ")
    # resized_image = cv2.resize(image, (500, 500))  # 根据您的要求调整原始图像的大小
    # cv2.imshow(image_name, resized_image)

    text = showData(image)
    return text

def main():
    a = input("【图像隐写术】 \n 1. 信息隐藏(加密) \n 2. 信息显示(解密) \n 请输入选项: ")
    userinput = int(a)
    if (userinput == 1):
        print("\n加密中....")
        encode_text()

    elif (userinput == 2):
        print("\n解密中....")
        print("获得真实信息： " + decode_text())
    else:
        raise Exception("请输入正确选项！！")

if __name__ == '__main__':
    main()