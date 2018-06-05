# -*- coding: utf-8 -*-
# 块移动

import pyglet
import random
from pyglet.window import key
import copy

# 定义全局变量
# 1. 窗口
WIN_WIDTH = 530
WIN_HEIGHT = 720
# 2. 棋盘起始位置
STARTX = 15
STARTY = 110
# 3. 每行的块数（默认正方形块）
WINDOW_BLOCK_NUM = 4
# 4. 【实际棋盘总宽度】和【每块的宽度】
BOARD_WIDTH = (WIN_WIDTH - 2 * STARTX)
BLOCK_WIDTH = BOARD_WIDTH / WINDOW_BLOCK_NUM  # 整个棋盘宽度除以块数
# 5. 标签（文字）、背景颜色的设定
LABEL_COLOR = (119, 110, 101, 255)
BG_COLOR = (250, 248, 239, 255)
# 6. 网线颜色
LINE_COLOR = (165, 165, 165, 225)
# 7. 方块颜色
COLORS = {
    0: (204, 192, 179),
    2: (238, 228, 128),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (233, 170, 7),
    512: (215, 159, 14),
    1024: (222, 186, 30),
    2048: (222, 212, 30),
}


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 绑定按键（注意要先导入key）
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)

        self.game_init()

    def game_init(self):
        # pyglet.graphics.Batch相当于一个样本集，我们把想放的文字放入
        self.main_batch = pyglet.graphics.Batch()
        # 重要：维护棋盘每个格子的数据是什么。之前用0填空的形式如下：
        # self.data = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.data = [[2 ** (i + j + 1) for i in range(WINDOW_BLOCK_NUM)] for j in range(WINDOW_BLOCK_NUM)]

        # 背景Sprite
        # 注：这里的SolidColorImagePattern表示纯色背景
        background_img = pyglet.image.SolidColorImagePattern(color=BG_COLOR)
        # pyglet.sprite.Sprite要传入图片，图片起始x，图片起始y三个参数
        self.background = pyglet.sprite.Sprite(background_img.create_image(WIN_WIDTH, WIN_HEIGHT), 0, 0)

        # 以下都是在界面上显示的文字
        # Title
        self.title_label = pyglet.text.Label(text="贰零肆捌", bold=True, color=LABEL_COLOR, x=STARTX,
                                             y=BOARD_WIDTH + STARTY + 30, font_size=18, batch=self.main_batch)

        # Score
        self.score = 0
        self.score_label = pyglet.text.Label(text="Score = %d" % (self.score), bold=True, color=LABEL_COLOR, x=200,
                                             y=BOARD_WIDTH + STARTY + 30, font_size=36, batch=self.main_batch)

        # Help
        self.help_label = pyglet.text.Label(text="Please use up, down, -> and <- to play!", bold=True,
                                            color=LABEL_COLOR, x=STARTX, y=STARTY - 30, font_size=18,
                                            batch=self.main_batch)

    # 刷新、绘图用函数
    def on_draw(self):
        self.clear()
        self.score_label.text = "Score = %d" % (self.score)
        self.background.draw()
        self.main_batch.draw()

        # 绘制块
        for row in range(WINDOW_BLOCK_NUM):
            for col in range(WINDOW_BLOCK_NUM):
                x = STARTX + BLOCK_WIDTH * col
                y = STARTY + BOARD_WIDTH - BLOCK_WIDTH - BLOCK_WIDTH * row
                # 具体绘制方法在下方定义
                self.draw_title((x, y, BLOCK_WIDTH, BLOCK_WIDTH), self.data[row][col])

        # 绘制网格线
        self.draw_grid(STARTX, STARTY)

    def draw_grid(self, startx, starty):
        # 横竖均是4条网格线
        rows = columns = WINDOW_BLOCK_NUM + 1

        # 水平线
        for i in range(rows):
            # 注：下面的2（size）表示有几个顶点，pyglet.gl.GL_LINES（mode）表示绘制的是线，随后传入的是坐标值（x1, y1, x2, y2），最后是颜色
            # 注2：v2f表示坐标由浮点数表示（v2i表示整数）
            # 注3：c4B表示用4个0~255之间的数表示颜色（RGBa），*2表示两个顶点分别由什么颜色表示。如果不同，则中间为渐变色。
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', (
                startx,
                i * BLOCK_WIDTH + starty,
                WINDOW_BLOCK_NUM * BLOCK_WIDTH + startx,
                i * BLOCK_WIDTH + starty)),
                                 ('c4B', (LINE_COLOR * 2)))

        #  垂直线
        for j in range(columns):
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', (
                j * BLOCK_WIDTH + startx,
                starty,
                j * BLOCK_WIDTH + startx,
                WINDOW_BLOCK_NUM * BLOCK_WIDTH + starty)),
                                 ('c4B', (LINE_COLOR * 2)))

    def draw_title(self, xywh, data):
        x, y, dx, dy = xywh
        color_rgb = COLORS[data]
        # 各个方块四顶点坐标
        corners = [x + dx, y + dy, x, y + dy, x, y, x + dx, y]
        # GL_QUADS表示填充颜色的方块
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', corners), ('c3B', color_rgb * 4))

        if data != 0:
            a = pyglet.text.Label(text=str(data), bold=True, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255),
                                  x=x + dx / 2, y=y + dy / 2, font_size=28)

            a.draw()

    def on_key_press(self, symbol, modifiers):
        """让窗口识别按键"""
        eq_title = False
        score = 0

        # 注意在之前初始化时要绑定按键key
        if symbol == key.UP:
            print("up press")
            # 在某位置生成2，这里固定是左上角
            self.data[0][0] = 2
        elif symbol == key.DOWN:
            print("down press")
            self.data[WINDOW_BLOCK_NUM-1][WINDOW_BLOCK_NUM-1] = 2
        elif symbol == key.LEFT:
            print("left press")
            self.data[WINDOW_BLOCK_NUM-1][0] = 2
        elif symbol == key.RIGHT:
            print("right press")
            self.data[0][WINDOW_BLOCK_NUM-1] = 2
        elif symbol == key.ESCAPE:
            self.close()


# 创建窗口
win = Window(WIN_WIDTH, WIN_HEIGHT)

# 设置图标
icon = pyglet.image.load('icon.ico')
win.set_icon(icon)

pyglet.app.run()
