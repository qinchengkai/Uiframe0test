# coding=utf-8
from selenium import webdriver
from public.login import Mylogin
import unittest
import os
import time
from selenium.webdriver.common.action_chains import ActionChains

class TestShouye(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://101.133.169.100/yuns/index.php")
        self.driver.maximize_window()
        time.sleep(5)
        print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        filedir = "D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    def testShouye01_01(self):
        '''测试首页导航文案显示是否正常'''
        Mylogin(self.driver).login()
        firstPageNavi = self.driver.find_element_by_xpath("//div[@class='top']/span")
        loginText = self.driver.find_element_by_css_selector("div.login>a:nth-child(1)")
        regisText = self.driver.find_element_by_css_selector("div.login>a:nth-child(3)")

        self.assertEqual("亲，欢迎您来到云商系统商城！",firstPageNavi.text)#顺序可以换
        self.assertEqual("182****0897", loginText.text)
        self.assertEqual("退出", regisText.text)
        #self.assertNotEqual("dd", regisText.text)#断言不相等

        #self.assertIn("云商系统商城",firstPageNavi.text)#断言包含
        #self.asserNotIn("云商系统")

        #self.assertTrue(self.driver.find_element_by_xpath("//div[@class='top']/span").is_displayed())#判断控件是否加载出来
        #self.assertFalse(firstPageNavi.is_displayed())

        # if loginText.text == "182****8888":#如果不用assert断言，可以用if条件语句判断，一般都用assert断言，断言和if判断二选一
        #     print("文案显示正常")
        # else:
        #     print("文案显示异常")
        #     self.driver.find_element_by_xpath("王麻子")



    def testShouye01_02(self):
        '''验证搜索内容无时，提示语是否正常'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[1]").send_keys("王麻子")
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[2]").click()
        time.sleep(2)
        searchText = self.driver.find_element_by_xpath("//div[@class='nomsg']")
        print(searchText.text)
        self.assertEqual(searchText.text, "抱歉，没有找到相关的商品")
        if searchText.text == "抱歉，没有找到相关的商品":
            print("文案显示正常")
        else:
            print("文案显示异常")
            self.driver.find_element_by_xpath("王麻子")

    def testShouye01_03(self):
        '''验证输入搜索内容时，搜索结果相符'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[1]").send_keys("女装")
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[2]").click()
        time.sleep(2)
        searchText_1=self.driver.find_element_by_xpath('//div[@class="nm"]/a[1]')
        self.assertIn("女装", searchText_1.text)
        if '女装' in searchText_1.text:
            print("搜索成功")
        else:
            print("搜索失败")
            self.driver.find_element_by_xpath("王麻子")

    def testShouye01_04(self):
        '''验证“会员中心”控件是否正常跳转'''
        Mylogin(self.driver).login()
        memberIndex = self.driver.find_element_by_link_text("会员中心")
        memberIndex.click()
        time.sleep(3)
        loginText=self.driver.find_element_by_xpath("//ul[@class='login']/a[1]")
        logoutText = self.driver.find_element_by_xpath("//ul[@class='login']/a[2]")
        self.assertEqual("182****0897",loginText.text)
        self.assertEqual("退出", logoutText.text)
        if loginText.text == "182****0897":
            print("正常跳转")
        else:
            print("跳转失败")

    def testShouye01_05(self):
        '''验证秒杀控件是否正常跳转'''
        Mylogin(self.driver).login()
        seckill=self.driver.find_element_by_xpath('//div[@class="nav_pub"]/a[2]')
        seckill.click()
        time.sleep(3)
        dd = self.driver.window_handles
        self.driver.switch_to.window(dd[1])
        seckillText=self.driver.find_element_by_xpath("//div[@class='bnma']/a[1]")
        self.assertEqual("限时抢购",seckillText.text)
        if seckillText.text == "限时抢购":
            print("跳转成功")
        else:
            print("跳转失败")

    def testShouye01_06(self):
        '''存在优惠券时，验证‘优惠券’控件是否正常跳转'''
        Mylogin(self.driver).login()
        coupon=self.driver.find_element_by_xpath('//div[@class="nav_pub"]/a[3]')
        coupon.click()
        time.sleep(3)
        dd = self.driver.window_handles
        self.driver.switch_to.window(dd[1])
        couponText=self.driver.find_element_by_xpath('//div[@class="lq"]/a')
        self.assertEqual("立即领取",couponText.text)
        if couponText.text == "立即领取":
            print("跳转成功")
        else:
            print("跳转失败")

    def testShouye01_07(self):
        '''验证商城动态新闻是否正常跳转'''
        Mylogin(self.driver).login()
        target_2=self.driver.find_element_by_xpath('//div[@class="con1"]/a[2]')
        target_2.click()
        time.sleep(3)
        dd = self.driver.window_handles
        self.driver.switch_to.window(dd[1])
        target_3=self.driver.find_element_by_xpath("//div[@class='nm']/h1")
        self.assertIn("阿里脱贫基金",target_3.text)
        if '阿里脱贫' in target_3.text:
            print("正常跳转")
        else:
            print("跳转失败")

    def testShouye01_08(self):
        '''验证‘男装女装’的子分类‘女装’控件是否正常跳转'''
        Mylogin(self.driver).login()
        goods_01=self.driver.find_element_by_xpath('//div[@class="mbig"]/span/a')
        time.sleep(3)
        ActionChains(self.driver).move_to_element(goods_01).perform()
        time.sleep(3)
        goods_01_05=self.driver.find_element_by_xpath('//div[@class="mshow"]/div[5]/div/a')
        goods_01_05.click()
        dh=self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]')
        self.assertIn("女装",dh.text)
        if '女装' in dh.text:
            print("正常跳转")
        else:
            print("跳转失败")
            self.driver.find_element_by_xpath("王麻子")

    def testShouye01_09(self):
        '''验证‘夏天最热’控件是否正常跳转'''
        Mylogin(self.driver).login()
        summerhot=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/a[4]')
        summerhot.click()
        time.sleep(3)
        dd = self.driver.window_handles
        self.driver.switch_to.window(dd[1])
        summerhot_result=self.driver.find_element_by_xpath('//div[@class="nomsg"]')
        self.assertEqual("抱歉，没有找到相关的商品",summerhot_result.text)
        if summerhot_result.text == "抱歉，没有找到相关的商品":
            print("无商品，成功跳转")
        else:
            print("跳转失败")
            self.driver.find_element_by_xpath("王麻子")

    def testShouye01_10(self):
        '''验证‘男装活动’控件是否正常跳转'''
        Mylogin(self.driver).login()
        theme=self.driver.find_element_by_xpath('//div[@class="nav_pub"]/a[5]')
        theme.click()
        time.sleep(3)
        dd = self.driver.window_handles
        self.driver.switch_to.window(dd[1])
        theme_result=self.driver.find_element_by_xpath('//div[@class="nav_bar"]')
        self.assertEqual("抱歉，没有找到相关的商品",theme_result.text)
        if summerhot_result.text == "抱歉，没有找到相关的商品":
            print("无商品，成功跳转")
        else:
            print("跳转失败")
            self.driver.find_element_by_xpath("王麻子")

    def testShouye01_11(self):
        '''验证‘品牌街’控件是否正常跳转'''
        Mylogin(self.driver).login()
        brand=self.driver.find_element_by_xpath('//div[@class="nav_pub"]/a[6]')
        brand.click()
        time.sleep(3)
        dd = self.driver.window_handles
        self.driver.switch_to.window(dd[1])
        brand_result=self.driver.find_element_by_xpath('//div[@class="bname"]/span')
        self.assertEqual("品牌街",brand_result.text)
        if brand_result.text == "品牌街":
            print("品牌街成功跳转")
        else:
            print("跳转失败")
            self.driver.find_element_by_xpath("王麻子")

    def testShouye01_12(self):
        '''验证‘运动健身’的子分类‘户外健身’控件是否正常跳转'''
        Mylogin(self.driver).login()
        goods_08=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[8]/dt/div/span/a')
        time.sleep(3)
        ActionChains(self.driver).move_to_element(goods_08).perform()
        time.sleep(3)
        goods_08_02=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[8]/div/div[2]/div/a')
        goods_08_02.click()
        dh_01=self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]')
        self.assertIn("户外健身",dh_01.text)
        if '户外健身' in dh_01.text:
            print("正常跳转")
        else:
            print("跳转失败")
            self.driver.find_element_by_xpath("王麻子")




if __name__ == "__main__":
    unittest.main()


