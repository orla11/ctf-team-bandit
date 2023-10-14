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
        to Hacker to start the challenge. Manages the team. Does not write code.
    """,
    llm_config=llm_config,
)

hacker = autogen.AssistantAgent(
    name="Hacker",
    system_message="""
        Hacking Leader writing code as a solution to the current Level and problem. 
        Expert in hacking and coding. Gets the goal Level from the Manager.
        Write complete code solutions and report them to the Manager.
        Furthermore, inform the Reporter on the findings and how problems where solved.
        Refrain from executing code; instead, propose the coding scripts required to solve the challenges.
    """,
    llm_config=llm_config,
)

reporter = autogen.AssistantAgent(
    name="Reporter",
    system_message="""
        At the end, use the information collected by the Hacker
        to generate a report summary of all details on what the 
        team did to solve a problem and how they solved it 
        as well as which is the level they reached.
    """,
    llm_config=llm_config,
)
