def common_elements(list1, list2, list3):
	return list(set(list1) & set(list2) & set(list3))
with open("Outputs/output1.txt", 'r') as f:
    output1 = [line.strip() for line in f]
with open("Outputs/output2.txt", 'r') as f:
	output2= [line.strip() for line in f]
with open("Outputs/output3.txt", 'r') as f:
	output3= [line.strip() for line in f]
print (common_elements (output1,output2,output3))
