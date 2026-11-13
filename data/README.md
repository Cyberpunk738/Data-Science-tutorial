# Orders dataset

`orders.csv` is the 40-row teaching dataset from Tech With Tim's [PanadasTutorial](https://github.com/techwithtim/PanadasTutorial). It is included unchanged for this workshop, except for a final newline if required by the text transport.

- Upstream commit: `d15b5b450411e1634961de40f5a4c3fe12ef187f`
- Upstream Git blob: `64c6609f606c50aec6ac9a2e98d9d419405a18eb`
- [Original CSV at that commit](https://github.com/techwithtim/PanadasTutorial/blob/d15b5b450411e1634961de40f5a4c3fe12ef187f/orders.csv)
- Retrieved for this workshop on 13 November 2026.
- The upstream root has no license file. No new license is asserted over this third-party dataset. Dataset credit remains with its source.

The lesson notebooks and explanations in this repository are newly written for this class. The upstream notebook, setup files and package-manager lock file have not been copied.

| Column | Meaning in the exercise |
|---|---|
| OrderID | Identifier for an order, not a row position |
| CustomerName | Name recorded on the order |
| Product | Product description |
| Category | Electronics, Furniture or Stationery |
| Quantity | Number of units |
| Price | Price field from the source; no currency is specified |
| OrderDate | Recorded date in YYYY-MM-DD form |
| Shipped | Yes/No shipping status, stored as text |
| Country | Country label as recorded in the source |

One row represents an order record. Repeated country labels count orders, not unique customers or all residents of that country. The dataset does not specify currency or explicitly document whether Price is per unit. Avoid inventing those details.
