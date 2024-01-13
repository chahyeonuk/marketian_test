import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler


train_data = pd.read_csv('./train.csv')
test_data = pd.read_csv('./test.csv')

# train 데이터 X_train에서는 카드 정보만 가져옴
X_train = train_data.drop(['CLASS', 'Id'], axis=1)
y_train = train_data['CLASS']

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(X_train)

# 머신러닝 모델
model = RandomForestClassifier(random_state=42)
model.fit(x_train_scaled, y_train)

# 테스트 데이터의 Id
X_test = test_data.drop('Id', axis=1)

X_test_scaled = scaler.transform(X_test)

# 테스트 데이터에 대한 예측
predictions = model.predict(X_test_scaled)

# 결과를 DataFrame으로 만들어 CSV 파일로 저장
result_df = pd.DataFrame({'Id': test_data['Id'], 'CLASS': predictions})
result_df.to_csv('result.csv', index=False)

# 예측 결과 출력
print(result_df)

