# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe, sys
sys.argv.append("py2exe")
op={
	"py2exe":{
		"includes":"Carbon, Carbon.Files, _scproxy, _sysconfigdata, http.client, netbios, win32pipe, win32wnet, winreg"
	}
}
setup(
	option=op,
    console=[{"script": "main_logic.py"}]
    
)