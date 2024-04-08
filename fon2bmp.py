# coding: utf-8


# fonファイルを幅128ドット高さ128ドット2色のbmpファイルに変換するスクリプト
# VERSION:1.0
# DATE:2024/04/08
# AUTHER:chiqlappe
# USAGE: python3 fon2bmp.py <fon file> <bmp file>


import argparse	# https://docs.python.org/ja/3/howto/argparse.html?highlight=argparse
import os # os.path.isfile()

parser = argparse.ArgumentParser()
parser.add_argument("fonfile", help="FON file name")
parser.add_argument("bmpfile", help="BMP file name")
args = parser.parse_args()

ws = 128 # bmpの幅
hs = 128 # bmpの高さ

print(args.fonfile,"->",args.bmpfile)

header = [0x42,0x4d,0x3e,0x08,0x00,0x00,0x00,0x00,0x00,0x00,0x3e,0x00,0x00,0x00,0x28,0x00,
		  0x00,0x00,  ws,0x00,0x00,0x00,  hs,0x00,0x00,0x00,0x01,0x00,0x01,0x00,0x00,0x00,
		  0x00,0x00,0x00,0x08,0x00,0x00,0x12,0x0b,0x00,0x00,0x12,0x0b,0x00,0x00,0x02,0x00,
		  0x00,0x00,0x02,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xff,0xff,0xff,0x00]

if os.path.isfile(args.fonfile):

	bmp = [[0 for _ in range(8)] for _ in range(256)] # bmp[256][8]

	r = open(args.fonfile,'rb')
	w = open(args.bmpfile,'wb')
	w.write(bytearray(header))
	
	for x in range(16):
		for y in range(16):
			for l in range(8):
				bmp[(15-y) + x * 16][7-l] = r.read(1)

	for y in range(16):
		for l in range(8):
			for x in range(16):
				w.write(bmp[y + x * 16][l])

	r.close()
	w.close()
	
	print("Done.")
	
else:

	print(args.fonfile," is not found.");

