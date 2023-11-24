model.fit([train_data['user'], train_data['skill'], train_data['timestamp']], train_data['level'], epochs=10, batch_size=32, class_weight=class_weights)
