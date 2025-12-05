**Project Introduction: Scholarship Analyzer System**

The Scholarship Eligibility Analyzer is a system that helps organizations quickly and fairly identify the most deserving scholarship applicants. Instead of reviewing applications manually, our project automates the process by collecting applicant data, cleaning it, and calculating an eligibility score based on factors like academics, financial need, and supporting documents.

# We will build:

A clean database to store applicants
A Python ETL pipeline to load and process data
An eligibility scoring algorithm
An optional API layer for accessing results
A final report or dashboard showing shortlisted candidates

The Scholarship Analyzer is a data-driven system designed to help organizations identify the most deserving scholarship applicants in a transparent, fair, and efficient way. Instead of manually sorting through hundreds of applications, our system automates the entire evaluation 

Our goal as a team is to collaborate across roles—data engineering, analysis, documentation, and development—to deliver a system that could be used by schools, NGOs, foundations, or government agencies.

We are not just doing an assignment; we’re building a practical product that solves a 
real-world problem using data.



# Project Task Breakdown
Duration: 1 Week
Size: 9 Members

1.	Data Engineer — ETL Pipeline Lead Tasks:
(Members - Ikpeka Peace/Jonah Ndukwe)

•	Collect and Prepare Raw Data: Gather raw CSV/Excel datasets, validate column names, data types, missing values, duplicates, and store raw files in /data/raw.
•	Implement ETL Pipeline: Extract raw files, clean data, apply transformations (normalize GPA, income, attendance, encode extracurriculars), compute derived fields, and load into PostgreSQL tables.
•	Test and Document ETL: Validate row counts, produce logs, handle errors, and document required file format and running instructions.

2.	Data Analyst — Eligibility Score Model Lead Tasks:
(Members - Chinonso Chiemela Onyeama/Uchechukwu Onyinyechi Christabel)

•	Define Scoring Logic: Finalize scoring formula components (Academic 50%, Financial 20%, Attendance 15%, Extracurricular 15%).
•	Implement Python Score Computation: Read cleaned data, compute eligibility_score, label students.
•	Validate Model: Test scoring with sample profiles, edge cases, and summarize score distribution.
•	Document Scoring Logic: Explain metrics, weights, thresholds, and provide a flowchart.

3.	Backend Engineer — Database & API Lead Tasks:
(Members - Onyedikachi Delight Chihurumnanya/Atulegwu Osinachi/Chizaram Ikechukwu)

•	Implement PostgreSQL Schema: Create tables (students, scholarships, applications, eligibility_scores), set keys, indexes, update/insert logic.
•	Build CRUD APIs: GET /students, GET /eligible, POST /new-application, GET /scholarships.
•	Handle Error Cases: Invalid IDs, missing fields, duplicates.
•	Document APIs: Parameters, responses, example requests.

4.	Frontend Engineer — Streamlit App Lead Tasks:
(Members - Anaba Chinemerem John/Glory Oluchi Akwara)

•	Build Dashboard Layout: Header, filters sidebar, main table, score breakdown, charts.
•	Implement Features: Display eligibility table, filters, score components, input form, top eligible students section.
•	Connect App to Backend/DB: Use SQLAlchemy.
•	Final Testing: Check responsiveness, filters, data display.

5.	Project Manager — Team Lead Tasks:
•	Review Deliverables: Ensure ETL, scoring logic, Streamlit app, and documentation are complete.
•	Prepare Final Presentation: Slides with introduction, problem, data pipeline, scoring model, demo, results.
•	Final Submission Checklist: GitHub repo structure (/app, /etl, /database, /docs, /streamlit_app), README.md, requirements.txt, final dataset.

6.	QA / Tester — Quality & Documentation Lead Tasks
•	Test Entire Workflow: ETL, scoring, dashboard, DB constraints.
•	Handle Bug Reporting: Create issue tracking, report feedback daily, retest after fixes.
•	Documentation: User guide (running ETL, starting app, using filters), setup guide (Python libs, DB connection).