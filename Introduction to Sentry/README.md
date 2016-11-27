## 介绍

Sentry 是一个错误日志收集，聚合以及告警平台。

2010 年由 Disqus 公司开源。源码地址: https://github.com/getsentry

## 特性

* 错误告警功能 （**在错误发生的第一时间就知晓，而不是等待客户主动告知我们**）
* 告警合并功能（**一段时间内相同告警只通知一次，免于被告警信息淹没**）
* 可以查看错误发生位置的详细堆栈信息（**更利于查找问题**）
* 可以查看错误发生位置的前后代码片段（**不需要翻代码就可以知道前后代码**）
* 可以查看发生错误时上下文的局部变量的值（**便于快速复现/查找问题**）
* 支持多种编程语言: JavaScript, Node, Python, PHP, Ruby, Go, Objective-C, Swift, C#, Java, Perl, 
Elixir, ... （**支持目前公司所用技术栈**）
* ...

## 文档

https://docs.sentry.io/

## 栗子 🌰

```python
$ pip install raven
$ export SENTRY_DSN='xxx'
$ cat demo.py

def setup_raven(dsn):
    from raven import Client
    from raven.conf import setup_logging
    from raven.handlers.logging import SentryHandler
    client = Client(dsn)
    handler = SentryHandler(client)
    setup_logging(handler)


def foo(m, n):
    h = m / n - 10
    return m / h

if __name__ == '__main__':
    import logging
    import os
    dsn = os.environ['SENTRY_DSN']
    logging.basicConfig()
    setup_raven(dsn)
    m, n = 10, 1
    try:
        foo(m, n)
    except Exception as e:
        logging.exception(e)
```

```
$ python demo.py
ERROR:root:integer division or modulo by zero
Traceback (most recent call last):
  File "demo.py", line 22, in <module>
    foo(m, n)
  File "demo.py", line 12, in foo
    return m / h
ZeroDivisionError: integer division or modulo by zero
Sentry is attempting to send 1 pending error messages
Waiting up to 10 seconds
Press Ctrl-C to quit
```

上面输出中的 

```
ERROR:root:integer division or modulo by zero
Traceback (most recent call last):
  File "demo.py", line 22, in <module>
    foo(m, n)
  File "demo.py", line 12, in foo
    return m / h
ZeroDivisionError: integer division or modulo by zero
```
是默认的 logging 记录的错误日志。

下面看一下 Sentry 中记录的错误日志：
<img width="801" alt="demo 1" src="https://cloud.githubusercontent.com/assets/18389003/20585342/7237d718-b235-11e6-95ae-2ae5fa75f1cc.png">
<img width="776" alt="demo 2" src="https://cloud.githubusercontent.com/assets/18389003/20585346/7a4c97d6-b235-11e6-8f8c-1de638f031f1.png">

## 部署

* 不使用 docker: https://docs.sentry.io/server/installation/python/
* 使用 docker: https://docs.sentry.io/server/installation/docker/

## FAQ

Q: 带web portal么?
A: 带 web portal。

