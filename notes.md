## 一些零散的说明
- 网站文字编辑器：SimpleMDE Markdown Editor
SimpleMDE is a simple, embeddable, and beautiful JS markdown editor
More: https://www.zhihu.com/question/24368769

- Phpstorm默认开启自动换行（use soft wraps）

## Markdown的增强
1. 在VScode中安装Markdown Preview Enhance。
2. 一些实时预览的配置：https://www.jianshu.com/p/18876655b45222123
    - 配置预览风格：在VScode的配置文件里面增加一行：
        ``` javascript
        "markdown.styles": ["file:///Users/you-name/Documents/vscode-markdown.css"],
        ```
        这表示markdown预览的风格将用我自定义的vscode-markdown.css文件，记得这里需要填写file://协议，因为预览功能是基于浏览器实现的，接下来让我们创建这个css文件。
        ``` css
        @charset "utf-8";
        /** * vscode-markdown.css */
        h1, h2, h3, h4, h5, h6, p, blockquote { margin: 0; padding: 0;}
        body { font-family: "PingFang SC", "Hiragino Sans GB", Helvetica, Arial, sans-serif; padding: 1em; margin: auto; max-width: 42em; color: #737373; background-color: white; margin: 10px 13px 10px 13px;}
        table { margin: 10px 0 15px 0; border-collapse: collapse;}
        td, th { border: 1px solid #ddd; padding: 3px 10px;}
        th { padding: 5px 10px; }
        a { color: #0069d6; }
        a:hover { color: #0050a3; text-decoration: none;}
        a img { border: none; }
        p { margin-bottom: 9px; }
        h1, h2, h3, h4, h5, h6 { color: #404040; line-height: 36px;}
        h1 { margin-bottom: 18px; font-size: 30px; }
        h2 { font-size: 24px; }
        h3 { font-size: 18px; }
        h4 { font-size: 16px; }
        h5 { font-size: 14px; }
        h6 { font-size: 13px; }
        hr { margin: 0 0 19px; border: 0; border-bottom: 1px solid #ccc;}
        blockquote{ color:#666666; margin:0; padding-left: 3em; border-left: 0.5em #EEE solid; font-family: "STKaiti", georgia, serif;}
        code, pre { font-family: Monaco, Andale Mono, Courier New, monospace; font-size: 12px;}
        code { background-color: #ffffe0; border: 1px solid orange; color: rgba(0, 0, 0, 0.75); padding: 1px 3px; -webkit-border-radius: 3px; -moz-border-radius: 3px; border-radius: 3px;}
        pre { display: block; background-color: #f8f8f8;  border: 1px solid #2f6fab; border-radius: 3px; overflow: auto; padding: 14px; white-space: pre-wrap; word-wrap: break-word;}
        pre code { background-color: inherit; border: none;  padding: 0;}
        sup { font-size: 0.83em; vertical-align: super; line-height: 0;}
        * { -webkit-print-color-adjust: exact;}
        @media screen and (min-width: 914px) { 
        body { width: 854px; margin: 10px auto; }
        }
        @media print { 
        body, code, pre code, h1, h2, h3, h4, h5, h6 { color: black; } 
        table, pre { page-break-inside: avoid; }
        }

        作者：混沌边缘的伊卡洛斯
        链接：https://www.jianshu.com/p/18876655b452
        來源：简书
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        ```
3. 更多Markdown说明：http://wowubuntu.com/markdown/index.html
4. Markdown的常用语法：https://www.jianshu.com/p/82e730892d42

## Markdown导出pdf：
1. princexml（收费），但是对中文支持似乎不好，来自Markdown Preview Enhance推荐。官网：https://www.princexml.com/

## git
### 1. git add 命令添加所有改动内容
git add xx命令可以将xx文件添加到暂存区，如果有很多改动可以通过 git add -A .来一次添加所有改变的文件。

注意 -A 选项后面还有一个句点。 git add -A表示添加所有内容， git add . 表示添加新文件和编辑过的文件不包括删除的文件; git add -u 表示添加编辑或者删除的文件，不包括新添加的文件。

### 2. Git 提交时报错warning: LF will be replaced by CRLF in
今天在自己的hexo博客上提交东西时 出现这样一段代码 warning: LF will be replaced by CRLF 虽然只是个warning 也还是可以提交，但是看着实在恶心啊，网上有很多解决办法 我看了下 还是把他们总结在这里吧，免得下次又忘了怎么解决了。

方法一：
配置选项修改 把core.autocrlf 设置成false
``` bash
git config –global core.autocrlf true #这个是转换，也是默认值
git config –global core.autocrlf input #貌似是上库转换，从库中迁出代码不转换
git config –global core.autocrlf false #这个一般是window上的，不转换
```

方法二：
将你源文件中的CRLF转为LF，在window中都是CRLF 而在linux是LF 
这时候会存在一个转换 
上库的时候 通过git add . 手动转换 
下载下来再重新转换 
听说这个很麻烦，我也没搞懂，但是用了第一种方法之后我的问题反正时解决了的。

### 3.Git切换远程仓库地址
方法一：修改命令<br>
``` bash
git remote set-url origin url
```
方法二：先删后加
``` bash
git remote rm origin
git remote add origin git@github.com:sheng/demo.git
```
方法三：修改config文件<br>
.git文件夹 --> config文件 --> 修改git remote origin地址

方法四：通过第三方git客户端修改

### 4.删除git远程库中已存在的文件,并且在本地保留
1. 备份项目
2. git rm --cached xxxx //从版本库中删除xxxx文件，但在工作目录中仍然保留。可以使用
git rm -r --cached directory_name递归删除目录
3. 在.gitignore中添加要忽略的文件
4. 把修改的文件commit并且push到服务端
5. 从git上重新拉取这个项目。

## 参数传递（*args, **kwargs）
- 多个实参，放到一个元组里面,以*开头，可以传多个参数；**是形参中按照关键字传值把多余的传值以字典的方式呈现
- *args：（表示的就是将实参中按照位置传值，多出来的值都给args，且以元祖的方式呈现）
- 位置参数、*args、**kwargs三者的顺序必须是位置参数、*args、**kwargs，不然就会报错
- 以下举例说明
    ``` python
    def foo(x, *args, **kwargs):
        print(x)
        print(args)
        print(kwargs)
        
    >>> foo(1,2,3,4,5,y=2)
    1
    (2, 3, 4, 5)
    {'y': 2}
    ```
- More: https://www.cnblogs.com/xuyuanyuan123/p/6674645.html