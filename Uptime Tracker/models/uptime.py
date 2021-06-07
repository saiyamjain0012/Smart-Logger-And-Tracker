import os
def beatstracker(url,myid):
    fin = open("heartbeat_conf.yml", "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace('replace-id', myid)
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open("heartbeat_conf.yml", "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()
    fin = open("heartbeat_conf.yml", "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace('replace-url', '["'+url+'"]')
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open("heartbeat_conf.yml", "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()
    output = subprocess.check_output("heartbeat.exe -c heartbeat_conf.yml", shell=True)
     