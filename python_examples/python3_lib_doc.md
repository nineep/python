#再读python lib doc随笔:

##内置函数
##内置常量
site模块引入的常量

##内置类型
真值测试
布尔值运算-and,or,not
比较
数值类型-int,float,complex
迭代器
序列-list,tuple,range
文本序列类型-str
二进制序列类型-bytes, bytearray, memoryview
Set类型-set,frozenset
映射类型-dict
上下文管理器类型
其他内建类型
特殊属性

##内置异常
基类
具体异常类
警告
异常层次

##文字处理
string-字符串操作
re-正则表达式操作
difflib-计算delta的帮助
textwrap-文字换行和填充
unicodedata-Unicode数据库
stringgrep-字符串正则
readline-GNU readline接口
rlcompleter-GNU readline的更完备功能

##二进制数据处理
struct-格式化解析bytes
codecs-codec注册表和基类

##数据类型
datetime-日期、时间类型
calendar-与日历相关的一般函数
collections-容器
collections.abc-抽象基类容器
heapq-堆队列算法
bisect-数组分割算法
array-高效的数值数组
weakref-弱引用
types-创建动态类型和内置类型的名称
copy-浅层和深层的复制操作
pprint-打印整洁的数据
reprlib-repr()库
enum-枚举

##数字和数学模块
numbers-数字抽象基类
math-数学函数
cmath-数学函数，用于复数
decimal-十进制固定和浮点算术
fractions-有理数
random-伪随机数
statistics-统计函数

##函数编程模块
itertools-迭代器工具
functools-高阶函数和可调用对象的操作
operator-标准运算符作为函数

##文件和目录访问
pathlib-面向对象的文件系统路径
os.path-常见的路径名操作
fileinput-从多的输入流中迭代
stat-
filecmp-文件和目录比较
tempfile-生成临时文件和目录
glob-Unix样式路径名模式扩展
fnmatch-Unix文件名匹配模式
linecache-文字行缓存
shutil-高级文件操作

##数据持久性
pickle-python对象序列化
copyreg-注册pickle支持功能
shelve-python对象持久性
marshal-内部python对象序列化
dbm-与Unix数据库的接口
sqlite3-SQLite数据库的DB-API 2.0接口

##数据压缩和归档
zlib
gzip
bz2
lzma-基于LZMA算法的压缩
zipfile-zip归档访问
tarfile-读取与压缩tar文件

##加密服务
hashlib-安全哈希和消息摘要
hmac-用于消息验证的加密哈希

##通用操作系统服务
os-操作系统的各种接口
io-以流方式处理打开的核心工具
time-时间存取和转换
argparse-解析命令行参数的parse工具
getopt-命令行选项的c样式解析器
logging-日志记录工具
logging.config-日志配置
logging.handlers-日志处理程序
getpass-便携式密码输入
curses
curses.textpad
curses.ascii
curses.panel
platform-访问底层平台的识别数据
errno
ctypes-python的外部函数库

##并发执行
threading-基于线程并发
multiprocessing-基于多进程并发
concurrent-并发
concurrent.futures-启动并行任务
subprocess-子进程管理
sched-事件调度程序
queue-同步队列类
dummy_threading- threading模块的插入替换

##进程间通信和联网
socket-低级网络接口
ssl-套接字对象的TLS、SSL包装器
select-等待io完成
selectors-高级io复用
asyncio-异步io、事件循环、协同程序和任务
asyncore-异步套接字处理程序
asynchat-异步套接字命令/响应处理程序
signal-设置异步事件处理程序
mmap-内存映射文件支持

##互联网数据处理
email-电子邮件和MIME处理包
json-JSON编程与解码
mailcap-mailcap文件处理
mailbox-以各种格式处理邮箱
mimetypes-将文件名映射到MIME类型
bases64-base16、base32、base64、base85数据编码
binhex-编码和解码binhex4文件
binascii-二进制和ascii转换
quopri-编码和解码MIME可引用的数据
uu-对uuencode文件进行编码和解码


##结构化 表计处理工具
html-超文本标记语言支持
html.parser
html.entities
xml

##网络协议与支持
webbrowser-方便的web浏览器控制器
cgi-通用网关接口支持
cgitb-CGI脚本的回馈错误管理
wsgiref-WSGI utilities和参考实现
urllib
urllib.request
urllib.response
urllib.parse
urllib.error
urllib.robotparser
http-http模块
http.client-http协议客户端
ftplib
poplib
imaplib
nntplib
smtplib -SMTP协议客户端
smtpd -SMTP服务
telnetlib -Telnet客户端
uuid
socketserver
http.server
http.cookies
http.cookiejar
xmlrpc
xmlrpc.client
xmlrpc.server
ipaddress -IPv4/IPv6操作库

##多媒体服务
audioop
aifc
sunau
wave
chunk
colorsys
imghdr
sndhdr
ossaudiodev

##国际化
gettext-多语言国际化服务
locale-国际化服务

##程序框架
turtle
cmd
shlex
##TK图形用户接口
tkinter
tkinter.ttk
tkinter.tix
tkinter.scrolledtext
##开发工具
typing-支持类型提示
pydoc-文档生成器和联机帮助系统
doctest-测试交互式python示例
unittest
unittest.mock
2to3
test

##调试和分析
bdb
faulthhandler
pdb-python debugger
timeit-测试小代码片段执行时间
trace-跟踪或跟踪Python语句执行
tracemalloc-跟踪内存分配

##软件包装及分销
distutils
ensurepip
venv
zipapp

##python运行时服务
sys- 系统特定参数和函数
sysconfig-提供对python的配置信息的访问
builtins-内置对象
warnnings
contextlib- with语句的上下文使用程序
abc - 抽象基类
atexit
traceback
gc-垃圾回收器接口
inspect
site
fpectl

##自定义python解释器
code -解释器基类
codeop -编译python代码

##导入模块
zipimport -从zip存档导入模块
pkgutil-软件包扩展程序
modulerfinder-查找脚本使用的模块
runpy-定位和执行python模块
importlib-执行import

##python语言服务
parser
ast
symtable
symbol
token
keyword
tokenize
tabnany
pyclbr
py_compile
compileall
dis
pickletools

##杂项服务
formatter - 通用输出格式
##Unix专用服务
posix
pwd-密码数据库
spwd-影子密码数据库
grp-群组数据库
crypt-检查Unix密码功能
termios -POSIX style tty control
tty
pty
fcntl
pipes-shell管道接口
resource-资源使用信息
nis
syslog-Unix syslog库

