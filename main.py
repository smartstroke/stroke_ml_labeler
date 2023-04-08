import matplotlib.pyplot as plt
import pandas as pd
from csv import writer


def show(x_in, data_in):
    graph_start = int((int(x_in / 1000)) * 1000)
    num_of_points_big = 1150
    num_of_points_around = 40
    num_of_points_small = 10
    start = x_in

    # x axis values
    x = data_in.loc[:, "Time(ms)"]
    # corresponding y axis values
    acc_x = data_in.loc[:, "AccX"]
    acc_y = data_in.loc[:, "AccY"]
    acc_z = data_in.loc[:, "AccZ"]
    fsr = data_in.loc[:, "ADC"]

    plt.clf()
    plt.subplots_adjust(hspace=0.25)

    plt.subplot(4, 1, 1)
    plt.plot(x[graph_start:graph_start + num_of_points_big], acc_x[graph_start:graph_start + num_of_points_big], label="AccX")
    plt.axvspan(x[start - num_of_points_around], x[start + num_of_points_around + num_of_points_small], color='blue', alpha=0.1)
    plt.axvspan(x[start], x[start + num_of_points_small], color='red', alpha=0.5)
    plt.legend()
    plt.title("Accelerometer X 1000 points            || (c)catch - (v)nothing - (x)exit || ")

    plt.subplot(4, 1, 2)
    plt.plot(x[graph_start:graph_start + num_of_points_big], fsr[graph_start:graph_start + num_of_points_big], label="FSR")
    plt.axvspan(x[start - num_of_points_around], x[start + num_of_points_around + num_of_points_small], color='blue', alpha=0.1)
    plt.axvspan(x[start], x[start + num_of_points_small], color='red', alpha=0.5)
    plt.legend()
    plt.title("FSR 1000 points")

    # plotting the points
    plt.subplot(4, 2, 5)
    plt.plot(x[start - num_of_points_around:start + num_of_points_around + num_of_points_small],
             acc_x[start - num_of_points_around:start + num_of_points_around + num_of_points_small], label="AccX")
    plt.plot(x[start - num_of_points_around:start + num_of_points_around + num_of_points_small],
             acc_y[start - num_of_points_around:start + num_of_points_around + num_of_points_small], label="AccY")
    plt.plot(x[start - num_of_points_around:start + num_of_points_around + num_of_points_small],
             acc_z[start - num_of_points_around:start + num_of_points_around + num_of_points_small], label="AccZ")
    plt.axvspan(x[start], x[start + num_of_points_small], color='red', alpha=0.5)
    plt.legend()
    plt.title("Accelerometer Raw 100 points Subset")

    plt.subplot(4, 2, 7)
    plt.plot(x[start: start + num_of_points_small], acc_x[start: start + num_of_points_small], label="AccX")
    plt.plot(x[start: start + num_of_points_small], acc_y[start: start + num_of_points_small], label="AccY")
    plt.plot(x[start: start + num_of_points_small], acc_z[start: start + num_of_points_small], label="AccZ")
    plt.legend()
    plt.title("Accelerometer Raw 10 points Subsubset")

    plt.subplot(4, 2, 6)
    plt.plot(x[start - num_of_points_around:start + num_of_points_around + num_of_points_small],
             fsr[start - num_of_points_around:start + num_of_points_around + num_of_points_small], label="FSR")
    plt.axvspan(x[start], x[start + num_of_points_small], color='red', alpha=0.5)
    plt.legend()
    plt.title("FSR Raw 100 points Subset")

    plt.subplot(4, 2, 8)
    plt.plot(x[start: start + num_of_points_small], fsr[start: start + num_of_points_small], label="FSR")
    plt.legend()
    plt.title("FSR Raw 10 points Subsubset")

    plt.draw()
    plt.tight_layout()


data = pd.read_csv("data/mar24_2023_normal.csv")
# print(data.to_string())

plt.figure(figsize=(20, 12))
plt.show(block=False)

while True:
    point = int(input('Show data point:'))
    if point < 50:
        print("Choose another point greater than 50.")
    elif point >= len(data) - 50:
        print("Choose another point less than " + str(len(data) - 50) + ".")
    else:
        while True:
            show(point, data)
            choice = input('(c)atch, (v)nothing, z(skip 10) (q)uit:')

            if choice == "q":
                exit()
            elif choice == "c":
                with open('output.csv', 'a', newline='') as f_object:

                    # Pass this file object to csv.writer()
                    # and get a writer object
                    writer_object = writer(f_object)

                    # Pass the list as an argument into
                    # the writerow()
                    acc_x = list(data.loc[point: point + 9, "AccX"])
                    acc_y = list(data.loc[point: point + 9, "AccY"])
                    acc_z = list(data.loc[point: point + 9, "AccZ"])
                    fsr = list(data.loc[point: point + 9, "ADC"])
                    gyro_x = list(data.loc[point: point + 9, "GyroX"])
                    gyro_y = list(data.loc[point: point + 9, "GyroY"])
                    gyro_z = list(data.loc[point: point + 9, "GyroZ"])

                    writer_object.writerow([1] + acc_x+acc_y+acc_z+gyro_x+gyro_y+gyro_z+fsr)

                    # Close the file object
                    f_object.close()
            elif choice == "z":
                point = point + 9
            elif choice == "v":
                with open('output.csv', 'a', newline='') as f_object:

                    # Pass this file object to csv.writer()
                    # and get a writer object
                    writer_object = writer(f_object)

                    # Pass the list as an argument into
                    # the writerow()
                    acc_x = list(data.loc[point: point + 9, "AccX"])
                    acc_y = list(data.loc[point: point + 9, "AccY"])
                    acc_z = list(data.loc[point: point + 9, "AccZ"])
                    fsr = list(data.loc[point: point + 9, "ADC"])
                    gyro_x = list(data.loc[point: point + 9, "GyroX"])
                    gyro_y = list(data.loc[point: point + 9, "GyroY"])
                    gyro_z = list(data.loc[point: point + 9, "GyroZ"])

                    writer_object.writerow([0] + acc_x+acc_y+acc_z+gyro_x+gyro_y+gyro_z+fsr)

                    # Close the file object
                    f_object.close()

            point = point + 1


