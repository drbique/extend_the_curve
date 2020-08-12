# lsextend

 Filename: lsextend.py 
 Purpose: Provide the functionality of extend_the_curve() as follows:

 Inputs:
    y                          data (dependent variable)
    desired_forecast_periods   desired number of intervals/periods in forecast
    interval                   constant width on x-axis between adjacent points, which should always be specified
                               whenever same units are used on both axes.
                               interval >= 0; interval == 0 (default) => use average change in y
                               whenever default yields unsatisfactory forecast, try non-zero interval (e.g. interval=1.0)
    origin                     x[0]
    returns                    one of the following
                                   "step" for an integer step-function result
                                   "line" for the line segment which is the extension of the curve (default)
                                   "slope" for slope and intercept only
                                   "length" for for slope and intercept with suggested length of forecast (periods)
                                   "flag" for slope and intercept with length and flag (See below)
    epsilon                    estimate of 'machine' or computational error
                               (normally omit this optional parameter)                            

 Require: 1 < desired_forecast_periods

 Returns - Depend on return argument, which defaults to "line" 
    "flag"
        Returns m,i,p,flag
            m and i denote the slope and intercept, respectively, of the desired line
            p denotes the number of valid periods for forecast
            flag  < 1 indicates forecast is proportionately less reliable for desired period, 
            flag >= 1 indicates forecast if proportionately more reliable for desired period

    "length"
        Returns m,i
            m and i denote the slope and intercept, respectively, of the desired line, and
            suggested number of periods in forecast, which is the suggested length of the predicted line

    "slope"
        Returns m,i
            m and i denote the slope and intercept, respectively, of the desired line

    "step"
        Returns z
            z is the extended line segment or step-function rounding results to integers

    "line"
        Returns z
            z is the extended line segment