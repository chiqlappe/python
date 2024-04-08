# coding: utf-8


# 幅128ドット高さ128ドット2色のbmpファイルをfonファイルに変換するスクリプト
# VERSION:1.0
# DATE:2024/03/29
# AUTHER:chiqlappe
# USAGE: python3 bmp2fon.py <bmp file> <font file>


import argparse	# https://docs.python.org/ja/3/howto/argparse.html?highlight=argparse
import os # os.path.isfile()

parser = argparse.ArgumentParser()
parser.add_argument("bmpfile", help="BMP file name")
parser.add_argument("fonfile", help="FON file name")
args = parser.parse_args()

print(args.bmpfile,"->",args.fonfile)

if os.path.isfile(args.bmpfile):

	font = [[0 for _ in range(8)] for _ in range(256)] # font[256][8]

	r = open(args.bmpfile,'rb')
	w = open(args.fonfile,'wb')

	r.read(62) # ヘッダ部を捨てる

	for y in range(16): # 0~15
		for l in range(8): # 0~7
			for x in range(16): # 0~15
				font[y + x * 16][l] = r.read(1)

	for x in range(16):
		for y in range(16):
			for l in range(8):
				w.write(font[(15-y) + x * 16][7-l])

	r.close()
	w.close()

	print("Done.")
	
else:

	print(args.bmpfile," is not found.");

