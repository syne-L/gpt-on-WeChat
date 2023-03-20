from WechatController import WeChatController

'''
This demonstration gives an example of using the Python module <WechatController> to control the WeChat software to 
send and read messages. (see the details in the program and the comments) 
'''

if __name__ == '__main__':

    partner1 = '林熠程'
    partner2 = '文件传输助手'
    HistoryMsgs = []            # history msgs container
    msgHead = '[PROGRAM TEST]'  # head of msg
    msgTail = '[MESSAGE END]'   # tail of msg

    # Instantiate a WeChatController to chat with the partner1
    WechatCtrlr = WeChatController(partner1)

    # Change the partner to chat from partner1 to partner2
    WechatCtrlr.SetPartner(partner2)

    # You can set the head and tail of every message to send.
    WechatCtrlr.SetHead(msgHead)
    WechatCtrlr.SetTail(msgTail)

    # Set the content of message to be sent.
    # The content will be stored into the MsgsToSend, a member variable of the class WeChatController.
    WechatCtrlr.SetMsgToSend("This is an automatic message to test the Python module <WechatController.py>. ")

    # You can append a new message to the previous one. It will be also stored into the MsgsToSend.
    WechatCtrlr.AppendMsgToSend("--- from one of the developers. ")

    # Send a message whose content is stored in the MsgsToSend.
    WechatCtrlr.SendMsg()

    # You can also input the content as a parameter directly, and the previous  MsgsToSend will be alternated.
    WechatCtrlr.SendMsg("This is another message.")

    # Get history message
    HistoryMsgs = WechatCtrlr.GetHistoryMsgs()
    for item in HistoryMsgs:
        print(f"{item[0]}:{item[1]}")


