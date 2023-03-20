from AiAssistantController import AI_ASSISTANT  # a class of AI assistant
from AiAssistantController import DIALOG_LINE   # a class as a container to store the data of one-way-dialog
from WechatController import WeChatController   # is used to control WeChat
import random
import time

'''

'''

# Parameters of AiAssistantController
nameAI = " -Syne- "  # AI's name
nameHu = "nameHu"  # user's name
nameDv = "SyneL"  # developer's name
AiAssistant_Syne = AI_ASSISTANT(nameAI, nameHu, nameDv)

# Parameters of WechatController
partner = nameHu            # WeChat name the partner
myWeChatName = "myWeChatName"   # WeChat name of mine
HistoryMsgs = []            # history msgs container
msgHead = '[AI] '   # head of msg
msgTail = ' [AUTO REPLY]'   # tail of msg


if __name__ == '__main__':
    WechatCtrlr = WeChatController(partner)
    WechatCtrlr.SetHead(msgHead)
    WechatCtrlr.SetTail(msgTail)

    while True:

        # 读取历史记录
        HistoryMsgs = WechatCtrlr.GetHistoryMsgs()

        # 是否是新消息
        IsNewMsg = False
        MsgNo_last = ""
        MsgNo_new = HistoryMsgs[-1][2]
        if MsgNo_new == MsgNo_last:
            IsNewMsg = False
        else:
            IsNewMsg = True
            MsgNo_last = MsgNo_new

        # 解析最新一条历史记录，判断是否是正常的对话
        if HistoryMsgs[-1][0] != "Time" \
                and HistoryMsgs[-1][0] != myWeChatName \
                and '[图片]' not in HistoryMsgs[-1][1]:
            dialogLine_a = DIALOG_LINE(HistoryMsgs[-1][0], HistoryMsgs[-1][1])

            # 是否新消息
            if IsNewMsg and HistoryMsgs[-1][0] != myWeChatName:
                need_to_reply = random.random() < 0.3  # percent of True
                print(f" * New message[{MsgNo_new}] received!   {dialogLine_a.ToString()}")
                print(f" * Parameter <need_to_reply> is <{need_to_reply}>.")
                AiAssistant_Syne.Update(dialogLine_a, need_to_reply)

                # 回复
                if need_to_reply:
                    dialogLine_r = AiAssistant_Syne.GetReply()
                    WechatCtrlr.SetMsgToSend(dialogLine_r.GetContent())
                    WechatCtrlr.SendMsg()
                    print(f" * Message[{MsgNo_new}] has been replied!  {dialogLine_r.ToString()}")

        time.sleep(2)
    pass
