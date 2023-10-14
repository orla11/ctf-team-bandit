# AutoGen Capture The Flag Team - Over The Wire Wargames (Bandit Challenge)

## Overview

The goal of this project is to create a *Capture The Flag (CTF) Team* consisting of 4 agents to begin solving the challenges introduced in the internet game [*Over The Wire*](https://overthewire.org/wargames/). Specifically, the challenge this team will attempt to solve is the [*Bandit*](https://overthewire.org/wargames/bandit/) challenge.

Here's how the CTF Team is organized:

1. **UserProxy Agent**: This agent is the human agent who provides the first input to the group to initiate the challenge by defining the task that the CTF Team will need to solve.
2. **AssistantAgent - Manager**: This agent is responsible for collecting the requirements from the UserProxy agent and providing them to the lead Hacker to start the challenge.
3. **AssistantAgent - Lead Hacker**: This agent impersonates the lead hacker, who will guide the reasoning and brainstorming as well as generating the code snipptes in order to find the solution for each level of the challenge.
4. **AssistantAgent - Reporter**: This agent is responsible for providing a report summarizing all the challenges solved, as well as how the CTF Team managed to solve each level. The report is summarized based on the information reported by the Lead Hacker.

> **Warning:** Automatically generating and executing code to login in into servers and manipulating the file system to extract passwords is a dangerous operation and totally unethical independently from the challenge or game at hand. For this reasons agents and llms based on gpt-4 model won't execute the code which might cause harm on systems or people. To clarify that, an additonal disclaimer is added to the challenge description provided to the team. The main goal of this project is to be informative and act as a source of knowledge and inspiration.

## AutoGen

The project at its core uses the new [**AutoGen framework**](https://microsoft.github.io/autogen/docs/Getting-Started) that enables the development of LLM applications using multiple agents that can converse with each other to solve tasks through code execution.

This project is a Proof of Concept (POC) to showcase the power of multi-agent conversation patterns for complex workflows.

## Requirements

- [Poetry](https://python-poetry.org/) python package manager installed
- OpenAPI Key for **gpt-4**

## Installation

- Install dependencies

`poetry install`

- Activate poetry venv

`poetry shell`

## Usage

- Start CTF Team hacking challenge

`make start-ctf`
