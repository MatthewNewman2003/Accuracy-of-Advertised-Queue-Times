#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Reading in the data
DataFrame = pd.read_csv("https://docs.google.com/spreadsheets/d/1jpqqpu2pErHY41vHTpDP_NEZqnjuMwgtVVp99JexjvI/export?format=csv&gid=0", na_values="N/A")

#Printing a summary of the data
print(DataFrame)

#Reading the advertised and actual queue time columns
Advertised = DataFrame["Advertised Queue Time"]
Actual = DataFrame["Actual Queue Time"]

#Calculating the mean and median of advetised queue time
AdvertisedQueueMean = np.mean(Advertised)
AdvertisedQueueMedian = np.median(Advertised)

#Showing a scatter graph comparing advertised queue times to actual queue times
plt.scatter(Advertised, Actual)
plt.title("UK Merlin Park Queue Times")
plt.xlabel("Advertised Queue Time (minutes)")
plt.ylabel("Actual Queue Time (minutes)")
plt.show()

#Calculating correlation coefficients between advertised and actual queue times and outputting the results
AdvertisedActualPearsonCorrelation = Actual.corr(Advertised, method="pearson")
AdvertisedActualSpearmanCorrelation = Actual.corr(Advertised, method="spearman")

print("The Pearson correlation coefficient between Advertised Queue Time and Actual Queue Time is:",AdvertisedActualPearsonCorrelation)
print("The Spearman correlation coefficient between Advertised Queue Time and Actual Queue Time is:",AdvertisedActualSpearmanCorrelation)

#Dropping any N/A columns for calculation of proportional discrepancies
ProportionalAbsoluteDataFrame = DataFrame.dropna()

#Declaring raw and proportional discrepancy columns
Discrepancy = DataFrame["Raw Discrepancy"]
ProportionalDiscrepancy = ProportionalAbsoluteDataFrame["Unformatted Proportional Discrepancy"]
RawAbsoluteDiscrepancy = DataFrame["Raw Absolute Discrepancy"]
ProportionalAbsoluteDiscrepancy = ProportionalAbsoluteDataFrame["Unformatted Proportional Absolute Discrepancy"]

#Calculating means of raw and proportional discrepancy and their absolute equivalents
DiscrepancyMean = np.mean(Discrepancy)
ProportionalDiscrepancyMean = (np.mean(ProportionalDiscrepancy))*100
RawAbsoluteMean = np.mean(RawAbsoluteDiscrepancy)
ProportionalAbsoluteMean = (np.mean(ProportionalAbsoluteDiscrepancy))*100

#Calculating medians of raw and proportional discrepancy and their absolute equivalents
DiscrepancyMedian = np.median(Discrepancy)
ProportionalDiscrepancyMedian = (np.median(ProportionalDiscrepancy))*100
RawAbsoluteMedian = np.median(RawAbsoluteDiscrepancy)
ProportionalAbsoluteMedian = (np.median(ProportionalAbsoluteDiscrepancy))*100

#Calculating mean and median of adjusted discrepancies to adjust for the fact that some advertised queue times are 0 minutes (meaning that proportional discrepancies can't be calculated)
AdjustedDiscrepancyMean = (DiscrepancyMean/AdvertisedQueueMean)*100
AdjustedDiscrepancyMedian = (DiscrepancyMedian/AdvertisedQueueMedian)*100
AdjustedProportionalDiscrepancyMean = (RawAbsoluteMean/AdvertisedQueueMean)*100
AdjustedProportionalDiscrepancyMedian = (RawAbsoluteMedian/AdvertisedQueueMedian)*100

#Showing boxplots of different discrepancy types
sns.boxplot(y="Raw Discrepancy", data=DataFrame)
plt.title("UK Merlin Park Raw Discrepancy")
plt.show()

sns.boxplot(y="Unformatted Proportional Discrepancy", data=ProportionalAbsoluteDataFrame)
plt.title("UK Merlin Park Proportional Discrepancy")
plt.show()

sns.boxplot(y="Raw Absolute Discrepancy", data=DataFrame)
plt.title("UK Merlin Park Raw Absolute Discrepancy")
plt.show()

sns.boxplot(y="Unformatted Proportional Absolute Discrepancy", data=ProportionalAbsoluteDataFrame)
plt.title("UK Merlin Park Proportional Absolute Discrepancy")
plt.show()

#Showing the raw calculated statistics
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
