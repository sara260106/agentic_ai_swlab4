# Assignment 4: Multi-Step Agent (Planning)

## Objective
To build an AI agent capable of solving multi-step problems.

## Description
This agent breaks tasks into steps and executes them sequentially.

## Example
Input:
Find average of 5, 10, 15 and summarize

Steps:
1. Extract numbers
2. Calculate average
3. Summarize result

## Architecture
Input → Planning → Step Execution → Output

## Components
- planner.py → Generates steps
- tools.py → Performs actions
- agent.py → Controls execution

## Learning Outcomes
- Task decomposition
- Sequential reasoning
- Planning-based AI systems
