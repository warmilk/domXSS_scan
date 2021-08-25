## 第一步：安装chrome ##

linux用户请先保证自己的chrome是安装在默认路径/usr/bin/google-chrome（可以在命令行终端直接输入/usr/bin/google-chrome看是否能打开chrome作为测试），window用户也同理，chrome应该安装在默认安装路径，否则会很麻烦，可能会导致第二步需要的chrome webdrive无法唤醒chrome

## 第二步：安装chrome webdriver ##
### 方法一（图形界面操作） ###
查阅自己的Chrome版本号，之后去 https://sites.google.com/a/chromium.org/chromedriver/downloads 手动下载对应版本号的webDrive，然后解压安装到项目根目录


### 方法二（命令行操作） ###

1. 在项目根目录下，下载对应版本的chrome webdrive，我的是92版本，链接如下:

 wget https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_linux64.zip

2. 直接解压到项目根目录：
 
 unzip chromedriver_linux64.zip 
 
 
3. 给予chrome driver可读写执行权限：
 
 chmod 777 chromedriver
 
 ### 第三步：pip安装项目需要的依赖 ###
 
 新建venv之后，用venv里面的pip安装requirement.txt的依赖，就可以运行main.py了