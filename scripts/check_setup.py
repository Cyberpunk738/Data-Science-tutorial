"""Run with the same Python selected as your VS Code notebook kernel."""
import importlib
from pathlib import Path
import sys


def main():
    print("Python executable:", sys.executable)
    if sys.version_info < (3, 12):
        print("Please use Python 3.12 or newer for this class.")
        return 1
    for name in ("pandas", "ipykernel"):
        try:
            module = importlib.import_module(name)
        except ImportError:
            print(f"Missing {name}. Run python -m pip install -r requirements.txt")
            return 1
        print(name, getattr(module, "__version__", "installed"))
    root = Path(__file__).resolve().parents[1]
    df = importlib.import_module("pandas").read_csv(root / "data" / "orders.csv")
    expected = ["OrderID", "CustomerName", "Product", "Category", "Quantity", "Price", "OrderDate", "Shipped", "Country"]
    if df.shape != (40, 9) or list(df.columns) != expected:
        print("The source CSV differs from the class snapshot. Restore data/orders.csv.")
        return 1
    print("Ready: 40 orders and 9 columns.")
    print("In VS Code, select this project's .venv in the notebook kernel picker.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
