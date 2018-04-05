# Mzitu_Spider

[![license](https://img.shields.io/github/license/ZYSzys/Mzitu_Spider.svg)](https://github.com/ZYSzys/Mzitu_Spider/blob/master/LICENSE)

对http://www.mzitu.com 进行爬取，下载首页美女图片

## 依赖环境
python2.7, 3.6
### python库
http请求：requests  
图片提取：bs4  
存储相关: os  


## 下载安装
在终端输入如下命令：
```bash
git clone https://github.com/ZYSzys/Mzitu_Spider.git
```

## 使用方法
在当前目录下输入：
```bash
cd Mzitu_Spider
pip install -r requirements.txt
python mz.py
```
运行爬虫，如图所示  
![](/screenshots/1.png)  

稍等几分钟后，当前目录下生成Mzitu文件夹，首页每套图以存储在其中  
![](/screenshots/2.png)  

