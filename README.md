# 🧹 Amazon Product Data Cleaning

This project demonstrates a basic data cleaning workflow using **Python (Pandas)** on a raw dataset of Amazon product listings. The cleaned dataset can be used for further analysis, visualization, or machine learning.

---

## 📁 Dataset

- **Input file**: `amazon.csv`  
- **Output file**: `amazon_cleaned.csv`

The raw dataset contains product information such as prices, ratings, and discount percentages, but includes missing values, duplicates, and inconsistent formatting.

---

## 🛠️ Tools Used

- Python 3
- Pandas

---

## 📌 Objectives

- Identify and handle **missing values**
- Remove **duplicate records**
- Convert **currency and percentage strings** to numeric types
- Standardize **column names**
- Convert text-formatted **numerical and date columns** into proper types

---

## ⚙️ Steps Performed

1. Loaded the dataset using `pandas.read_csv()`
2. Removed duplicate rows using `drop_duplicates()`
3. Filled missing `rating_count` with `0`
4. Cleaned and converted:
   - `discounted_price` and `actual_price` → float (removed ₹, commas)
   - `rating` → float
   - `rating_count` → int (removed commas)
   - `discount_percentage` → int (removed %)
5. Standardized column names to lowercase with underscores
6. Exported the cleaned dataset using `to_csv()`

---

## 📦 How to Run

> Make sure `amazon.csv` is in the same folder as your script.

```bash
pip install pandas
python clean_amazon.py
