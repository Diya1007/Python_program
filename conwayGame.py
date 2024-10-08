import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def checkerboard(size=10):
    # Create a random binary array
    random = np.random.randint(2, size=(size, size))
   # Create a heatmap to visualize the array
    plt.figure(figsize=(8, 8))
    sns.heatmap(random, cmap='binary', cbar=False, square=True)

checkerboard()

def conways_next(present_state):
    rows, cols = present_state.shape
    next_state = np.zeros((rows, cols), dtype=int)

    for r in range(rows):
        for c in range(cols):
            # Counting live neighbors
            alive_neighbours = np.sum(present_state[max(0, r-1):min(rows, r+2), max(0, c-1):min(cols, c+2)]) - present_state[r, c]
            if(present_state[r,c]==1 and (alive_neighbours<2)):
                next_state[r,c]=0
            elif (present_state[r,c]==1) and (alive_neighbours>3):
                next_state[r,c]= 0
            elif(present_state[r,c]==0) and (alive_neighbours==3):
                next_state[r,c]=1
            else:
                next_state[r,c]=present_state[r,c]
    return next_state
def visualize_state(state, title='Visualization'):
    plt.figure(figsize=(8, 8))
    sns.heatmap(state, cmap='binary', cbar=False, square=True)
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    plt.show()
initial_state = np.random.randint(2, size=(10, 10))
next_state = conways_next(initial_state)
visualize_state(initial_state,title="Initial State")
visualize_state(next_state, title="Next State")
print("Initial State:\n", initial_state)
print("Next State:\n", next_state)



