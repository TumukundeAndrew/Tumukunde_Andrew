import numpy as np
import random

# Define constants
GRID_HEIGHT = 5
GRID_WIDTH = 5
ACTIONS = ['left', 'right', 'forward']
ACTION_TO_INDEX = {a: i for i, a in enumerate(ACTIONS)}
EPSILON = 0.1  # Exploration rate
ALPHA = 0.1    # Learning rate
GAMMA = 0.9    # Discount factor

# Initialize Q-table
Q_table = np.zeros((GRID_HEIGHT, GRID_WIDTH, len(ACTIONS)))

# Function to randomly place cars (obstacles)
def get_random_cars(row):
    car_positions = np.zeros(GRID_WIDTH)
    car_pos = np.random.choice(GRID_WIDTH, size=2, replace=False)
    for pos in car_pos:
        car_positions[pos] = 1
    return car_positions

# Define the environment step
def step(state, action, road):
    row, col = state
    if action == 'left':
        col = max(0, col - 1)
    elif action == 'right':
        col = min(GRID_WIDTH - 1, col + 1)
    elif action == 'forward':
        row = max(0, row - 1)
    reward = 0
    done = False
    if row == 0:
        reward = 10
        done = True
    elif road[row][col] == 1:
        reward = -10
        done = True
    else:
        reward = -0.1
    return (row, col), reward, done

# Train the agent using Q-Learning
episodes = 1000
for episode in range(episodes):
    state = (GRID_HEIGHT - 1, np.random.randint(0, GRID_WIDTH))
    road = [get_random_cars(r) if r != GRID_HEIGHT - 1 else np.zeros(GRID_WIDTH) for r in range(GRID_HEIGHT)]
    done = False
    while not done:
        row, col = state
        if random.uniform(0, 1) < EPSILON:
            action = random.choice(ACTIONS)
        else:
            action = ACTIONS[np.argmax(Q_table[row, col])]
        next_state, reward, done = step(state, action, road)
        next_row, next_col = next_state
        best_next_q = np.max(Q_table[next_row, next_col])
        Q_table[row, col, ACTION_TO_INDEX[action]] += ALPHA * (reward + GAMMA * best_next_q - Q_table[row, col, ACTION_TO_INDEX[action]])
        state = next_state

# Evaluate the trained agent
def evaluate_agent():
    state = (GRID_HEIGHT - 1, 2)
    road = [get_random_cars(r) if r != GRID_HEIGHT - 1 else np.zeros(GRID_WIDTH) for r in range(GRID_HEIGHT)]
    path = [state]
    done = False
    while not done:
        row, col = state
        action = ACTIONS[np.argmax(Q_table[row, col])]
        state, _, done = step(state, action, road)
        path.append(state)
    return path

# Run evaluation and print the path taken
path = evaluate_agent()
print("Agent path:", path)
