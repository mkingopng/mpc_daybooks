<img src="data/Data_Analysis.jpg"/>

# mpc_daybooks
This problem was where it all started for me. We had a problem. As part of a multi-year project to transform as many 
business processes as possible from manual, paper-driven processes to ERP driven processes. We had recently gone live 
with MRP driven production updates. Initially we noticed minor issues with strange figures being updated to the General 
Ledger (GL). As time passed, the problem grew and became a very material accounting issue that could not be easily 
explained.

My employers ERP does a daily 'update' or journal of accounting transactions from the manufacturing module to general 
ledger. The detail for these daily journals is captured in 'day books' which are saved as txt files. The structure and 
volume of the data meant that our 'go-to' tool Excel struggled with the task. Each daybook contained between 5000 - 
10000 rows of useful data. Each txt file was >1mb. Each month comprises 30 txt files

After accounting, manufacturing and IT all gave up on this problem, I volunteered. I think everyone (including myself) 
expected me to fail. The first file took me 9 hours to manually clean into a usable form. I learned to record macros 
which reduced the task to about 1 hour per file. I learned to write a little VBA which reduced the processing time to 
about 10 minutes per file.

By this time the problem had been solved, but it was already clear to me that the information in these daybooks 
contained valuable insights that should be analysed and actioned.

# Objective: 
to automate the process of: 
    - iterating through all txt files in a directory; 
    - converting mpc daybook files from txt to pd.dataframe; 
    - cleaning the data; then returning a clean file containing all the mpc transactions for a month. 
    - analyse that file to identify outlier transactions.