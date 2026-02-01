# LLM Data Validator

This project implements an LLM-based data validation engine using `groq` and `promptfoo` for evaluation. It strictly validates user profiles against a set of real-world standards (ISO-2 country codes, E.164 phone numbers, etc.).

## Setup Instructions

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd DeepStack_Assigment_submission
    ```

2.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\Activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    npm install
    ```

4.  **Configure Environment**:
    Copy `.env.example` to `.env` and add your Groq API key:
    ```bash
    cp .env.example .env
    ```
    Edit `.env`:
    ```
    GROQ_API_KEY=your_actual_api_key
    ```

## How to Run the Script

To validate a single user JSON file:

```bash
python validate_user.py test_input/input_1.json
```

**Example Output:**
```json
{
  "is_valid": false,
  "errors": ["Name is required..."],
  "warnings": []
}
```

## How to Run Evals

We use `promptfoo` to evaluate the model's accuracy against a suite of test cases.

**Command:**
```bash
npx promptfoo@latest eval
```

**View Results:**
```bash
npx promptfoo view
```

### Test Coverage
The evaluation suite covers:
*   Schema Correctness (Valid JSON structure)
*   No Hallucination (Strict field checking)
*   Classification Accuracy (Valid vs Invalid inputs)
*   Edge Cases (SQL Injection, Null values, mixed valid/invalid fields)
