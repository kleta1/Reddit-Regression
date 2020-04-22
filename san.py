import json

file_name = "RS_2019-08"

txt_file = open(file_name)

saved_lines = 0
saved_files = 0

lines = 0

out_file = open('out' + str(saved_files) + ' .json', 'w+')

for line in txt_file:
    lines = lines + 1
    try:
        if out_file.closed:
            out_file = open('out' + str(saved_files) + '.json', 'w+')

        j = json.loads(line)
        
        if j["score"] < 100 or j["over_18"] == True:
            continue
        
        p = {
            "score": j["score"],
            "submit_time": j["created_utc"],
            "subreddit": j["subreddit"]
        }

        out_file.write(json.dumps(p) + '\n')
        
        saved_lines = saved_lines + 1
        
        if saved_lines >= 100000:
            print('Saved lines: ' + str(saved_lines * (saved_files + 1)))
            print('Lines Processed: ' + str(lines))
            out_file.close()
            saved_files = saved_files + 1
            saved_lines = 0
    except:
        continue