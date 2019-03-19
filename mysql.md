## mysql绿色版的安装：
解压后得到文件夹：mysql-5.7.25-winx64
1.创建文件： ‘my.ini’
```shell
[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8 
[mysqld]
#设置3306端口
port = 3306 
# 设置mysql的安装目录
basedir=D:\mysql-5.7.25-winx64
# 设置mysql数据库的数据的存放目录
datadir=D:\mysql-5.7.25-winx64\data
# 允许最大连接数
max_connections=200
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
```
2.安装
```shell
net stop mysql ##停止mysql服务
cd **/mysql-5.7.25-winx64  #到达根目录
mysqld remove #移除mysql
mysqld install  #安装mysql
#生成无密码账户
mysqld --initialize-insecure  --explicit_defaults_for_timestamp
net start mysql    #启动mysql

cmd到bin目录下执行mysql -uroot （无需密码） ，

给用户设置一个密码：mysqladmin -u root -p password  ，设置密码时发现报错：Access denied for user 'root'@'localhost' (using password: YES)

是因为未给localhost root用户授权，这里新建一个用户，然后授权给他
create user 'test'@'localhost' identified by '你的密码';
grant all privileges on *.* to test@'localhost';
运行这两句sql语句，再次用test的身份输入密码进入

在命令行输入：mysql -utest -p 回车 ， 再输入刚刚设置的密码即可进入。

如果要退出sql环境回到正常的cmd环境，输入exit回车即可。 再次进入mysql 执行第3条即可。
```
