import pandas as pd
from ..req_utils import *
from ...preprocessing._split import train_test_split
class models():
    def __init__(self, m_info):
        self.m_info = m_info
        check_scaler(self.m_info.scaler)
        check_M_modelname(self.m_info.modelname,self.m_info.auto)
        if bool(self.m_info.metric):
            evaluate(self.m_info.metric)

    @staticmethod
    def opt(X_train, X_test, y_train, y_test,mod,scaler):
        reg = mod(verbose=0, ignore_warnings=True, custom_metric=None,scaler = scaler)
        models, predictions = reg.fit(X_train, X_test, y_train, y_test)
        return models,predictions

    #@staticmethod
    #def opt(dataFrame : pd.DataFrame, testsize,y,mod,shuffle = True):
    #    X = dataFrame.loc[:, dataFrame.columns != y]
    #    y = dataFrame[[y]]
    #    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testsize, random_state=123,shuffle=shuffle)
    #    reg = mod(verbose=0, ignore_warnings=True, custom_metric=None)
    #    models, predictions = reg.fit(X_train, X_test, y_train, y_test)
    #    return models,predictions
