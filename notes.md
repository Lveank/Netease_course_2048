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