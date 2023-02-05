import itertools
import wx
import numpy as np
import sys

print(sys.version)
print(wx.VERSION)


color_base = '#FFFFFF' #白
pixelSize = 10
text_base_Eng = ' All these places have their moments. '
text_base_Jpn = ' 日々鍛錬し、いつ来るともわからぬ機会に備えよ。 '
Jpn = False
if Jpn:
    text_base = text_base_Jpn
else:
    text_base = text_base_Eng

family = [
    wx.FONTFAMILY_DEFAULT,
    wx.FONTFAMILY_DECORATIVE,
    wx.FONTFAMILY_ROMAN,
    wx.FONTFAMILY_SCRIPT,
    wx.FONTFAMILY_SWISS,
    # wx.FONTFAMILY_MODERN, #なかった
    wx.FONTFAMILY_TELETYPE,
    # wx.FONTFAMILY_MAX #なかった
    ]
fam_num = np.arange(len(family))

style = [
    wx.FONTSTYLE_NORMAL,
    wx.FONTSTYLE_ITALIC,
    wx.FONTSTYLE_SLANT,
    wx.FONTSTYLE_MAX]
sty_num = np.arange(len(style))

weight = [
    wx.FONTWEIGHT_EXTRALIGHT,
    wx.FONTWEIGHT_LIGHT,
    wx.FONTWEIGHT_NORMAL,
    wx.FONTWEIGHT_MEDIUM,
    wx.FONTWEIGHT_SEMIBOLD,
    wx.FONTWEIGHT_BOLD,
    wx.FONTWEIGHT_EXTRABOLD,
    wx.FONTWEIGHT_HEAVY,
    wx.FONTWEIGHT_EXTRAHEAVY,
    wx.FONTWEIGHT_MAX]

weight = [
    # wx.FONTWEIGHT_EXTRALIGHT, #normalと変わらなかった。
    wx.FONTWEIGHT_NORMAL,
    wx.FONTWEIGHT_BOLD,]
wei_num = np.arange(len(weight))

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, 'wxPython', (500, 200))
        self.SetBackgroundColour(color_base)
        sizer = wx.WrapSizer(orient=wx.HORIZONTAL, flags=wx.WRAPSIZER_DEFAULT_FLAGS)

        for fam, sty, wei in itertools.product(fam_num, sty_num, wei_num):
            text = wx.StaticText(self, id=-1, label=F'   F{fam+1} S{sty+1} W{wei+1} : {text_base}')
            font = wx.Font(pixelSize, family[fam], style[sty], weight[wei], underline=False,faceName="", encoding=wx.FONTENCODING_DEFAULT) # wx.FONTENCODING_CP932
            text.SetFont(font)
            sizer.Add(text, 1, wx.TOP |wx.DOWN, 3)  #wx.EXPAND |
        self.SetSizer(sizer) 

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.SetTopWindow(frame) 
    app.MainLoop()