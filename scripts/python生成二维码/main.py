from MyQR import myqr

#普通二维码
myqr.run(
    words='https://www.mehoon.com',
    save_name='images/qrPic.png'
)

#图片二维码
myqr.run(
    words='https://www.mehoon.com',
    picture='avatar.jpg',
    colorized=True,
    save_name='images/qrPicColor.png',
)

#GIF二维码
myqr.run(
    words='https://www.mehoon.com',
    picture='cat.gif',
    colorized=True,
    save_name='images/qrPicGif.gif',
)