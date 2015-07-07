import time
import threading
import logging

logger = logging.getLogger('athena')

class WinFileUploader(threading.Thread):
	def __init__(self, file_path):
		threading.Thread.__init__(self)
		self.file_path =  file_path
		# logger.debug(self.file_path)
		
	def run(self):
		# logger.debug("winFileUploader: Begins1")
		logger.debug("Native Windows : Import PyWinAuto")
		import pywinauto
		# logger.debug("winFileUploader: Begins2")
		pwa_app = pywinauto.application.Application()
		for i in range(1,50):
			logger.debug("Finding. iteration: %d" % (i + 1))
			w_handle = None
			try:
				logger.debug("Native Windows : Title = 'Open'")
				w_handle = pywinauto.findwindows.find_windows(title=u'Open', class_name='#32770')[0]
				break
			except:
				try:
					logger.debug("Native Windows : Title = 'File Upload'")
					w_handle = pywinauto.findwindows.find_windows(title=u'File Upload', class_name='#32770')[0]
					break
				except:
					try:
						logger.debug("Native Windows : Title = 'ChooseFile to Uploads'")
						w_handle = pywinauto.findwindows.find_windows(title=u'Choose File to Upload', class_name='#32770')[0]
						break
					except:
						try:
							logger.debug("Native Windows : Title = 'Select Files to upload'")
							w_handle = pywinauto.findwindows.find_windows(title_re=u'Select\s+file\(s\)\s+to\s+upload by', class_name='#32770')[0]
							break
						except:
							logger.debug("Not found in this cycle")
							time.sleep(1)

		logger.debug("w_handle is %s" % w_handle)
		if w_handle is None:
			logger.debug("WinFileUploader: Windows handle is None")
			raise Exception("Upload Window was not found, so WinFileUploader closed the browser.")
		else:
			logger.debug("WinFileUploader: Clicking Edit")
			window = pwa_app.window_(handle=w_handle)
			window.SetFocus()
			ctrl = window['Edit']
			ctrl.Click()
			ctrl = window['Edit']
			logger.debug("WinFileUploader: Sending keys for file path")
			ctrl.TypeKeys(self.file_path)
			time.sleep(3)
			logger.debug("WinFileUploader: Clicking opne button")
			ctrl = window['&Open']
			ctrl.SetFocus()
			ctrl.Click()
			logger.debug("WinFileUploader: all done.")

class WinFileDownloader(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		logger.debug("WinFileDownloader: Initialized")
		
	def run(self):
		logger.debug("WinFileDownloader: Started")
		import pywinauto
		pwa_app = pywinauto.application.Application()
		w_handle = None
		logger.debug("WinFileDownloader: Finding Mozilla download Dialog window")
		for i in range(1,50):
			try:
				w_handle = pywinauto.findwindows.find_windows(title_re=u'Opening\s+', class_name='MozillaDialogClass')[0]
				break
			except:
				time.sleep(1)				
		logger.debug("w_handle is %s" % w_handle)
		if w_handle is None:
			logger.debug("WinFileDownloader: Windows handle is None")
			raise Exception("Download Window was not found, so WinFileDownloader closed the browser.")
		else:
			logger.debug("WinFileDownloader: Download window found.")
			window = pwa_app.window_(handle=w_handle)
			window.SetFocus()
			window.TypeKeys('%s')
			window = pwa_app.window_(handle=w_handle)
			# window.Click()
			window.SetFocus()
			window.TypeKeys('{TAB}')
			window.TypeKeys('{TAB}')
			window.TypeKeys('{ENTER}')
			time.sleep(15)
			logger.debug("WinFileDownloader: Exiting.")

			
class AuthenticateLogin(threading.Thread):
	def __init__(self , username , pwd):
		threading.Thread.__init__(self)
		self.username = username
		self.pwd= pwd
		logger.debug("AuthenticateLogin: Initialized")
		
	def run(self):
		logger.debug("AuthenticateLogin: Started")
		import pywinauto
		pwa_app = pywinauto.application.Application()
		w_handle = None
		logger.debug("AuthenticateLogin: Finding Mozilla login Authentication window")
		for i in range(1,50):
			try:
				w_handle = pywinauto.findwindows.find_windows(title_re=u'Authentication Required', class_name='MozillaDialogClass')[0]
				break
			except:
				time.sleep(1)			
		logger.debug("w_handle is %s" % w_handle)
		if w_handle is None:
			logger.debug("AuthenticateLogin: Windows handle is None")
			raise Exception("Login Window was not found, so AuthenticateLogin closed the browser.")
		else:
			logger.debug("AuthenticateLogin: Authentication window found.")
			window = pwa_app.window_(handle=w_handle)
			window.SetFocus()
			window.TypeKeys(self.username)
			window.TypeKeys('{TAB}')
			window.TypeKeys(self.pwd)
			window.TypeKeys('{TAB}')
			window.TypeKeys('{ENTER}')
			time.sleep(3)
			logger.debug("AuthenticateLogin: Exiting.")

	
class WinDownloadNotificationBypass(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		logger.debug("WinDownloadNotificationBypass: Initialized.")
		
	def run(self):
		logger.debug("WinDownloadNotificationBypass: Started.")
		try:
			logger.debug("WinDownloadNotificationBypass: Finding Notification window.")
			import pywinauto
			pwa_app = pywinauto.application.Application()
			w_handle = pywinauto.findwindows.find_windows(title_re=u'(.*?)', class_name='MozillaWindowClass')[0]
			if w_handle is not None:
				logger.debug("WinDownloadNotificationBypass: Notification window found.")
				window = pwa_app.window_(handle=w_handle)
				window.Click()
				logger.debug("WinDownloadNotificationBypass: Exiting.")
			else:
				logger.debug("WinDownloadNotificationBypass: Notification window not found.")
		except:
			pass
		time.sleep(15)
		
class chromeDownloadAlert(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)		
		logger.debug("chromeDownloadAlert: Initialized")
		
	def run(self):

		import pywinauto
		logger.debug("chromeDownloadAlert: Started")
		logger.debug("Native Windows : Import PyWinAuto")
		pwa_app = pywinauto.application.Application()
		for i in range(1,50):
			logger.debug("Finding. iteration: %d" % (i + 1))
			w_handle = None
			try:
				logger.debug("chromeDownloadAlert : Title = 'Downloads'")
				w_handle = pywinauto.findwindows.find_windows(title=u'Downloads - Google Chrome', class_name='Chrome_WidgetWin_1')[0]
				break
			except:
				time.sleep(1)

		logger.debug("w_handle is %s" % w_handle)
		if w_handle is None:
			logger.debug("chromeDownloadAlert: Download Window not found.")
		else:
			window = pwa_app.window_(handle=w_handle)
			logger.debug("chromeDownloadAlert: Set Focus")
			window.SetFocus()
			logger.debug("chromeDownloadAlert: ENTER")
			window.TypeKeys('{ENTER}')	
			logger.debug("chromeDownloadAlert: Go Back All Done")	