#!/usr/bin/python
# -*- coding: utf-8 -*-
evil = "Prepare to be destroyed!"
good = "I come in peace."
junk = """                �+��S��w����[.�o����3�?.�$.�,��L���o
H�F�)Uv%*]V�H�4�N/UƁ�w�U�~YM�&NSw �g:�s�~��G[oAl�����r��o��K�$ц��ޜ1K	��}�
"""
from hashlib import sha256
if sha256(junk).hexdigest() == "b89730b8e7fb523c6a1fa635c026705fe71599380f5463591098cf5f5b82ef8c": 
	print (good)
else:
	print (evil)
