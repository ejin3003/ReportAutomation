from read.read_reports import ReadReports
from clean.alter_reports import AlterReport

# Import designated file
rep_path = r"C:\Users\JT883\Desktop\UsageDaily_Aug.xls"
rep_1 = ReadReports(rep_path)
df = rep_1.import_report()

# Alter Excel THINK IPA's: Daily Usage Report
replace_col_dict = {
    "A SPD Dispenser #1": "Dispenser A: Lunder LL1",
    "B Lunder 2 Dispenser": "Dispenser B: Lunder 2",
    "C Lunder 2 Dispenser": "Dispenser C: Lunder 2",
    "D SPD Receiver": "Receiver D: Lunder LL1",
    "E PACU left receiver": "Receiver E: Lunder 2",
    "F OR Right Receiver": "Receiver F: OR Lounge",
    "G OR Lounge Straight Sizes 1": "Dispenser G: OR Lounge",
    "H OR Lounge Straight Sizes 2": "Dispenser H: OR Lounge",
    "I OR Lounge Straight Sizes 3": "Dispenser I: OR Lounge",
    "J OR Straight Sizes 4": "Dispenser J: OR Lounge",
    "K OR Lounge Mixed Sizes 1": "Dispenser K: OR Lounge",
    "L OR Lounge Mixed Sizes 2": "Dispenser L: OR Lounge",
    "M OR Jackets 1": "Dispenser M: OR Jackets",
    "N OR Jackets 2": "Dispenser N: OR Jackets",
    "O OR Female Locker": "Receiver O: OR Female Lockers",
    "P GRB4 Lounge": "Receiver P: OR Lounge",
    "Q OR Mens Locker Room": "Receiver Q: OR Male Lockers",
    "R OR Female Locker": "Receiver R: OR Female Lockers",
    "S Gen Pop": "Dispenser S: GRB4 Hallway",
    "T Gen Pop": "Receiver T: GRB4 Hallway",
    "U GRB4 Hallway Reciever": "Receiver U: OR Lounge",
    "V Blake 9": "Receiver V: Blake 9",
    "W Blake 9": "Dispenser W: Blake 9"
}
alt_rep_1 = AlterReport(df, "Machine", replace_col_dict)
new_df = alt_rep_1.replace_col_val()

new_col_dict = {
    "Dispenser A: Lunder LL1": ["A", "Dispenser"],
    "Dispenser B: Lunder 2": ["B", "Dispenser"],
    "Dispenser C: Lunder 2": ["C", "Dispenser"],
    "Receiver D: Lunder LL1": ["D", "Receiver"],
    "Receiver E: Lunder 2": ["E", "Receiver"],
    "Receiver F: OR Lounge": ["F", "Receiver"],
    "Dispenser G: OR Lounge": ["G", "Dispenser"],
    "Dispenser H: OR Lounge": ["H", "Dispenser"],
    "Dispenser I: OR Lounge": ["I", "Dispenser"],
    "Dispenser J: OR Lounge": ["J", "Dispenser"],
    "Dispenser K: OR Lounge": ["K", "Dispenser"],
    "Dispenser L: OR Lounge": ["L", "Dispenser"],
    "Dispenser M: OR Jackets": ["M", "Dispenser"],
    "Dispenser N: OR Jackets": ["N", "Dispenser"],
    "Receiver O: OR Female Lockers": ["O", "Receiver"],
    "Receiver P: OR Lounge": ["P", "Receiver"],
    "Receiver Q: OR Male Lockers": ["Q", "Receiver"],
    "Receiver R: OR Female Lockers": ["R", "Receiver"],
    "Dispenser S: GRB4 Hallway": ["S", "Dispenser"],
    "Receiver T: GRB4 Hallway": ["T", "Receiver"],
    "Receiver U: OR Lounge": ["U", "Receiver"],
    "Receiver V: Blake 9": ["V", "Receiver"],
    "Dispenser W: Blake 9": ["W", "Dispenser"]
}
# new_df["Label"] = new_df["Machine"].map(new_col_dict)
new_df["Label"] = new_df["Machine"].map(lambda x: new_col_dict[x][0])
new_df["Type"] = new_df["Machine"].map(lambda x: new_col_dict[x][1])
print(new_df)

# print(new_col_dict["Dispenser A: Lunder LL1"][0])
0