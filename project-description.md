# Project Description

## Objective

As AI consultants to Global Bike Inc. (GBI), the objective is to design and implement a Python-based generative AI solution that enables self-service analytics through an agent capable of generating SQL from natural language. The implementation should use Python as the primary language. All components must be included in a GitHub repository.

## The Challenge

GBI has a lot of data in their Microsoft SQL Server, but accessing it requires technical skills. Business users want to ask questions in plain English and get immediate answers.

## The Solution

Build an AI agent that turns text questions from GBI into safe, correct SQL, executes the query on GBI’s Microsoft SQL Server, and automatically produces both a suitable visualization and a plain-language explanation. The user interface displays the generated SQL, a data table, the visualization, and the explanation.

The end-to-end interaction can follow, as an example, the following path:

1.  **User Input**: A user poses a question by text.
2.  **Text-to-SQL**: The text question is converted by a schema-aware text-to-SQL model into a read-only, parameterized SQL statement.
3.  **Execution**: The statement is executed against the SQL Server with timeouts, row limits, and guardrails in place.
4.  **Analysis**: The resulting dataset is routed to:
    *   A **visualization component** that selects an appropriate chart based on the data shape.
    *   An **explanation component** that generates a faithful narrative grounded in the returned numbers.
5.  **Presentation**: The interface then presents the generated SQL, a paginated data table, the selected visualization, and an explanatory summary.

*Note: This flow is provided to illustrate the intended user experience; you may refine it as needed while preserving the core capability of safe text-to-SQL, execution, visualization, and explanation.*

## Deliverables

Deliverables include a GitHub repository containing:

*   All code (agents, guardrails, database connector, and UI).
*   Configuration and prompt templates.
*   Reproducible setup instructions using **uv** python package manager.
*   A lightweight test suite that exercises benchmark questions and safety checks.
*   A short explanation (one page) describing the architecture, prompts, safety measures, and evaluation procedure.

## Expected Business Impact

A single natural-language interface that:

*   Reduces analyst bottlenecks.
*   Shortens time-to-insight for sales.
*   Standardizes how data is queried, visualized, and explained across GBI.

## Technologies

*   **Python**: The primary programming language.
*   **Google Gemini**: For the intelligence (LLM).
*   **Gradio**: To build the user interface.
*   **Microsoft SQL Server**: The database.
*   **VS Code**: The primary IDE.
*   **GitHub**: To store and share your code.
*   **uv**: For Python package management.

## Getting Started

To be ready for our first session, please complete the steps in the [Prepare Your Machine](preparation.qmd) section *before* class. This includes installing Python and setting up your development environment.

We look forward to building the future of analytics with you!
