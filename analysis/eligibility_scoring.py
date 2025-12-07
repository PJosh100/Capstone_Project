import pandas as pd
import os

# Path to your CSV file
file_path = r"C:\project\Capstone_Project\analysis\sample_data.csv"
output_file = r"C:\project\Capstone_Project\analysis\eligibility_result.csv"

# Read CSV
df = pd.read_csv(file_path)

# ---------- Scoring Functions ----------

def academic_score(row):
    gpa_scale = row['grading_system']
    gpa_normalized = (row['cgpa'] / gpa_scale) * 100
    academic_component = gpa_normalized * 0.7

    if row['courses_passed'] > 10:
        academic_component += 3

    penalty = (row['courses_failed'] // 2) * 1
    academic_component -= penalty

    academic_component = max(0, min(academic_component, 70))
    return academic_component


def financial_score(row):
    income = row['income']

    if income < 300_000:
        income_points = 8
    elif 300_000 <= income <= 600_000:
        income_points = 5
    elif 600_001 <= income <= 1_000_000:
        income_points = 3
    elif 1_000_001 <= income <= 2_000_000:
        income_points = 1
    else:
        income_points = 0

    orphan_points = 5 if row['is_orphan'] == 1 else 0

    dependents = row['dependents']
    if dependents > 4:
        dep_points = 5
    elif 3 <= dependents <= 4:
        dep_points = 3
    elif 1 <= dependents <= 2:
        dep_points = 1
    else:
        dep_points = 0

    total_financial_points = income_points + orphan_points + dep_points
    financial_component = (total_financial_points / 18) * 30
    financial_component = max(0, min(financial_component, 30))
    return financial_component

# ---------- Calculate Scores ----------

df['academic_component'] = df.apply(academic_score, axis=1)
df['financial_component'] = df.apply(financial_score, axis=1)
df['eligibility_score'] = df['academic_component'] + df['financial_component']

# Round score to 1 decimal place
df['eligibility_score'] = df['eligibility_score'].round(1)

# ---------- Assign Eligibility Label ----------

def eligibility_label(score):
    if score >= 85:
        return "Highly Eligible"
    elif 70 <= score < 85:
        return "Eligible"
    elif 50 <= score < 70:
        return "Conditional / Waiting List"
    else:
        return "Not Eligible"

df['eligibility_label'] = df['eligibility_score'].apply(eligibility_label)

# ---------- Tie-breaker Logic ----------

df['gpa_normalized'] = (df['cgpa'] / df['grading_system']) * 100

df = df.sort_values(
    by=['eligibility_score', 'gpa_normalized', 'income', 'courses_failed'],
    ascending=[False, False, True, True]
).reset_index(drop=True)

# ---------- Select Key Columns ----------

display_cols = [
    'student_name',
    'student_id',
    'department',
    'faculty',
    'institution',
    'eligibility_score',
    'eligibility_label'
]

# Display results
print(df[display_cols])

# ---------- Export Eligibility Results ----------

df[display_cols].to_csv(output_file, index=False)
print(f"\nEligibility results saved to: {output_file}")

# ---------- Summary Export Function ----------

def save_summary_to_csv(df, filename="eligibility_summary.csv"):
    summary_data = {"Metric": [], "Value": []}

    # Statistical distribution
    stats = df['eligibility_score'].describe()
    for metric, value in stats.items():
        summary_data["Metric"].append(metric)
        summary_data["Value"].append(round(value, 2))

    # Category counts
    label_counts = df['eligibility_label'].value_counts()
    for label, count in label_counts.items():
        summary_data["Metric"].append(f"Total {label}")
        summary_data["Value"].append(count)

    # Score buckets
    buckets = {
        "Highly Eligible (85–100)": df[df['eligibility_score'] >= 85].shape[0],
        "Eligible (70–84)": df[(df['eligibility_score'] >= 70) & (df['eligibility_score'] < 85)].shape[0],
        "Conditional (50–69)": df[(df['eligibility_score'] >= 50) & (df['eligibility_score'] < 70)].shape[0],
        "Not Eligible (<50)": df[df['eligibility_score'] < 50].shape[0],
    }

    for label, count in buckets.items():
        summary_data["Metric"].append(label)
        summary_data["Value"].append(count)

    # Save summary
    summary_df = pd.DataFrame(summary_data)
    summary_df.to_csv(filename, index=False)
    print(f"Summary saved to: {filename}")

# ---------- Save Summary CSV ----------

summary_path = r"C:\project\Capstone_Project\analysis\eligibility_summary.csv"
save_summary_to_csv(df, filename=summary_path)
