import pandas as pd

def create_features(data):
    # Example: Creating a new feature for family size
    data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
    return data
