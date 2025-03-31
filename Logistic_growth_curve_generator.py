
import numpy as np
import matplotlib.pyplot as plt

def logistic_growth():

    print("Welcome to a logistic growth curve generator!")

    population = input("Enter your respective population. e.g [20000, 30000, 5000000]")
    pop_values = np.array([float(p.strip()) for p in population.split(',') ])
    
    time = input("Enter the corresponding time in days e.g [1, 3, 5,7]")
    time_series = np.array([float(t.strip()) for t in time.split(',')])

    if len(time_series) != len(pop_values):
        raise ValueError("Please ensure that the number of values for both your population and time are equal")

    carrying_capacity = float(input("Please enter the carrying capacity of your environment e.g 100000")) 
    growth_rate = float(input("Please enter the growth rate of your plasmodium population, e.g if growth rate is 20%, enter 0.2"))

    smooth_time = np.linespace(min(time_series), max(time_series), 20)
    p0 = pop_values[0]

    smooth_population = carrying_capacity / (1 + ((carrying_capacity - p0)/p0) * np.exp(- growth_rate * smooth_time))

    plt.figure(figsize = (10,6))
    plt.plot(smooth_time, smooth_population, "y-", label = 'Input your data points')
    plt.scatter(time_series, pop_values, 'green', 'Data points')
    plt.xlabel('Time')
    plt.ylabel('Population size')
    plt.title('Logistical growth curve')
    plt.legend()
    plt.grid(True)
    plt.show()

    if __name__ == "__main__":
        logistic_growth()

