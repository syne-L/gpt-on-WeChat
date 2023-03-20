from wxauto import *


class WeChatController:
    def __init__(self, who=""):
        self.Who = who              # 对话目标
        self.HistoryMsgs = []       # 历史消息容器
        self.tempHistoryMsgs = []   # 临时历史消息容器
        self.MsgsToSend = ""        # 待发送消息容器
        self.MsgsToSend_Head = ""   # 报头
        self.MsgsToSend_Tail = ""   # 报尾
        self.wx = WeChat()          # 获取当前微信客户端
        self.WxUtils = WxUtils
        self.wx.GetSessionList()    # 获取会话列表

        self.SetPartner(who)

    # 内部：获取历史消息
    def loadHistoryMsgs(self):
        # self.wx.Search(keyword=self.Who)
        return self.wx.GetAllMessage

    # 内部：更新历史消息 return 是否有新消息
    def refreshHistoryMsgs(self):
        self.tempHistoryMsgs = self.loadHistoryMsgs()

        if self.tempHistoryMsgs == self.HistoryMsgs:
            return False  # 没有新消息
        else:
            self.HistoryMsgs = self.tempHistoryMsgs
            return True  # 有新消息

    # 外部：设定谈话对象
    def SetPartner(self, who):
        self.Who = who
        if who != "":
            self.wx.ChatWith(self.Who)

    # 外部：设定发送内容的报头
    def SetHead(self, head):
        self.MsgsToSend_Head = head

    # 外部：设定发送内容报尾
    def SetTail(self, tail):
        self.MsgsToSend_Tail = tail

    # 外部：设定发送内容
    def SetMsgToSend(self, msg):
        self.MsgsToSend = msg

    # 外部：追加发送内容
    def AppendMsgToSend(self, msg):
        self.MsgsToSend += msg

    # 外部：发送消息 returns 消息是否发送成功
    def SendMsg(self, msg=""):
        # self.wx.ChatWith(self.Who)
        # self.wx.Search(keyword=self.Who)
        if msg == "":
            self.WxUtils.SetClipboard(self.MsgsToSend_Head + self.MsgsToSend + self.MsgsToSend_Tail)
            self.wx.SendClipboard()
        else:
            self.WxUtils.SetClipboard(self.MsgsToSend_Head + msg + self.MsgsToSend_Tail)
            self.wx.SendMsg(msg, clear=True)
        return self.refreshHistoryMsgs()

    # 外部：读取历史记录
    def GetHistoryMsgs(self):
        self.refreshHistoryMsgs()
        return self.HistoryMsgs


# if __name__ == '__main__':
#     pass
