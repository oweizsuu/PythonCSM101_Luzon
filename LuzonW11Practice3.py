Machine_Learning = [ ("Supervisor" , "Decision Tree"),
                     ("Supervisor" , "Random Forest"),
                     ("Unsupervised" , "K-means"),
                     ("Unsupervised" , "Gaussian Mixture Model")]
print("Learning Type:" , Machine_Learning[0][0])
for item in Machine_Learning:
    if item[0] == "Supervisor":
        print(item[1])


print("Learning Type:", Machine_Learning[3][0])
for item in Machine_Learning:
    if item[0] == "Unsupervised":
        print(item[1])