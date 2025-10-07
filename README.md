# Demo Project


This repository contains several Python modules and packages for various agents and utilities.

## File Structure

```
demo/
│   requirements.txt              # Python dependencies
│   README.md                     # Project documentation
│   .gitignore                    # Git ignore rules
│
├── database_session/             # Database session management
│   ├── __init__.py
│   ├── agent.py                  # Database agent logic
│   └── habit_data.db             # SQLite database file
│
├── Session/                      # Session management
│   ├── __init__.py
│   └── agent.py
│
├── structured_output/            # Structured output handling
│   ├── __init__.py
│   └── agent.py
│
├── tarvel_planner_agent/         # Travel planner agent and instructions
│   ├── __init__.py
│   ├── agent.py
│   └── instructions.py
│
├── test/                         # Test utilities and agent logic
│   ├── __init__.py
│   └── agent.py
│
└── tools_agent/                  # Tools agent logic
    ├── __init__.py
    └── agent.py
```


## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd demo
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   # Activate the environment:
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## How to Run Agents Locally

You can run any agent module directly from the command line. For example:

```bash
# Run the database session agent
python database_session/agent.py

# Run the session agent
python Session/agent.py

# Run the structured output agent
python structured_output/agent.py

# Run the travel planner agent
python tarvel_planner_agent/agent.py

# Run the tools agent
python tools_agent/agent.py

# Run tests
python test/agent.py
```

> **Note:** Each agent/module may have its own entry point or usage instructions. Refer to the code or add more details as needed.

