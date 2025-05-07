def take_user_input():
    # Number of jobs to be entered
    n = int(input("Enter the number of jobs: "))
    
    arr = []
    
    # Taking input for each job: name, deadline, and profit
    for i in range(n):
        job_name = input(f"Enter name for job {i+1}: ")
        deadline = int(input(f"Enter deadline for job {i+1}: "))
        profit = int(input(f"Enter profit for job {i+1}: "))
        arr.append([job_name, deadline, profit])
    
    return arr

def job_sequencing(arr, t):
    # Sort all jobs according to decreasing order of profit
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # To keep track of free time slots
    result = [False] * t

    # To store result (Sequence of jobs)
    job = ['-1'] * t

    # Iterate through all given jobs
    for i in range(len(arr)):
        # Find a free slot for this job (starting from the last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break

    return job

def main():
    # Take input from user
    arr = take_user_input()

    # Maximum number of time slots (can be user-defined or calculated from the jobs)
    t = int(input("Enter the maximum number of time slots: "))
    
    # Get the job sequence
    job_sequence = job_sequencing(arr, t)

    # Print the maximum profit sequence of jobs
    print("Following is the maximum profit sequence of jobs: ")
    print(job_sequence)

if __name__ == "__main__":
    main()


OUTPUT:
Enter the number of jobs: 4
Enter name for job 1: a
Enter deadline for job 1: 2
Enter profit for job 1: 200
Enter name for job 2: b
Enter deadline for job 2: 1
Enter profit for job 2: 1000
Enter name for job 3: c
Enter deadline for job 3: 1
Enter profit for job 3: 500
Enter name for job 4: d
Enter deadline for job 4: 3
Enter profit for job 4: 4000
Enter the maximum number of time slots: 3
Following is the maximum profit sequence of jobs: 
['b', 'a', 'd']