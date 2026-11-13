"""Validate notebook syntax, run each notebook's code fresh, and check results.

Default: fresh Python processes, suitable for restricted CI without kernel sockets.
Optional --kernel: execute actual Jupyter kernels on a machine that allows them.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile

import nbformat
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def run_cells(path):
    runner = r'''
import contextlib, io, json, sys
from pathlib import Path
notebook = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
namespace = {"__name__": "__main__"}
with contextlib.redirect_stdout(io.StringIO()):
    for i, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] == "code":
            source = cell["source"]
            if isinstance(source, list):
                source = "".join(source)
            exec(compile(source, f"{sys.argv[1]}:cell-{i}", "exec"), namespace)
'''
    subprocess.run([sys.executable, "-c", runner, str(path.resolve())],
                   check=True, cwd=path.parent)


def run_kernel(path):
    from nbclient import NotebookClient
    from jupyter_client import KernelManager
    from jupyter_client.kernelspec import KernelSpecManager
    with tempfile.TemporaryDirectory(prefix="ds-workshop-") as tmp:
        kernel_dir = Path(tmp) / "workshop"
        kernel_dir.mkdir()
        (kernel_dir / "kernel.json").write_text(json.dumps({
            "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
            "display_name": "Workshop validation", "language": "python"
        }))
        specs = KernelSpecManager(kernel_dirs=[tmp], ensure_native_kernel=False)

        class WorkshopKernelManager(KernelManager):
            def __init__(self, **kwargs):
                kwargs["kernel_spec_manager"] = specs
                super().__init__(**kwargs)

        notebook = nbformat.read(path, as_version=4)
        NotebookClient(notebook, kernel_name="workshop", timeout=90,
                       kernel_manager_class=WorkshopKernelManager,
                       resources={"metadata": {"path": str(path.parent)}}).execute()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kernel", action="store_true", help="Launch real Jupyter kernels instead of cell-only execution")
    args = parser.parse_args()
    source = ROOT / "data" / "orders.csv"
    before = hashlib.sha256(source.read_bytes()).hexdigest()
    subprocess.run([sys.executable, str(ROOT / "scripts" / "check_setup.py")], check=True, cwd=ROOT)
    notebooks = sorted((ROOT / "notebooks").glob("*.ipynb")) + [ROOT / "teacher" / "solutions.ipynb"]
    for path in notebooks:
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
        (run_kernel if args.kernel else run_cells)(path)
        print("PASS", path.relative_to(ROOT), "(kernel)" if args.kernel else "(fresh Python process)")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "class_demo.py")],
                   check=True, cwd=ROOT, stdout=subprocess.DEVNULL)
    df = pd.read_csv(source)
    assert df.shape == (40, 9)
    assert len(df[df["Category"] == "Electronics"]) == 18
    assert len(df[(df["Category"] == "Electronics") & (df["Country"] == "USA")]) == 1
    assert len(df[(df["Category"] == "Electronics") | (df["Country"] == "USA")]) == 20
    assert df.loc[df["Quantity"] > 20, "CustomerName"].tolist() == ["Alex Johnson"]
    assert len(df[df["Quantity"] >= 20]) == 2
    assert df["Country"].nunique() == 28
    assert df["Country"].value_counts()["USA"] == 3
    assert len(df[df["CustomerName"].str.startswith("A", na=False)]) == 7
    assert len(df[df["CustomerName"].str.endswith("son", na=False)]) == 5
    edited = pd.read_csv(ROOT / "outputs" / "orders_edited.csv")
    assert "Order ID" in edited.columns and "OrderID" not in edited.columns
    assert len(edited[edited["Country"] == "United States"]) == 3
    assert edited.loc[edited["CustomerName"] == "Anna Ivanova", "Product"].item() == "Desk Timer"
    assert not any(c.startswith("Unnamed:") for c in edited.columns)
    assert len(pd.read_csv(ROOT / "outputs" / "usa_orders.csv")) == 3
    assert len(pd.read_csv(ROOT / "outputs" / "stationery_orders.csv")) == 8
    shipping = pd.read_csv(ROOT / "outputs" / "shipping_practice.csv")
    assert "Customer" in shipping.columns and "No" not in set(shipping["Shipped"])
    assert hashlib.sha256(source.read_bytes()).hexdigest() == before
    print("PASS script, filters, edits, exports and unchanged source dataset")


if __name__ == "__main__":
    main()
