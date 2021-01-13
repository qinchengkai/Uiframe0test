import os
import unittest
import time
from public.loginApp import Mylogin
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )


class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'
        #desired_caps['app'] = PATH('E:/newCourse/zuiyou518.apk')
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['automationName'] = 'Uiautomator2'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        filedir = "D:/test/appscreenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'appscreenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def testshouye01_01(self):
        '''验证首页顶部导航栏文案显示是否正常'''
        time.sleep(8)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(6)
        navText = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        self.assertEqual(navText[0].text,"关注")
        self.assertEqual(navText[1].text, "推荐")
        self.assertEqual(navText[2].text, "视频")
        self.assertEqual(navText[3].text, "图文")


    def testshouye01_02(self):
        '''验证帖子列表内容跳转'''
        self.driver.implicitly_wait(30)
        aa = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        bb = aa.text
        aa.click()
        time.sleep(3)
        forumDetailText = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvTitle")
        cc = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvPostContent")
        self.assertEqual(forumDetailText.text,"帖子详情")
        self.assertEqual(bb,cc.text)


    def testshouye01_03(self):
        '''验证评论帖子功能'''
        # Mylogin(self.driver).login()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/iconTabItem").click()
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").send_keys("textCESHI")
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
        time.sleep(6)
        sendContent = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expandTextView")
        sendContentRawList = []
        for i in range(0, len(sendContent)):
            sendContentRawList.append(sendContent[i].text)
        sendContentList = "".join(sendContentRawList)
        self.assertIn("textCESHI", sendContentList)

    def testshouye01_04(self):
        '''验证首页搜索控件是否正常跳转'''
        time.sleep(8)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        time.sleep(6)
        search_01 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input")
        self.assertTrue(search_01.is_displayed())

    def testshouye01_05(self):
        '''验证帖子顶帖功能是否正常'''
        time.sleep(8)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ivUpArrow").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ivUpArrow").click()
        time.sleep(3)
        iv_up=self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_func_click")
        self.assertEqual(iv_up.text,"取消顶")
        self.assertTrue(iv_up.is_displayed())

    def testshouye01_06(self):
        '''验证帖子取消顶帖功能是否正常'''
        time.sleep(8)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ivUpArrow").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ivUpArrow").click()
        time.sleep(3)
        iv_up=self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_func_click")
        iv_up.click()
        time.sleep(3)
        toast_loc = ("xpath", './/*[contains(@text,"取消成功")]')
        el = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
        print(el.text)
        self.assertEqual(el.text,"取消成功")
        # self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ivUpArrow").click()
        # time.sleep(3)
        # self.assertFalse(iv_up.is_displayed())

    def testshouye01_07(self):
        '''验证首页底部导航栏文案显示是否正常'''
        time.sleep(8)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(6)
        homeText = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/textTabItem")
        self.assertEqual(homeText[0].text,"最右")
        self.assertEqual(homeText[1].text, "动态")
        self.assertEqual(homeText[2].text, "消息")
        self.assertEqual(homeText[3].text, "我的")

    def testshouye01_08(self):
        '''验证我的空间动态是否正常展示'''
        time.sleep(8)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/my_space").click()
        time.sleep(3)
        my_zone=self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btn_zone")
        self.assertEqual(my_zone.text,"空间")
        self.assertTrue(my_zone.is_displayed())

    def testshouye01_09(self):
        '''验证退出当前账号功能是否正常'''
        # Mylogin(self.driver).login()
        time.sleep(8)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/setting").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvLogout").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/bt_positive").click()
        time.sleep(6)
        log_in=self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_notLogin_goLogin")
        self.assertEqual(log_in.text,"立即登录/注册")
        self.assertTrue(log_in.is_displayed())

    def testshouye01_10(self):
        '''验证添加关注功能是否正常'''
        Mylogin(self.driver).login()
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view").click()
        time.sleep(6)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/layout_subscribe_unselected").click()
        time.sleep(3)
        select_name=self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_subscribe_name_selected")
        self.assertEqual(select_name.text,"已关注")

    def testshouye01_11(self):
        '''验证取消关注功能是否正常'''
        time.sleep(8)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_subscribe_name_unselected").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_subscribe_name_selected").click()
        time.sleep(3)
        unselect=self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_subscribe_name_unselected")
        self.assertEqual(unselect.text,"关注")

    def testshouye01_12(self):
        '''验证点击帖子头像是否正常跳转到账号主页'''
        time.sleep(8)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/avatar_view_avatar").click()
        time.sleep(6)
        aa=self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btn_profile")
        bb=self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btn_zone")
        self.assertEqual(aa.text,"主页")
        self.assertEqual(bb.text, "空间")













if __name__ == "__main__":
    unittest.main()