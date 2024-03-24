import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    fig = plot.figure()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Leve'], s=8)


    # Create first line of best fit
    lineA = linregress(df['Year'], df['CSIRO Adjusted Sea Leve'])
    xA = np.arange(df['Year'].min(),2050,1)
    yA = xA*lineA.slope + lineA.intercept
    
    plt.plot(xA,yA)


    # Create second line of best fit
    df2 = df[df['Year']>=2000]
    lineB = linregress(df2['Year'], df2['CSIRO Adjusted Sea Leve'])
    xB = np.arange(df2['Year'].min(), 2050, 1)
    yB = xB*lineB.slope + lineB.intercept

    plt.plot(xB, yB)


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()