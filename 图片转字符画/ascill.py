# coding:utf-8 
import argparse
# PIL是Python的一个图像处理库
from PIL import Image

# 命令行输入参数处理
parser = argparse.ArgumentParser()
# 输入文件
parser.add_argument('file')
# 输出文件
parser.add_argument('-o','--output')
# 输出字符画宽
parser.add_argument('--width',type = int,default = 80)
# 输出字符画高
parser.add_argument('--height',type = int,default = 80)
#获取参数
args = parser.parse_args()

IMAGE = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#将256灰度映射到70个字符上
def getChar(r, g, b, alpha= 256 ):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]
if __name__ == '__main__':
    im = Image.open(IMAGE)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += getChar(*im.getpixel((j,i)))
        txt += '\n'

    print (txt)

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
