# 1. Importing packages
import pickle
import joblib
import json
from student_class import Student


# 2. Create a student object
student = Student("Afivi", "Kodjo", 12345)
student.display()

# 3. Serialize by creating a pickle/joblib files.
joblib.dump(student, 'joblib_object.joblib')                # serialize with joblib.dump()
pickle.dump(student, open('pickle_object.pkl', 'wb'))       # serialize with pickle.dump()

with open('obj.pkl', 'wb') as f:                            # Another way to serialize with pickle.dump() 
    pickle.dump(student, f)
    print('Pickling completed')

# 4. Deserialize objects to python objects
student_djob = joblib.load('joblib_object.joblib')                        # Deserialize with joblib.load()
student_dpkl = pickle.load(open('pickle_object.pkl', 'rb'))               # Deserialize with pickle.load()
print(f"Deserialized object with joblib: {student_djob.display()}")
print(f"Deserialized object with pickle: {student_dpkl.display()}")


with open('obj.pkl', 'rb') as f:                             # Another way to deserialize with pickle.load()
    student_d = pickle.load(f)
    print("Unpickling completed")
    print(f"Deserialized object with pickle: {student_d.display()}")


#### Thank you ######