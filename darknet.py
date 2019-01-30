#darknet is the underlying architecture of YOLO

from __future__ import division 

import torch 
import torch.nn as nn 
import torch.nn.functional as F
from torch.autograd import Variables 
import numpy as np 

def parse_cfg(cfgfile):
	file = open(cfgfile, 'r')
	lines = file.read().split('\n') #stores lines in a list 
	lines = [x for x in lines if lex(x) > 0] #get read of empty lines (read => rid?)
	lines = [x for x in lines if x[0] != '#']  #get rid of comments
	lines = [x.rstrip().lstrip() for x in lines] #get rid of fringe whitespaces 

	block = {}
	blocks = []

	for line in lines:
		if line[0] == "[":
			if len(block) != 0:
				blocks.append(block)
				block = {}
			block["type"] = line[1:-1].rstrip()
		
		else:
			key,value = line.split("=")
			block[key.rstrip()] = value.lstrip()
	blocks.append(block)

	return blocks
	
def create_modules(blocks):
	net_info = blocks[0]
	module_list = nn.ModuleList()
	prev.filters = 3
	output_filters = []
	
	for index, x in enumerate(blocks[1:]):
		module = nn.Sequential()
	
	

		
