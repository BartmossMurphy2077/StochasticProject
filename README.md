# Stochastic Models with Applications

University group project on Monte Carlo simulation, stochastic processes, and financial applications.

The repository holds shared Python code, Jupyter notebooks, and a place for figures and tables. Mathematical models and experiments are added notebook by notebook. This setup only prepares the working environment.

## Project Overview

The project studies a small set of stochastic processes and then uses those processes to price financial options. Work is split between numerical simulation, comparison with known theoretical results, and interpretation of the estimates.

Two themes run through the notebooks:

- Simulate a process and check that the numerical results match the theory.
- Use the simulated paths to estimate option prices, including cases where a closed-form benchmark exists.

## Project Objectives

The notebooks are reserved for these topics:

1. Poisson process simulation and numerical validation.
2. Brownian motion simulation and numerical validation.
3. Geometric Brownian motion.
4. European call option pricing with Monte Carlo, compared with the Black–Scholes price.
5. Continuously monitored up-and-out barrier options.
6. Discretely monitored up-and-out barrier options.
7. Jump-diffusion models.
8. An optional snowball option case study.

## Project Structure

```text
.
├── notebooks/          Experiments, explanations, and plots
├── src/stochastic_models/   Reusable Python functions imported by the notebooks
├── results/figures/    Saved figures
├── results/tables/     Saved tables
├── docs/               Extra written notes, if the team adds them later
├── .venv/              Local virtual environment (not shared)
├── requirements.txt    Python dependencies
├── pyproject.toml      Makes the src package importable after an editable install
└── README.md
```

| Path | Role |
|---|---|
| `notebooks/01_poisson_process.ipynb` | Task 1. Poisson process simulation and checks. |
| `notebooks/02_brownian_motion.ipynb` | Task 2. Brownian motion simulation and checks. |
| `notebooks/03_geometric_brownian_motion.ipynb` | Task 3. Geometric Brownian motion. |
| `notebooks/04_european_call.ipynb` | Task 4. European call, Monte Carlo and Black–Scholes. |
| `notebooks/05_barrier_options.ipynb` | Tasks 5 and 6. Continuous and discrete up-and-out barriers. |
| `notebooks/06_jump_diffusion.ipynb` | Task 7. Jump-diffusion models. |
| `notebooks/07_snowball_options.ipynb` | Task 8 (optional). Snowball option case study. |
| `src/stochastic_models/` | Shared implementations so notebooks do not copy the same code. |
| `results/` | Output produced by notebooks. Figures and tables are kept separate. |

Each notebook is a starter template: a title, the task it belongs to, a short description, and the section headings the analysis should follow. The algorithms themselves are not written yet.

## Prerequisites

Install these before working on the project:

- **Python 3.12** (3.11 is also suitable). Check with `python --version`.
- **Git**, for sharing changes in the existing repository.
- **JupyterLab**, installed into the virtual environment from `requirements.txt`. You do not need a separate global install.

On Windows, if `python` is not 3.11 or 3.12, create the environment with `py -3.12` as shown below.

## Installation

Run these commands from this project directory.

### 1. Open the project directory

**Windows PowerShell**

```powershell
cd C:\Users\hugok\OneDrive\Dokumenty\GitHub\StochasticProject
```

**Windows Command Prompt**

```cmd
cd C:\Users\hugok\OneDrive\Dokumenty\GitHub\StochasticProject
```

**macOS/Linux**

```bash
cd /path/to/StochasticProject
```

Use the path where this project actually lives on that machine.

### 2. Create the virtual environment

Skip this step if `.venv` already exists.

**Windows PowerShell or Command Prompt**

```powershell
py -3.12 -m venv .venv
```

If Python 3.12 is already the `python` command:

```powershell
python -m venv .venv
```

**macOS/Linux**

```bash
python3 -m venv .venv
```

### 3. Activate it

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

If execution policy blocks the script, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then activate again.

**Windows Command Prompt**

```cmd
.venv\Scripts\activate.bat
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

With the environment activated:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e . --no-deps
```

The last command registers `stochastic_models` so notebooks and scripts can import it from the project root. Dependencies stay listed in `requirements.txt`.

Register a Jupyter kernel that points at this environment:

```bash
python -m ipykernel install --user --name stochastic-models --display-name "Python (Stochastic Models)"
```

### 5. Start JupyterLab

With the environment still activated:

```bash
jupyter lab
```

Activation puts this project's JupyterLab on `PATH`. If Anaconda or another Python is also installed, starting JupyterLab from an unactivated shell can open that other installation instead of `.venv`.

## Running the Notebooks

In JupyterLab, select the kernel **Python (Stochastic Models)** if it is not already selected. Run cells from top to bottom.

Recommended order:

1. `01_poisson_process.ipynb`
2. `02_brownian_motion.ipynb`
3. `03_geometric_brownian_motion.ipynb`
4. `04_european_call.ipynb`
5. `05_barrier_options.ipynb`
6. `06_jump_diffusion.ipynb`
7. `07_snowball_options.ipynb` (optional case study)

Later notebooks assume the earlier processes are understood. Barrier and European pricing both rely on geometric Brownian motion. The jump-diffusion notebook should be in place before any experiment that adds jumps to a price path.

Suggested section order inside every notebook:

1. Introduction and objectives
2. Mathematical background
3. Simulation methodology
4. Implementation
5. Numerical experiments
6. Visualisations
7. Comparison with theoretical results
8. Interpretation and conclusions

Keep explanations and experiments in the notebooks. Put functions that more than one notebook needs in `src/stochastic_models/`.

Import the shared package from a notebook or script after the editable install:

```python
from stochastic_models import poisson
```

## Reproducibility

Monte Carlo estimates change when the random draws change. Fix the random seed for any result the team wants to compare or hand in, and record that seed next to the experiment.

Use NumPy’s generator API:

```python
import numpy as np

rng = np.random.default_rng(seed)
```

Pass `rng` into simulation functions. Do not rely on the global random state (`numpy.random.seed` together with `numpy.random.rand` and similar). A generator makes each experiment independent and keeps later draws from silently changing earlier results.

Save figures under `results/figures/` and tables under `results/tables/` with relative paths from the project root.

## Team Collaboration

Reusable mathematics lives in `src/stochastic_models/`. Each module has a single job: Poisson paths, Brownian paths, geometric Brownian motion, jump-diffusion, option payoffs, and small shared helpers. If two notebooks need the same calculation, add it once in the package and import it.

Use the existing folders as follows:

- Edit the notebook that matches the task you are working on.
- Add or change shared functions in the matching module under `src/stochastic_models/`.
- Write outputs to `results/`, not into the source tree.
- Keep notes that are not part of a notebook in `docs/`.

Do not copy a finished function from one notebook into another. Do not install packages into the global Python environment; install them into `.venv` and add them to `requirements.txt` when the whole team needs them.

`.venv/` is local. Each person creates it on their own machine using the steps above.

## Team Contribution

Team members and individual contributions can be recorded here as the work progresses.
