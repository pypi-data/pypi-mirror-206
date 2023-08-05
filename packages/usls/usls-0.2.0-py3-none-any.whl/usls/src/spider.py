from baiduspider import BaiduSpider
from tqdm import tqdm
import urllib
from pathlib import Path
import rich
import sys
import re
from omegaconf import OmegaConf, DictConfig
from typing import Dict, List


from usls.src.utils import CONSOLE, IMG_FORMAT, VIDEO_FORMAT, LABEL_FORMAT, increment_path




def spider_baidu_image(
		words,
		output_dir,
	):
	# assert isinstance(word, str), f'[b green]{word}[/b green] [red]is not type of string!'


	responses = []
	for word in words:
		responses.append(BaiduSpider().search_pic(word))


	# get global info
	# response = BaiduSpider().search_pic(word)

	table = rich.table.Table(
		title='\nbaidu image spider', 
		# title_style='left',
		box=rich.box.ASCII,   # box.MARKDOWN ,SIMPLE   , rich.box.ASCII2
		show_lines=False, 
		show_header=True,
		caption='',
		caption_justify='center',
		header_style='',
		# show_footer=True,
	)

	table.add_column(
		header="Words", 
		footer='',
		justify="left", 
		# style="b", 
		no_wrap=False
	)
	table.add_column(
		header="Pages Found", 
		footer='',
		justify="left", 
		# style="b", 
		no_wrap=False
	)
	table.add_column(
		header="Images Found", 
		footer='',
		justify="left", 
		# style="b", 
		no_wrap=False
	)

	for i in range(len(words)):
		table.add_row(f"{words[i]}", f"{responses[i].pages}", f"{responses[i].total}", end_section=False)
	CONSOLE.print(table)


	# interact with user about page start & end.
	CONSOLE.log(f"😁 Give me 2 numbers(page begin & end, seperated by whatever you want).")
	page_begin, page_end = list(), list()
	for i, word in enumerate(words):
		_count = 0
		while True:
			_count += 1  # attempt counter
			_input = CONSOLE.input(
				# prompt=f"{word} | 😁 Give me 2 numbers(page begin & end, seperated by whatever you want).\n> "
				prompt=f"{word} > "
			)
			c = re.findall('\d+', _input)

			if len(c) != 2:
				if _count == 1:
					CONSOLE.log(f"[b red]🙂 Two Numbers! Do it again!")
				elif _count == 2:
					CONSOLE.log(f"[b red]🙃 What's wrong with you! 2! Numbers!")
				else:
					CONSOLE.log(f"[b red]🤬 Fuck you! Mother-fucker! Fuck offffff!")
					sys.exit()
			elif int(c[0]) >= int(c[1]):
				CONSOLE.log(f"[b red]😑 Page_begin should be less than page end!!")
			elif int(c[0]) < 0:
				CONSOLE.log(f"[b red]😑 Page_begin should be grater than 0!!")
			elif int(c[1]) > responses[i].pages:
				CONSOLE.log(f"[b red]😑 Page_end should be less than max num_page!!")
			else:
				# page_begin, page_end = int(c[0]), int(c[1])
				page_begin.append(int(c[0]))
				page_end.append(int(c[1]))
				break


	for i, word in enumerate(tqdm(words, desc='Downloading...')):

		# saveout dir
		save_dir = increment_path(Path(output_dir)/word, exist_ok=False, sep='-')  # increment run

		# loop
		for n in range(page_begin[i], page_end[i]):
			
			res = BaiduSpider().search_pic(word, n)  # spider
			(save_dir / str(n)).mkdir(parents=True, exist_ok=True)  # make dir for every page

			# loop to save
			plain = res.__dict__['plain']
			for idx, item in enumerate(plain):
				url = item['url']
				try:
					saveout = Path(save_dir / str(n) / (str(idx) + '.jpg')) 
					urllib.request.urlretrieve(str(url), filename=str(saveout))
				# except [urllib.error.ContentTooShortError, urllib.error.HTTPError]:
				except Exception as error:
					# print(error)
					continue
					# pass
				# finally:
				# 	continue



def run_spider(args: DictConfig):
	spider_baidu_image(
		words=args.words,
		output_dir=args.output_dir
	)

