import numpy as np

class DataGenerator():
    
    def __init__(self):
        self.min = 0
        self.max = 0
        self.size = 0
        self.range = 0
        self.mean = 0
        
        self.values = np.empty(0)
        
        
    def __str__():
        pass
    
    def plot():
        pass
    
    def recalculate():
        pass
        
    def rand_skew_norm(self, fAlpha, fLocation, fScale):
        sigma = fAlpha / np.sqrt(1.0 + fAlpha**2) 

        afRN = np.random.randn(2)
        u0 = afRN[0]
        v = afRN[1]
        u1 = sigma*u0 + np.sqrt(1.0 -sigma**2) * v 

        if u0 >= 0:
            return u1*fScale + fLocation 
        return (-u1)*fScale + fLocation 

    
    def normal(self, N=1, skew=0.0):
        
        self.values = np.array([self.rand_skew_norm(skew, 0, 1) for x in range(N)])
        
        return self.values
        
        
    def discrete(self, n, values=[], weights=[]):

        n_values = len(values)

        rand = np.random.rand(n)
        arr_str = np.empty(n, dtype='object')
        cum_weights = np.cumsum(weights) - weights
        
        if ((round(sum(weights)) == 1) or (round(sum(weights)) == 1.0)) and (len(weights) == len(values)):

            for idx in range(0, len(values)):

                boundary = (cum_weights[idx], cum_weights[idx]+weights[idx])

                arr_str[(rand>=boundary[0]) & (rand<boundary[1])] = values[idx]

        else:

            weight = 1.0 / n_values

            for idx, value in enumerate(values):

                boundary = (weight*idx, weight*idx+weight)

                arr_str[(rand>=boundary[0]) & (rand<boundary[1])] = value

        try:
            return arr_str.astype('int32')
        except:
            return arr_str
        
        
    def concat(self, arr1, arr2, blend=0):

        if blend<0:
            blend = 0

        arr1_range = (max(arr1) - min(arr1))/(1+blend)


        new_arr = np.concatenate((arr1, arr2+arr1_range))

        return new_arr
    

    def minmax_scaler(self, arr, vmin, vmax):
        return ((arr - arr.min()) * (vmax - vmin)) / (arr.max() - arr.min()) + vmin
