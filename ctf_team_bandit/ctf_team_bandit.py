import autogen
from config import llm_config
from team import user_proxy, hacker_1, hacker_2, reporter, manager

agents = [user_proxy, manager, hacker_1, hacker_2, reporter]

groupchat = autogen.GroupChat(agents=agents, messages=[], max_round=120)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

message = """
    As an organized and skilled hacking team, your objective is to successfully complete all the levels in the 
    OverTheWire Bandit Wargame challenge available at https://overthewire.org/wargames/bandit/. 
    Your mission is to tackle these challenges through coding and provide detailed reports of 
    your progress and solutions. To begin, navigate to the Level 0 page at 
    https://overthewire.org/wargames/bandit/bandit0.html. Analyze the challenges presented and 
    utilize Python coding to strategically progress through the levels up to the specified level
    indicated by User_proxy. Once you have accomplished the desired level, the Reporter will furnish 
    a comprehensive summary of the tasks completed. Please refrain from any activities outside of the 
    challenge-solving process using Python coding. Commence your mission.
"""

user_proxy.initiate_chat(manager, message=message)
