#!/usr/local/bin/python3
#import sqlite3
import json, glob, os, re

for cached_package_module in glob.glob( './cache/*' ):
	#print( cached_package_module )
	if re.match( '.*package-show.*', cached_package_module ) is not None:
		with open( cached_package_module, 'r' ) as package_metadata_file:
			api_response_string = package_metadata_file.read()
			package_metadata = json.loads( api_response_string )[ 'result' ]
			with open( './cache/renamed/http-data-gc-ca-data-en-api-action-package-show-id-' + package_metadata[ 'id' ], 'w' ) as renamed_file:
				renamed_file.write( api_response_string )
