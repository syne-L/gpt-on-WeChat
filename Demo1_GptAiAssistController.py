from AiAssistantController import AI_ASSISTANT  # a class of AI assistant
from AiAssistantController import DIALOG_LINE   # a class as a container to store the data of one-way-dialog

'''
This demonstration gives an example of using the Python module <AiAssistantController> to build a simple conversation 
model, which contains two fundamental classes 'AI_ASSISTANT' and 'DIALOG_LINE'.

As a container, the class 'DIALOG_LINE' stores the data of one-way-dialog that contains who said this sentence and what 
the content is, which provides the functions to access the speaker's name, the content, and to origin a string for 
output:  (see the details in 'DemoIntroduction' and the comments)

DIALOG_LINE.ToString()   # returns a string that contains the basic information of a one-way dialog as <name>:<content>.
DIALOG_LINE.GetLabel()   # returns the <name> part of a dialog.
DIALOG_LINE.GetContent() # returns the <content> part of a dialog.

'AI_ASSISTANT' is a class with an abstract concept, whose instance can be regarded as a chat agent when instantiated 
through assigning the names of the user, the developer, and the agent itself. The names would be used to establish the 
background stories of the agent, which helps the agent to talk about some topics like 'who are you?',  
or 'who created you?' and so on. The class 'AI_ASSISTANT' provides the functions to update and access the information
of the agent, contains: (see the details in 'DemoIntroduction' and the comments)

AI_ASSISTANT.GetDialogLinesNum()   # returns the number of one-way dialogs has occurred.
AI_ASSISTANT.Update()              # input a new dialog to update the conversation data.
AI_ASSISTANT.GetReply()            # returns the most recent reply in the conversation data.
AI_ASSISTANT.GetHistoryDialog()    # is used to access the history dialogs.
'''

def DemoIntroduction():
    # 测试 AI_ASSISTANT
    nameAI = "AI's name"  # AI's name
    nameHu = "User_1"  # user's name
    nameDv = "SyneL"  # developer's name

    # An Instantiation of the class AI_ASSISTANT by an instance AiAssistant_SiRong.
    AiAssistant_SiRong = AI_ASSISTANT(nameAI, nameHu, nameDv)

    numOfRounds = 0
    while True:
        numOfRounds += 1
        print(f"============= Round [{numOfRounds}] =============")

        # Define the content that human is saying by var /a/ determined by keyboard inputting.
        content_a = input(f"{nameHu}:")

        # Define a dialog_line by instantiation of the class DIALOG_LINE, in which DIALOG_LINE(name, content).
        dialogLine_a = DIALOG_LINE(nameHu, content_a)

        # Update the conversation date of AiAssistant_SiRong by using its function Update(dialog_line, need_to_reply).
        # If the parameter need_to_reply were False, the AI would listen to you but not reply.
        need_to_reply = True
        AiAssistant_SiRong.Update(dialogLine_a, need_to_reply)

        # Get the most recently reply by the class DIALOG_LINE.
        if need_to_reply:
            dialogLine_r = AiAssistant_SiRong.GetReply()
        else:
            dialogLine_r = DIALOG_LINE("-", "-")

        # Class DIALOG_LINE is used to store the dialog data contains the speaker's name and the contents,
        # where the self functions have been defined as ToString(), GetLabel(), and GetContent() to output
        # a string, get the speaker's name, and get the content.
        print(dialogLine_r.ToString())
        print("  *  Access the information of a dialog:")
        print(f"  *  *  The one said this sentence is  : [{dialogLine_r.GetLabel()}]")
        print(f"  *  *  The content of this sentence is: [{dialogLine_r.GetContent()}]")

        # You can get the number of the dialog lines of the conversation using the function GetDialogLinesNum().
        NumDiaLs = AiAssistant_SiRong.GetDialogLinesNum()
        print(f"  *  Number of dialog lines: [{NumDiaLs}]")

        # You can also get the history dialog by using the list Dialogs[i] or the function GetHistoryDialog(idt).
        print("  *  Access the history dialog by the list AI_ASSISTANT.Dialogs[i] or the function GetHistoryDialog():")
        for idt in range(NumDiaLs):
            dialogLine_i = AiAssistant_SiRong.Dialogs[idt]  # AiAssistant_SiRong.GetHistoryDialog(idt)
            print(f"  *  *  The sentence[{idt}] was said by [{dialogLine_i.GetLabel()}]. "
                  f"He said: [{dialogLine_i.GetContent()}]")
        print("  *  ...")

        # In addition, the function GetHistoryDialog() with no input parameter will return the most recently dialog.
        dialogLine_n = AiAssistant_SiRong.GetHistoryDialog()
        print(f"  *  *  The last sentence was said by [{dialogLine_n.GetLabel()}]. "
              f"He said: [{dialogLine_n.GetContent()}]")
        print("...")


if __name__ == "__main__":
    DemoIntroduction()
