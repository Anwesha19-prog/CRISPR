import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the dataset
data = {
    "Cell_Line": ["HT29", "HT29", "HCT116", "HCT116", "SW480", "SW480", "CCD841", "CCD841"],
    "Gene": ["PKL1", "PKL3", "PKL1", "PKL3", "PKL1", "PKL3", "PKL1", "PKL3"],
    "log2FC": [-2.0, -1.2, -2.3, -1.1, -0.5, -0.3, -0.1, 0.2],
    "ICG_Uptake": [20, 35, 18, 40, 75, 80, 95, 100]
}
df = pd.DataFrame(data)

# Add a stress interpretation
def classify_stress(fc):
    if fc <= -2:
        return "High"
    elif fc <= -1:
        return "Moderate"
    elif fc < -0.3:
        return "Low"
    else:
        return "None"

df["Stress"] = df["log2FC"].apply(classify_stress)

# Visualization: ICG uptake by gene and cell line
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="Cell_Line", y="ICG_Uptake", hue="Gene", palette="viridis")
plt.title("ICG Uptake After CRISPR Knockout of PKL1/PKL3")
plt.ylabel("ICG Uptake (AU)")
plt.axhline(50, linestyle="--", color="gray", label="Mid-range uptake")
plt.legend()
plt.show()

# Correlation plot
plt.figure(figsize=(6, 6))
sns.scatterplot(data=df, x="log2FC", y="ICG_Uptake", hue="Cell_Line", style="Gene", s=100)
plt.title("ICG Uptake vs CRISPR-Induced Stress (log2FC)")
plt.xlabel("log2 Fold Change (Viability)")
plt.ylabel("ICG Uptake (Fluorescence Units)")
plt.axhline(50, linestyle="--", color="gray")
plt.axvline(-1, linestyle="--", color="gray")
plt.show()
