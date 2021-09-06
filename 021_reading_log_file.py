filename = input()
full_path_fname = "resources/" + filename
fp = open(full_path_fname,'r')
file_content = fp.read()
fp.close()
split_content = file_content.splitlines()
host_list = []

for i in range(len(split_content)):
    host_list.append(split_content[i].split()[0])
#print(host_list)
unique_host = set(host_list)
#print(unique_host)

output_list = []
for j in unique_host:
    output_list.append(j + " " + str(host_list.count(j)))
    #print(j + " " + str(host_list.count(j))) #print for verification

#now, let's save the output_list to a file
full_path_output = "resources/" + "records_" + filename
save_output = open(full_path_output,'w')
for k in output_list:
    save_output.write(k + "\n")
save_output.close()

read_output = open(full_path_output,'r')
file_content = read_output.read()
read_output.close()
print(file_content)
