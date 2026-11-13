# Student workbook
## Introduction to Python and pandas
Afeez Sule · DSN FUOYE · Class 1

This workbook goes with the Jupyter notebooks in the class repository. Type your answers in the notebook practice cells, or make notes here. The supplied orders data comes from Tech With Tim's PanadasTutorial.

## Before the class
1. Clone https://github.com/Cyberpunk738/Data-Science-tutorial.git
2. Follow README.md to install requirements in .venv.
3. In desktop VS Code, install the Microsoft Python and Jupyter extensions.
4. Open notebooks/00_setup_check.ipynb and select the .venv kernel.
5. Confirm the ready message says 40 orders and 9 columns.

## What we will do
Learn Python basics, read an orders CSV using pandas, select and filter records, count labels and save a result. Charts belong to a later class.

## Key words
| Word | Meaning |
|---|---|
| Python | The programming language |
| Interpreter | Software that runs Python code |
| Kernel | The running environment behind notebook cells |
| pandas | A library for working with tables |
| pd | The alias used for pandas |
| DataFrame | A labelled table |
| Series | A labelled one-dimensional collection |
| CSV | A text file with comma-separated fields |

<!-- PAGEBREAK -->
# Part 1: Python foundations

## P1. Your first output
Write code to display your name and one sentence about what you want to learn.

```python
# Your answer:


```

## Predict before running
```python
quantity = 3
print(quantity)
print("quantity")
```

What does each line display? Why are the results different?

Notes: ___________________________________________________________

__________________________________________________________________

## Types
| Value | Your predicted type |
|---|---|
| 3 | ____________________ |
| 45.0 | ____________________ |
| "Alice Wong" | ____________________ |
| True | ____________________ |

## P2. Add two quantities
Store 3 and 5 in variables, then print their total.

```python
# Your answer:


```

## Lists and comparisons
For countries = ["USA", "Canada", "UAE"], what do countries[0], countries[1] and len(countries) return?

Notes: ___________________________________________________________

For quantity = 20, predict quantity > 20, quantity >= 20 and quantity != 20.

Notes: ___________________________________________________________

<!-- PAGEBREAK -->
# Part 1 continued

## P3. A simple decision
Write an if/else statement: display Multiple units when quantity is at least 2; otherwise display One unit or fewer. Try quantity = 1.

```python
# Your answer:




```

## Explain the symbols
| Symbol | Your explanation |
|---|---|
| = | ______________________________ |
| == | ______________________________ |
| != | ______________________________ |
| >= | ______________________________ |
| [] | ______________________________ |
| () | ______________________________ |

## Before pandas
What is a library? What is the difference between installing pandas and importing it?

Notes: ___________________________________________________________

__________________________________________________________________

__________________________________________________________________

<!-- PAGEBREAK -->
# Part 2: The orders table

Open notebooks/02_pandas_first_class.ipynb. Run the path helper and import/read cells. Keep the exact column spelling and capitalisation.

## What does a row represent?
One row represents: _______________________________________________

| Question | Your answer |
|---|---|
| How many rows? | ____________________ |
| How many columns? | ____________________ |
| What does pd mean? | ____________________ |
| What does df refer to? | ____________________ |
| Why df.columns rather than df.columns()? | ____________________ |

## Practice A. Several columns
Show Product, Category and Quantity for the first five orders.

```python
# Your answer:


```

## One row
Write code to get the first row by integer position. Which positions does df.iloc[0:3] select?

```python
# Your answer:

```

Notes: ___________________________________________________________

## Filter quantities
Predict the difference between Quantity > 20 and Quantity >= 20. Run both and record the customers that appear.

Notes: ___________________________________________________________

__________________________________________________________________

<!-- PAGEBREAK -->
# Part 2 continued

## Practice B. Orders from USA
Select only USA orders. How many rows match?

```python
# Your answer:


```

## Counts and meaning
What does len(df["Country"]) count? How does value_counts() differ? How would you count distinct country labels?

Notes: ___________________________________________________________

__________________________________________________________________

## Practice C. Save Stationery orders
Select Stationery orders. Save them to OUTPUT_DIR / "stationery_orders.csv" without the pandas row index. Confirm the source CSV is unchanged.

```python
# Your answer:



```

Why is False capitalised? What would index=True include?

Notes: ___________________________________________________________

## Exit questions
Explain one selection and one filter to a partner. How would you restore the original table after experimenting? What would you like to analyse next?

Notes: ___________________________________________________________

__________________________________________________________________

<!-- PAGEBREAK -->
# Part 3: Extra practice
Optional after the first class. Use notebook 03. Each update exercise starts with a copy.

## Practice D. Combined and text filters
Show orders that are both Stationery and from Canada. Then show customer names beginning with J. Explain where each pair of parentheses belongs.

```python
# Your answer:



```

## Practice E. Update, rename and export
Starting from df.copy(), change every No in Shipped to Pending, rename CustomerName to Customer, and save outputs/shipping_practice.csv. Check df remains unchanged.

```python
# Your answer:





```

## Correct the preparation shorthand
| Shorthand | Your corrected form |
|---|---|
| df.columns() | _____________________________ |
| df.iloc() for first row | _____________________________ |
| startwith | _____________________________ |
| rename(column=...) | _____________________________ |
| index=false | _____________________________ |

Try before opening teacher/solutions.ipynb. The solutions are public for review after practice.

Dataset: https://github.com/techwithtim/PanadasTutorial
Class repository: https://github.com/Cyberpunk738/Data-Science-tutorial
