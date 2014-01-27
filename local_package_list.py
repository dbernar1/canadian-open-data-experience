#!/usr/local/bin/python3
#import sqlite3
import json, urllib.request, time
from caching import the_data_is_available_in_cache, save_data_in_local_cache, get_cached_data_for
import re

def get_api_data_that_may_be_from_local_cache( url ):
	'''
	To clear the cache, delete the file from the cache directory.
	Files are named same as the URL.
	'''
	if the_data_is_available_in_cache( url ):
		if re.search( 'package_show', url ) is not None:
			api_data = '{"result": ""}'
		else:
			api_data = get_cached_data_for( url )
	else:
		api_data = urllib.request.urlopen( url ).read().decode( 'utf-8' )
		save_data_in_local_cache( url, api_data )
		time.sleep( 0.1 )
	
	return api_data

def all_package_ids():
	'''
	>>> isinstance( all_packages(), list )
	True
	'''
	package_list_json = get_api_data_that_may_be_from_local_cache( 'http://data.gc.ca/data/en/api/action/package_list' )
	return json.loads( package_list_json )[ 'result' ]

def package_data( package_id ):
	package_data = get_api_data_that_may_be_from_local_cache( 'http://data.gc.ca/data/en/api/action/package_show?id=' + package_id )

if '__main__' == __name__:
	import sys

	for package_id in all_package_ids():
		package_data( package_id )

	#import doctest
	#doctest.testmod()
