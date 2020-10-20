import pandas as pd

df = pd.read_excel(r"C:\Users\tyson\OneDrive\Desktop\June Prod Extract.xlsx")
pd.set_option("display.width", 400)
pd.set_option("display.max_columns", None)

# print(df.columns)

for i in df.index:
    escort = df["Transporter"][i]
    completed_trips = df["Completed"][i]
    outliers = df["Outliers"][i]
    escalations = df["Escalations"][i]
    delay_time = df["Delay Time"][i]
    ack_inp = df["Ack -> In P"][i]
    inp_comp = df["In P -> Comp"][i]
    ack_comp = df["Ack -> Comp"][i]
    working_time = df["Working Time"][i]
    idle_time = df["Idle Time"][i]
    break_time = df["Break Time"][i]
    worked_days = df["Work Days"][i]
    total_patient = df["Total Patient"][i]
    total_non_patient = df["Total Non-Patient"][i]
    month_name = df["Month"][i]

    print()
    if i == 3:
        break




