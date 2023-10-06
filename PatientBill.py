import PatientClass as pat
import ProcedureClass as pro



Patient=pat.Patient(1,"Matt Jones", "123 Main st, Waco TX 76706","254-555-7415",True)
Procedure1=pro.Procedure("Physical Exam","2/15/2022","Dr. Irvine", 250,1)
Procedure2=pro.Procedure("MRI","2/15/2022","Dr. Hamilton",1500,1)
Procedure3=pro.Procedure("CT Scan","2/17/2022","Dr. Drey", 1200,2)

Procedure_list=[Procedure1,Procedure2,Procedure3]


print("*** Patient Bill ***")
print("Name:", Patient.get_name())
print("Adress:", Patient.get_address())
print("Phone:", Patient.get_phone())

Total_Charges=0
for i in Procedure_list:
    if i.get_pID()==1:
        print()
        print("Procedure:",i.get_name())
        print("Date:",i.get_date())
        print("Practitioner:",i.get_pract())
        print(f"Charge: ${i.get_charges():,.2f}")
        print()
        Total_Charges+=i.get_charges()
if Patient.get_veteran_status()==True:
    Total_Charges=Total_Charges*0.6
    
print(f"Total Charges: ${Total_Charges:,.2f}")