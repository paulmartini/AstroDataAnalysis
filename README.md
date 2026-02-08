# AstroDataAnalysis

Repository for introductory astronomy data analysis: Jupyter notebooks, exercises, and supporting materials.

## Structure

- **Exercises/** — Jupyter notebooks, image assets, and local environment file (`.env`). Run notebooks from this directory so paths to data and images resolve correctly.
- **Root** — Project-level config: `README.md`, `requirements.txt`, `.gitignore`.

## Setup

1. Clone the repository (or download and extract).
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. For notebooks that use an API key (e.g., LiteLLM), add a `.env` file in **Exercises/** with the required variables (e.g. `ASTRO1221_API_KEY=...`). Do not commit `.env`; it is listed in `.gitignore`.

## Running the notebooks

From the repo root:

```bash
jupyter notebook Exercises/
```

Or open `Exercises/` in JupyterLab / VS Code and run the notebooks there.

## License

See course or institutional guidelines.
