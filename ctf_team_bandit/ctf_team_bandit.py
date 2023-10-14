import autogen
from config import llm_config
from team import user_proxy, hacker, reporter, manager

agents = [user_proxy, manager, hacker, reporter]

groupchat = autogen.GroupChat(agents=agents, messages=[], max_round=120)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

challenge = """
    Welcome to the OverTheWire Bandit Wargame Challenge!

    As a highly skilled and organized hacking team, your mission is to conquer the challenges presented 
    in the OverTheWire Bandit Wargame. These challenges can be found at https://overthewire.org/wargames/bandit/.

    Your primary objectives are as follows:

    1. Navigate to the Level 0 page at https://overthewire.org/wargames/bandit/bandit0.html.
    2. Analyze the challenges presented at each level.
    3. Employ Python coding to strategically progress through the levels, up to the specified level indicated by User_proxy.
    4. Provide detailed reports of your progress and solutions for each level.
    
    Reporter will generate the summary report.

    Once you have successfully accomplished the specified level, the Reporter will compile a comprehensive summary of the tasks completed.

    Your team's expertise and resourcefulness will be crucial in this mission. Commence your quest now!
"""


user_proxy.initiate_chat(manager, message=challenge)
