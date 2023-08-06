import numpy as np
from datetime import datetime, timedelta


def get_total(tup):
    arr = np.atleast_2d(tup)
    tot = sum(arr[:,3])

    benz_indx = np.where(arr[:,2] == 'benzina')
    benzina = arr[benz_indx]
    tot_benzina = sum(benzina[:, 3])

    elec_indx = np.where(arr[:,2] != 'benzina')
    electric = arr[elec_indx]
    tot_electric = sum(electric[:, 3])

    today = datetime.today()
    day_mnth_before = today - timedelta(days=30)
    last_mnth_ind = np.where(arr[:,1] > day_mnth_before)
    last_mnth_arr = arr[last_mnth_ind]
    tot_lm = float(sum(last_mnth_arr[:,3]))

    lm_ind_benz = np.where((arr[:,1] > day_mnth_before) &
                           (arr[:,2] == 'benzina'))
    lm_arr_benz = arr[lm_ind_benz]
    lm_benz = float(sum(lm_arr_benz[:,3]))

    lm_ind_elec = np.where((arr[:,1] > day_mnth_before) &
                           (arr[:,2] != 'benzina'))
    lm_arr_elec = arr[lm_ind_elec]
    lm_elec = float(sum(lm_arr_elec[:,3]))

    return tot, tot_benzina, tot_electric, tot_lm, lm_benz, lm_elec, day_mnth_before


if __name__ == '__main__':
    tup = ((80, datetime(2021, 12, 7, 0, 0), 'SWM', 3.34, 8.78),
           (81, datetime(2021, 12, 13, 0, 0), 'SWM', 3.39, 8.92),
           (81, datetime(2021, 2, 25, 0, 0), 'benzina', 4, 8.92),
           (81, datetime(2021, 3, 13, 0, 0), 'SWM', 6, 8.92),
           )
    get_total(tup)