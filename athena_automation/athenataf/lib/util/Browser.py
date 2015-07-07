from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.common.exceptions import (
    NoSuchAttributeException,
    NoSuchElementException,
    NoSuchFrameException,
    NoSuchWindowException,
    StaleElementReferenceException,
    WebDriverException,
)

import logging
logger = logging.getLogger('athenataf') 
from athenataf.config import wd
from athenataf.config import fwork
'''
wait_for(get_element, tag='body')

'''
class Browser:
    '''
        Base class for Web Automation uses python selenium Web Driver for this module
    '''
    
    def __init__(self, name):
        '''
            Web Automation base class initiator which sets Default browser as Chrome
        '''
        self._browser = None
        try:
            if name == "firefox":
                try:
                    import os
                    profile_path = os.path.join(fwork.THIRD_PARTY_DIR, 'firefox_profile.default')
                    profile_obj = webdriver.FirefoxProfile(profile_path)
                    profile_obj.set_preference("browser.cache.disk.enable", False)
                    profile_obj.set_preference("browser.cache.memory.enable", False)
                    profile_obj.set_preference("browser.cache.offline.enable", False)
                    profile_obj.set_preference("network.http.use-cache", False)
                    profile_obj.set_preference("browser.download.folderList", 2)
                    profile_obj.set_preference("browser.download.manager.showWhenStarting", False)
                    profile_obj.set_preference("browser.download.dir", os.getcwd())
                    profile_obj.set_preference("browser.helperApps.neverAsk.openFile","text/csv,application/pdf,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")
                    profile_obj.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv,application/pdf,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")
                    profile_obj.set_preference("browser.helperApps.alwaysAsk.force", False)
                    profile_obj.set_preference("browser.download.manager.alertOnEXEOpen", False)
                    profile_obj.set_preference("browser.download.manager.focusWhenStarting", False)
                    profile_obj.set_preference("browser.download.manager.useWindow", False)
                    profile_obj.set_preference("browser.download.manager.showAlertOnComplete", False)
                    profile_obj.set_preference("browser.download.manager.closeWhenDone", False)
                    self._browser = webdriver.Firefox(profile_obj)
                except Exception,e:
                    raise
            elif name == "chrome":
                self._browser = webdriver.Chrome()
            elif name == "ie":
                self._browser = webdriver.Ie()
            else:
                raise Exception(" Invalid Browser Name")
        except Exception as e:
            logger.debug("Browser.__init__: Exception: %s" % e)
            raise
        self._browser.implicitly_wait(60)
        self._browser.set_page_load_timeout(60)
        self._browser.maximize_window()
        self.timeout = wd.TIMEOUT
        self.interval = wd.INTERVAL
        self.retries = wd.RETRIES

    def set_timeout(self, timeout):
        self.timeout = timeout
        
    def reset_timeout(self):
        self.timeout = wd.TIMEOUT

    def wait_for_body(self):
        kwargs = {'tag' : 'body'}
        vargs = []
        self.wait_for(self.get_element, *vargs, **kwargs)    

    def go_to(self, url):
        '''
            go_to() method goes to the specific URL after the browser instance launches
        '''
        self._browser.get(url)
        self.wait_for_body()

    def _get_name(self, obj):
        try:
            return obj.__name__
        except:
            return repr(obj)
            
    def get_screenshot_as_file(self, screenshot_file):
        self._browser.get_screenshot_as_file(screenshot_file)
        
    def wait_for(self, condition, *args, **kwargs):
        # print condition
        # print self._get_name(condition)
        # print args
        # print kwargs
        result = "NOT_SET"
        condition_name = self._get_name(condition)
        for try_count in range(self.retries):
            max_time = time.time() + self.timeout
            # counter = 1
            while True:
                # counter += 1
                exc = False
                exc_msg = None
                exc_trace = None
                try:
                    result = condition(*args, **kwargs)
                except Exception, e:
                    exc = True
                    exc_msg = str(e)
                    import traceback
                    exc_trace = traceback.format_exc()
                else:
                    if result != "NOT_SET":
                        return result
                if time.time() > max_time:
                    msg = 'Timed out waiting for: %s with args vargs: %s kwargs: %s' % (condition_name, str(args), str(kwargs))
                    logger.info("Problem in element identification: %s" % (msg))                    
                    if exc:
                        logger.info("Exception message for the function called in wait_for: %s" % (exc_msg))
                        logger.info("Exception trace %s" % (exc_trace))                            
                    return None
                else:
                    exc = False
                    exc_msg = None
                    exc_trace = None
                time.sleep(self.interval)        
        
    def get_elements(self, tag=None, id=None, text=None, name=None, value=None, css_class=None, index=None,text_regex=None):
        '''
            get_elements() api works for multiple web elements Identification
            on web pages
        '''
        try:
            elements = None
            if id:
                elements = self._browser.find_elements_by_id(id)
            elif name:
                # print "Tag name supplied: " + name
                elements = self._browser.find_elements_by_name(name)
            elif text:
                elements = self._browser.find_elements_by_xpath('//*[text() = %r]' % text)
            elif tag:
                elements = self._browser.find_elements_by_tag_name(tag)
            elif css_class:
                elements = self._browser.find_elements_by_class_name(css_class.replace(" ","."))
            elif text_regex:
                elements = self._browser.find_elements_by_partial_link_text(text_regex)
                print elements
            if index is None:
                # print "Index is None, return all elements found"
                return elements
            else:
                if index >= len(elements):
                    # print "Element index is outside of number of elements found."                
                    raise Exception("Element index is outside of number of elements found.")                
                else:
                    # print "Returning elements at index %d" % index
                    if (not elements[index].is_displayed()) or (not elements[index].is_enabled()):
                        raise Exception("The element is found but is not enabled/visible.")                        
                    return elements[index]
        except (WebDriverException, NoSuchElementException) as e:
            logger.debug("Browser.get_elements: Exception: %s" % str(e))
            import traceback
            raise AssertionError("Exception occured in element identification. Traceback: %s" % traceback.format_exc())                

    def get_element(self, tag=None, id=None, text=None, name=None, value=None, css_class=None, text_regex=None):
        '''
            get_element() api works for web element Identification
            on web pages uses get_elements() method and returns single 
            element on call
        '''
        try:
            elements = self.get_elements(tag,id,text,name,value,css_class,text_regex)
            # print elements
            if len(elements) == 0:
                raise Exception("0 elements found.")
            elif len(elements) > 1:
                raise Exception(">1 elements found.")
            elif (not elements[0].is_displayed()) or (not elements[0].is_enabled()):
                raise Exception("The element is found but is not enabled/visible.")                
            else:
                return elements[0]
        except (WebDriverException, NoSuchElementException) as e:
            import traceback
            raise AssertionError("Exception occured in element identification. Traceback: %s" % traceback.format_exc())        
        
    def get_elements_by_xpath(self, selector , index = None):
        '''
            Finds multiple web elements Using Xpath 
        '''
        try:
            elements = self._browser.find_elements_by_xpath(selector)
            if index is None:
                return elements
            else:
                if index >= len(elements):            
                    raise Exception("Element index is outside of number of elements found.")                
                else:
                    if (not elements[index].is_displayed()) or (not elements[index].is_enabled()):
                        raise Exception("The element is found but is not enabled/visible.")                        
                    return elements[index]
        except (WebDriverException, NoSuchElementException) as e:
            import traceback
            raise AssertionError("Element not found. Traceback: %s" % traceback.format_exc())    
        
    def get_element_by_xpath(self, selector):
        '''
            Finds single web element Using Xpath 
        '''
        try:
            elements = self.get_elements_by_xpath(selector)
            if len(elements) != 1:
                msg = 'Could not identify element: %s element(s) found' % len(elements)
                raise AssertionError(msg)
            return elements[0]
        except (WebDriverException, NoSuchElementException) as e:
            import traceback
            raise AssertionError("Element not found. Traceback: %s" % traceback.format_exc())
        
    def get_elements_by_css(self, selector , index = None):
        '''
            Finds multiple web elements Using CSS_Selectors 
        '''
        try:
            elements = self._browser.find_elements_by_css_selector(selector)
            if index is None:
                return elements
            else:
                if index >= len(elements):            
                    raise Exception("Element index is outside of number of elements found.")                
                else:
                    if (not elements[index].is_displayed()) or (not elements[index].is_enabled()):
                        raise Exception("The element is found but is not enabled/visible.")                        
                    return elements[index]
        except (WebDriverException, NoSuchElementException) as e:
            import traceback
            raise AssertionError("Element not found. Traceback: %s" % traceback.format_exc())
        
    def get_element_by_css(self, selector):
        '''
            Finds multiple web elements Using CSS_Selectors 
        '''
        try:
            elements = self.get_elements_by_css(selector)
            if len(elements) != 1:
                msg = 'Could not identify element: %s element(s) found' % len(elements)
                raise AssertionError(msg)
            return elements[0]
        except (WebDriverException, NoSuchElementException) as e:
            import traceback
            raise AssertionError("Element not found. Traceback: %s" % traceback.format_exc())
            
    def close(self):
        '''
            Close the Browser
        '''
        try:
            self._browser.quit()
        except:
            import time
            time.sleep(2)
            try:
                self._browser.quit()
            except:
                logger.debug("Webdriver was not able to close browser.")
                import traceback
                logger.debug(traceback.format_exc())
            
    def get_custom_element(self, screen_name, elem_type, elem_name, element):
        if element is None:
            return None
        ret_element = None
        if elem_type == "textbox":
            logger.debug("Control type: %s::%s :: TextBox" % (screen_name,elem_name))            
            ret_element = TextBox(element, self)
            logger.debug("Element Created: TextBox:: %s::%s" % (screen_name,elem_name))                
        elif elem_type == "select":
            ret_element = Dropdown(element, self)
        elif elem_type == "button":
            ret_element = Button(element, self)
        elif elem_type == "submit":
            ret_element = Submit(element, self)    
        elif elem_type in ["link", "menu", "bcrumb"]:
            ret_element = Link(element, self)
        elif elem_type == "chain":
            ret_element = element
        elif elem_type == "label":
            ret_element = Label(element, self)
        elif elem_type == "radio":
            ret_element = Radio(element, self)
        elif elem_type == "checkbox":
            ret_element = Checkbox(element, self)
        elif elem_type == "ignore":
            ret_element = element
        else:
            raise Exception("Control type not identified: %s" % elem_type)
        return ret_element
        
    def _alert_action(self, action, expected_text=None, text_to_write=None):
        """
        Accept or dismiss a JavaScript alert, confirmation or prompt.

        Optionally, it takes the expected text of the Popup box to check it,
        and the text to write in the prompt."""
        self.wait_for(self._browser.switch_to_alert)
        alert = self._browser.switch_to_alert()
        alert_text = alert.text
        if expected_text and expected_text != alert_text:
            raise Exception ('Element text should be %r. It is %r.' % (expected_text, alert_text))
        if text_to_write:
            alert.send_keys(text_to_write)
        if action == 'accept':
            alert.accept()
        elif action == 'dismiss':
            alert.dismiss()
        else:
            raise Exception('%r is an unknown action for an alert' % action)

    def accept_alert(self, expected_text=None, text_to_write=None):
        """
        Accept a JavaScript alert, confirmation or prompt.

        Optionally, it takes the expected text of the Popup box to check it,
        and the text to write in the prompt.

        Note that the action that opens the alert should not wait for a page with
        a body element. This means that you should call functions like
        click_element with the argument wait=Fase."""
        logger.debug('Accepting Alert')
        # self._alert_action('accept', expected_text, text_to_write)
        self._browser.find_element_by_xpath("//*[@id='confirm-save-ok']/span[text()='Yes']").click()

    def dismiss_alert(self, expected_text=None, text_to_write=None):
        """
        Dismiss a JavaScript alert.

        Optionally, it takes the expected text of the Popup box to check it.,
        and the text to write in the prompt.

        Note that the action that opens the alert should not wait for a page with
        a body element. This means that you should call functions like
        click_element with the argument wait=Fase."""
        logger.debug('Dismissing Alert')
        self._alert_action('dismiss', expected_text, text_to_write)        
            
    def getPageSource(self):
        return self._browser.page_source
        
    def refresh(self):
        self._browser.refresh()
        
    def key_press(self , key_to_press):
        '''
            sends keys to the current focused element...
        '''
        ActionChains(self._browser).send_keys(key_to_press).perform()
        
    def get_action_chain(self):
      '''
      returns an action_chain instance
      '''
      return ActionChains(self._browser)
      
    def open_new_tab(self):
        from selenium.webdriver.common.keys import Keys
        body = self._browser.find_element_by_tag_name("body")
        body.send_keys(Keys.CONTROL + 't')
    
    def assert_element(self, element, msg, raise_exception=True):
        logger.debug("Checking for element existance.")
        if element is None:
            if raise_exception:
                raise AssertionError(msg)
        if not raise_exception:
            logger.debug(msg)
        else:
            logger.debug("Element Found!!")
        return True
        
    def assert_text(self, element, value, msg, attribute=None, raise_exception=True):
        logger.debug("Check for the element")
        if self.assert_element(element, "Element Not Found"):
            src_text = element.text if not attribute else element.get_attribute_value(attribute)
            if src_text == value:
                return True
            else:
                if raise_exception:
                    raise AssertionError(msg)
        return True
        
    def assert_drop_down_value(self, element, value, msg, raise_exception=True):
        logger.debug("Check for the element")
        if self.assert_element(element, "Element Not Found"):    
            current_value = element.get_selected()  
            if current_value == value:
                return True
            else:
                if raise_exception:
                    raise AssertionError(msg)
        return True
    
    def assert_check_box_value(self, element, msg, check=False, uncheck=False):
        logger.debug("Check for the element")
        if self.assert_element(element, "Element Not Found"):
            if check:
                if element.is_selected():
                    raise AssertionError(msg)
            if uncheck:
                if not element.is_selected():
                    raise AssertionError(msg)
        return True
            
class Control:
    def __init__(self, element, browser, wait=False):
        self._elem = element
        self.counter = 1
        self.browser = browser
        self.wait = wait
        
    def __getattr__(self, property):
        if not self.__class__.__dict__.has_key("get_%s"% property):
            raise Exception("Invalid attribute name provided for control.")
        else:
            ret_value = apply(self.__class__.__dict__["get_%s"% property], [self])
            return ret_value
        
    def __nonzero__(self):
        return True
        
    def is_visible(self, raise_assert=False):
        if not self._elem.is_displayed():
            if raise_assert:
                raise AssertionError("Not visible")
            else:
                return False
        else:
            return True
            
    def is_enabled(self, raise_assert=False):
        if not self._elem.is_enabled():
            if raise_assert:
                raise AssertionError("Not visible")
            else:
                return False
        else:
            return True
            
    def wait_for_interaction(self):
        self.browser.wait_for(self.is_visible, raise_assert=True)
        self.browser.wait_for(self.is_enabled, raise_assert=True)    
    
    def get_attribute_value(self, attribute):
        '''
            Returns the value for attribute given.
        '''
        self.wait_for_interaction()
        if attribute == "text":
            return self._elem.text
        else:
            return self._elem.get_attribute(attribute)

        
class TextBox(Control):

    def set(self, text):
        '''
            Write in to the Text Field by first clicking, clearing
            and then writing in to it.
        '''
        self.wait_for_interaction()
        self._elem.click()
        self._elem.clear()
        self._elem.send_keys(text)
        self.is_visible()

    def clear(self):
        '''
            clears the text field.
        '''
        self.wait_for_interaction()
        return self._elem.clear()
    
    def get(self):
        '''
            Returns the string value written in the textbox.
        '''
        self.wait_for_interaction()
        return self._elem.get_attribute("value")

class Dropdown(Control):

    def set(self, text):
        '''
            Identifies the element in the Drop Down menu
            and then sets it to the Value.
        '''
        self.wait_for_interaction()        
        select = Select(self._elem)
        select.select_by_visible_text(text)

    def get_selected(self):
        select = Select(self._elem)
        return select.first_selected_option.text

    def get_options(self):
        '''
        Returns all the option values from a drop down value.
        '''
        options_list=[]
        for element in self._elem.find_elements_by_tag_name('option'):
            options_list.append(element.text)
        return options_list

class Clickable(Control):
    def click(self):
        '''
            Clicks the Identified web Element
        '''
        self.wait_for_interaction()
        self._elem.location_once_scrolled_into_view
        try:
            self._elem.click()
        except Exception,e:
            if self.browser._browser.name.lower()=="chrome":
                try:
                    print "Element Not Found Moving Down....."
                    print "*"*10
                    self.browser.key_press(u'\ue009')
                    self.browser.key_press(u'\ue010')
                    # self.browser.key_press(u'\ue00f')
                    self._elem.click()
                    self.browser.key_press(u'\ue009')
                    self.browser.key_press( u'\ue011')
                except:
                    raise e
            else:
                raise e
        if self.wait:
            self.browser.wait_for_body()
            
    def get_label_text(self):
        return self._elem.text
        
    def is_selected(self):
        if self._elem.is_selected():
            return True
        else:
            return False

class Link(Clickable):
    def __init__(self, element, browser):
        Clickable.__init__(self, element, browser, True)

Submit = Link
Button = Clickable
Label = Clickable
Radio = Clickable
Checkbox = Clickable