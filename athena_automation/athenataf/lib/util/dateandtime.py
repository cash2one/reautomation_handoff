import os
import logging
import time as BaseTime
from datetime import *

def get_current_date_mmddyyyy():
	return BaseTime.strftime("%m/%d/%Y", BaseTime.localtime(BaseTime.time()))

def get_date_after_ndays_mmddyyyy(days):
	return BaseTime.strftime("%m/%d/%Y", BaseTime.localtime(BaseTime.time() + days*24*60*60))	
	
def get_date_after_nmonths_mmddyyyy(months):
	return BaseTime.strftime("%m/%d/%Y", BaseTime.localtime(BaseTime.time() + months*30*24*60*60))	
	
def get_date_after_nyears_mmddyyyy(years):
	return BaseTime.strftime("%m/%d/%Y", BaseTime.localtime(BaseTime.time() + years*12*30*24*60*60))	

def get_date_after_ndays_ddmmyyyy(days):
	return BaseTime.strftime("%d/%m/%Y", BaseTime.localtime(BaseTime.time() + days*24*60*60))	
	
def get_date_after_nmonths_ddmmyyyy(months):
	return BaseTime.strftime("%d/%m/%Y", BaseTime.localtime(BaseTime.time() + months*30*24*60*60))	
	
def get_date_after_nyears_ddmmyyyy(years):
	return BaseTime.strftime("%d/%m/%Y", BaseTime.localtime(BaseTime.time() + years*12*30*24*60*60))	
	
def get_date_after_nmonths_mmddyyyy_hyphenformat(months):
	return BaseTime.strftime("%m-%d-%Y", BaseTime.localtime(BaseTime.time() + months*30*24*60*60))

def get_date(days,format):
	
	'''
	`	This function give the date of specified format after adding the days given 
		:Param : days 		:   No of Days to add for the current date 
		:Param : type		:   int
		
		:Param : Format		:   What Format that the should be return
		:Param : type		:   string
		
		
	'''
	
	newDate = date.today()+timedelta(days=days)
	return newDate.strftime("%s"%format)

def get_current_hour_minute_second(): 
	'''
	This function give the current time in hours : minutess : seconds
	'''
	import datetime
	now = datetime.datetime.now()  
	return str(datetime.time(now.hour, now.minute, now.second)).split(':')	