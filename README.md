# AstroDataAnalysis

Repository for introductory astronomy data analysis: Jupyter notebooks, exercises, and supporting materials.

These materials are based on the online textbook [Coding Essentials for Astronomers](https://tingyuansen.github.io/coding_essential_for_astronomers/index.html) by Prof. Yuan-Sen Ting of The Ohio State University. 

```
Ting, Y.-S. (2025). Coding Essentials for Astronomers. The Ohio State University. 
DOI: 10.5281/zenodo.17850426
```

## Structure

- **[Exercises/](Exercises/)** — Jupyter notebooks, image assets, and local environment file (`.env`). Run notebooks from this directory so paths to data and images resolve correctly. See the [Exercises README](Exercises/README.md) for a list of class notebooks.
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

These materials are made available for education purposes. Many of the code examples are from [Coding Essentials for Astronomers](https://tingyuansen.github.io/coding_essential_for_astronomers/index.html). Please refer to that textbook for further license information.
