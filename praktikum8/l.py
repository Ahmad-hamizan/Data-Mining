# Model terbaik
order = auto_model.order

print("Best ARIMA order:", order)

model = ARIMA(train, order=order)

model_fit = model.fit()

print(model_fit.summary())

====================================================

Best ARIMA order: (2, 1, 2)
                               SARIMAX Results                                
==============================================================================
Dep. Variable:                  Close   No. Observations:                 1044
Model:                 ARIMA(2, 1, 2)   Log Likelihood               -4620.749
Date:                Mon, 25 May 2026   AIC                           9251.497
Time:                        14:56:44   BIC                           9276.247
Sample:                    11-23-2015   HQIC                          9260.885
                         - 11-21-2019                                         
Covariance Type:                  opg                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1         -0.3300      0.061     -5.447      0.000      -0.449      -0.211
ar.L2         -0.8753      0.058    -15.054      0.000      -0.989      -0.761
ma.L1          0.2945      0.069      4.265      0.000       0.159       0.430
ma.L2          0.8207      0.068     12.146      0.000       0.688       0.953
sigma2       412.6158     10.459     39.450      0.000     392.116     433.116
===================================================================================
Ljung-Box (L1) (Q):                   0.38   Jarque-Bera (JB):              1030.57
Prob(Q):                              0.54   Prob(JB):                         0.00
Heteroskedasticity (H):               2.57   Skew:                            -0.72
Prob(H) (two-sided):                  0.00   Kurtosis:                         7.65
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).