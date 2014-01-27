#!/usr/local/bin/python3
import os, re

def the_data_is_available_in_cache( url ):
	'''
	>>> the_data_is_available_in_cache( 'http://some-url-that-does-not-exist-in-cache.com' )
	False

	>>> url = 'http://cache-this-url-for-purposes-of-this-example.com'
	>>> save_data_in_local_cache( url, 'sample data' )
	>>> the_data_is_available_in_cache( url )
	True
	>>> clear_from_cache( 'http://cache-this-url-for-purposes-of-this-example.com' )
	'''
	return os.path.exists( local_cache_path_for( url ) )

def save_data_in_local_cache( url, data ):
	'''
	>>> example_url = 'http://example.com/data_path'
	>>> save_data_in_local_cache( example_url, 'example data' )
	>>> get_cached_data_for( example_url )
	'example data'
	>>> clear_from_cache( example_url )
	'''
	with open( local_cache_path_for( url ), 'w' ) as cache_file:
		cache_file.write( data )

def get_cached_data_for( url ):
	'''
	>>> example_url = 'http://example.com/path'
	>>> save_data_in_local_cache( example_url, 'example data' )
	>>> get_cached_data_for( example_url )
	'example data'
	>>> clear_from_cache( example_url )
	'''
	with open( local_cache_path_for( url ) ) as cache_file:
		cached_data = cache_file.read()
	
	return cached_data

def local_cache_path_for( url ):
	'''
	>>> local_cache_path_for( 'http://example.com/path' )
	'./cache/http-example-com-path'
	'''
	filename_for_url = re.sub( '[^a-zA-Z]+', '-', url )
	return os.path.join( os.path.dirname( __file__ ), 'cache/' + filename_for_url )

def clear_from_cache( url ):
	'''
	>>> example_url = 'http://example.com/api_path'
	>>> save_data_in_local_cache( example_url, 'example data' )
	>>> clear_from_cache( example_url )
	>>> os.path.exists( local_cache_path_for( example_url ) )
	False
	'''
	os.unlink( local_cache_path_for( url ) )

if '__main__' == __name__:
	import doctest
	doctest.testmod()
