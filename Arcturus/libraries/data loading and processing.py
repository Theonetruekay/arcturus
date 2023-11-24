# Load data
data = pd.read_csv("data.csv")

# Data Preprocessing
user_mapping = {user: i for i, user in enumerate(data['user'].unique())}
skill_mapping = {skill: i for i, skill in enumerate(data['skill'].unique())}

data['user'] = data['user'].map(user_mapping)
data['skill'] = data['skill'].map(skill_mapping)

# Normalize timestamps
scaler = StandardScaler()
data['timestamp'] = scaler.fit_transform(data['timestamp'].values.reshape(-1, 1))

# Convert 'level' to one-hot encoding
data['level'] = to_categorical(data['level'])

# Compute class weights
class_weights = class_weight.compute_class_weight('balanced', np.unique(data['level']), data['level'])
