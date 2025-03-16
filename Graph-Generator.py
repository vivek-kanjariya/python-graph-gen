import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
def load_data(filename):
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(filename)
        print("\n✅ Data loaded successfully!\n")
        return df
    except Exception as e:
        print(f"\n❌ Error loading data: {e}\n")
        return None

# Function to plot different types of graphs
def plot_graph(df, x_column, y_column, graph_type):
    """Plot various types of graphs based on user input."""
    if x_column not in df.columns or y_column not in df.columns:
        print("\n⚠️ Please enter valid column names for both X and Y axes!\n")
        # return
    
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    palette = sns.color_palette("coolwarm", as_cmap=True)
    
    if graph_type == "bar":
        ax = sns.barplot(x=df[x_column], y=df[y_column], palette="Blues")
        plt.title(f"📊 Bar Chart: {y_column} vs {x_column}", fontsize=14)
        for p in ax.patches:
            ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', fontsize=10, color='black', xytext=(0, 5), textcoords='offset points')
    
    elif graph_type == "line":
        sns.lineplot(x=df[x_column], y=df[y_column], marker='o', color='green')
        plt.axhline(df[y_column].mean(), color='red', linestyle='dashed', label='Mean')
        plt.title(f"📈 Line Chart: {y_column} vs {x_column}", fontsize=14)
        plt.legend()
    
    elif graph_type == "scatter":
        sns.scatterplot(x=df[x_column], y=df[y_column], color='red')
        plt.title(f"🔴 Scatter Plot: {y_column} vs {x_column}", fontsize=14)
    
    elif graph_type == "stackplot":
        plt.stackplot(df[x_column], df[y_column], labels=[y_column], colors=["skyblue"])
        plt.title(f"📊 Stackplot: {y_column} vs {x_column}", fontsize=14)
        plt.legend()

    elif graph_type == "plot":
        plt.plot(df[x_column], df[y_column], color="blue")
        plt.axhline(df[y_column].median(), color='purple', linestyle='dashed', label='Median')
        plt.title(f"📉 Plot: {y_column} vs {x_column}", fontsize=14)
        plt.legend()
    
    elif graph_type == "stairs":
        plt.stairs(df[x_column], color="purple")
        plt.title(f"📊 Stairs Chart:{x_column}", fontsize=14)
    
    else:
        print("\n⚠️ Invalid graph type! Choose from: bar, line, scatter, stackplot, plot, stairs.\n")
        return
    
    plt.xlabel(x_column, fontsize=12)
    plt.ylabel(y_column, fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Provide the CSV file name
    filename = "final_OTD_time_forecasting_dataframe.csv"  # Change to your actual file
    df = load_data(filename)
    
    if df is not None:
        print("\n📌 Available columns:", df.columns.tolist(), "\n")
        x_column = input("📝 Enter the column name for X-axis: ")
        y_column = input("📝 Enter the column name for Y-axis: ")
        graph_type = input("📊 Enter graph type (bar/line/scatter/stackplot/plot/stairs): ")
        plot_graph(df, x_column, y_column, graph_type)
    else:
        print("\n❌ Data loading failed. Please check the file path.\n")
