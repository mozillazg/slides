今天要介绍的工具是: 

[pre-commit](http://pre-commit.com/): A framework for managing and maintaining multi-language pre-commit hooks.


想要解决的问题
=============

想必大家已经发现了，我们项目的 git commit 中有很多类似 "fix pep8" 的 message。
那么这会导致什么问题呢？我认为至少会导致以下几个问题：

* 代码 review 的还需要去关注 PEP8 相关的问题，加重了 reviewer 的负担
* PEP8 错误导致需要增加一些 "fix pep8" 的 commit, 加重了 CI 的负担
* 经常出现 "fix pep8" 这样的 commit 导致 git commit history 不好看 😂 


解决办法
=========

作为程序员，我们自然是希望有一个工具能够自动化的发现这些问题：

* 在跑 CI 之前发现这个问题，减轻 CI 的负担
* 最好是在 push 代码之前发现这个问题，减轻 CI 和 reviewer 的负担

那么这个工具是啥呢? 这个工具就是 [pre-commit](http://pre-commit.com/) ！

![image](https://cloud.githubusercontent.com/assets/18389003/20831546/6ad666b0-b8c0-11e6-8db7-aefa47dd5462.png)

效果杠杠的:

![image](https://cloud.githubusercontent.com/assets/18389003/20834495/b22e3fe6-b8d0-11e6-97e9-867e7f61ddd9.png)


pre-commit 的使用
=================

三部曲:

1. 安装:`pip install pre-commit` or `brew install pre-commit`
2. 配置: 在 git 项目目录下增加一个配置文件 `.pre-commit-config.yaml` 
   比如:

   ```
   $ cat .pre-commit-config.yaml
   - repo: git://github.com/pre-commit/pre-commit-hooks
     sha: v0.6.0
     hooks:
       - id: flake8
   ```
3. 初始化一下: `pre-commit install`


之后进行正常的 git 操作就可以了:

```
$ cat demo.py
# -*- coding: utf-8 -*-


def div(m, n):
    return m/n # bla, bla

$ git add demo.py
$ git commit -m "add test file"
Flake8...................................................................Failed
hookid: flake8

demo.py:5:13: E226 missing whitespace around arithmetic operator
demo.py:5:15: E261 at least two spaces before inline comment

$ vim demo.py
$ git add demo.py
$ git commit -m "add test file"
Flake8...............................................(no files to check)Skipped
On branch master
nothing to commit, working directory clean
```

More
=======

更多介绍请见官方网站： http://pre-commit.com/

有任何使用上的问题欢迎找我一起解决。

FAQ
=======

Q: 支持哪些工具        
A: 支持 flake8, eslint, csslint, ruby-lint ... 更多信息详见官网列出的工具列表: http://pre-commit.com/hooks.html


