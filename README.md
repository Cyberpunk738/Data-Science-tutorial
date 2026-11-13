# Data-Science-tutorial

**First class: Introduction to Python and pandas**  
Afeez Sule · DSN FUOYE

Learn Python basics, then explore an orders CSV in a **Jupyter notebook inside desktop VS Code**. This class uses pandas for data analysis. Charts and Matplotlib are reserved for a later class.

## Before the class

Install:

1. **Python 3.12 or newer**. Python 3.13 is a good workshop choice. Download from [python.org](https://www.python.org/downloads/). On current Windows installations, Python Install Manager supports `py install 3.13`. If Python already works, check its version before installing another copy.
2. **Git** from [git-scm.com](https://git-scm.com/downloads).
3. **Desktop VS Code** from [code.visualstudio.com](https://code.visualstudio.com/).
4. Microsoft's **Python** (`ms-python.python`) and **Jupyter** (`ms-toolsai.jupyter`) extensions in VS Code. The repository recommends them when opened.

The VS Code editor is where you write; Python runs the code; a notebook kernel is the running Python environment behind your cells. `ipykernel` connects that environment to the notebook. A separate Jupyter server installation is not needed for this VS Code setup.

## 1. Clone the class files

In a terminal:

```bash
git clone https://github.com/Cyberpunk738/Data-Science-tutorial.git
cd Data-Science-tutorial
```

Open this folder using **File > Open Folder** in VS Code. If the `code` command is available, `code .` also works.

## 2. Create your environment and install packages

Run the commands for your system in a terminal opened in the repository folder. A virtual environment gives this project its own installed packages. `pip` is the installer. You do not type these commands into an ordinary Python code cell.

### Windows: Command Prompt

If VS Code's terminal is PowerShell, use its terminal profile menu to open **Command Prompt** for these instructions.

```bat
py -3 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python scripts/check_setup.py
```

If `py` is not recognised but `python --version` shows Python 3.12+, use `python -m venv .venv` for the first command.

### Windows: PowerShell alternative without activation

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts/check_setup.py
```

These direct interpreter commands avoid changing the PowerShell execution policy. Select that same `.venv` as your notebook kernel.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/check_setup.py
```

On Ubuntu/Debian, if Python or venv support is missing, install the distribution packages `python3`, `python3-venv`, and `python3-pip` using your package manager, then retry. Keep system-managed Python installed.

## 3. Select the notebook kernel

1. Open `notebooks/00_setup_check.ipynb` in VS Code.
2. Choose **Select Kernel** at the top right.
3. Choose **Python Environments**, or **Select Another Kernel > Python Environments** if prompted.
4. Choose this project's `.venv` Python. The interpreter path should contain `Data-Science-tutorial` and `.venv`.
5. Run its cells with the play button or **Shift+Enter**.
6. You should see `Ready: 40 orders and 9 columns.`

If `.venv` is missing from the list, run **Python: Select Interpreter** from the Command Palette and choose the `.venv` interpreter, then refresh/reopen the notebook's kernel picker. Restart VS Code if necessary.

## 4. Class order

| File | Purpose |
|---|---|
| `notebooks/00_setup_check.ipynb` | Confirm the environment and find the CSV |
| `notebooks/01_python_basics.ipynb` | Print, variables, types, calculations, lists, comparisons, if and dictionaries |
| `notebooks/02_pandas_first_class.ipynb` | Read a CSV, inspect, select columns, get a row, filter, count and save |
| `notebooks/03_pandas_extra_practice.ipynb` | Optional: multiple filters, text matching, updates and renaming |
| `teacher/solutions.ipynb` | Exercise answers for the facilitator or after you try |
| `teacher/TEACHER_NOTES.md` | Teaching script and corrected examples from the preparation notes |
| `teacher/Teacher_Notes.pdf` | Printable version of the teacher notes |
| `docs/Student_Workbook.pdf` | Printable exercise workbook |
| `scripts/class_demo.py` | Commented `.py` version of the demonstrations |

Examples are runnable; practice cells contain comments where you write your own answer. Do not open solutions until you have tried. The teacher folder is public, not hidden or access-controlled.

## Working with notebooks

Run cells from top to bottom. Variables remain in the kernel until you restart it. If a name is undefined, run the earlier setup cells. Restart the kernel and run all cells to check a clean start. Save your work with Ctrl+S (Cmd+S on Mac).

The CSV is in `data/orders.csv`. The notebooks find the repository root from either the repository folder or the `notebooks` folder. Keep the folder structure intact. Example exports go into `outputs/`, never over the original dataset. If the repository moves, restart the kernel and rerun the path setup cell.

## Quick questions

- **What is `pd`?** A conventional short alias for pandas in `import pandas as pd`.
- **What is `df`?** Our variable name for the table (DataFrame).
- **What is a CSV?** A text file holding rows and comma-separated fields.
- **Why `df.columns`, not `df.columns()`?** `columns` is an attribute; `head()` is a method we call.
- **Why no chart?** This first class focuses on Python foundations and pandas.
- **What is in requirements.txt?** pandas, plus ipykernel for the notebook. Package dependencies install automatically.

## Troubleshooting

| Problem | First check |
|---|---|
| `ModuleNotFoundError: pandas` | The selected notebook kernel must be the `.venv` where requirements were installed |
| `No module named ipykernel` | Install `requirements.txt` using that environment's Python |
| CSV not found | Open the full repository folder; retain `data/orders.csv` and run the path setup cell |
| `KeyError: country` | Use the exact label `Country`; case and spelling matter |
| `Index object is not callable` | Use `df.columns`, without parentheses |
| Ambiguous truth-value error | Use `&` / `\|` for pandas conditions and enclose each condition in parentheses |
| Updates disappear on restart | Notebook memory is temporary; export a new CSV to keep edits |
| `git` or `code` not recognised | Install Git, reopen the terminal; VS Code can be opened through its menu |

## Facilitator validation

With the environment active:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_workshop.py
```

This validates notebook format, executes each notebook’s code in a fresh Python process, and checks the demonstration results, source dataset and exported CSV. To test actual Jupyter kernels on your laptop, run `python scripts/validate_workshop.py --kernel`. Student setup only requires `requirements.txt`.

## Dataset and references

The orders data comes from [Tech With Tim's PanadasTutorial](https://github.com/techwithtim/PanadasTutorial). See [data/README.md](data/README.md) for the exact snapshot and field notes. This class uses that dataset with newly written teaching material.

- [VS Code Jupyter notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- [VS Code notebook kernels](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management)
- [pandas indexing guide](https://pandas.pydata.org/docs/user_guide/indexing.html)
