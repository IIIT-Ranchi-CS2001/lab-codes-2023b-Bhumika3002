'''Check if the file `election_data.csv` exists in the directory. If not, create the file and write the election data into it. Handle file-related exceptions gracefully.
Read the data into a Pandas DataFrame and calculate the percentage of seats won by each party. Add this as a new column named Seats_Percentage.
Determine the party with the highest number of seats in each state and display their names.
Create a bar chart showing the number of seats won by each party in each state using Matplotlib or Seaborn.
Ensure your script includes exception handling for file reading, writing, and any potential calculation errors.
'''
import pandas as pd
import matplotlib.pyplot as plt

election_data = [
    ["Madhya Pradesh", "BJP", 163, 230, 72.1],
    ["Madhya Pradesh", "INC", 66, 230, 72.1],
    ["Madhya Pradesh", "BSP", 0, 230, 72.1],
    ["Madhya Pradesh", "Others", 1, 230, 72.1],
    ["Rajasthan", "BJP", 115, 200, 74.2],
    ["Rajasthan", "INC", 69, 200, 74.2],
    ["Rajasthan", "BSP", 2, 200, 74.2],
    ["Rajasthan", "Others", 13, 200, 74.2]
]

columns = ['State', 'Party', 'Seats_Won', 'Total_Seats', 'Voter_Turnout']

file_path = 'election_data.csv'

try:
    df = pd.DataFrame(election_data, columns=columns)
    df.to_csv(file_path, index=False)
    print(f"Data written to '{file_path}' successfully.")
except Exception as e:
    print(f"Error writing to the file: {e}")

try:
    df = pd.read_csv(file_path)
    print("\nData read successfully into DataFrame:")
    print(df)
except Exception as e:
    print(f"Error reading the file: {e}")

try:
    df['Seats_Percentage'] = (df['Seats_Won'] / df['Total_Seats']) * 100
    print("\nData with Seats_Percentage:")
    print(df)
except Exception as e:
    print(f"Error calculating Seats_Percentage: {e}")

try:
    highest_seats = df.loc[df.groupby('State')['Seats_Won'].idxmax()]
    print("\nParty with the highest number of seats in each state:")
    print(highest_seats[['State', 'Party', 'Seats_Won']])
except Exception as e:
    print(f"Error determining party with highest seats: {e}")

try:
    plt.figure(figsize=(10, 6))

    for state in df['State'].unique():
        state_data = df[df['State'] == state]
        plt.bar(state_data['Party'] + ' (' + state_data['State'] + ')', state_data['Seats_Won'], label=state)

    plt.title('Number of Seats Won by Each Party in Each State')
    plt.ylabel('Seats Won')
    plt.xlabel('Party and State')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend(title='State')
    plt.show()
except Exception as e:
    print(f"Error creating bar chart: {e}")
