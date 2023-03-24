import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Useful only for producing predicted masks (fill nan values)
bands_mean = np.array([0.05197577, 0.04783991, 0.04056812, 0.03163572, 0.02972606, 0.03457443,
 0.03875053, 0.03436435, 0.0392113,  0.02358126, 0.01588816]).astype('float32')

# gb = GradientBoostingClassifier(n_estimators=100, verbose=1, random_state=42)

# pipe = make_pipeline(MinMaxScaler(),GradientBoostingClassifier())

# gb_classifier = Pipeline(steps=[('scaler', MinMaxScaler()), ('gb', GradientBoostingClassifier)])

gb = GradientBoostingClassifier(n_estimators=125,
                                criterion='friedman_mse',
                                max_depth=20,
                                min_samples_leaf=1,
                                min_impurity_decrease=0,
                                random_state=5,
                                subsample=0.8,
                                max_features='sqrt')

pipe = make_pipeline(MinMaxScaler(), gb)

