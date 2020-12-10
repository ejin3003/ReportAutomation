#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
file_path = r"C:\Users\tyson\OneDrive\Desktop\ED Act Rep Nov 2020.xlsx"
df = pd.read_excel(file_path)


# In[87]:


def shift(row):
    if row['Hour'] >= 7 and row['Hour'] < 15:
        val = 'Morning Shift'
    elif row['Hour'] >= 15 and row['Hour'] < 23:
        val = 'Evening Shift'
    else:
        val = 'Overnight Shift'
    return val
    
df["Shift"] = df.apply(shift, axis=1)
shift_cols = ['Hour', 'Shift']
df[shift_cols].head()


# In[88]:


mask = df["Status"] != "Canceled"
df = df[mask]

sector_list = ['MGH ED Radiology', 'MGH RAD XRAY ER WH1']
df = df[df["Sector"].isin(sector_list)]

dept_lst = ['MGH IMG US MG WHT1', 'MGH IMG XR ER MG WHT1', 'MGH IMG CT ER MG WHT1', 'MGH IMG MR ER MG WHT1', 'Shift']
ed_pkup_dept_df = df[df["Pick-Up Department"].isin(dept_lst)]
ed_dest_dept_df = df[df["Destination Department"].isin(dept_lst)]

clear_str_cols = ['Ack->Cmp', 'Ack->InP', 'Asgn->Ack', 'Asgn->Cmp', 'InP->Cmp', 'Pnd->Asgn', 'Pnd->Cmp', 'Total Delay Time']
for num in range(len(clear_str_cols)):
    col = clear_str_cols[num]
    df[col] = df[col].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)


# In[100]:


dest = r"C:\Users\tyson\OneDrive\Desktop\ED Act Rep Altered PKUP Nov 2020.xlsx"
dest_2 = r"C:\Users\tyson\OneDrive\Desktop\ED Act Rep Altered DEST Nov 2020.xlsx"
ed_pkup_dept_df.to_excel(dest)
ed_dest_dept_df.to_excel(dest_2)
df.columns


# In[19]:


selected_cols = ['Ack->Cmp', 'Ack->InP', 'Asgn->Ack', 'Asgn->Cmp', 'InP->Cmp', 'Pnd->Asgn', 'Pnd->Cmp', 'Total Delay Time', 'Assigned To']
df[selected_cols].head(5)


# In[18]:


see_cols = ['Transport Date', 'Transport Time', 'Hour','Pick-up Location', 'Destination', 'Pick-Up Department', 'Destination Department', 'Status', 'Assigned To']
df[see_cols].head(3)


# In[93]:


gb_cols = ed_pkup_dept_df.groupby(['Pick-Up Department', 'Shift'])
gb_cols.agg({
    'Status': ['count'],
    'Pnd->Asgn': ['mean'],
    'Pnd->Cmp': ['mean'],
    'Asgn->Ack': ['mean'],
    'Asgn->Cmp': ['mean'],
    'Ack->Cmp': ['mean'],
    'Ack->InP': ['mean'],
})


# In[94]:


gb_dest_cols = ed_dest_dept_df.groupby(['Destination Department', 'Shift'])
gb_dest_cols.agg({
    'Status': ['count'],
    'Pnd->Asgn': ['mean'],
    'Pnd->Cmp': ['mean'],
    'Asgn->Ack': ['mean'],
    'Asgn->Cmp': ['mean'],
    'Ack->Cmp': ['mean'],
    'Ack->InP': ['mean'],
})


# In[ ]:




