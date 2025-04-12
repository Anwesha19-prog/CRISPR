CRISPR_gene_analysis

Python Script 
Author: Anwesha Sarkar

Date: December, 2023

Description:

# CRISPR-Induced Stress Analysis

## Overview

This repository contains Python code for analyzing CRISPR knockout effects on gene expression and fluorescence-based uptake measurements. The dataset includes information on different **cell lines**, **genes**, **log2 fold changes (log2FC) in gene expression**, and **ICG uptake** values.



**#Images**
![CRISPR_coloncells1](https://github.com/user-attachments/assets/669f1434-547e-4072-a8ee-c51528706687)
![CRISPR_coloncells2](https://github.com/user-attachments/assets/13a28650-b66d-4a88-938c-84df3061983d)




## Dataset

The dataset consists of cell lines subjected to **CRISPR knockout** of two genes: `PKL1` and `PKL3`. The **log2FC values** represent gene expression changes post-knockout, and the ICG uptake values quantify fluorescence intensity.

## Features

- **Stress Classification**: Log2FC values are classified into four categories:
  - High Stress (`log2FC ≤ -2`)
  - Moderate Stress (`-2 < log2FC ≤ -1`)
  - Low Stress (`-1 < log2FC < -0.3`)
  - No Stress (`log2FC ≥ -0.3`)

- **Data Visualization**:
  - A **bar plot** showing ICG uptake across different cell lines and genes.
  - A **scatter plot** depicting the correlation between ICG uptake and log2FC values.

## Dependencies

Ensure the following Python libraries are installed before running the code:

```python
pip install eaborn
