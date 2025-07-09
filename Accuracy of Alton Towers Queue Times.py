#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Reading in data
DataFrame = pd.read_csv("https://docs.google.com/spreadsheets/d/1c2b05czi2xwwDxKRVBMJ9qyB3_-_b0RyMdc-N8n8JJI/export?format=csv&gid=0", na_values="N/A")

#Printing a summary of the dataset
print(DataFrame)

#Separating advertised queue time and actual queue time
Advertised = DataFrame["Advertised Queue Time"]
Actual = DataFrame["Actual Queue Time"]

#Calculating means of advertised and actual queue times
AdvertisedQueueMean = np.mean(Advertised)
AdvertisedQueueMedian = np.median(Advertised)

#Showing a scatter graph of advertised queue times compared to actual queue times at Alton Towers
plt.scatter(Advertised, Actual)
plt.title("Alton Towers Queue Times")
plt.xlabel("Advertised Queue Time (minutes)")
plt.ylabel("Actual Queue Time (minutes)")
plt.show()

#Performing correlation analysis between advertised and actual queue times and outputting the results
AdvertisedActualPearsonCorrelation = Actual.corr(Advertised, method="pearson")
AdvertisedActualSpearmanCorrelation = Actual.corr(Advertised, method="spearman")

print("The Pearson correlation coefficient between Advertised Queue Time and Actual Queue Time is:",AdvertisedActualPearsonCorrelation)
print("The Spearman correlation coefficient between Advertised Queue Time and Actual Queue Time is:",AdvertisedActualSpearmanCorrelation)

#Dropping any N/A values
ProportionalAbsoluteDataFrame = DataFrame.dropna()

#Declaring raw and proportional discrepancy columns
Discrepancy = DataFrame["Raw Discrepancy"]
ProportionalDiscrepancy = ProportionalAbsoluteDataFrame["Unformatted Proportional Discrepancy"]
RawAbsoluteDiscrepancy = DataFrame["Raw Absolute Discrepancy"]
ProportionalAbsoluteDiscrepancy = ProportionalAbsoluteDataFrame["Unformatted Proportional Absolute Discrepancy"]

#Calculating means of raw discrepancy, proportional discrepancy and their absolute equivalents
DiscrepancyMean = np.mean(Discrepancy)
ProportionalDiscrepancyMean = (np.mean(ProportionalDiscrepancy))*100
RawAbsoluteMean = np.mean(RawAbsoluteDiscrepancy)
ProportionalAbsoluteMean = (np.mean(ProportionalAbsoluteDiscrepancy))*100

#Calculating medians of raw discrepancy, proportional discrepancy and their absolute equivalents
DiscrepancyMedian = np.median(Discrepancy)
ProportionalDiscrepancyMedian = (np.median(ProportionalDiscrepancy))*100
RawAbsoluteMedian = np.median(RawAbsoluteDiscrepancy)
ProportionalAbsoluteMedian = (np.median(ProportionalAbsoluteDiscrepancy))*100

#Calculating means and medians of discrepancy adjusted for the fact that some have an actual queue time of 0 (meaning that proportional discrepancy can't be calculated)
AdjustedDiscrepancyMean = (DiscrepancyMean/AdvertisedQueueMean)*100
AdjustedDiscrepancyMedian = (DiscrepancyMedian/AdvertisedQueueMedian)*100
AdjustedProportionalDiscrepancyMean = (RawAbsoluteMean/AdvertisedQueueMean)*100
AdjustedProportionalDiscrepancyMedian = (RawAbsoluteMedian/AdvertisedQueueMedian)*100

#Showing a boxplot of raw discrepancies between advertised and actual queue times
sns.boxplot(y="Raw Discrepancy", data=DataFrame)
plt.title("Alton Towers Raw Discrepancy")
plt.show()

#Showing a boxplot of proportional discrepancies between advertised and actual queue times
sns.boxplot(y="Unformatted Proportional Discrepancy", data=ProportionalAbsoluteDataFrame)
plt.title("Alton Towers Proportional Discrepancy")
plt.show()

#Showing a boxplot of raw absolute discrepancies between advertised and actual queue times
sns.boxplot(y="Raw Absolute Discrepancy", data=DataFrame)
plt.title("Alton Towers Raw Absolute Discrepancy")
plt.show()

#Showing a boxplot of proportional absolute discrepancies between advertised and actual queue times
sns.boxplot(y="Unformatted Proportional Absolute Discrepancy", data=ProportionalAbsoluteDataFrame)
plt.title("Alton Towers Proportional Absolute Discrepancy")
plt.show()

#Printing the aggregated statistics
print("")
print("Mean Advertised Queue Time: {} minutes".format(AdvertisedQueueMean))
print("Median Advertised Queue Time: {} minutes".format(AdvertisedQueueMedian))
print("Mean Raw Discrepancy: {} minutes".format(DiscrepancyMean))
print("Median Raw Discrepancy: {} minutes".format(DiscrepancyMedian))
print("Mean Proportional Discrepancy: {}%".format(ProportionalDiscrepancyMean))
print("Median Proportional Discrepancy: {}%".format(ProportionalDiscrepancyMedian))
print("")
print("Mean Raw Absolute Discrepancy: {} minutes".format(RawAbsoluteMean))
print("Median Raw Absolute Discrepancy: {} minutes".format(RawAbsoluteMedian))
print("Mean Proportional Absolute Discrepancy: {}%".format(ProportionalAbsoluteMean))
print("Median Proportional Absolute Discrepancy: {}%".format(ProportionalAbsoluteMedian))
print("")
print("Adjusted Mean Proportional Discrepancy: {}%".format(AdjustedDiscrepancyMean))
print("Adjusted Median Proportional Discrepancy: {}%".format(AdjustedDiscrepancyMedian))
print("Adjusted Mean Proportional Absolute Discrepancy: {}%".format(AdjustedProportionalDiscrepancyMean))
print("Adjusted Median Proportional Absolute Discrepancy: {}%".format(AdjustedProportionalDiscrepancyMedian))
