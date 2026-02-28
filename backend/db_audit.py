import sqlite3
import os

def audit():
    db_path = r'c:\InsuranceProject\Sajuapp\backend\saju_data.db'
    if not os.path.exists(db_path):
        print(f"Error: {db_path} not found")
        return

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # Get all tables
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]
    print(f"Tables: {tables}")
    
    # Audit each table
    for table in tables:
        cur.execute(f"SELECT count(*) FROM {table}")
        count = cur.fetchone()[0]
        cur.execute(f"PRAGMA table_info({table})")
        cols = [r[1] for r in cur.fetchall()]
        print(f"Table {table}: {count} rows, Columns: {cols}")
    
    # Verify celebrity count
    if 'celebrity_saju' in tables:
        cur.execute("SELECT count(*) FROM celebrity_saju")
        celeb_count = cur.fetchone()[0]
        print(f"Total Celebrities: {celeb_count}")

    conn.close()

if __name__ == '__main__':
    audit()
