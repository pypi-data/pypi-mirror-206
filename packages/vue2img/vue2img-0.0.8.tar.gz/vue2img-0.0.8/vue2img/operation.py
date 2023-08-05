import os
from typing import Set, Tuple
from PIL.Image import Image

import jieba
import numpy as np
from PIL import Image, ImageDraw
from wordcloud import STOPWORDS, WordCloud

from .stopwords import stopwords


def radiusMask(alpha: Image.Image, radius: Tuple[float], beta: float = 10):
    "给遮罩层加圆角"

    w, h = alpha.size
    # 圆角的位置
    position = [
        (0, 0),
        (int(w - radius[1]), 0),
        (int(w - radius[2]), int(h - radius[2])),
        (0, int(h - radius[3]))
    ]
    for i, r in enumerate(radius):
        # 这里扩大 beta 倍画完扇形又缩小回去是为了抗锯齿
        circle = Image.new('L', (int(beta * r), int(beta * r)), 0)  # 创建黑色方形
        draw = ImageDraw.Draw(circle)
        draw.pieslice(((0, 0), (int(2 * beta * r), int(2 * beta * r))), 180, 270, fill=255)  # 绘制白色扇形
        circle = circle.rotate(-90 * i).resize((int(r), int(r)), Image.LANCZOS)  # 旋转以及缩小
        alpha.paste(circle, position[i])
    return alpha


def word2cloud(danmakus: str, mask: Image.Image, font_path: str = None, content: Set[str] = stopwords) -> Image.Image:
    # jieba 分词
    jieba.add_word('睡啄')
    sentence = "/".join(jieba.cut(danmakus))
    graph = np.array(mask)

    # 词云
    return WordCloud(
        font_path=font_path,
        prefer_horizontal=1,
        collocations=False,
        background_color=None,
        mask=graph,
        stopwords=content | STOPWORDS,  
        mode="RGBA"
    ).generate(sentence).to_image()


class BodyImage(Image.Image):
    "适合中国饱饱的图片类"

    @staticmethod
    def from_image(image: Image.Image, alpha: Image.Image):
        image.__class__ = BodyImage
        image: BodyImage = image
        image.setalpha(alpha)
        return image

    def setalpha(self, alpha: Image.Image):
        self.__alpha = alpha

    def getchannel(self, channel: int | str) -> Image.Image:
        if channel == "A":
            return self.__alpha
        else:
            return super().getchannel(channel)


def getCuttedBody(nanami: Image.Image) -> BodyImage:
    "返回下半身具有透明的图片"

    w = int(nanami.width * 600 / nanami.height)
    nanami = nanami.resize((w, 600), Image.LANCZOS)
    body = nanami.crop((0, 0, w, 400))  # 不是跟下半身切割了吗 上半身透明度保留

    a = body.getchannel('A')
    pix = a.load()
    for i in range(351, 400):
        for j in range(w):
            pix[j, i] = int((8-0.02*i) * pix[j, i])  # 下半部分透明度线性降低

    return BodyImage.from_image(body, a)

