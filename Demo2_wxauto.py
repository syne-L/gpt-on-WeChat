from wxauto import *

'''
This demonstration gives an example of how to control the WeChat software on a PC Windows system for some 
simple use. The programs are based on the Python package <wxauto>, and provide some functions for reading and 
sending messages.

!NOTE:  
   *  Please install the package <pywin32> firstly, on which the package <wxauto> is based.
   *  Before running, set {Enter} to send a message in WeChat software, rather than {Ctrl + Enter}.
'''


testMsg = "[PROGRAM TEST] hello, this is a test message sent automatically based on the Python package " \
          "<wxauto>.\n[PROGRAM TEST] 您好，这是一条用于程序测试的消息，它基于Python扩展包<wxauto>开发，自动发出。"

def DemoIntroction():
    # 获取当前微信客户端
    wx = WeChat()

    # 获取会话列表
    wx.GetSessionList()

    # to indicate who you want to chat with.
    wx.ChatWith('Lin', RollTimes=None)

    # get the Messages in the present window, and obtain a 2D list as [[name0, content0], [name1, content1], ...]
    msgs = wx.GetAllMessage
    print(f"{msgs[-1][0]}:{msgs[-1][1]}")

    # load more messages in the present window by rolling up the screen.
    wx.LoadMoreMessage()

    # you can store the text or image to the Clipboard.
    WxUtils.SetClipboard(testMsg)

    # and send it to the person indicated by the function wx.SendClipboard()
    wx.SendClipboard()

    # you can also send a message directly by the function wx.ChatWith().
    # If the parameter 'clear' were True, the original words in the dialog box would be deleted.
    # But, this method is not suitable for multi-line word, while the SendClipboard() is recommended
    wx.SendMsg(testMsg, clear=True)

    # search the keywords in the bar, and select the first result.
    wx.Search(keyword='收到')


if __name__ == '__main__':
    # example1: send the message 'testMsg' to '林熠程'
    wx = WeChat()
    wx.GetSessionList()
    wx.Search(keyword='Lin')
    WxUtils.SetClipboard(testMsg)
    wx.SendClipboard()
    pass





