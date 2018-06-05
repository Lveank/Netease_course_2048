# -*- coding: utf-8 -*-
# 绘制窗口部分

import pyglet

# 定义全局变量
WIN_WIDTH = 530
WIN_HEIGHT= 720


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_init()

    def game_init(self):
        pass


# 创建窗口
win = Window(WIN_WIDTH, WIN_HEIGHT)

# 设置图标
icon = pyglet.image.load('icon.ico')
win.set_icon(icon)

pyglet.app.run()
