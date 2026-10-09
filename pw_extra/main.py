import os
import pandas as po

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class PoDataFrame:

    def __init__(self, df: po.DataFrame = None):
        self.df = df if df is not None else po.DataFrame()

    def load_csv(self, filename: str) -> po.DataFrame:
        """Loads CSV file into Po's dataframe from current directory."""
        file_path = os.path.join(BASE_DIR, filename)
        if not os.path.exists(file_path):
            print(f"[Po Error] File '{filename}' not found at {file_path}")
            return po.DataFrame()
        
        self.df = po.read_csv(file_path)
        print(f"[Po] Successfully loaded {filename}")
        return self.df

    def query(self, condition: str) -> po.DataFrame:
        """
        Executes a filter query string on Po's dataframe.
        Examples:
            - 'name == "Alice"'
            - 'major == "ICT"'
            - 'python > 85'
        """
        if self.df.empty:
            print("[Po Warning] Dataframe is empty.")
            return po.DataFrame()
        
        try:
            result = self.df.query(condition)
            return result
        except Exception as e:
            print(f"[Po Query Error] {e}")
            return po.DataFrame()


def main():
   
    po_students = PoDataFrame()
    po_scores = PoDataFrame()

    
    students_df = po_students.load_csv("students.csv")
    scores_df = po_scores.load_csv("scores.csv")

    print("\n=== Query on Students (e.g., name == 'Alice') ===")
    res_student = po_students.query('name == "Alice"')
    print(res_student)

    
    print("\n=== Query on Scores (e.g., python >= 90) ===")
    res_scores = po_scores.query("python >= 90")
    print(res_scores)

    
    if not students_df.empty and not scores_df.empty:
        merged_df = po.merge(students_df, scores_df, on="student_id", how="inner")
        po_merged = PoDataFrame(merged_df)

        print("\n=== Query on Combined Data (e.g., major == 'ICT' and python >= 85) ===")
        res_combined = po_merged.query('major == "ICT" and python >= 85')
        print(res_combined)

if __name__ == "__main__":
    main()