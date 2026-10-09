
import os
import pickle
import zipfile

DATA_ARCHIVE = "students.dat"
PICKLE_FILES = ["students.pkl", "courses.pkl"]

def save_and_compress(students, courses):
    """Serialize objects to pickle files and archive them into students.dat"""
   
    with open("students.pkl", "wb") as f:
        pickle.dump(students, f)
        
    with open("courses.pkl", "wb") as f:
        pickle.dump(courses, f)
        
    
    with open(DATA_ARCHIVE, "wb") as archive_file:
        with zipfile.ZipFile(archive_file, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for pkl in PICKLE_FILES:
                if os.path.exists(pkl):
                    zip_file.write(pkl)
                    os.remove(pkl) 
                    
    print("\n[+] Data successfully compressed and saved to students.dat")

def decompress_and_load():
    """Check if students.dat exists, decompress, and load data via pickle"""
    if not os.path.exists(DATA_ARCHIVE):
        print("\n[*] No students.dat found. Starting with empty data.")
        return [], []
        
    students = []
    courses = []
    
    try:
        
        with zipfile.ZipFile(DATA_ARCHIVE, "r") as zip_file:
            zip_file.extractall()
            
        
        if os.path.exists("students.pkl"):
            with open("students.pkl", "rb") as f:
                students = pickle.load(f)
            os.remove("students.pkl")
            
        if os.path.exists("courses.pkl"):
            with open("courses.pkl", "rb") as f:
                courses = pickle.load(f)
            os.remove("courses.pkl")
            
        print("\n[+] Successfully decompressed and loaded data from students.dat")
    except Exception as e:
        print(f"\n[!] Error loading data from {DATA_ARCHIVE}: {e}")
        
    return students, courses