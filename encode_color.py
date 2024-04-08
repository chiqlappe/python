# coding: utf-8


# 幅128ドット高さ128ドット4色のbmpファイルをマルチカラーエンコードされたbmpファイルに変換するスクリプト
# VERSION:1.0
# DATE:2024/04/08
# AUTHER:chiqlappe
# USAGE: python3 encode_color.py <in file> <out file>


import argparse	# https://docs.python.org/ja/3/howto/argparse.html?highlight=argparse
import os # os.path.isfile()

parser = argparse.ArgumentParser()
parser.add_argument("infile", help="4-colors BMP file name")
parser.add_argument("outfile", help="2-colors BMP file name")
args = parser.parse_args()

ws = 128 # bmpの幅
hs = 128 # bmpの高さ

print(args.infile,"->",args.outfile)

header = [0x42,0x4d,0x3e,0x08,0x00,0x00,0x00,0x00,0x00,0x00,0x3e,0x00,0x00,0x00,0x28,0x00,
		  0x00,0x00,  ws,0x00,0x00,0x00,  hs,0x00,0x00,0x00,0x01,0x00,0x01,0x00,0x00,0x00,
		  0x00,0x00,0x00,0x08,0x00,0x00,0x12,0x0b,0x00,0x00,0x12,0x0b,0x00,0x00,0x02,0x00,
		  0x00,0x00,0x02,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xff,0xff,0xff,0x00]


if os.path.isfile(args.infile):

	r = open(args.infile,'rb')
	r.read(118) # ヘッダ部を捨てる
	w = open(args.outfile,'wb')
	if w:
		w.write(bytearray(header))
		for _ in range(128*16):
			b = 0b00000000
			for _ in range(4):
				dots = r.read(1) # %uuuudddd %uuuu=パレット番号1, %dddd=パレット番号2
				b = b << 2
				b |= dots[0] & 0b00000011
			w.write(b.to_bytes(1,"little"))
		w.close()
	else:
		print("FILE OPEN ERROR")

	r.close()
	print("Done.")
	
else:
	print(args.infile," IS NOT FOUND");


