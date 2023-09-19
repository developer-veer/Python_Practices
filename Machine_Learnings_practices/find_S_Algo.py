def find_S(hypo_space):
    h = hypo_space[0][:-1]  # Initialize h to the most specific hypothesis in hypo_space
    for hypo in hypo_space:
        features = hypo[:-1]
        label = hypo[-1]
        if label == "Yes":
            for x in range(len(h)):
                if h[x] != features[x]:
                    h[x] = "?"
    return h


training_data_ = [

    ["Young", "High", "Yes"],
    ["Young", "Low", "No"],
    ["Middle", "High", "Yes"],
    ["Senior", "Medium", "Yes"],
    ["Senior", "Low", "No"],
    ["Middle", "Low", "Yes"]
]
training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Weak', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

res = find_S(training_data)
print(f"Most Specific hypothesis : {res}")