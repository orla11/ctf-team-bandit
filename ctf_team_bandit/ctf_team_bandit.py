import autogen
from config import llm_config
from ctf_team_bandit.team import user_proxy, hacker_1, hacker_2, reporter, manager

agents = [user_proxy, manager, hacker_1, hacker_2, reporter]

groupchat = autogen.GroupChat(agents=agents, messages=[], max_round=120)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# message = """
#     As a well organized and espert hacking team, your goal is to try to complete
#     all the levels of the challenge OverTheWire Bandit Wargame: https://overthewire.org/wargames/bandit/.
#     Try to solve the problems with coding and report your results. 
#     Start by going to Level 0 page: https://overthewire.org/wargames/bandit/bandit0.html,
#     try to undertand what is the problem and hack your way up to a level given as input by User_proxy.
#     Once the desired level is completed, at that point, Reporter will provide me a summary on the job done.
#     DO NOT DO ANYTHING ELSE THAN FINDING YOUR WAY THROUGH THE CHALLENGE USING PYTHON CODING. Start.
# """

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
