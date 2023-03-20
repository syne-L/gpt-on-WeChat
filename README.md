# gpt-on-WeChat
This is a slight project developed on Python to connect the chat software 'WeChat' with the semantic proccessing model 'GPT' of OpenAI API, by which we can receive and  reply message automatically on WeChat.

## Preparing to start
1. You need a Python3.9 environment with follow packages:

  'openai'    - to access some facilities of semantic proccessing model 'GPT'.
  
  'pywin32'   - the package 'wxauto' needs it.
  
  'wxauto'    - to manipulate the WeChat software on Windows PC.

2. You need an API key of OpenAI API to obtain a permittion for accessing the functions of the Python package 'openai', which can be proposed at:

  https://platform.openai.com/account/api-keys

## Introduction

In this project are two modules intergrate the functions of the packages mentioned above and provides a easier way to access, one Main program to realize the fundamental facilities, and three demonstrations as the example of these modules.

Information of each module are shown in follow:

### AissistantController.py

A basic module developed on Python package 'openai' to establish a conversation agent and store the dialogs structurially.
The demonstration 'Demo1_GptAiAssistController.py' tells how to use it.

### WechatController.py

Previously, the Python package 'wxauto' provides the functions to send or read the messages on WeChat software. 
The demonstration 'Demo2_wxauto.py' tells how to use it.

Moreover, based on it, we have tried to intergrate the functions and develope a module 'WechatController.py' which adapt for connecting with GPT conveniently.

### Main1_GptOnWeChat.py

Based on the modules that 'AissistantController.py' and 'WechatController.py', this is the main program of this project that realizes chatting on WeChat automatically.
You can enjoy it after setting your agent's name, your chat partner's name, and your WeChat nickname on this program.

In addition, head and tail of each message are able to assigned such as:

    [AI AUTO REPLY] Hello! This is a test message sent automatically by AI assistent '-Syne-' [END]

!NOTE:  
   *  Please run your WeChat software on your PC firstly before start this.
   *  When this program is running, do not switch the chat partner manually, which may lead a wrong message sending.
   *  When this program is running on the PC, you can use your cell phone to get a word in edgewise, but the AI assistant may ignore this message.

### Demo1_GptAiAssistController.py

This demonstration gives an example of using the Python module <AiAssistantController> to build a simple conversation 
model, which contains two fundamental classes 'AI_ASSISTANT' and 'DIALOG_LINE'.

As a container, the class 'DIALOG_LINE' stores the data of one-way-dialog that contains who said this sentence and what 
the content is, which provides the functions to access the speaker's name, the content, and to origin a string for 
output (see the details in 'DemoIntroduction' and the comments).

'AI_ASSISTANT' is a class with an abstract concept, whose instance can be regarded as a chat agent when instantiated 
through assigning the names of the user, the developer, and the agent itself. The names would be used to establish the 
background stories of the agent, which helps the agent to talk about some topics like 'who are you?',  
or 'who created you?' and so on. The class 'AI_ASSISTANT' provides the functions to update and access the information
of the agent (see the details in 'DemoIntroduction' and the comments).


### Demo2_wxauto.py

This demonstration gives an example of how to control the WeChat software on a PC Windows system for some 
simple use. The programs are based on the Python package <wxauto>, and provide some functions for reading and 
sending messages.

!NOTE:  
   *  Please install the package <pywin32> firstly, on which the package <wxauto> is based.
   *  Before running, set {Enter} to send a message in WeChat software, rather than {Ctrl + Enter}.

### Demo3_WechatController.py

This demonstration gives an example of using the Python module <WechatController> to control the WeChat software to 
send and read messages. (see the details in the program and the comments) 
  
## Declarations
  
The level of developers is limited. If there are omissions, criticism and discussion are welcome.
This project is only for learning. Developers will not be responsible for any losses caused by applications that exceed the scope of learning.
  
