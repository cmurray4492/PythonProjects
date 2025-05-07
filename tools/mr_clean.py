# pesudo 4 sigma filter for outliers
# Used to filter continous data using 4 std
# dft = target Pandas DataFrame
# para = column we want to filter
# need to have Numpy and Pandas imoported
import numpy as np


def pseudo4sigmafilter(dft, para):
    mean = dft[para].mean()
    stdev = dft[para].std()
    lowerfiltervalue = mean - (4 * stdev)
    upperfiltervalue = mean + (4 * stdev)
    # print(mean)
    # print(stdev)
    # print(lowerfiltervalue)
    # print(upperfiltervalue)

    dft["filter_" + para] = np.where(
        (dft[para] > lowerfiltervalue) & (dft[para] < upperfiltervalue),
        dft[para],
        np.nan,
    )
