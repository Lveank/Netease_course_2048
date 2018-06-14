## Goal
1. 了解面向对象编程（学会创建类、类的实例化）
2. 第三方库：pyglet

## Steps
1. 绘制字和窗口
2. 绘制线和方块
3. 让方块随键盘动起来
4. 随机添加块、判断输赢
5. 悔棋功能

## Pyglet的说明
- pyglet是一个python下的多媒体框架，属于轻量级不，可以轻易的做出交互丰富的应用。同样的框架还有 pygame，panda3d，这两个学起来更难，学习成本更大。
- x、y坐标与pygame相同，均是左上角为(0,0)
- 

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

## 