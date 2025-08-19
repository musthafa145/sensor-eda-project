import pandas as pd
from load_data import load_dataset, display_basic_info, convert_datetime, display_unique_value_info
from eda import identify_numerical_cols, calculate_correlation, detect_outliers_iqr, visualize_sensor_trends, plot_all_sensors, display_comparative_stats, analyze_trends_and_correlations

def main():
    # Step 1: Load and inspect data
    filepath = '/content/dataset.csv'
    df = load_dataset(filepath)
    print("\n--- Basic Dataset Information ---")
    display_basic_info(df)

    # Step 2: Convert Datetime and check uniqueness
    df = convert_datetime(df)
    print("\n--- Data Types After Conversion ---")
    display(df.dtypes)
    print("\n--- Uniqueness Check ---")
    display_unique_value_info(df)

    # Step 3: EDA - Identify numerical columns
    print("\n--- Numerical Columns ---")
    numerical_cols = identify_numerical_cols(df)
    selected_cols = ['Temperature', 'Humidity', 'Pressure', 'Co2 Gas', 'PM2.5', 'PM10']

    # Step 4: Correlation analysis
    print("\n--- Correlation Analysis ---")
    corr_matrix = calculate_correlation(df, selected_cols)

    # Step 5: Basic statistics
    print("\n--- Descriptive Statistics ---")
    display_comparative_stats(df, selected_cols)

    # Step 6: Outlier detection and visualization
    print("\n--- Outlier Detection ---")
    outliers = detect_outliers_iqr(df, selected_cols)

    # Step 7: Visualize sensor trends
    print("\n--- Sensor Trends Over Time ---")
    visualize_sensor_trends(df, selected_cols)

    # Step 8: Compare all sensors on one plot
    print("\n--- All Sensor Readings on One Plot ---")
    plot_all_sensors(df, selected_cols)

    # Step 9: Summarize findings
    print("\n--- Summary of Trends and Relationships ---")
    analyze_trends_and_correlations(df, selected_cols, corr_matrix)

if __name__ == "__main__":
    main()
