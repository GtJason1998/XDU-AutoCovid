# 自动化晨午检脚本

## 注意
- 默认填报地址为**西电北校区**

- **该填报脚本对填报系统的学号密码没有任何的记录行为**

## 依赖
1. python3环境
2. requests包,本机使用requests == 2.25.0

## 使用方法
进入相应目录下，执行命令
```bash
python DailyCheck.py username password
```
其中`username`为系统登录学号，`password`为登录密码，比如学号为`20021210899`，密码为`amdYes!!!`，则执行命令
```bash
python DailyCheck.py 20021210899 amdYes!!!
```
若密码中含有空格，比如密码为`amd Yes!!!`，请将密码用双引号概括起来，执行命令
```bash
python DailyCheck.py 20021210899 "amd Yes!!!"
```
可将该脚本挂到系统定时任务中，实现自动填报
