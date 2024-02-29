import os


def kill_streamlit():
    #Gets the full list of processes that are in the unknown status (other forms of status are 'running' and 'not responding')
    full_task_list = os.popen('tasklist /fi "STATUS eq unknown" /fo list').readlines()
    processes = []
    proc_to_elim = []

    #Finds all the instances of the process name within the list, and appends it to another list
    for i, word in enumerate(full_task_list):
        if 'pythonw.exe' in word:
            processes.append(word)
            
    #Further cleans the appended list by only including the process name itself, and appending that to yet another list
    #"If pythonw.exe is in the list, then copy the process name (which is pythonw.exe) out of the list"
    for j, words in enumerate(processes):
        if 'pythonw.exe' in words:
            proc_to_elim.append(words[14:25])

    #Takes just the first process name in the list
    one_process = proc_to_elim[0]

    #Kills every process with the process name
    os.system('taskkill /im ' + str(one_process) + ' /f')
    exit()

kill_streamlit()