# Assignment 1: Rule-Based AI Agent

## Objective
To understand the concept of an AI agent using rule-based logic.

## Description
This program simulates a simple AI agent that:
- Takes user input
- Detects intent using keyword matching
- Performs actions accordingly

## Architecture
The agent follows a pipeline:
Input → Decision → Action

### Components

1. Input Handler
   - Takes user input from terminal

2. Decision Logic
   - Identifies intent using keywords like:
     - "hello" → Greeting
     - "date" → Date request
     - "calculate" → Math operation

3. Action Execution
   - Executes task based on detected intent

## Features
- Greeting response
- Current date retrieval
- Basic arithmetic calculation
- Handles unknown inputs

## Learning Outcomes
- Understanding of agent architecture
- Rule-based reasoning
- Modular programming approach
