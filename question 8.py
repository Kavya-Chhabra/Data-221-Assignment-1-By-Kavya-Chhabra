import pandas as pd

#given data from the question
data = {
    "A":[1,2,2,1],
    "B":[3.1,4.2,1.5,6.3],
    "C":[800,150,400,210]
}

# Create the DataFrame
data_frame = pd.DataFrame(data)

# Add a new computed column using existing columns
data_frame["D"] = data_frame["A"] * data_frame["B"]

# Print the final DataFrame
print(data_frame)
