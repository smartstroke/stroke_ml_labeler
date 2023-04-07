import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/mar24_2023_normal.csv")
print(data.to_string())

graphStart = 1000
numOfPointsBig = 1000
numOfPointsAround = 40
numOfPointsSmall = 10
start = graphStart + 199

# x axis values
x = data.loc[:, "Time(ms)"]
# corresponding y axis values
AccX = data.loc[:, "AccX"]
AccY = data.loc[:, "AccY"]
AccZ = data.loc[:, "AccZ"]
FSR = data.loc[:, "ADC"]

plt.figure(figsize=(20,12))
plt.subplots_adjust(hspace=0.25)

plt.subplot(4, 1, 1)
plt.plot(x[graphStart:graphStart+numOfPointsBig], AccX[graphStart:graphStart+numOfPointsBig], label="AccX")
plt.axvspan(x[start-numOfPointsAround], x[start+numOfPointsAround+numOfPointsSmall], color='blue', alpha=0.1)
plt.axvspan(x[start], x[start+numOfPointsSmall], color='red', alpha=0.5)
plt.legend()
plt.title("Accelerometer X 1000 points            || (c)catch - (v)nothing - (x)exit || ")

plt.subplot(4, 1, 2)
plt.plot(x[graphStart:graphStart+numOfPointsBig], FSR[graphStart:graphStart+numOfPointsBig], label="FSR")
plt.axvspan(x[start-numOfPointsAround], x[start+numOfPointsAround+numOfPointsSmall], color='blue', alpha=0.1)
plt.axvspan(x[start], x[start+numOfPointsSmall], color='red', alpha=0.5)
plt.legend()
plt.title("FSR 1000 points")

# plotting the points
plt.subplot(4, 2, 5)
plt.plot(x[start-numOfPointsAround:start+numOfPointsAround+numOfPointsSmall], AccX[start-numOfPointsAround:start+numOfPointsAround+numOfPointsSmall], label="AccX")
plt.plot(x[start-numOfPointsAround:start+numOfPointsAround+numOfPointsSmall], AccY[start-numOfPointsAround:start+numOfPointsAround+numOfPointsSmall], label="AccY")
plt.plot(x[start-numOfPointsAround:start+numOfPointsAround+numOfPointsSmall], AccZ[start-numOfPointsAround:start+numOfPointsAround+numOfPointsSmall], label="AccZ")
plt.axvspan(x[start], x[start+numOfPointsSmall], color='red', alpha=0.5)
plt.legend()
plt.title("Accelerometer Raw 100 points Subset")

plt.subplot(4, 2, 7)
plt.plot(x[start: start+numOfPointsSmall], AccX[start: start+numOfPointsSmall], label="AccX")
plt.plot(x[start: start+numOfPointsSmall], AccY[start: start+numOfPointsSmall], label="AccY")
plt.plot(x[start: start+numOfPointsSmall], AccZ[start: start+numOfPointsSmall], label="AccZ")
plt.legend()
plt.title("Accelerometer Raw 10 points Subsubset")

plt.subplot(4, 2, 6)
plt.plot(x[start-numOfPointsAround:start+numOfPointsAround+numOfPointsSmall], FSR[start-numOfPointsAround:start+numOfPointsAround+numOfPointsSmall], label="FSR")
plt.axvspan(x[start], x[start+numOfPointsSmall], color='red', alpha=0.5)
plt.legend()
plt.title("FSR Raw 100 points Subset")

plt.subplot(4, 2, 8)
plt.plot(x[start: start+numOfPointsSmall], FSR[start: start+numOfPointsSmall], label="FSR")
plt.legend()
plt.title("FSR Raw 10 points Subsubset")

plt.show()
