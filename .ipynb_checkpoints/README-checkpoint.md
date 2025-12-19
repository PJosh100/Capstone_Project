# Scholarship Eligibility ETL Pipeline

## Overview
This system is an automated **ETL (Extract, Transform, Load)** solution for processing scholarship applications. It captures student data via an interactive CLI, evaluates candidates based on academic and financial need, and synchronizes the results with a centralized MySQL database.


## Features
- **Data Ingestion:** Interactive CLI with validation for NIN (uniqueness), phone (11 digits), and dates.
- **Normalization:** Automatically adjusts CGPA from 4.0 to 5.0 grading systems for standardized ranking.
- **Scoring Engine:** Business logic based on weighted academic performance and socio-economic status.
- **SQL Synchronization:** High-performance "Upsert" logic using SQLAlchemy transactions to prevent data duplication.
- **Ranking System:** Dynamic ranking of candidates updated in real-time during the Load phase.


## Eligibility Criteria
The pipeline evaluates students based on a **100-point scale**:

The system looks at two main areas:
1. Academic Performance (60 Points Max)
40 points for a high CGPA (4.5 or higher).
20 points for having no failed courses.

2. Financial Need (40 Points Max)
20 points if family income is low.
10 points for large families with many dependents.
10 points if the student is an orphan.
Total Eligibility: - Highly Eligible: 75 to 100 points.

**Status Thresholds:**
Highly Eligible:** 75 - 100 Points
Eligible:** 50 - 74 Points
Not Eligible:** Below 50 Points


## Project Structure
- `students.csv`: Primary records for identity and contact info.
- `academic_records.csv`: Educational performance metrics.
- `financial_records.csv`: Socio-economic data.
- `eligibility_ranking.csv`: Final output file containing ranked candidates.


##  Getting Started

### 1. Installation
Ensure you have Python 3.x installed, then install the required dependencies:
```bash
pip install pandas sqlalchemy pymysql