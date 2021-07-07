#1
file_name = "write_sample.txt"

handle = open(file_name, "w")
handle.write("Hello\n")
handle.write("Bioinformatics\n")
handle.close()


#2
with open(file_name, "a") as handle:
    handle.write("ken\n")
