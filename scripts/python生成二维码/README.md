# python脚本-生成二维码


- 普通二维码

![](images/qrPic.png)

- 图片二维码

![](images/qrPicColor.png)

- GIF二维码

![](images/qrPicGif.gif)


# 函数接口
```
myqr.run()
```
# 参数简介

|    参数   |  含义 |   详细  |
| :------: | :----: | :----: |
|words |二维码指向链接 |str，输入链接或者句子作为参数|
|version|边长|int，控制边长，范围是1到40，数字越大边长越大,默认边长是取决于你输入的信息的长度和使用的纠错等级|
|level|纠错等级|str，控制纠错水平，范围是L、M、Q、H，从左到右依次升高，默认纠错等级为'H'|
|picture|结合图片|str，将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片|
|colorized|颜色|bool，使产生的图片由黑白变为彩色的|
|contrast|对比度|float，调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0brightness亮度float，调节图片的亮度，其余用法和取值与 contrast 相同|
|save_name|输出文件名|str，默认输出文件名是"qrcode.png"|
|save_dir|存储位置|str，默认存储位置是当前目录|



