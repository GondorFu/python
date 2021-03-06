# struct
# 在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，
# 你得配合位运算符这么写
# 0xff = b(11111111) = 1 byte(字节) = 8 bits(比特)
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)

# 好在Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换
import struct
print(struct.pack('>I', 10240099))
# '>I'的意思是：>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。

# unpack把bytes变成相应的数据类型：
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。


# Windows的位图文件（.bmp）是一种非常简单的文件格式，我们来用struct分析一下。
# 读入前30个字节来分析：
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

# BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。
print(struct.unpack('<ccIIIIIIHH', s))


# 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，
# 如果是，打印出图片大小和颜色数。
def isbmp(file):
	with open(file, 'rb') as f:
		bit30 = f.read(30)
		info = struct.unpack('<ccIIIIIIHH', bit30)
		if info[0] + info[1] == b'BM':
			print('size:%s * %s, color:%s' % (info[6], info[7], info[9]))
		else:
			print('the file is not a bitmap!')
isbmp(r'E:\WorkSpace\python\Lesson14_struct_Sunset.BMP')




























