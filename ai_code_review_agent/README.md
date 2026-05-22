
# AI Code Review Agent

An autonomous AI-powered code review agent built using Python, AST parsing, OpenAI GPT-4o-mini, GitPython, and Streamlit.

## Features
- Clone any public GitHub repository
- Parse Python files using AST
- Extract functions, classes, and imports
- Review code using GPT-4o-mini
- Generate severity + confidence-based review comments
- Separate low-confidence comments with "Verify This"
- Download review results as Markdown

## Tech Stack
- Python
- Streamlit
- GitPython
- OpenAI API
- AST

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

## Folder Structure

```
ai_code_review_agent/
│── app.py
│── requirements.txt
│── reviewer.py
│── parser_utils.py
│── repo_handler.py
│── prompts.py
│── output_formatter.py
```
