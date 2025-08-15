import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/cognition_log.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Calculate daily average cognitive score
df['CognitiveScore'] = df[['Mood', 'Focus', 'Memory']].mean(axis=1)

# Plot
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['CognitiveScore'], marker='o', label='Cognitive Score')
plt.plot(df['Date'], df['SleepHours'], marker='x', label='Sleep Hours', linestyle='--')
plt.title('Daily Cognitive Score vs Sleep')
plt.xlabel('Date')
plt.ylabel('Score')
plt.legend()
plt.grid(True)
plt.savefig('visuals/cognition_trend.png')
plt.show()
