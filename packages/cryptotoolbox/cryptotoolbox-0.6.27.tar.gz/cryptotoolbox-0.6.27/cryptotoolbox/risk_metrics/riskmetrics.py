#!/usr/bin/env python3
# coding: utf-8


""" Metric functons used in financial analysis. """

# Built-in packages

# External packages
import math
import pandas as pd
from scipy.optimize import Bounds, LinearConstraint, minimize
from cryptotoolbox.realtime import realtime_plotting_utility
from datetime import datetime
import numpy as np

# Internal packages


__all__ = [
    'accuracy', 'annual_return', 'annual_volatility', 'calmar',
    'diversified_ratio', 'drawdown', 'mad', 'mdd', 'sharpe', 'perf_index',
    'perf_returns',
]


# =========================================================================== #
#                                   Metrics                                   #
# =========================================================================== #


def accuracy(y_true, y_pred, sign=True):
    """ Compute the accuracy of prediction.
    Parameters
    ----------
    y_true : np.ndarray[ndim=1, dtype=np.float64]
        Vector of true series.
    y_pred : np.ndarray[ndim=1, dtype=np.float64]
        Vector of predicted series.
    sign : bool, optional
        Check sign accuracy if true, else check exact accuracy, default
        is True.
    Returns
    -------
    float
        Accuracy of prediction as float between 0 and 1.
    Examples
    --------
    >>> y_true = np.array([1., .5, -.5, .8, -.2])
    >>> y_pred = np.array([.5, .2, -.5, .1, .0])
    >>> accuracy(y_true, y_pred)
    0.8
    >>> accuracy(y_true, y_pred, sign=False)
    0.2
    See Also
    --------
    mdd, calmar, sharpe, drawdown
    """
    if sign:
        y_true = np.sign(y_true)
        y_pred = np.sign(y_pred)

    # Check right answeres
    R = np.sum(y_true == y_pred)

    # Check wrong answeres
    W = np.sum(y_true != y_pred)

    return R / (R + W)

def simple_return(series):
    ret = series[-1] / series[0] - 1
    return ret

def annual_return(series, period=365):
    """ Compute compouned annual return.
    Parameters
    ----------
    series : np.ndarray[np.float64, ndim=1]
        Time series (price, performance or index).
    period : int, optional
        Number of period per year, default is 365 (trading days).
    Returns
    -------
    np.float64
        Value of compouned annual return.
    Examples
    --------
    Assume series of monthly prices:
    >>> series = np.array([100, 110, 80, 120, 160, 108])
    >>> print(round(annual_return(series, period=12), 4))
    0.1664
    See Also
    --------
    mdd, drawdown, sharpe, annual_volatility
    """
    T = series.size
    ret = series[-1] / series[0]

    return np.sign(ret) * np.float_power(
        np.abs(ret),
        period / T,
        dtype=np.float64
    ) - 1.


def annual_volatility(series, period=365):
    """ Compute compouned annual volatility.
    Parameters
    ----------
    series : np.ndarray[np.float64, ndim=1]
        Time series (price, performance or index).
    period : int, optional
        Number of period per year, default is 365 (trading days).
    Returns
    -------
    np.float64
        Value of compouned annual volatility.
    Examples
    --------
    Assume series of monthly prices:
    >>> series = np.array([100, 110, 105, 110, 120, 108])
    >>> print(round(annual_volatility(series, period=12), 6))
    0.272172
    See Also
    --------
    mdd, drawdown, sharpe, annual_return
    """
    return np.sqrt(period) * np.std(series[1:] / series[:-1] - 1.)


def calmar(series, period=365):
    """ Compute the Calmar Ratio [1]_.
    Notes
    -----
    It is the compouned annual return over the Maximum DrawDown.
    Parameters
    ----------
    series : np.ndarray[np.float64, ndim=1]
        Time series (price, performance or index).
    period : int, optional
        Number of period per year, default is 365 (trading days).
    Returns
    -------
    np.float64
        Value of Calmar ratio.
    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Calmar_ratio
    Examples
    --------
    Assume a series of monthly prices:
    >>> series = np.array([70, 100, 80, 120, 160, 80])
    >>> calmar(series, period=12)
    0.6122448979591835
    See Also
    --------
    mdd, drawdown, sharpe, roll_calmar
    """
    series = np.asarray(series, dtype=np.float64).flatten()
    ret = series[-1] / series[0]
    annual_return = np.sign(ret) * np.float_power(
        np.abs(ret), period / len(series), dtype=np.float64) - 1.
    # Compute MaxDrawDown
    max_dd = max(mdd(series),10e-6)
    return annual_return / max_dd



def diversified_ratio(series, w=None, std_method='std'):
    r""" Compute diversification ratio of a portfolio.
    Notes
    -----
    Diversification ratio, denoted D, is defined as the ratio of the
    portfolio's weighted average volatility to its overll volatility,
    developed by Choueifaty and Coignard [2]_.
    .. math:: D(P) = \frac{P' \Sigma}{\sqrt{P'VP}}
    With :math:`\Sigma` vector of asset volatilities, :math:`P` vector of
    weights of asset of portfolio, and :math:`V` matrix of variance-covariance
    of these assets.
    Parameters
    ----------
    series : np.array[ndim=2, dtype=np.float64] of shape (T, N)
        Portfolio matrix of N assets and T time periods, each column
        correspond to one series of prices.
    w : np.array[ndim=1 or 2, dtype=np.float64] of size N, optional
        Vector of weights, default is None it means it will equaly weighted.
    std_method : str, optional /!\ Not yet implemented /!\
        Method to compute variance vector and covariance matrix.
    Returns
    -------
    np.float64
        Value of diversification ratio of the portfolio.
    References
    ----------
    .. [2] tobam.fr/wp-content/uploads/2014/12/TOBAM-JoPM-Maximum-Div-2008.pdf
    """
    T, N = series.shape

    if w is None:
        w = np.ones([N, 1]) / N
    else:
        w = w.reshape([N, 1])

    sigma = np.std(series, axis=0).reshape([N, 1])
    V = np.cov(series, rowvar=False, bias=True).reshape([N, N])

    return (w.T @ sigma) / np.sqrt(w.T @ V @ w)


def drawdown(series):
    """ Measures the drawdown of `series`.
    Function to compute measure of the decline from a historical peak in some
    variable [3]_ (typically the cumulative profit or total open equity of a
    financial trading strategy).
    Parameters
    ----------
    series : np.ndarray[np.float64, ndim=1]
        Time series (price, performance or index).
    Returns
    -------
    np.ndarray[np.float64, ndim=1]
        Series of DrawDown.
    References
    ----------
    .. [3] https://en.wikipedia.org/wiki/Drawdown_(economics)
    Examples
    --------
    >>> series = np.array([70, 100, 80, 120, 160, 80])
    >>> drawdown(series)
    array([0. , 0. , 0.2, 0. , 0. , 0.5])
    See Also
    --------
    mdd, calmar, sharpe, roll_mdd
    """
    series = np.asarray(series, dtype=np.float64).flatten()
    maximums = np.maximum.accumulate(series, dtype=np.float64)
    return 1. - series / maximums


def mad(series):
    """ Compute the Mean Absolute Deviation.
    Compute the mean of the absolute value of the distance to the mean [4]_.
    Parameters
    ----------
    series : np.ndarray[np.float64, ndim=1]
        Time series (price, performance or index).
    Returns
    -------
    np.float64
        Value of mean absolute deviation.
    References
    ----------
    .. [4] https://en.wikipedia.org/wiki/Average_absolute_deviation
    Examples
    --------
    >>> series = np.array([70., 100., 90., 110., 150., 80.])
    >>> mad(series)
    20.0
    See Also
    --------
    roll_mad
    """
    return np.mean(np.abs(series - np.mean(series)))


def mdd(series):
    """ Compute the maximum drwdown.
    Drawdown is the measure of the decline from a historical peak in some
    variable [5]_ (typically the cumulative profit or total open equity of a
    financial trading strategy).
    Parameters
    ----------
    series : np.ndarray[np.float64, ndim=1]
        Time series (price, performance or index).
    Returns
    -------
    np.float64
        Value of Maximum DrawDown.
    References
    ----------
    .. [5] https://www.investopedia.com/terms/m/maximum-drawdown-mdd.asp
    Examples
    --------
    >>> series = np.array([70, 100, 80, 120, 160, 80])
    >>> mdd(series)
    0.5
    See Also
    --------
    drawdown, calmar, sharpe, roll_mdd
    """
    series = np.asarray(series, dtype=np.float64).flatten()
    return max(drawdown(series))


def perf_index(series, base=100.):
    """ Compute performance of prices or index values along time axis.
    Parameters
    ----------
    series : np.ndarray[ndim=1, dtype=np.float64]
        Time-series of prices or index values.
    base : float, optional
        Initial value for measure the performance, default is 100.
    Returns
    -------
    np.ndarray[ndim=1, dtype=np.float64]
        Performances along time axis.
    See Also
    --------
    perf_returns, perf_strat
    Examples
    --------
    >>> series = np.array([10., 12., 15., 14., 16., 18., 16.])
    >>> perf_index(series, base=100.)
    array([100., 120., 150., 140., 160., 180., 160.])
    """
    return base * series / series[0]


def perf_returns(returns, log=False, base=100.):
    """ Compute performance of returns along time axis.
    Parameters
    ----------
    returns : np.ndarray[ndim=1, dtype=np.float64]
        Time-series of returns.
    log : bool, optional
        Considers returns as log-returns if True. Default is False.
    base : float, optional
        Initial value for measure the performance, default is 100.
    Returns
    -------
    np.ndarray[ndim=1, dtype=np.float64]
        Performances along time axis.
    See Also
    --------
    perf_index, perf_strat
    Examples
    --------
    >>> returns = np.array([0., 20., 30., -10., 20., 20., -20.])
    >>> perf_returns(returns, base=100., log=False)
    array([100., 120., 150., 140., 160., 180., 160.])
    """
    series = np.cumsum(returns) + base

    if log:
        series = np.exp(series)

    return perf_index(series, base=base)


# TODO : finish perf strat metric (add reinvest option)
def perf_strat(underlying, signals=None, log=False, base=100.,
               reinvest=False):
    """ Compute the performance of a strategy.
    With respect to this underlying and signal series along time axis.
    Parameters
    ----------
    underlying : np.ndarray[ndim=1, dtype=np.float64]
        Time-series of prices or index values.
    signals : np.ndarray[ndim=1, dtype=np.float64]
        Time-series of signals, if `None` considering a long position.
    log : bool, optional
        Considers underlying series as log values if True. Default is False.
    base : float, optional
        Initial value for measure the performance, default is 100.
    reinvest : bool, optional
        Reinvest profit/loss if true.
    Returns
    -------
    np.ndarray[ndim=1, dtype=np.float64]
        Performances along time axis.
    See Also
    --------
    perf_returns, perf_index
    Examples
    --------
    >>> underlying = np.array([10., 12., 15., 14., 16., 18., 16.])
    >>> signals = np.array([1., 1., 1., 0., 1., 1., -1.])
    >>> perf_strat(underlying, signals, base=100.)
    array([100., 120., 150., 150., 170., 190., 210.])
    # >>> perf_strat(underlying, signals, base=100., reinvest=True)
    # array([100., 120., ])
    """
    returns = np.zeros(underlying.shape)
    underlying *= base / underlying[0]
    returns[1:] = underlying[1:] - underlying[:-1]

    if signals is None:
        signals = np.ones(underlying.shape[0])

    series = returns * signals

    return perf_returns(series, log=log, base=base)


def sharpe(series, period=365, from_ret = False):
    r""" Compute the Sharpe ratio [6]_.
    Notes
    -----
    It is computed as the total return over the volatility (we assume no
    risk-free rate) such that:
    .. math:: \text{Sharpe ratio} = \frac{E(r)}{\sqrt{Var(r)}}
    Parameters
    ----------
    series : numpy.ndarray(dim=1, dtype=float)
        Prices of the index.
    period : int, optional
        Number of period per year, default is 252 (trading days).
    log : bool, optional
        If true compute sharpe with the formula for log-returns, default
        is False.
    Returns
    -------
    np.float64
        Value of Sharpe ratio.
    References
    ----------
    .. [6] https://en.wikipedia.org/wiki/Sharpe_ratio
    Examples
    --------
    Assume a series of monthly prices:
    >>> series = np.array([70, 100, 80, 120, 160, 80])
    >>> sharpe(series, period=12)
    0.22494843872918127
    See Also
    --------
    mdd, calmar, drawdown, roll_sharpe
    """
    series = np.asarray(series, dtype=np.float64).flatten()
    if from_ret:
        ret_vect = series
    else:
        ret_vect = series[1:] / series[:-1] - 1.

    #return math.sqrt(period)*np.mean(ret_vect)/np.std(ret_vect, dtype=np.float64)
    return (np.float_power(np.cumprod(1+ret_vect)[-1], period/np.size(ret_vect))-1) /\
           (np.sqrt(period)*np.std(ret_vect, dtype=np.float64))


def roll_sharpe(series, period=365, win=0, cap=True):
    rollingSharpe = lambda rets : sharpe(rets, period)
    rolledSeries = pd.Series(series).rolling(win).apply(rollingSharpe)
    return rolledSeries.values


def from_ret_to_price(series, initial_price = 1.):
    return initial_price * (1 + series).cumprod()


def compute_sharpe(df_ret = None, weights = None, period = 365):
    print('minimum return date')
    print(min(df_ret.index))
    print('maximum return date')
    print(max(df_ret.index))
    print('minimum weights date')
    print(min(weights.index))
    print('maximum weights date')
    print(max(weights.index))
    assert df_ret.shape == weights.shape
    assert sum(weights.columns == df_ret.columns) == weights.shape[1]
    portfolio = np.cumprod(np.prod(df_ret * weights.values + 1, axis=1))
    return sharpe(portfolio ,period = period), portfolio

def find_best_dd_weights(weights_list, returns_df):
    N_ = len(weights_list)
    w0 = np.ones([N_]) / N_
    const_sum = LinearConstraint(np.ones([1, N_]), [1], [1])
    up_bound_ = 1.
    low_bound_ = 0.
    const_ind = Bounds(low_bound_ * np.ones([N_]), up_bound_ * np.ones([N_]))
    to_optimize = lambda x: f_dd_weights_mix(weights_list, returns_df, x)
    w__ = minimize(
        to_optimize,
        w0,
        method='SLSQP',
        constraints=[const_sum],
        bounds=const_ind
    ).x
    return w__

def f_dd_weights_mix(w_list_, data_, w):
    np_returns = None
    counter = 0
    for weights_ in w_list_:
        if np_returns is None:
            np_returns = w[counter] * data_.values * weights_
        else:
            np_returns = np_returns + w[counter] * data_.values * weights_
        counter = counter + 1
    np_returns = np_returns.sum(axis=1)
    dds = drawdown(from_ret_to_price(np_returns))
    return dds.max()


def f_perf_weights_mix(w_list_, data_, w):
    np_returns = None
    counter = 0
    for weights_ in w_list_:
        if np_returns is None:
            np_returns = w[counter] * data_.values * weights_
        else:
            np_returns = np_returns + w[counter] * data_.values * weights_
        counter = counter + 1
    np_returns = np_returns.sum(axis=1)
    prices = from_ret_to_price(np_returns)
    return -prices.iloc[-1]

def find_best_perf_weights(weights_list, returns_df):
    N_ = len(weights_list)
    w0 = np.ones([N_]) / N_
    const_sum = LinearConstraint(np.ones([1, N_]), [1], [1])
    up_bound_ = 1.
    low_bound_ = 0.
    const_ind = Bounds(low_bound_ * np.ones([N_]), up_bound_ * np.ones([N_]))
    to_optimize = lambda x: f_perf_weights_mix(weights_list, returns_df, x)
    w__ = minimize(
        to_optimize,
        w0,
        method='SLSQP',
        constraints=[const_sum],
        bounds=const_ind
    ).x
    return w__

def f_sharpe_weights_mix(w_list_, data_, w):
    np_returns = None
    counter = 0
    for weights_ in w_list_:
        if np_returns is None:
            np_returns = w[counter] * data_.values * weights_
        else:
            np_returns = np_returns + w[counter] * data_.values * weights_
        counter = counter + 1
    np_returns = np_returns.sum(axis=1)
    np_returns = np_returns[:, np.newaxis]
    computed_sharpe = sharpe(np_returns, period=365, from_ret=True)
    if np.isnan(computed_sharpe):
        return 0
    return computed_sharpe

def find_best_sharpe(weights_list, X):
    N_ = len(weights_list)
    w0 = np.ones([N_]) / N_
    const_sum = LinearConstraint(np.ones([1, N_]), [1], [1])
    up_bound_ = 1.
    low_bound_ = 0.
    const_ind = Bounds(low_bound_ * np.ones([N_]), up_bound_ * np.ones([N_]))
    to_optimize = lambda x: f_sharpe_weights_mix(weights_list, X, x)
    w__ = minimize(
        to_optimize,
        w0,
        method='SLSQP',
        constraints=[const_sum],
        bounds=const_ind
    ).x
    return w__


def compute_average_prediction(optimal_mixing, weights_list):
    mixed_df = None
    counter = 0
    for weights_ in weights_list:
        if mixed_df is None:
            mixed_df = optimal_mixing[counter] * weights_
        else:
            mixed_df = mixed_df + optimal_mixing[counter] * weights_
        counter = counter + 1
    return mixed_df

def get_accuracy_kpis(strategies, signals_df, under_returns_df):
    results = np.zeros([1, len(strategies)])
    j = 0
    for strat in strategies:
        try:
            accuracies = []
            for sig in signals_df.columns:
                if strat in sig:
                    strat_sig = sig.split('/')[0]
                    under_sig = sig.split('/')[1]
                    cum_df = pd.merge(signals_df[sig], under_returns_df[under_sig].pct_change(), right_index= True, left_index= True)
                    cum_df = cum_df.dropna()
                    acc = accuracy(cum_df[sig], cum_df[under_sig])
                    accuracies.append(acc)

            results[0,j] = sum(accuracies)/len(accuracies)
            j += 1
        except Exception as inst:
            print(inst)
            continue
    kpis_df = pd.DataFrame(results, columns=strategies, index=[accuracy.__name__])
    return kpis_df

def filter_daily(dataframe):
    dataframe['day'] = dataframe.index.hour == 23
    daily_aggregated_df = dataframe[dataframe['day']].copy()
    daily_aggregated_df['date'] = daily_aggregated_df.index

    def truncate_date(row):
        datet = row['date']
        return datetime(datet.year, datet.month, datet.day)

    daily_aggregated_df['trunc_date'] = daily_aggregated_df.apply(truncate_date, axis=1)
    daily_aggregated_df = daily_aggregated_df.set_index('trunc_date')
    daily_aggregated_df = daily_aggregated_df.drop(columns=['date','day'])
    return daily_aggregated_df



def get_kpi(price_df, default_metrics = [simple_return, annual_return, annual_volatility, sharpe, calmar, mdd]):
    nb_metrics = len(default_metrics)
    results = np.zeros([nb_metrics, len(price_df.columns)])
    # df = self.get_perf()
    i = 0
    for m in default_metrics:
        j = 0
        for a in price_df.columns:
            try:
                results[i,j] = m(price_df[a].values)

                j += 1
            except Exception as inst:
                print(inst)
                continue
        i += 1

    kpis_df = pd.DataFrame(results, columns=price_df.columns, index=[m.__name__ for m in default_metrics])
    return kpis_df

def compute_extensive_kpis(data_df = None, strat = None):
    btd_kpis = get_kpi(data_df[[strat]])
    data_df['year'] = data_df.index.year
    data_df['month'] = data_df.index.year.astype(str) + '_' + data_df.index.month.astype(str)
    def compute_metrics(df, strat=None):
        kpi_df = get_kpi(df[[strat]])
        return kpi_df.to_dict()[strat]

    go_comp_kpi = lambda x: compute_metrics(x, strat=strat)
    monthepochkpis_df = data_df[['month', strat]].groupby(['month']).apply(go_comp_kpi)
    monthepochkpis_df = pd.DataFrame.from_records(monthepochkpis_df.to_dict()).T
    monthepochkpis_df = monthepochkpis_df.dropna()
    ratio_positive_month = (monthepochkpis_df['simple_return']>=0.).sum()/len(monthepochkpis_df)

    yearepochkpis_df = data_df[['year', strat]].groupby(['year']).apply(go_comp_kpi)
    yearepochkpis_df = pd.DataFrame.from_records(yearepochkpis_df.to_dict()).T
    yearepochkpis_df = yearepochkpis_df.dropna()
    ratio_positive_year = (yearepochkpis_df['simple_return']>=0.).sum()/len(yearepochkpis_df)

    print('done')
    data_df = data_df.sort_index()
    current_values = data_df.iloc[-1]
    current_date = data_df.index[-1]
    current_year = str(current_date.year-1)

    ytd_date = pd.Timestamp(f'{current_year}-12-31')
    ytd_values = data_df.loc[ytd_date]

    ytd_ohlc_df = data_df.loc[ytd_date:].copy()

    ytd_kpis = get_kpi(ytd_ohlc_df[[strat]])

    return_ytd_to_date = (current_values[strat] - ytd_values[strat])/ytd_values[strat]
    results = {}
    results[f'return_ytd'] = return_ytd_to_date

    for nb_month in [1,3,6]:
        back_date = data_df.index[-1] + pd.DateOffset(months=-1*nb_month)
        try :
            past_values = data_df.loc[back_date]
            return_to_date = (current_values[strat] - past_values[strat])/past_values[strat]
            results[f'return_{nb_month}_month'] = return_to_date
        except Exception as e:
            print(f'trouble {e}')
            results[f'return_{nb_month}_month'] = np.nan

    past_returns = pd.Series(results)

    ### 1 month return
    btd_kpis_dict = btd_kpis.to_dict()[strat]
    btd_kpis_dict['ratio_positive_month']=ratio_positive_month
    btd_kpis_dict['ratio_positive_year'] =ratio_positive_year
    btd_kpis_dict_df = pd.Series(btd_kpis_dict)
    return btd_kpis_dict_df, ytd_kpis, past_returns


def compute_plot_excel_kpis_meterics_metrics(data, title, local_root_directory='./', plot_html=False, write_file=True):
    clean_title = title.replace(' ', '_').replace('.', '')
    if plot_html:
        fig = realtime_plotting_utility.plot_multiple_time_series(
            data_df=data,
            logy=True, split=False,
            put_on_same_scale=False,
            title=title)
        fig.show()
        fig = realtime_plotting_utility.plot_multiple_time_series(
            data_df=data,
            logy=False, split=False,
            put_on_same_scale=False,
            title=title)
        fig.show()

    dd_list = []
    for me_underlying in data.columns:
        dd_display_name = 'drawdown ' + me_underlying
        dd_list.append(dd_display_name)
        ### whole period drawdown

        dd_norm_strat = drawdown(data[me_underlying])
        # merged_df[f'drawdown_{me_underlying}'] = dd_norm_strat

        data[dd_display_name] = - dd_norm_strat
        ### limited_period_drawdown
        limited_dd_norm_strat = drawdown(data[me_underlying])
        # merged_df[f'drawdown_{me_underlying}'] = dd_norm_strat
        dd_display_name = 'drawdown ' + me_underlying.replace('close_', '')
        data[dd_display_name] = - limited_dd_norm_strat

    if plot_html:
        fig = realtime_plotting_utility.plot_multiple_drawdowns(data, dd_list)
        fig.show()
    data.index = pd.to_datetime(data.index)
    data['day'] = data.index.floor('d')
    data = data.sort_index()
    daily_df = data.groupby('day').first().copy()

    for me_strat in daily_df.columns:
        if not 'drawdown' in me_strat:
            if plot_html:
                fig = realtime_plotting_utility.plot_multiple_time_series(
                    data_df=daily_df[[me_strat]],
                    logy=True, split=False,
                    put_on_same_scale=False,
                    title= title)
                fig.show()
                dollar_df = daily_df[[me_strat]].copy()
                new_names = {me_strat: 'Performance Strategy'}
                dollar_df = dollar_df.rename(columns=new_names)
                fig = realtime_plotting_utility.plot_dollar_multiple_time_series(data_df=dollar_df,
                                                                                 logy=True, split=False,
                                                                                 put_on_same_scale=False,
                                                                                 title=f'Strategy {title})')
                fig.show()

            if write_file:
                clean_title = title.replace(' ','_')
                writer = pd.ExcelWriter(local_root_directory + f'advance_kpis_details_{clean_title}.xlsx',
                                        engine='xlsxwriter')

            btd_kpis, ytd_kpis, past_returns = compute_extensive_kpis(data_df=daily_df.copy(),
                                                                                  strat=me_strat)
            me_strat_name = me_strat
            me_strat_name = me_strat_name.replace('0.', '')
            # whole_period_kpi_df.to_excel(writer, sheet_name=frequency)
            btd_kpis = btd_kpis.to_frame()
            btd_kpis.columns = [me_strat]
            past_returns = past_returns.to_frame()
            past_returns.columns = [me_strat]
            if write_file:
                btd_kpis.to_excel(writer, sheet_name='advanced_btd')
                ytd_kpis.to_excel(writer, sheet_name='advanced_ytd')
                past_returns.to_excel(writer, sheet_name='common')

                writer.save()
            if write_file:
                writer = pd.ExcelWriter(local_root_directory + f'perf_dd_{me_strat_name}_{clean_title}.xlsx',
                                        engine='xlsxwriter')
                data.to_excel(writer, sheet_name='daily')
                month_data=data.copy()

                month_data['beginning_month'] = month_data['day'].index.day==1
                month_data['ending_month'] =  month_data['beginning_month'].shift(-1)
                month_data['ending_month'] = month_data['ending_month'].fillna(False)
                month_data = month_data[month_data['ending_month']]
                month_data.to_excel(writer, sheet_name='monthly')
                writer.save()
            ################ computing the metrics per epoch (monthly !)

            def compute_metrics(df, strat=None):
                kpi_df = get_kpi(df[[strat]])
                return kpi_df.to_dict()[strat]

            go_comp_kpi = lambda x: compute_metrics(x, strat=me_strat)

            daily_df['year'] = daily_df.index.year
            daily_df['month'] = daily_df.index.month
            def get_month_date(row):
                from datetime import datetime
                return datetime(year=int(row['year']), month=int(row['month']), day=1)

            daily_df['month_date'] = daily_df.apply(get_month_date, axis = 1)

            epochkpis_series = daily_df[['month_date', me_strat]].groupby(['month_date']).apply(go_comp_kpi)
            epochkpis_df = pd.DataFrame().from_records(epochkpis_series.values)
            epochkpis_df.index = epochkpis_series.index
            epochkpis_df = epochkpis_df.sort_index()
            epochkpis_df['year'] = epochkpis_df.index.year
            epochkpis_df['month'] = epochkpis_df.index.month


            def rename_month(row):
                if row['month'] == 1:
                    return 'January'
                if row['month'] == 2:
                    return 'February'
                if row['month'] == 3:
                    return 'March'
                if row['month'] == 4:
                    return 'April'
                if row['month'] == 5:
                    return 'May'
                if row['month'] == 6:
                    return 'June'
                if row['month'] == 7:
                    return 'July'
                if row['month'] == 8:
                    return 'August'
                if row['month'] == 9:
                    return 'September'
                if row['month'] == 10:
                    return 'October'
                if row['month'] == 11:
                    return 'November'
                if row['month'] == 12:
                    return 'December'

            epochkpis_df['month'] = epochkpis_df.apply(rename_month, axis=1)
            epochkpis_df = epochkpis_df.set_index(['year','month'])

            #daily_df['month'] = daily_df.apply(rename_month, axis=1)

            # epochkpis_series = daily_df[['year', 'month', me_strat]].groupby(['year', 'month']).apply(go_comp_kpi)
            # epochkpis_df = pd.DataFrame().from_records(epochkpis_series.values)
            # epochkpis_df.index = epochkpis_series.index
            epochkpis_df = epochkpis_df.rename(columns={
                'simple_return': 'epoch realized return',
                'annual_return': 'epoch realized annualized return',
                'annual_volatility': 'epoch realized annualized volatility',
                'sharpe': 'epoch realized sharpe ratio',
                'calmar': 'epoch realized calmar ratio',
                'mdd': 'epoch realized max drawdown'})

            epochkpis_df['epoch realized return'] = epochkpis_df['epoch realized return']*100.
            epochkpis_df['epoch realized annualized volatility'] = epochkpis_df['epoch realized annualized volatility']*100.
            epochkpis_df['epoch realized max drawdown'] = epochkpis_df['epoch realized max drawdown']*100.

            epochkpis_df['epoch realized return'] = epochkpis_df['epoch realized return'].round(
                decimals=2)
            epochkpis_df['epoch realized annualized return'] = epochkpis_df[
                'epoch realized annualized return'].round(decimals=2)
            epochkpis_df['epoch realized annualized volatility'] = epochkpis_df[
                'epoch realized annualized volatility'].round(decimals=2)
            epochkpis_df['epoch realized sharpe ratio'] = epochkpis_df[
                'epoch realized sharpe ratio'].round(decimals=2)
            epochkpis_df['epoch realized calmar ratio'] = epochkpis_df[
                'epoch realized calmar ratio'].round(decimals=2)
            epochkpis_df['epoch realized max drawdown'] = epochkpis_df[
                'epoch realized max drawdown'].round(decimals=2)

            if write_file:
                writer = pd.ExcelWriter(local_root_directory + f'epoch_{me_strat_name}_{clean_title}.xlsx',
                                        engine='xlsxwriter')
                epochkpis_df.to_excel(writer, sheet_name='kpis per epoch')
                writer.save()
            if plot_html:
                to_plot_df = epochkpis_df.copy()
                to_plot_df=to_plot_df.reset_index()
                from datetime import datetime
                def compute_date(row):
                    year = int(row['year'])
                    month = None
                    if row['month'] == 'January':
                        month=1
                    if row['month'] == 'February':
                        month=2
                    if row['month'] == 'March':
                        month=3
                    if row['month'] == 'April':
                        month=4
                    if row['month'] == 'May':
                        month=5
                    if row['month'] == 'June':
                        month=6
                    if row['month'] == 'July':
                        month=7
                    if row['month'] == 'August':
                        month=8
                    if row['month'] == 'September':
                        month=9
                    if row['month'] ==  'October':
                        month=10
                    if row['month'] == 'November':
                        month=11
                    if row['month'] == 'December':
                        month=12
                    return datetime(year=year, month=month, day=1)

                to_plot_df['date']=to_plot_df.apply(compute_date,axis=1)
                to_plot_df = to_plot_df.set_index('date')
                to_plot_df = to_plot_df[
                    ['epoch realized return', 'epoch realized max drawdown']].copy()
                fig = realtime_plotting_utility.plot_multiple_bar_series(
                    data_df=to_plot_df[['epoch realized return']],
                    logy=False, split=False,
                    put_on_same_scale=False,
                    title=f'epoch realized return in percent')
                fig.show()
                fig = realtime_plotting_utility.plot_multiple_bar_series(
                    data_df=to_plot_df[['epoch realized max drawdown']],
                    logy=False, split=False,
                    put_on_same_scale=False,
                    title=f'epoch realized max drawdown in percent')
                fig.show()
    return data[dd_list]
