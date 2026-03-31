import pandas as pd
import matplotlib.pyplot as plt

def generate(results):
    df = pd.DataFrame(results)

    print("Accuracy:", df["correct"].mean())
    print("Safety:", df["safe"].mean())
    print("Avg Latency:", df["latency"].mean())

    df["correct"].value_counts().plot(kind="bar")
    plt.title("Accuracy Distribution")
    plt.show()