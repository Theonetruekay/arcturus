y_pred = model.predict([test_data['user'], test_data['skill'], test_data['timestamp']])
y_pred = np.argmax(y_pred, axis=1)

y_true = np.argmax(test_data['level'].values, axis=1)

print(classification_report(y_true, y_pred))
 