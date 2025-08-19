import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def identify_numerical_cols(df, exclude_cols=['ID']):
    """Identify numerical columns, excluding specified columns."""
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    numerical_cols = [col for col in numerical_cols if col not in exclude_cols]
    print("Numerical columns:", numerical_cols)
    return numerical_cols

def calculate_correlation(df, cols):
    """Calculate and display correlation matrix for specified columns."""
    corr_matrix = df[cols].corr()
    display(corr_matrix)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix of Environmental Factors")
    plt.show()
    return corr_matrix

def detect_outliers_iqr(df, cols):
    """Detect and visualize outliers using the IQR method."""
    outliers = {}
    for col in cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        col_outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        outliers[col] = col_outliers
        print(f"Outliers for column '{col}':")
        if not col_outliers.empty:
            display(col_outliers)
        else:
            print("No outliers detected based on IQR method.")

        # Visualize outliers
        if not col_outliers.empty:
            plt.figure(figsize=(8, 6))
            sns.boxplot(y=df[col])
            plt.title(f"Box Plot of {col} (with outliers)")
            plt.ylabel(col)
            plt.show()

            plt.figure(figsize=(12, 6))
            plt.scatter(df['Datetime'], df[col], label='All Data', alpha=0.5)
            plt.scatter(col_outliers['Datetime'], col_outliers[col], color='red', label='Outliers')
            plt.title(f"Scatter Plot of {col} over Time (with outliers)")
            plt.xlabel("Datetime")
            plt.ylabel(col)
            plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()
            plt.show()
    return outliers

def visualize_sensor_trends(df, cols, datetime_col='Datetime'):
    """Generate line plots for each sensor column over time."""
    for col in cols:
        plt.figure(figsize=(12, 6))
        sns.lineplot(x=datetime_col, y=col, data=df)
        plt.title(f'Sensor Reading Over Time: {col}')
        plt.xlabel('Datetime')
        plt.ylabel(col)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def plot_all_sensors(df, cols, datetime_col='Datetime'):
    """Plot all sensor readings on the same graph for comparison."""
    fig, ax = plt.subplots(figsize=(14, 8))
    for col in cols:
        ax.plot(df[datetime_col], df[col], label=col)
    ax.set_title('Sensor Readings Over Time')
    ax.set_xlabel('Datetime')
    ax.set_ylabel('Sensor Reading')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def display_comparative_stats(df, cols):
    """Display descriptive statistics for sensor columns."""
    stats = df[cols].describe()
    display(stats)
    return stats

def analyze_trends_and_correlations(df, cols, corr_matrix):
    """Summarize trends and correlations based on visualizations and statistics."""
    print("\nAnalysis of Sensor Reading Trends and Relationships:")
    print("\nOverall Trends:")
    print("- Temperature shows a general upward trend over the observed period.")
    print("- Humidity shows a general downward trend, inversely related to temperature.")
    print("- Pressure remains relatively stable with one significant spike.")
    print("- Co2 Gas, PM2.5, and PM10 show more volatile patterns with notable spikes, particularly towards the end of the period for PM2.5 and PM10.")
    print("\nRelationships and Correlations:")
    print(f"- The strong negative correlation between Temperature and Humidity is visually evident in the line plot (r = {corr_matrix.loc['Temperature', 'Humidity']:.2f}).")
    print(f"- The very strong positive correlation between PM2.5 and PM10 is also clearly visible, with their lines closely mirroring each other (r = {corr_matrix.loc['PM2.5', 'PM10']:.2f}).")
    print(f"- Co2 Gas shows some positive correlation with PM2.5 and PM10 during certain periods of spikes, but the relationship is not as consistent (r = {corr_matrix.loc['Co2 Gas', 'PM2.5']:.2f}).")
    print("- Pressure does not appear to have strong visual correlations with other sensor readings.")
    print("\nVariability:")
    print("- Based on the standard deviations from the comparative statistics, PM2.5 and PM10 exhibit the highest variability, followed by Co2 Gas.")
    print("- Temperature and Humidity show moderate variability, while Pressure is the most stable.")
    print("\nSignificant Spikes/Anomalies:")
    print("- A distinct spike in Pressure is observed around the middle of the timeframe.")
    print("- Significant spikes in Co2 Gas are noticeable in the earlier part of the timeframe.")
    print("- Both PM2.5 and PM10 show substantial spikes and fluctuations towards the end of the observed period, occurring concurrently.")
    print("\nPotential Explanations:")
    print("- The inverse relationship between Temperature and Humidity is a common meteorological phenomenon.")
    print("- The strong correlation between PM2.5 and PM10 suggests they are likely influenced by the same sources of particulate matter.")
    print("- Spikes in Co2 Gas, PM2.5, and PM10 could be related to specific events such as increased human activity, changes in ventilation, or external environmental factors.")
    print("- The spike in Pressure could be an isolated sensor anomaly or related to a localized atmospheric event.")

if __name__ == "__main__":
    pass
