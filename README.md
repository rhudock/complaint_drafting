# Complaint Drafting Expert System

A PocketFlow-based Python LLM expert system for drafting legal complaints with structured workflows and AI-powered analysis.

## Overview

This expert system leverages PocketFlow and Large Language Models to guide users through the process of drafting legal complaints. It provides a structured workflow that:

1. **Gathers and organizes facts** from user input
2. **Identifies potential legal claims** and causes of action
3. **Drafts a formal complaint** following legal conventions
4. **Reviews and refines** the draft for quality and completeness

## Features

- 🤖 **AI-Powered Analysis**: Uses LLMs to analyze case facts and identify legal claims
- 📝 **Structured Workflow**: PocketFlow-based multi-step process ensures comprehensive coverage
- ⚖️ **Legal Formatting**: Generates complaints with proper legal structure and conventions
- 🔄 **Iterative Refinement**: Includes review and refinement step for quality assurance
- 💻 **Interactive & Programmatic**: Use via command line or integrate into your applications

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (or compatible LLM service)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/rhudock/complaint_drafting.git
cd complaint_drafting
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API key:
```bash
# Option 1: Environment variable
export OPENAI_API_KEY='your-api-key-here'

# Option 2: Create a .env file
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

## Usage

### Interactive Mode

Run the expert system in interactive mode:

```bash
python complaint_drafter.py
```

You'll be prompted to enter information about your case, including:
- Parties involved (plaintiff and defendant)
- Date and location of the incident
- Description of what happened
- Harm or damages suffered
- Relevant laws or regulations

The system will then process your information through the workflow and generate a complete complaint draft.

### Programmatic Usage

Use the expert system in your own Python code:

```python
from complaint_drafter import ComplaintDraftingExpertSystem

# Initialize the system
system = ComplaintDraftingExpertSystem()

# Prepare case information
case_info = """
Plaintiff: Jane Doe
Defendant: XYZ Company
Date: March 1, 2025
Location: New York, NY

[Detailed description of the case...]
"""

# Draft the complaint
results = system.draft_complaint(case_info)

# Access the results
print(results['facts_summary'])
print(results['legal_claims'])
print(results['draft_complaint'])
print(results['final_complaint'])
```

### Example Script

Run the included example script to see demonstrations:

```bash
python example.py
```

## Project Structure

```
complaint_drafting/
├── complaint_drafter.py    # Main expert system implementation
├── example.py              # Example usage demonstrations
├── requirements.txt        # Python dependencies
├── pyproject.toml         # Project configuration
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## How It Works

The expert system uses PocketFlow to create a structured workflow with four main steps:

### Step 1: Gather Facts
Extracts and organizes key information from user input including parties, dates, events, and damages.

### Step 2: Identify Claims
Analyzes the facts to identify potential legal claims, their legal basis, required elements, and how the facts support each element.

### Step 3: Draft Complaint
Generates a formal legal complaint with:
- Caption (court, parties, case number)
- Introduction
- Parties description
- Jurisdiction and venue
- Factual allegations
- Causes of action (separate counts)
- Prayer for relief
- Signature block

### Step 4: Review and Refine
Reviews the draft for strengths, weaknesses, and improvements, then produces a refined final version.

## Dependencies

- **pocketflow**: Workflow framework for LLM applications
- **openai**: OpenAI API client for LLM access
- **python-dotenv**: Environment variable management

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black .
```

## Limitations and Disclaimers

⚠️ **Important**: This system is for educational and drafting assistance purposes only. It does not provide legal advice. Always consult with a qualified attorney before filing any legal documents.

- Generated complaints should be reviewed and modified by legal professionals
- The system may not be aware of recent changes in laws or jurisdiction-specific requirements
- AI-generated content should be verified for accuracy and completeness

## License

This project is provided as-is for educational purposes.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Support

For questions or issues, please open an issue on GitHub.
