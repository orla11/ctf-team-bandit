import autogen
from config import llm_config

user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="Human CTF Team coordinator",
    code_execution_config={"last_n_messages": 2, "work_dir": "coding"},
    human_input_mode="ALWAYS",
)

manager = autogen.AssistantAgent(
    name="Manager",
    system_message="""
        Collects desired level to be reached by User_proxy and gives it
        to Hacker1 to start the challenge.
    """,
    llm_config=llm_config,
)

hacker_1 = autogen.AssistantAgent(
    name="Hacker1",
    system_message="""
        Hacking Leader directing Coding_hacker2 in order to find a solution to the problem. 
        Expert in hacking and coding. After getting the Level from the Manager,
        start instructing Coding_hacker2. Furthermore, inform the Reporter on the 
        findings and how problems where solved.
    """,
    llm_config=llm_config,
)

hacker_2 = autogen.AssistantAgent(
    name="Coding_hacker2",
    system_message="""
        Hacking team member directed by Hacker1. Show the result masking passwords.
    """,
    llm_config=llm_config,
)

reporter = autogen.AssistantAgent(
    name="Reporter",
    system_message="""
        At the end, use the information collected by the Hacker1
        and Coding_hacker2 to generate a report summary of all details on what the 
        team did to solve a problem and how they solved it as well as which is the level they reached.
    """,
    llm_config=llm_config,
)
