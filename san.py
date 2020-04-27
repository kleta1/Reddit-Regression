"""
Authors: Justin Duhaime, Kaityln Leta
Title: Reddit  Regression

Description:
This file sanitizes the raw reddit data from 
https://files.pushshift.io/reddit/
"""
import json

# Define the data file name
file_name = "RS_2019-08"

# Open the datafile for reading
txt_file = open(file_name)

# Variables to track progress of file slicing
saved_lines = 0
saved_files = 0

lines = 0

# Open the initial ouput file
out_file = open('out' + str(saved_files) + '.json', 'w+')

# Loop through each line of the reddit datafile
for line in txt_file:
    lines = lines + 1

    try:
        # open a new file if the last file was just closed / full
        if out_file.closed:
            out_file = open('out' + str(saved_files) + '.json', 'w+')

        # load the line into a json object
        # if this fails, then the line wasn't valid json and will be skipped
        j = json.loads(line)
        
        # remove lines that have scores under 100 or are in 18+ communities
        if j["score"] < 100 or j["over_18"] == True:
            continue
        
        # construct the final data object
        p = {
            "score": j["score"],
            "submit_time": j["created_utc"],
            "subreddit": j["subreddit"]
        }

        # write the data to the opened output file
        out_file.write(json.dumps(p) + '\n')
        
        saved_lines = saved_lines + 1
        
        # if the current file has 100,000+ lines saved to it
        if saved_lines >= 100000:
            # output some debugging information
            print('Saved lines: ' + str(saved_lines * (saved_files + 1)))
            print('Lines Processed: ' + str(lines))

            # close the output file
            out_file.close()

            # reset the vounter variables
            saved_files = saved_files + 1
            saved_lines = 0
    except:
        # should only get here if the data row isn't valid json
        continue
