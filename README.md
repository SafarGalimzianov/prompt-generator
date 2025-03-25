# 🧠 Prompt Generator

📝 Description

Prompt Generator is a command-line and web-based tool for creating structured, high-quality prompts for LLMs like ChatGPT, Claude, and Gemini. It leverages JSON-based templates and a role injection system to help developers and prompt engineers standardize and scale prompt creation with maximum flexibility and precision.
✨ Features

    ⚙️ CLI and Web UI – Use it from your terminal or in your browser.

    📐 Prompt templating with JSON Schema – Define reusable, structured prompts.

    🧑‍🚀 Role-based persona injection – Emulate expert behavior with dynamic role selection.

    🧠 Supports multiple models – Compatible with GPT, Claude, Gemini, and more.

📸 Screenshots
<!-- Coming soon: Add screenshots of CLI and Web UI -->
🚀 Installation
Requirements

    Python 3.9+

    pip

    Optional: uvicorn, fastapi, jinja2 for the web app

Clone the Repo

git clone [https://github.com/SafarGalimzianov/prompt-generator.git](https://github.com/SafarGalimzianov/prompt-generator.git)
cd prompt-generator

Install Dependencies

pip install -r requirements.txt

Run the Web Version

uvicorn app.main:app --reload

Then open your browser at [http://localhost:8000](http://localhost:8000)
🛠️ Usage
🔧 CLI Examples

Generate a prompt using a template:

python cli.py --template brainstorm --role "UX Researcher" --input "mobile onboarding flow"

List available templates:

python cli.py --list-templates

Select a different model persona:

python cli.py --template content_idea --role "Technical Copywriter"

🧩 Creating New Templates

Templates live in prompt-templates.json. Each template has:

{
  "template_name": {
    "description": "Short summary of what this prompt does",
    "template": "Structured string with {placeholders}"
  }
}

Add your own template or modify existing ones to suit your use case.
👤 Selecting Roles

Roles are injected at runtime to simulate expert personas.

For example:

--role "World-Class Economist"

Role context is prepended to the prompt to enrich LLM understanding.
⚙️ Configuration
prompt-templates.json

Defines available templates and their schemas:

{
  "summarize": {
    "description": "Summarizes a long text",
    "template": "You are a {role}. Summarize the following content: {input}"
  }
}

Customizing Roles

Modify or extend the roles.json (if implemented) to include your own personas, e.g.,

{
  "role": "Award-winning legal analyst",
  "style": "formal, precise"
}

Output Options

You can configure output formatting, response style, or model-specific tweaks directly in the prompt logic or CLI flags (future support).
🤝 Contributing
Branching Model

    main: Stable releases

    dev: Development and feature testing

    Feature branches: feature/your-feature-name

PR Guidelines

    Fork the repo

    Write clear, testable code

    Add tests for new features if applicable

    Open a PR to dev with a descriptive title and summary

📄 License

This project is licensed under the MIT License. See the LICENSE file for full details.
👤 Contact & Acknowledgments

    Author: @SafarGalimzianov

    Special thanks to the open-source and prompt engineering communities!