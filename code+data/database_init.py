import sqlite3

def create_database():
    conn = sqlite3.connect('employee_management.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        Answer TEXT,
        Year INTEGER,
        PerNo TEXT PRIMARY KEY,
        PerStatus INTEGER,
        Sex TEXT,
        Job_classification TEXT,
        Grade TEXT,
        FactoryCode TEXT,
        ManageLevel TEXT,
        BelongingDepartment TEXT,
        WorkQualifications1 TEXT,
        WorkQualifications2 TEXT,
        WorkQualifications3 TEXT,
        WorkQualifications4 TEXT,
        WorkQualifications5 TEXT,
        WhetherPromoted TEXT,
        PromotedSpeed TEXT,
        ProjectHours INTEGER,
        ProjectTotal INTEGER,
        CurrentProjectRole TEXT,
        ProportionOfSpecialProject TEXT,
        WorkPlace TEXT,
        TrainingHoursA INTEGER,
        TrainingHoursB INTEGER,
        TrainingHoursC INTEGER,
        TotalProduction INTEGER,
        NumberOfHonors INTEGER,
        CommutingCosts INTEGER,
        Leave3A INTEGER,
        Leave3B INTEGER,
        LeaveYearA INTEGER,
        LeaveYearB INTEGER,
        BusinessTripA INTEGER,
        BusinessTripB INTEGER,
        BusinessTripConcentration INTEGER,
        AnnualPerformanceGradeA TEXT,
        AnnualPerformanceGradeB TEXT,
        AnnualPerformanceGradeC TEXT,
        AgeLevel TEXT,
        MaritalStatus TEXT,
        Dependents INTEGER,
        SeniorityA INTEGER,
        SeniorityB INTEGER,
        SeniorityC INTEGER,
        AverageYear INTEGER,
        Education TEXT,
        School TEXT,
        Department TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

create_database()
