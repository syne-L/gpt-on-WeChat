import os
import openai

# openAI key 用于授权
openai.api_key = "your own key"


# 类：AI assistant
class AI_ASSISTANT(object):
    # nameAI = ""   # AI的名字   #"[AI assistant SiRong auto reply]"
    # nameHu = ""   # 用户的名字
    # nameDv = ""  # 开发者名字
    def __init__(self, name_ai, name_hu, name_dv):

        # 背景信息
        self.nameAI = name_ai
        self.nameHu = name_hu
        self.nameDv = name_dv
        # self.Background = f"{self.nameAI}, an AI assistant developed by a human engineer {self.nameDv}, " \
        #                   f"is very clever, outgoing, friendly, and accommodating." \
        #                   f"Here are a group of conversation of a human named {self.nameHu} with {self.nameAI}."

        self.Background = f"{self.nameAI}是一个聪明、外向、友善、乐于助人的AI助手，由工程师{self.nameDv}基于OpenAI API开发。" \
                          f"当{self.nameDv}不在时，{self.nameAI}会出现，帮他应对一些简单的问题。" \
                          f"" \
                          f"以下是一组它和人类朋友{self.nameHu}的对话。"

        # 预先设定初始的第一组对话
        # self.Dialogs = [DIALOG_LINE(self.nameHu, "Hello, Who are you?"),
        #                 DIALOG_LINE(self.nameAI, f"I'm an AI created by {self.nameDv}. What can I do for you?")]
        self.Dialogs = [DIALOG_LINE(self.nameHu, "你好。"),
                        DIALOG_LINE(self.nameAI, f"您好！我是AI助理{self.nameAI}，请问有什么可以帮您的吗？")]
        self.InitialDialogStr = ""
        for i in range(len(self.Dialogs)):
            self.InitialDialogStr += self.Dialogs[i].ToString()

        # 公共容器
        self.NewDialogLine = self.Dialogs[-1]  # self.reflashNewDialog(DIALOG_LINE(" ", " "))  # 新的对话行
        self.DocumentsForGPT = self.initDocument()  # 作为参数直接输入GPT

    # 内部：初始化DocumentsForGPT
    def initDocument(self):
        self.DocumentsForGPT = self.Background + self.InitialDialogStr
        return self.DocumentsForGPT

    # 内部：更新DocumentsForGPT
    def reflashDocument(self):
        self.DocumentsForGPT += self.NewDialogLine.ToString()
        return self.DocumentsForGPT

    # 内部：更新NewDialog
    def reflashNewDialog(self, new_dia):
        self.NewDialogLine = new_dia
        self.Dialogs.append(new_dia)
        return new_dia

    # 内部：获取一个GPT回答
    def get_response(self, prompt, stopStr):
        response = openai.Completion.create(
            model="text-davinci-003",  #"gpt-3.5-turbo",#
            prompt=prompt.encode("utf-8").decode("utf-8"),
            temperature=0.9,
            max_tokens=800,
            # top_p=1,
            # frequency_penalty=0,
            # presence_penalty=0.6,
            stop=[stopStr]  # =["Human:"]
        )
        return response.choices[0].text.strip()

    # 外部：根据输入更新状态
    def Update(self, dialog_line, need_to_reply):
        self.reflashNewDialog(dialog_line)
        self.reflashDocument()
        # print(f"dialog_line.GetLabel()={dialog_line.GetLabel()},  self.nameHu={self.nameHu},  need_to_reply={need_to_reply}")
        if dialog_line.GetLabel() == self.nameHu and need_to_reply:
            print(" * Getting response.....")
            strResponse = self.get_response(self.DocumentsForGPT, self.nameHu+":")  #+self.nameHu+":"
            print(f" * Response returned [{strResponse}]")
            self.reflashNewDialog(DIALOG_LINE(self.nameAI, strResponse.lstrip(self.nameAI+':')))  # [len(self.nameAI)+1:]
            self.reflashDocument()

    # 外部：获取AI最近的一次回答
    def GetReply(self, j=-1):
        if self.Dialogs[j].GetLabel() is self.nameAI:
            return self.Dialogs[j]
        else:
            j = j-1
            return self.GetReply(j)

    # 外部：获取历史对话记录 (默认最近一条）
    def GetHistoryDialog(self, idt=-1):
        if -len(self.Dialogs) <= idt < len(self.Dialogs):
            return self.Dialogs[idt]
        else:
            return self.Dialogs[-1]

    # 外部：获取目前对话条目数量
    def GetDialogLinesNum(self):
        return len(self.Dialogs)

#  类：用于存放单行对话的内容
class DIALOG_LINE(object):
    def __init__(self, label, context):
        self.Label = label
        self.Context = context

    def ToString(self):
        return self.Label + ":" + self.Context + "\n"

    def GetLabel(self):
        return self.Label

    def GetContent(self):
        return self.Context


# if __name__ == "__main__":
    # pass
