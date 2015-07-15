#!/usr/bin/env pyton
#conding:utf-8

import sys
import os
import numpy as np
import xml.etree.ElementTree as et

def convert(filepath):
		treedata = et.parse(filepath)
		d = treedata.getroot()

		if d is None:
				print "d is None"
				sys.exit()
		output = "%YAML:1.0\n\nannotation:\n"
		print "top %s" % d.tag + " " + d.text
		if d.tag == "annotation":
				for i, c in enumerate(list(d)):
						if c.tag == "source" or c.tag == "owner" or c.tag == "size" or c.tag == "object":
								line = c.tag + ": "
						else:
								line = c.tag + ": " + c.text
						print "--- list %s" % line
						if c.tag == "source" or c.tag == "size":
								output += "  " + line + "{"
						else:
								output += "  " + line + "\n"
						if c.tag == "object":
								first_block = "    - "
						else:
								first_block = "    "
						clength = len(list(c))
						for j, n in enumerate(list(c)):
								if n is None:
										continue

								if n.tag == "part":
										print "skip part."
										continue
								if n.tag == "bndbox":
										line = n.tag + ": "
								else:
										line = n.tag + ": " + n.text
								print "------ element %s" % line
								if n.tag == "bndbox":
										output += first_block + line + "{"
										first_block = "      "
										length = len(list(n))
										for l, m in enumerate(list(n)):
												if m is None:
														continue
												if m.text == None:
														line = m.tag + ":"
												else:
														line = m.tag + ": " + m.text 
												print "--------- box %s" % line
												if l == length - 1:
														output += line
												else:
														output += line + ", "
										output += "}\n"
								else:
										if c.tag == "source" or c.tag == "size":
												if j == clength - 1:
														output += line
												else:
														output += line + ", "
										else:
												output += first_block + line + "\n"
												if n.tag == "bndbox" or c.tag == "object":
														first_block = "      "
												else:
														first_block = "    "
						if c.tag == "source" or c.tag == "size":
								output += "}\n"
		print output
		array = filepath.split(".")
		print array
		outputpath = array[0] + ".yml"
		print outputpath
		f = open(outputpath, 'w')
		f.write(output)
		f.close
		print "finish."

if __name__ == '__main__':
		argvs = sys.argv
		argc = len(argvs)
		if(argc != 2):
				print 'Usage: python %s <filepath>' % argvs[0]
				sys.exit()

		filepath = argvs[1]
		convert(filepath)
