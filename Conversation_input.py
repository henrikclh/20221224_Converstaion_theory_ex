import setupObject as suO
import time

# 20221204 Entering information
print("Type 'exit' as 'object name' to end the conversation.")

# create a list to save all the conversation
convList = []
# record number of conversation
convNum = 0

# create a loop to enter and record all conversation information
while True:
    # enter the object name
    objName = input("Enter the object name: ")

    # jump out of the loop if objName is "exit"
    if objName == "exit":
        break
    
    # enter the number of m-individuals
    mInd = input("Enter the number of m-individuals: ")
    # enter the number of p-individuals
    pInd = input("Enter the number of p-individuals: ")
    # enter the current action
    act = input("Enter the current action: ")
    # create an object with the entered information
    obj = suO.Object(objName, mInd, pInd, act)

    # record the number of conversation
    convNum += 1
    # record the real time of the conversation
    convTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # store as a string in convList as "convNum. name: x m-individuals and y p-individuals current action at convTime"
    conv = f"{convNum}. {obj.name}: {obj.mInd} m-individuals and {obj.pInd} p-individuals {obj.act} at {convTime}"
    convList.append(conv)    
    
    # save all conversation in a csv file, each conversation starts a new line
    with open("conversation.csv", "w") as f:
        for conv in convList:
            f.write(conv)
            f.write("\n")

    # print all current conversations
    print(convList)

# print all the conversation and clarify it's the end of the conversation and notify the saved file name and file location.
print("End of conversation.")
print("The conversation is saved in conversation.csv in the same folder as this program.")

# print all the conversation
print("All the conversation record:")
print(convList)

