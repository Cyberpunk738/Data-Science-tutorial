"""Python foundations and pandas demonstrations for DSN FUOYE.
Run `python scripts/class_demo.py` from the repository folder.
Use # %% cells in VS Code to demonstrate one section at a time.
Practice answers live in teacher/solutions.ipynb.
"""


# %% 01 · Python before pandas

# %% 1. Showing a result with print
print("Hello, data science!")
print(2 + 3)

# **Practice P1:** print your name and a sentence about what you want to learn.

# %% 2. Variables and assignment
customer_name = "Alice Wong"
quantity = 3
price = 45.0
print(customer_name)
print(quantity)
print("quantity")

# %% 3. Common types
quantity = 3
price = 45.0
customer_name = "Alice Wong"
shipped = True
print(type(quantity))
print(type(price))
print(type(customer_name))
print(type(shipped))

# %% 4. Calculations
print(10 + 2)
print(10 - 2)
print(10 * 2)
print(10 / 2)

# **Practice P2:** store two quantities, 3 and 5, and print their total.

# %% 5. Lists and positions
countries = ["USA", "Canada", "UAE"]
print(countries[0])
print(countries[1])
print(len(countries))

# %% 6. Comparisons
quantity = 20
print(quantity > 20)
print(quantity >= 20)
print(quantity != 20)
print(quantity == 20)

# %% 7. A simple if statement
quantity = 3
if quantity >= 2:
    print("Multiple units")
else:
    print("One unit or fewer")

# **Practice P3:** change quantity to 1 and predict which message appears. Write and run your own if/else example.

# %% 8. Dictionaries: a short preview
order = {"CustomerName": "Alice Wong", "Quantity": 3}
print(order["CustomerName"])

# %% Checkpoint

# %% 02 · First class with pandas

# %% 1. Import pandas and load the CSV
from pathlib import Path

# Preparation helper: find the CSV whether the kernel starts in the
# repository folder, notebooks folder, or teacher folder.
# We use pathlib from Python's standard library, not another install.
ROOT = next(
    (folder for folder in [Path.cwd(), *Path.cwd().parents, Path(__file__).resolve().parents[1]]
     if (folder / "data" / "orders.csv").is_file()),
    None,
)
if ROOT is None:
    raise FileNotFoundError("Open the Data-Science-tutorial folder in VS Code.")
DATA_FILE = ROOT / "data" / "orders.csv"
OUTPUT_DIR = ROOT / "outputs"
print(OUTPUT_DIR.mkdir(exist_ok=True))
import pandas as pd

df = pd.read_csv(DATA_FILE)
print(df.head())

# `pd.read_csv()` reads a CSV into a DataFrame. `df.head()` shows its first five rows. The last expression in a notebook code cell displays automatically; scripts generally use print().

# %% 2. Inspect before selecting
print(df.columns)
print(df.shape)
print(len(df))

# %% 3. Select one column
print(df["Country"])
print(len(df["Country"]))

# `len(df["Country"])` counts entries, including missing entries if any. It does not count distinct countries. Here it is 40, because the table has 40 rows.

# %% 4. Select several columns
print(df[["CustomerName", "Country"]].head())

# **Practice A:** show Product, Category and Quantity for the first five orders.

# %% 5. Select a row by integer position
print(df.iloc[0])
print(df.iloc[0:3])

# The OrderID column contains identifiers such as 1001. Those identifiers are not automatically the table's index or row positions.

# %% 6. Filter orders by category
electronics = df["Category"] == "Electronics"
print(electronics.head())
print(df[electronics])
print(df[df["Category"] == "Electronics"])

# %% 7. Compare quantities
print(df[df["Quantity"] > 20])
print(df[df["Quantity"] >= 20])

# **Practice B:** select orders from USA. Predict how many rows will match, then run your code.

# %% 8. Count orders by country
print(df["Country"].value_counts())
print("Distinct country labels:", df["Country"].nunique())

# %% 9. Save a result
usa_orders = df[df["Country"] == "USA"]
export_path = OUTPUT_DIR / "usa_orders.csv"
usa_orders.to_csv(export_path, index=False)
print("Saved:", export_path)

# **Practice C:** select Stationery orders, then save them to `outputs/stationery_orders.csv` without the row index. Use OUTPUT_DIR to build the path.

# %% Finish here for the first class

# %% 03 · Extra pandas practice
from pathlib import Path

# Preparation helper: find the CSV whether the kernel starts in the
# repository folder, notebooks folder, or teacher folder.
# We use pathlib from Python's standard library, not another install.
ROOT = next(
    (folder for folder in [Path.cwd(), *Path.cwd().parents, Path(__file__).resolve().parents[1]]
     if (folder / "data" / "orders.csv").is_file()),
    None,
)
if ROOT is None:
    raise FileNotFoundError("Open the Data-Science-tutorial folder in VS Code.")
DATA_FILE = ROOT / "data" / "orders.csv"
OUTPUT_DIR = ROOT / "outputs"
print(OUTPUT_DIR.mkdir(exist_ok=True))
import pandas as pd
df = pd.read_csv(DATA_FILE)

# %% 1. AND: both conditions must be True
print(df[(df["Category"] == "Electronics") & (df["Country"] == "USA")])

# %% 2. OR: at least one condition must be True
print(df[(df["Category"] == "Electronics") | (df["Country"] == "USA")])

# %% 3. Other comparisons
print(df[df["Quantity"] >= 2])
print(df[df["Quantity"] <= 2])
print(df[df["Country"] != "USA"])

# %% 4. Names starting with A
print(df[df["CustomerName"].str.startswith("A", na=False)])

# %% 5. Names ending with son
print(df[df["CustomerName"].str.endswith("son", na=False)])

# **Practice D:** show orders that are both Stationery and from Canada. Then show names beginning with J.

# %% 6. Locate rows before editing
print(df.loc[df["CustomerName"] == "Anna Ivanova", ["CustomerName", "Product"]])

# %% 7. Update one selected customer's product
edited_df = df.copy()
edited_df.loc[edited_df["CustomerName"] == "Anna Ivanova", "Product"] = "Desk Timer"
print(edited_df.loc[edited_df["CustomerName"] == "Anna Ivanova", ["CustomerName", "Product"]])

# %% 8. Standardise every matching country entry
edited_df.loc[edited_df["Country"] == "USA", "Country"] = "United States"
print(edited_df.loc[edited_df["Country"] == "United States", ["CustomerName", "Country"]])

# %% 9. Rename the OrderID column
edited_df = edited_df.rename(columns={"OrderID": "Order ID"})
print(edited_df.columns)

# %% 10. Count and export the edited table
print(edited_df["Country"].value_counts())
edited_path = OUTPUT_DIR / "orders_edited.csv"
edited_df.to_csv(edited_path, index=False)
print("Saved:", edited_path)

# **Practice E:** starting from `df.copy()`, change every "No" in Shipped to "Pending", rename CustomerName to Customer, and export to `outputs/shipping_practice.csv`. Verify your result and check that df itself is unchanged.

# %% Reset
