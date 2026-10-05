# Inventory System

A command-line inventory ledger written in Python. It records assets, tracks stock levels and unit prices, calculates valuations, and logs every change to an in-memory audit trail.

## Features

- **Add assets** with an initial quantity and unit price. Duplicate names are rejected.
- **Update assets** by adjusting stock (positive or negative change) or setting a new unit price.
- **Search** for a single asset and view its units, unit price, and total value.
- **Summary table** of all assets with a portfolio total.
- **Audit trail** that records each initialisation, stock change, and price change, with the transaction count reported on exit.
- **Input validation** that catches non-numeric entries without terminating the program.

## Requirements

- Python 3.6 or later
- No third-party packages

## Usage

```bash
git clone https://github.com/shirleymutsai/Inventory-System.git
cd Inventory-System
python3 Inventory_service.py
```

The program presents a menu:

```
[1] Add New Asset
[2] Update Asset (Stock & Price)
[3] Search for Asset
[4] View Summary Table
[5] Exit
```

Asset names are normalised to title case, so `laptop`, `LAPTOP`, and `Laptop` refer to the same record.

### Example output

```
===========================================================================
ASSET NAME           | UNITS      | VALUE/UNIT      | TOTAL VALUE
---------------------------------------------------------------------------
Laptop               | 10         | $850.00         | $8,500.00
Monitor              | 25         | $120.00         | $3,000.00
---------------------------------------------------------------------------
PORTFOLIO TOTAL                                   | $11,500.00
===========================================================================
```

## Design

### Data model

| Structure | Type | Purpose |
|---|---|---|
| `inventory` | `dict` keyed by asset name | Holds `units` and `price` per asset, giving constant-time lookup for search and update |
| `audit_trail` | `list` of strings | Append-only log of every state change |

### Why a single file

The single-file structure is a deliberate choice, made for the following reasons.

1. **Proportionate to scope.** The program is roughly 100 lines with one responsibility: maintaining a ledger through a menu loop. Splitting it into modules would add imports and indirection without reducing complexity.
2. **Shared state is small and local.** The two data structures are used by every menu option. Keeping them inside one function avoids global variables and avoids passing state between modules.
3. **Ease of review.** A reviewer can read the full control flow from top to bottom in one pass, without navigating between files.
4. **No setup cost.** The program has no dependencies, no package structure, and no configuration. It runs with a single command on any machine with Python installed.

A multi-file structure would become appropriate once persistence, automated tests, or a second interface were added. At that point the natural split would be a data layer (inventory and audit logic), an interface layer (menu and input handling), and a test suite.

## Known limitations

- Data is held in memory and is lost when the program exits.
- Stock adjustments can reduce a quantity below zero. Negative initial units and prices are also accepted.
- The audit trail is recorded but cannot be viewed or exported. Only the transaction count is shown on exit.
- Audit entries carry no timestamp.
- The currency symbol is fixed as `$`.
- An invalid main menu selection redisplays the menu without an error message.

## Possible extensions

- Persist the ledger and audit trail to JSON, CSV, or SQLite.
- Add a menu option to view and export the audit trail, with timestamps.
- Validate against negative stock and negative prices.
- Add an option to delete an asset.
- Separate the logic into functions and add unit tests.

## Author

Shirley Mutsai
