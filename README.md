# AI Job Assistant v1

## Summary

AI Job Assistant v1 is a beginner-friendly Python tool that analyzes a job description and identifies common AI/software skills.

## Problem

Freshers often struggle to understand what skills a job description is asking for. This tool helps break the job description into visible skill matches and skill gaps.

## Features

- Accepts a job description as input
- Detects common AI/software skills
- Shows skills found in the job description
- Shows skills that may need improvement
- Suggests a next learning action

## Tech Stack

- Python
- GitHub
- Markdown

## Project Structure

```txt
ai-job-assistant-v1/
├── README.md
├── main.py
├── requirements.txt
└── notes.md
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/lovesemaar/ai-job-assistant-v1.git
```

Run the project:

```bash
python main.py
```

Or:

```bash
py main.py
```

## Example Input

```txt
We are looking for a fresher who knows Python, SQL, GitHub, APIs, AI tools, Docker, and FastAPI. Knowledge of RAG and LLMs is a plus.
```

## Example Output

```txt
Skills found in job description:
- Python
- SQL
- FastAPI
- AI
- LLM
- RAG
- Docker
- GitHub
- API

Skills you may need to improve:
- Prompt Engineering

Suggested next step:
Build one small project that proves 2-3 of the missing skills.
```

## What I Learned

- How to create a simple Python project
- How to compare user input with a list of skills
- How to organize code for a beginner project
- How to document a project for GitHub
- How to create the first version of a portfolio project

## Future Improvements

- Add OpenAI, Claude, or Gemini API
- Generate a custom learning roadmap
- Generate resume bullet suggestions
- Add a frontend interface
- Save results to a file
- Deploy as a web app

## Interview Explanation

I built this project to help freshers understand AI job descriptions. The first version uses keyword matching to identify required skills. It is simple, but it creates a foundation that can later be upgraded with LLM APIs, resume suggestions, and personalized learning plans.