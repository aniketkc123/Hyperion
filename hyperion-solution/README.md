# Hyperion: [Year] — Solution Template

**Project:** Hyperion — Astronomy Case Study Challenge (IIT Kanpur)  
**Author:** Aniket Kumar Choudhary  
**Description:** Reproducible solution template for Hyperion-style 48-hour astronomy case studies. Replace `data/` with the problem dataset and tailor the modeling steps in `src/modeling.py` to the specific problem statement.

## Repository structure
See the repo layout in the top-level README.

## How to use
1. Create a virtual environment: `python -m venv venv && source venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Place the dataset(s) in `data/` and update `data/README.md` with source and preprocessing notes.
4. Run exploratory analysis: open `notebooks/analysis.ipynb` and run cells top-to-bottom.
5. To run scripts:
   - `python -m src.analysis` (performs full analysis pipeline: load, preprocess, fit models, generate plots)

## Files of interest
- `src/data_loader.py` — functions to load and standardize datasets.
- `src/analysis.py` — pipeline orchestration, visualization.
- `src/modeling.py` — astrophysical model fitting (MLE / curve fit / detection).
- `notebooks/analysis.ipynb` — narrative notebook for results and figures.
- `results/` — generated plots and tables.

## Notes / Credits
- This repo is a generic template; adapt the modeling strategy to the problem statement.
- Cite any external datasets or libraries used in the final report.
