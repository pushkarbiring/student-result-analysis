import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(filename):
    """Loads student data from a CSV file."""
    if not os.path.exists(filename):
        print(f"Error: {filename} not found. Please check the file path.")
        return None
    
    print(f"Loading data from {filename}...\n")
    df = pd.read_csv(filename)
    return df

def calculate_basic_stats(df):
    """Calculates total scores, percentages, and pass/fail status."""
    # List of subjects
    subjects = ['Math_Score', 'Science_Score', 'English_Score', 'Coding_Score']
    
    # Calculate Total and Percentage
    df['Total_Score'] = df[subjects].sum(axis=1)
    df['Percentage'] = (df['Total_Score'] / 400) * 100
    
    # Determine Pass/Fail (Assuming 40% is the passing mark overall)
    # Using a simple lambda function which looks good for student projects
    df['Status'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
    
    return df

def display_summary(df):
    """Prints a statistical summary to the console."""
    print("--- Class Performance Summary ---")
    print(f"Total Students: {len(df)}")
    print(f"Class Average Percentage: {df['Percentage'].mean():.2f}%")
    print(f"Highest Percentage: {df['Percentage'].max():.2f}% (Student: {df.loc[df['Percentage'].idxmax(), 'Name']})")
    print(f"Lowest Percentage: {df['Percentage'].min():.2f}%")
    
    pass_count = len(df[df['Status'] == 'Pass'])
    fail_count = len(df[df['Status'] == 'Fail'])
    print(f"Passed: {pass_count} | Failed: {fail_count}\n")

def plot_subject_averages(df):
    """Generates a bar chart showing the average score for each subject."""
    subjects = ['Math_Score', 'Science_Score', 'English_Score', 'Coding_Score']
    averages = df[subjects].mean()
    
    plt.figure(figsize=(8, 5))
    # Using a standard color list rather than complex colormaps
    colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B2'] 
    
    averages.plot(kind='bar', color=colors, edgecolor='black')
    
    plt.title('Average Scores by Subject')
    plt.xlabel('Subjects')
    plt.ylabel('Average Score')
    plt.xticks(rotation=0) # Keep labels straight
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Save the plot before showing it
    plt.savefig('subject_averages.png')
    print("Saved bar chart as 'subject_averages.png'")
    plt.show()

def plot_pass_fail_ratio(df):
    """Generates a pie chart for the pass/fail ratio."""
    status_counts = df['Status'].value_counts()
    
    plt.figure(figsize=(6, 6))
    plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', 
            colors=['#66b3ff', '#ff9999'], startangle=90, explode=(0.05, 0))
    
    plt.title('Pass vs Fail Ratio')
    plt.savefig('pass_fail_ratio.png')
    print("Saved pie chart as 'pass_fail_ratio.png'")
    plt.show()

def main():
    # 1. Setup
    filename = 'student_scores.csv'
    
    # 2. Load and process
    df = load_data(filename)
    if df is None:
        return
        
    df = calculate_basic_stats(df)
    
    # 3. Output results
    display_summary(df)
    
    # Show the first few rows just to verify data processing worked
    print("Processed Data Preview:")
    print(df[['Name', 'Total_Score', 'Percentage', 'Status']].head())
    print("\nGenerating visualizations...")
    
    # 4. Visualizations
    plot_subject_averages(df)
    plot_pass_fail_ratio(df)
    
    print("Analysis complete.")

if __name__ == "__main__":
    main()