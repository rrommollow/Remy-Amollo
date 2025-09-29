import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("production.csv")

# Filter for Ghana and Ivory Coast
ghana_data = data[data['Area'] == 'Ghana']
ivory_data = data[data['Area'] == "Côte d'Ivoire"]

# Pivot so each measurement becomes a column
ghana = ghana_data.pivot(index='Year', columns='Element', values='Value').reset_index()
ivory_coast = ivory_data.pivot(index='Year', columns='Element', values='Value').reset_index()

# Optional: check pivoted data
#print(ghana.head())
#print(ivory_coast.head())

# Create 2x2 subplot
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Ghana - Yield
axs[0, 0].scatter(ghana['Year'], ghana['Yield'], color="green")
axs[0, 0].set_title("Ghana - Yield by Year")
axs[0, 0].set_xlabel("Year")
axs[0, 0].set_ylabel("Yield (hg/ha)")

# Ivory Coast - Yield
axs[0, 1].scatter(ivory_coast['Year'], ivory_coast['Yield'], color="brown")
axs[0, 1].set_title("Ivory Coast - Yield by Year")
axs[0, 1].set_xlabel("Year")
axs[0, 1].set_ylabel("Yield (hg/ha)")

# Ghana - Area harvested
axs[1, 0].bar(ghana['Year'], ghana['Area harvested'], color="orange")
axs[1, 0].set_title("Ghana - Area Harvested by Year")
axs[1, 0].set_xlabel("Year")
axs[1, 0].set_ylabel("Area harvested (ha)")

# Ivory Coast - Area harvested
axs[1, 1].bar(ivory_coast['Year'], ivory_coast['Area harvested'], color="blue")
axs[1, 1].set_title("Ivory Coast - Area Harvested by Year")
axs[1, 1].set_xlabel("Year")
axs[1, 1].set_ylabel("Area harvested (ha)")

# Overall title and layout
fig.suptitle("Cocoa Production in Ghana and Ivory Coast", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save to PDF
plt.savefig("cocoa_production_analysis.pdf")
plt.show()