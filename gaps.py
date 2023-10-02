

import pandas as pd
import matplotlib.pyplot as plt

# Read in CSV file containing gap information
gap_df = pd.read_csv("out_abv1.csv")

# Get a list of all unique stations
stations = gap_df["station"].unique()

# Set up the plot grid
fig, axes = plt.subplots(len(stations), 1, figsize=(8, 16), sharex=True)

# Iterate over stations and plot histogram of gap lengths for each station
for i, station in enumerate(stations):
    # Select only gap information for the current station
    station_gaps = gap_df[gap_df["station"] == station]
    
    # Plot histogram of gap lengths
    axes[i].hist(station_gaps["gaps"])
    
    # Add labels and title to subplot
    axes[i].set_xlabel("Gap Length (s)")
    axes[i].set_ylabel("Frequency")
    axes[i].set_title(f"Station {station}")
    
# Add overall x label and save the figure
fig.text(0.5, 0.04, "Gap Length (s)", ha="center")
#fig.savefig("gap_length_histograms.png")
plt.show()



