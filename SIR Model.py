#
# An agent-based model of spread of infectious diseases
# Uses the SIR model framework
# See pdf "Agent-based models of spread of infectious diseases using Python" for more details
#



### Needed libraries ###

# For assigning agents to random locations and for choosing random agents
import random as rd

# For visualizing the state of the agents using plot
import matplotlib.pyplot as plt

# For checking if a filename already exists, to avoid overwriting files
import os



### Initialize class to create people ###

class agent:
    pass



### Create population ###

def create_agents():
    
    # Allow the following variable to be accessed outside the function
    global agents_list
    
    # Initialize list of agents
    agents_list = []
    
    # Create specified number of agents
    for i in range(n_agents):
        
        # Create an agent
        agent_ = agent()
               
        # Assign the agent to a random location
        agent_.x, agent_.y = rd.uniform(0, 1), rd.uniform(0, 1)
        
        # Set the agent to be initially susceptible
        # 0 = susceptible, 1 = infectious, 2 = recovered
        agent_.state = 0
        
        # Count number of days the agent is infectious
        agent_.days_infectious = 0
        
        # Add the agent to the list
        agents_list.append(agent_)



### Everyone moves to a random location ###

## Scenario 1: Normal day

## Comment scenario not used        
# def move():

#     # Agent moves to a random location
#     for agent_ in agents_list:
#         agent_.x, agent_.y = rd.uniform(0, 1), rd.uniform(0, 1)

## Scenario 2: Somewhat limited social contact for infectious people

def move():

    # Infectious people do not move
    for agent_ in agents_list:
        if agent_.state != 1:
            agent_.x, agent_.y = rd.uniform(0, 1), rd.uniform(0, 1)



### Infection happens within a radius (for non-recovered people) ###

def infect():
    
    # Allow the following variable to be accessed outside the function
    global infectious_list

    # Create list of infectious people
    infectious_list = [agent_ for agent_ in agents_list if agent_.state == 1]

    # Create list of neighbors of infectious
    for agent_ in infectious_list:
        
        # Create list of neighbors within the radius specified
        neighbors = [neighbor for neighbor in agents_list if (neighbor.x - agent_.x)**2 + (neighbor.y - agent_.y)**2 <= infectious_radius**2]
        
        # Remove person himself from list of neighbors
        neighbors.remove(agent_)

        # Susceptible neighbors become infectious (recovered individuals are immune)
        for agent_ in neighbors:
            if agent_.state == 0:
                agent_.state = 1



### Monitor progress of infectious people at the start of the day ###

def monitor():

    # Add count for number of days an infectious person has been infectious
    for agent_ in agents_list:
        if agent_.state == 1:
            agent_.days_infectious += 1

            # Infectious people who reach the end of infectious period recover
            if agent_.days_infectious > days_to_recover:
                agent_.state = 2



### Count members of each compartment ###

def count():
    
    # Allow the following variables to be accessed outside the function
    global S_count, I_count, R_count
    
    # Count susceptible
    S_count = len([agent_ for agent_ in agents_list if agent_.state == 0])
    
    # Count infectious
    I_count = len([agent_ for agent_ in agents_list if agent_.state == 1])
    
    # Count recovered
    R_count = len([agent_ for agent_ in agents_list if agent_.state == 2])



### Visualize population ###

def visualize():
    
    # To ensure updated count of compartments
    count()
    
    # Initialize subplots
    fig, ax = plt.subplots()
    
    # Assign color per compartment
    agent_color = {0: 'b', 1: 'r', 2: 'g'}
    
    # Plot each person with his corresponding color
    for agent_ in agents_list:
        ax.plot(agent_.x, agent_.y, '.', color = agent_color[agent_.state])
    
    # Dummy plots for legend
    ax.plot([], [], 'bo', label = 'Susceptible: '+ str(S_count))
    ax.plot([], [], 'ro', label = 'Infectious: '+ str(I_count))
    ax.plot([], [], 'go', label = 'Recovered: '+ str(R_count))
    
    # Place legend below the figure
    ax.legend(ncol = 3, loc = 'upper center', bbox_to_anchor = (0.5, -0.01))

    # Fix the window: choose largest range for random location choices
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    
    # Title
    ax.set_title('Day: ' + str(day_count), loc = 'left')
       
    # Remove extra tick marks on the axes
    ax.set_xticks([])
    ax.set_yticks([])

    # Prepare format of file name
    filename = 'SIR'
    
    # Starting filename count
    i = 1
    
    # Check if filename already exists; add 1 if it does
    while os.path.exists('{}{:d}.png'.format(filename, i)):
        i += 1
	
    # Save figure
    plt.savefig('{}{:d}.png'.format(filename, i), bbox_inches = 'tight', dpi = 300)



### Graph trend of compartments ###

def trend():
    
    # To ensure updated count of compartments
    count()
    
    # Initialize subplots
    fig, ax = plt.subplots()
    
    # Plot daily count of each compartment
    ax.plot(days, S_list, color = 'blue', label = 'Susceptible')
    ax.plot(days, I_list, color = 'red', label = 'Infectious')
    ax.plot(days, R_list, color = 'green', label = 'Recovered')
    
    # Place legend on top of the figure
    ax.legend(ncol = 3, loc = 'upper center', bbox_to_anchor = (0.5, 1.15))
    
    # Set the axes to meet at (0, 0)
    ax.set_xlim(left = 0)
    ax.set_ylim(bottom = 0)
    
    # Horizontal axis label
    ax.set_xlabel('Days')

    # Prepare format of file name
    filename = 'SIR_Trend'
    
    # Starting filename count
    i = 1
    
    # Check if filename already exists; add 1 if it does
    while os.path.exists('{}{:d}.png'.format(filename, i)):
        i += 1
	
    # Save figure
    plt.savefig('{}{:d}.png'.format(filename, i), bbox_inches = 'tight', dpi = 300)


### Simulation ###

# Comment all visualize() for faster simulation
# But replace with count()

## Day 0

# Start day count
day_count = 0

# Initial values
S_initial = 1000
I_initial = 1
R_initial = 0

# Initial total population
n_agents = S_initial + I_initial + R_initial

# Infectious radius
infectious_radius = 0.025

# Number of days of infectiousness
days_to_recover = 7

# Initialize list of days
days = []
days.append(0)

# Initialize daily count of susceptible
S_list = []
S_list.append(S_initial)

# Initialize daily count of infectious
I_list = []
I_list.append(I_initial)

# Initialize daily count of recovered
R_list = []
R_list.append(R_initial)

# Create the population
create_agents()

# Choose a specified number of random people and make them infectious
for agent_ in rd.sample(agents_list, I_initial):
    agent_.state = 1 

# From the remaining susceptible, choose a specified number of random people and make them recovered
for agent_ in rd.sample([agent_ for agent_ in agents_list if agent_.state != 1], R_initial):
    agent_.state = 2

visualize()
# count()


## Day 1 onward

# Number of runs
runs = 100

for i in range(runs):

    # Add day count
    day_count += 1
    
    # Monitor infectiousness and recovery at the start of the day
    monitor()
    
    # Let everyone move
    move()
    
    # Visualize new positions
    visualize()
    # count()
    
    # Infections start after the movement
    infect()
    
    # Visualize
    visualize()
    # count()

    # Update lists
    days.append(day_count)
    S_list.append(S_count)
    I_list.append(I_count)
    R_list.append(R_count)

    # Stop simulation once number of infectious becomes 0
    if I_count == 0:
        break

# Plot trend
trend()

####### end of code #######

    
    
    
    
    
    