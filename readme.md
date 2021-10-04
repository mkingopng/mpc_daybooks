# mpc_daybooks
This problem was where it all started for me. We had a problem at work. As oart of a multi year project to transform as many business processes as possible from manual, paper=driven processes to ERP driven processes. We had recently gone live with MRP driven production updates. Initially we noticed minor issues with strange figures being updated to the General Ledger (GL). As time passed, the problem grew and became a very material accounting issue that could not be easily explained.

My employers ERP does a daily 'update' or journal of accounting transactions from the manufacturing module to general ledger. The detail for these daily jounals is captured in 'day books' which are saved as txt files. The struture and volume of the data meant that our 'go-to' tool Excel struggled with the task. Each dybook contained between 5000 - 10000 rows of useful data. Each txt file was >imb. Each month comprises 30 txt files

After accounting, manufacturing and IT all gave up on this problem, i volunteered. I think everyone (including myself) expected me to fail. The first file took me 9 hours to manually prune into a usable form. With practice i reduced this to 3 hours. 

By this time the problem had been solved, but it was already clear to me that the informmation in these daybooks contained valuable insigghts that should be analysed and actioned. So i persisited

I learned to record macros which reduced the task to about 1 hour per file. I learned to write a little VBA which reduced, the processing time to about 10 minutes per file. these were all massive improvements, but still operated file by file. I needed something that would iterate through all files in a directory and return the cleaned data.

I discovered python. the attached beta version is the most complete version so far. development continues. 

# Objective: 
to automate the process of: iterating through all txt files in a directory; converting mpc daybook files from txt to pd.dataframe; cleaning the data; then returning a clean file containing all the mpc transactions for a month. analyse that file to identify outlier transactions in the manufacturing variance accounts.

# Complete
- iterate through all files in a specified directory
- automate the conversion of .txt files to a single txt file
- convert to pd.dataframe
- clean the data
- export to xlsx
  
# To-do
- pivot the data
- visualize with hovertext
- identify outliers

# Excel Method
- pivot table: columns; rows; filters; values
- pivot chart
- identify outliers
