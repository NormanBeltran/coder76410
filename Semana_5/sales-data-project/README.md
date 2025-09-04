# Sales Data Project

This project is designed to generate random sales data for a selection of toys. The generated data is saved in an Excel file, which includes essential sales metrics.

## Project Structure

```
sales-data-project
├── src
│   ├── generate_sales_data.py  # Script to generate random sales data for toys
│   └── rag.py                   # Script for loading documents and setting up a Q&A system
├── requirements.txt             # Lists the dependencies required for the project
└── README.md                    # Documentation for the project
```

## Purpose

The main purpose of this project is to create a dataset that simulates sales data for 20 different toys. This data can be used for analysis, testing, or as a sample dataset for various applications.

## How to Run

1. **Install Dependencies**: Ensure you have the required libraries by installing them from `requirements.txt`. You can do this by running:
   ```
   pip install -r requirements.txt
   ```

2. **Generate Sales Data**: To generate the sales data, run the following command:
   ```
   python src/generate_sales_data.py
   ```

3. **Output**: The script will create an Excel file containing the sales data with the following columns:
   - Juguete
   - Mes de la Venta
   - Cantidad de juguetes vendidos
   - Monto total de la venta

## Additional Information

- The `rag.py` file is part of a separate functionality that deals with document loading and question-answering systems and does not directly relate to the sales data generation.
- Ensure you have the necessary permissions to write files in the directory where the script is executed.