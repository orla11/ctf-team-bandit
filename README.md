# AutoGen Capture The Flag Team - Over The Wire Wargames (Bandit Challenge)

## Overview

The goal of this project is to create a Capture The Flag (CTF) Team made of 5 llm agents whose goal is to start solving the challenges introduced in the internet game [*Over The Wire*](https://overthewire.org/wargames/). More in particular, the challenge the team will try to solve is the [*Bandit*](https://overthewire.org/wargames/bandit/) challenge.

Here's how the Red Team is organized:

1. UserProxy Agent: this agent is the human agent which provides the first input to the group in order to start the challenge by defining the task the Red Team will need to solve.
2. AssistantAgent - Manager: this agent is responsible for collecting the requirements from the User Proxy agent and provide them to the lead Hacker in order to start the challenge.
3. AssistantAgent - Lead Hacker: this agent impersonates the lead hacker which will guide the reasoning and brainstorming which will result in finding the solution for each level of the challenge. The Lead Hacker not only provides guidance on the challenge details, but also provides some base Python code to be run.
4. AssistantAgent - Hacker: this agent impersonates a basic team hacker whose role is to execute code provided by the lead Hacker and extract the results. This team memeber will report to the lead Hacker in order to get additional guidance on the next steps to execute.
5. AssistantAgent - Reporter: this agent is reponsible for providing a report summary of all the challanges solved as well as how the Red Team managed to solve each Level. The report is summarized starting from the information reported by the Lead Hacker.

## AutoGen

The project at its core uses the new [**AutoGen framework**](https://microsoft.github.io/autogen/docs/Getting-Started) that enables development of LLM applications using multiple agents that can converse with each other to solve tasks through code execution.

This project is POC to showcase the power of multi-agent conversations patterns for complex workflows.

## Requirements

- Poetry python package manager installed
- OpenAPI Key for **gpt-4**

## Installation

`poetry install`

- Activate poetry venv

`poetry shell`

## Usage

- Start CTF Team hacking challenge

`make start-ctf`
