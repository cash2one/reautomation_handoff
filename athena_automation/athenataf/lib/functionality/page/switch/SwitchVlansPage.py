from athenataf.lib.util.WebPage import WebPage
import traceback
import logging
import time
from __builtin__ import str
logger = logging.getLogger('athenataf')

class SwitchVlansPage(WebPage):
	def __init__(self, test, browser, config):
		WebPage.__init__(self, "SwitchVlans", test, browser, config)
		self.test.assertPageLoaded(self)


	def isPageLoaded(self):
		if self.new_vlan:
			return True    
		else:
			return False
			
	def buy_time(self):
		import time
		time.sleep(5)

	def creating_vlan(self):
		'''
			Creating new VLAN 1
		'''
		logger.debug("Clicking on New button ")
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id.set(self.config.config_vars.set_id)
		logger.debug("Vlan : Entering description ")
		# self.click_description.click()
		self.set_description.set(self.config.config_vars.set_description)
		logger.debug("Vlan : Entering ip address ")
		# self.click_ip_address.click()
		self.set_ip_address.set(self.config.config_vars.set_ip_address)
		logger.debug("Vlan : Entering net mask ")
		# self.click_net_mask.click()
		self.set_net_mask.set(self.config.config_vars.set_net_mask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_1.click()
		logger.debug("Clicking on save button ")
		self.save_setting.click()

	def change_default_vlan_value(self):
		'''
			Changing the value of vlan 
		'''
		logger.debug("Vlan : Changing the description value ")
		import time
		time.sleep(5)
		logger.debug("Vlan : Clicking on edit button ")
		self.edit_vlan_1.click()
		time.sleep(5)
		self.set_description.set(self.config.config_vars.set_description1)
		logger.debug("Vlan : Changing the ip address value ")
		self.set_ip_address.set(self.config.config_vars.set_ip_address1)
		logger.debug("Vlan : Changing the net mask value ")
		self.set_net_mask.set(self.config.config_vars.set_net_mask1)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_1.click()
		logger.debug("VLan : Clicking on save button ")
		self.save_setting.click()

	def delete_default_vlan(self):
		'''
			Deleting the vlans 
		'''
		if not self.zero_vlans :
			if self.test1:
				logger.debug("VLan : Clicking on test1")
				self.buy_time()
				self.test1.click()
				self._delete_vlan()
			if self.test2:
				logger.debug("VLan : Clicking on test2")
				self.buy_time()
				self.test2.click()
				self._delete_vlan()
			if self.test3:
				logger.debug("VLan : Clicking on test3")
				self.buy_time()
				self.test3.click()
				self._delete_vlan()
			if self.test4:
				logger.debug("VLan : Clicking on test4")
				self.buy_time()
				self.test4.click()
				self._delete_vlan()

	def _delete_vlan(self):
		'''
		Click on delete button and save settings .
		'''
		if self.delete_vlan :
			logger.debug("VLan : Clicking on delete button")
			self.delete_vlan.click()
			logger.debug("VLan : Clicking on save setting button")
			self.save_setting.click()
			import time
			time.sleep(8)

	def creating_vlan_2(self):
		'''
			Creating new VLAN 2
		'''
		logger.debug("Clicking on New button ")
		import time		
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_2.set(self.config.config_vars.set_id_2)
		logger.debug("Vlan : Entering description ")
		# self.click_description_2.click()
		self.set_description_2.set(self.config.config_vars.set_description_2)
		logger.debug("Vlan : Entering ip address ")
		# self.click_ip_address_2.click()
		self.set_ip_address_2.set(self.config.config_vars.set_ip_address_2)
		logger.debug("Vlan : Entering net mask ")
		# self.click_net_mask_2.click()
		self.set_net_mask_2.set(self.config.config_vars.set_net_mask_2)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_2.click()
		logger.debug("Clicking on save button ")
		self.save_setting.click()

	def creating_vlan_3(self):
		'''
			Creating new VLAN 3
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_3.set(self.config.config_vars.set_id_3)
		logger.debug("Vlan : Entering description ")
		# self.click_description_3.click()
		self.set_description_3.set(self.config.config_vars.set_description_3)
		logger.debug("Vlan : Entering ip address ")
		# self.click_ip_address_3.click()
		self.set_ip_address_3.set(self.config.config_vars.set_ip_address_3)
		logger.debug("Vlan : Entering net mask ")
		# self.click_net_mask_3.click()
		self.set_net_mask_3.set(self.config.config_vars.set_net_mask_3)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_3.click()
		logger.debug("Clicking on save button ")
		self.save_setting.click()

	def creating_vlan_4(self):
		'''
			Creating new VLAN 4
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_4.set(self.config.config_vars.set_id_4)
		logger.debug("Vlan : Entering description ")
		# self.click_description_4.click()
		self.set_description_4.set(self.config.config_vars.set_description_4)
		logger.debug("Vlan : Entering ip address ")
		# self.click_ip_address_4.click()
		self.set_ip_address_4.set(self.config.config_vars.set_ip_address_4)
		logger.debug("Vlan : Entering net mask ")
		# self.click_net_mask_4.click()
		self.set_net_mask_4.set(self.config.config_vars.set_net_mask_4)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_4.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()

	def verify_existing_vlan_description(self,value=None):
		'''
			Entering the value in description field
		'''
		logger.debug("Vlan : Clicking on edit button ")
		self.buy_time()
		self.edit_vlan_1.click()
		self.buy_time()
		logger.debug("Vlan : Changing the description value ")
		self.set_description.set(value)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_1.click()
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		time.sleep(2)

	def assert_vlan_description(self,value):
		self.buy_time()
		logger.debug("Vlan : Clicking on edit button ")
		self.edit_vlan_1.click()
		self.buy_time()
		# self.click_description.click()
		if not self.set_description.get() == value :
			raise AssertionError(" Vlan description is not set to given value '%s' .Traceback: %s " %(value,traceback.format_exc()))
		logger.debug("VLan : Clicking on cancel button ")
		self.edit_cancle_1.click()

	def editing_vlan_2(self):
		'''
			Editing the vlan 2 fields values
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_2.set(self.config.config_vars.set_id_2)
		logger.debug("Vlan : Entering description ")
		self.set_description_2.set(self.config.config_vars.set_description_2)
		logger.debug("Vlan : Entering ip address ")
		self.set_ip_address_2.set(self.config.config_vars.set_ip_address_2)
		logger.debug("Vlan : Entering net mask ")
		self.set_net_mask_2.set(self.config.config_vars.set_net_mask_2)       

	def clicking_cancel_button(self):
		'''
			Clicking on Cancel Button
		'''
		logger.debug("Clicking on cancel button ")
		self.cancel_vlan.click()		

	def editing_vlan_1(self):
		'''
			Editing the vlan 1 fields values
		'''
		logger.debug("Vlan : Changing the description value ")
		self.set_description.set(self.config.config_vars.set_description1)
		logger.debug("Vlan : Changing the ip address value ")
		self.set_ip_address.set(self.config.config_vars.set_ip_address1)
		logger.debug("Vlan : Changing the net mask value ")
		self.set_net_mask.set(self.config.config_vars.set_net_mask1)

	def clicking_id_label(self):
		'''
			Clicking on ID label
		'''
		logger.debug("Clicking on ID label ")
		self.id_header.click()

	def creating_new_vlan(self,id=None,dscrp=None,ip=None,netmask=None, save = True):
		'''
			Creating new VLAN 1
		'''
		logger.debug("Clicking on New button ")
		time.sleep(4)
		self.new_vlan.click()
		logger.debug("Vlan : Entering id ")
		self.set_id.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_1.click()
		if save:
			logger.debug("Clicking on save button ")
			self.save_setting.click()

	def assert_netmask_message(self):
		'''
			Asserting subnet mask
		'''
		if not self.netmask_error_msg:
			raise AssertionError("Netmask error message not shown .Traceback: %s " %(traceback.format_exc()))
		logger.debug("Clicking on OK button ")
		self.ok_error_msg.click()

	def selcet_source_nat(self):
		'''
			Clicking on Source NAT check box for vlan 1
		'''
		logger.debug('VLAN: clicking on edit button')
		self.buy_time()
		self.edit_vlan_1.click()
		logger.debug("Vlan : Selecting Source NAT ")
		self.buy_time()
		self.check_source_nat.click()
		logger.debug("Vlan : click on update button ")
		self.update_vlan_1.click()

	def click_save_button(self):
		'''
			Clicking on save setting button
		'''
		logger.debug("Clicking on save setting button ")
		self.save_setting.click()    

	def creating_new_vlan_2(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 2
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_2.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			# self.click_description_2.click()
			self.set_description_2.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			# self.click_ip_address_2.click()
			self.set_ip_address_2.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			# self.click_net_mask_2.click()
			self.set_net_mask_2.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_2.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()

	def creating_new_vlan_3(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 3
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_3.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			# self.click_description_3.click()
			self.set_description_3.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			# self.click_ip_address_3.click()
			self.set_ip_address_3.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			# self.click_net_mask_3.click()
			self.set_net_mask_3.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_3.click()
		logger.debug("Clicking on save button ")
		self.save_setting.click()    

	def selcet_source_nat_2(self):
		'''
			Clicking on Source NAT check box for vlan 2
		'''
		logger.debug('VLAN: clicking on edit button')
		self.edit_vlan_2.click()
		logger.debug("Vlan : Selecting Source NAT ")
		self.buy_time()
		self.check_source_nat_2.click()
		logger.debug("Vlan : click on update button ")
		self.update_vlan_2.click()

	def selcet_source_nat_3(self):
		'''
			Clicking on Source NAT check box for vlan 3
		'''
		logger.debug('VLAN: clicking on edit button')
		self.edit_vlan_3.click()
		logger.debug("Vlan : Selecting Source NAT ")
		self.buy_time()
		self.check_source_nat_3.click()
		logger.debug("Vlan : click on update button ")
		self.update_vlan_3.click()
		
	def assert_vlan_test1(self,value=None):
		'''
			Asserting vlan with description field as test1
		'''
		if value=='Exist':
			if not self.test1:
				raise AssertionError("Vlan test1 is not present in VLAN page")
		if value=='Not Exist':
			if self.test1:
				raise AssertionError("Vlan test1 is present in VLAN page")
			
	def assert_vlan_label_fields(self):
		'''
			Asserting label fields of vlan page
		'''
		if not self.vlan_id_label:
			raise AssertionError("Vlan: ID label is not present")
		if not self.description_label:
			raise AssertionError("Vlan: Description label is not present")
		if not self.ip_label:
			raise AssertionError("Vlan: IP address label is not present")
		if not self.netmask_label:
			raise AssertionError("Vlan: netmask label is not present")
			
	def creating_duplicate_ip_vlan(self,id=None,dscrp=None,ip=None,netmask=None):
		logger.debug("Clicking on New button ")
		self.buy_time()
		if self.new_vlan:
			self.new_vlan.click()
		self.buy_time()
		if id:
			logger.debug("Vlan : Entering id ")			
			self.set_id_2.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			# self.click_description_2.click()
			self.set_description_2.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			# self.click_ip_address_2.click()
			self.set_ip_address_2.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			# self.click_net_mask_2.click()
			self.set_net_mask_2.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_2.click()
		
	def asssert_duplicate_ip_address(self):
		'''
			Asserting duplicate ip address
		'''
		if not self.duplicate_ip_error:
			raise AssertionError("Duplicate ip address error message not shown")
		logger.debug("Vlan : click on OK error button ")
		self.ok_error_button.click()
		logger.debug("Vlan : click on edit cancel button ")
		self.edit_cancle_2.click()
	
	def asssert_duplicate_vlan_id(self,first = False):
		'''
			Asserting vlan id
		'''
		if not self.duplicate_id:
			raise AssertionError("Duplicate vlan id error message not shown")
		logger.debug("Vlan : click on OK error button ")
		self.ok_error_button.click()
		if first :
			logger.debug("Vlan : click on edit cancel button ")
			self.edit_cancle_1.click()		
		else :
			logger.debug("Vlan : click on edit cancel button ")
			self.edit_cancle_2.click()
	
	def asssert_invalid_netmask(self,edit_button=None):
		'''
			Asserting invalid subnet mask
		'''
		if not self.invalid_netmask_error:
			raise AssertionError("Invalid net mask error message not shown")
		logger.debug("Vlan : click on OK error button ")
		self.ok_error_button.click()
		if edit_button=='1':
			logger.debug("Vlan : click on edit cancel button ")
			self.edit_cancle_1.click()
		if edit_button=='2':
			logger.debug("Vlan : click on edit cancel button ")
			self.edit_cancle_2.click()	
	
	def assert_invalid_ip(self, first = False):
		'''
			Asserting invalid ip address
		'''
		if not self.invalid_ip_error:
			raise AssertionError("Invalid ip error message not shown")
		logger.debug("Vlan : click on OK error button ")
		self.ok_error_button.click()
		if first :
			logger.debug("Vlan : click on edit cancel button ")
			self.edit_cancle_1.click()		
		else :
			logger.debug("Vlan : click on edit cancel button ")
			self.edit_cancle_2.click()		
		
	def assert_invalid_ip_netmask(self):
		'''
			Asserting invalid ip address and netmask
		'''
		if not self.invalid_ip_netmask:
			raise AssertionError("Invalid ip subnet mask error message not shown")
		logger.debug("Vlan : click on OK error button ")
		self.ok_warning_button.click()
		
	def click_edit_vlan2(self):
		'''
			Clicking on vlan 2 edit button
		'''
		logger.debug("Vlan : click on edit vlan button ")
		self.edit_vlan_2.click()
		
	def delete_vlan_2(self):
		'''
			Deleting vlan 2
		'''
		if self.test2:
			logger.debug("VLan : Clicking on delete button")
			self.delete_vlan2.click()
			logger.debug("VLan : Clicking on save setting button")
			self.save_setting.click()
			import time
			time.sleep(8)
			
	def creating_new_vlan_4(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 4
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_4.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_4.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_4.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_4.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_4.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_5(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 5
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_5.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_5.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_5.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_5.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_5.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_6(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 6
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_6.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_6.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_6.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_6.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_6.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_7(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 7
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_7.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_7.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_7.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_7.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_7.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_8(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 8
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_8.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_8.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_8.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_8.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_8.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_9(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 9
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_9.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_9.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_9.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_9.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_9.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_10(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 10
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_10.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_10.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_10.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_10.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_10.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_11(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 11
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_11.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_11.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_11.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_11.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_11.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_12(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 12
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_12.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_12.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_12.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_12.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_12.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_13(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 13
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_13.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_13.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_13.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_13.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_13.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_14(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 14
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_14.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_14.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_14.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_14.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_14.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_15(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 15
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_15.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_15.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_15.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_15.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_15.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_16(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 16
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_16.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_16.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_16.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_16.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_16.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_17(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 17
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_17.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_17.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_17.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_17.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_17.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_18(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 18
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_18.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_18.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_18.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_18.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_18.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def creating_new_vlan_19(self,id=None,dscrp=None,ip=None,netmask=None):
		'''
			Creating new VLAN 19
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id_19.set(id)
		if dscrp:
			logger.debug("Vlan : Entering description ")
			self.set_description_19.set(dscrp)
		if ip:
			logger.debug("Vlan : Entering ip address ")
			self.set_ip_address_19.set(ip)
		if netmask:
			logger.debug("Vlan : Entering net mask ")
			self.set_net_mask_19.set(netmask)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_19.click()		
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def deleting_multiple_vlans(self):
		'''
			Deleting the multiple vlans
		'''
		if not self.zero_vlans :
			for num in range(1,7):
				if self.delete_vlan:
					logger.debug("VLan : Clicking on delete button")
					self.buy_time()
					self.delete_vlan.click()
					logger.debug("VLan : Clicking on save setting button")
					self.save_setting.click()
					import time
					time.sleep(3)	
	
	def vlan_1_cancel_button(self):
		'''
			Clicking on vlan 1 cancel  button
		'''
		logger.debug("Clicking on vlan 1 cancel button ")
		self.edit_cancle_1.click()
		
	def vlan_2_cancel_button(self):
		'''
			Clicking on vlan 2 cancel  button
		'''
		logger.debug("Clicking on vlan 2  cancel button ")
		self.edit_cancle_2.click()
		
	def vlan_1_edit_button(self):
		'''
			Clicking on vlan 1 edit  button
		'''
		logger.debug("Clicking on vlan 1  edit button ")
		self.buy_time()
		self.edit_vlan_1.click()
		
	def assert_source_nat(self,value=None):
		'''
			Assert source nat checkbox
		'''
		logger.debug("Vlan : Clicking on edit button ")
		self.buy_time()
		self.edit_vlan_1.click()
		time.sleep(5)
		if value == "checked":
			if self.check_source_nat.is_selected():
				raise AssertionError("VLAN page : Source nat checkbox is selected ")
		if value == "unchecked":
			if not self.check_source_nat.is_selected():
				raise AssertionError("VLAN page : Source nat checkbox is not selected ")
		logger.debug("Clicking on vlan 1 cancel button ")
		self.edit_cancle_1.click()
		
	def creating_vlan_for_description_field_validation(self,value):
		logger.debug("Clicking on New button ")
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering id ")
		self.set_id.set(self.config.config_vars.set_id)
		logger.debug("Vlan : Entering description ")
		self.set_description.set(value)
		logger.debug("Vlan : click on update button ")
		self.update_vlan_1.click()
		
	def click_save_settings(self):
		logger.debug("Clicking on save button ")
		self.save_setting.click()
		
	def assert_error_msg_for_description_field_with_33_char(self):
		if not self.set_description_33_char_error_msg :
			raise AssertionError("VLAN page : Description feild accepting more than 32 characters!! ")
		self.browser.refresh()
	
	def assert_vlan_id_max_and_min_value(self,id):
		'''
			Asserting max and min vlan id 
		'''
		logger.debug("Clicking on New button ")
		self.buy_time()
		self.new_vlan.click()
		self.buy_time()
		logger.debug("Vlan : Entering vlan id ")
		self.set_id.set(id)
		logger.debug("Clicking on Update button ")
		self.update_vlan_1.click()
		if not self.invalid_vlan_id_error_msg:
			raise AssertionError("VLAN page : max vlan id error message not shown  ")
		self.buy_time()
		logger.debug("Clicking on OK button ")
		self.ok_error_button.click()
		
	def asserting_no_of_vlans(self):
		'''
			Verify the no of created vlans on the top of vlan page
		'''
		if not self.no_of_vlans:
			raise AssertionError("VLAN page: number of created vlan not shown on the top of the page")