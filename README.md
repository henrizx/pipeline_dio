# Transformer Data Management

This repository contains Python code for managing and updating data about Transformers. The code uses the Pandas library to work with a CSV file ('data.csv') containing information about various Transformers. It provides a function to update the attributes of a Transformer based on their ID.

## Installation

Before running the code, make sure you have Python and Pandas installed on your system. You can install Pandas using pip:

```bash
pip install pandas
```

## Usage

1. **Import the Required Libraries**

   ```python
   import pandas as pd
   ```

2. **Load the Transformer Data**

   Read the initial Transformer data from 'data.csv':

   ```python
   df = pd.read_csv('data.csv')
   print(df)
   ```

   This step initializes a Pandas DataFrame containing the Transformer information.

3. **Update a Transformer's Attributes**

   Use the `update_transformer` function to update a Transformer's attributes. The function takes three arguments:

   - `id`: The ID of the Transformer you want to update.
   - `entry`: The attribute you want to update (e.g., 'Abilities').
   - `updated_entry`: The new value for the attribute.

   Example:

   ```python
   update_transformer(1, "Abilities", "['Leadership','Mega Punch','Eye Beam']")
   ```

   This function will update the specified attribute for the Transformer with ID 1 and save the changes back to 'data.csv'.

4. **Check the Updated Transformer Data**

   After updating a Transformer, you can load the updated data from 'data.csv' using the following code:

   ```python
   updated_df = pd.read_csv('data.csv')
   print(updated_df)
   ```

   This code reads the modified data and displays it.

## Data Format

The 'data.csv' file contains information about Transformers with the following columns:

- `ID`: Unique identifier for each Transformer.
- `Name`: The name of the Transformer.
- `Faction`: The faction to which the Transformer belongs (Autobot or Decepticon).
- `Abilities`: A list of abilities possessed by the Transformer.
- `Transforms Into`: The alternate form that the Transformer can transform into.
- `Color`: The color associated with the Transformer.

Please ensure that the data in 'data.csv' follows this format for the code to work correctly.

## License

This code is provided under the MIT License. Feel free to use and modify it as needed for your Transformer data management needs.