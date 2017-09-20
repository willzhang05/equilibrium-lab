#!/usr/bin/python3
# William Zhang and Mattia Shin
# Period 6
import sys
import math
import matplotlib.pyplot as plt

R1 = 2.75
R2 = 2.0
RC = 8.5


def run(a, b):
    V1 = a  # initial volumes in each cylinder
    V2 = b
    H1 = V1 / (math.pi * math.pow(RC, 2))  # water height
    H2 = V2 / (math.pi * math.pow(RC, 2))
    Vs1 = math.pi * math.pow(R1, 2) * H1
    Vs2 = math.pi * math.pow(R2, 2) * H2
    cylinders = []
    straws = []
    iterations = []
    ratio = (math.pow(R1, 2) * V1) / (math.pow(R2, 2) * V2)  # ratio
    i = 0
    while abs(1 - ratio) > 0.01:
        iterations.append(i)
        cylinders.append((V1, V2))
        straws.append((Vs1, Vs2))
        H1 = V1 / (math.pi * math.pow(RC, 2))  # water height
        H2 = V2 / (math.pi * math.pow(RC, 2))
        Vs1 = math.pi * math.pow(R1, 2) * H1
        Vs2 = math.pi * math.pow(R2, 2) * H2
        V1 = V1 - Vs1 + Vs2
        V2 = V2 - Vs2 + Vs1
        ratio = (math.pow(R1, 2) * V1) / (math.pow(R2, 2) * V2)  # ratio
        i += 1
    iterations.append(i)
    cylinders.append((V1, V2))
    straws.append((Vs1, Vs2))
    fig0, ax0 = plt.subplots(nrows=1, ncols=1)
    fig1, ax1 = plt.subplots(nrows=1, ncols=1)
    fig0.set_size_inches(16, 9)
    fig1.set_size_inches(16, 9)
    ax0.set_ylabel('Volume (mL)')
    ax0.set_xlabel('Iterations')
    ax1.set_ylabel('Volume (mL)')
    ax1.set_xlabel('Iterations')
    #plt.ylim([0, max([a, b])])
    ax0.plot(iterations, cylinders)
    fig0.savefig('./cyl.png')
    ax1.plot(iterations, straws)
    fig1.savefig('./straws.png')
    plt.close(fig0)
    plt.close(fig1)


def main():
    if len(sys.argv) == 3:
        run(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print("Please supply initial volumes for A and B.")


if __name__ == "__main__":
    main()

