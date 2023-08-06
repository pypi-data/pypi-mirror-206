"""
Author: Daniel Famutimi
Package Name: pdcscore
Usage:
    A package to faciliate efficent calculation of the medication adherence metric
        "Proportion of Days Covered" or "PDC".
    Currently contains a single public function (calculate_pdc) to calculate PDC at either the
        member level or the member-drug level as desired. 
"""

import numpy as np
import pandas as pd

class pdccalc:
    def __init__(self, dataframe, patient_id_col, drugname_col, filldate_col,
                          supply_days_col, mbr_elig_start_dt_col,
                          mbr_elig_end_dt_col):
        self.dataframe = dataframe
        self.patient_id_col = patient_id_col
        self.drugname_col = drugname_col
        self.filldate_col = filldate_col
        self.supply_days_col = supply_days_col
        self.mbr_elig_start_dt_col = mbr_elig_start_dt_col
        self.mbr_elig_end_dt_col = mbr_elig_end_dt_col
        self.patient_ids = set(dataframe[patient_id_col])
        self.drugs = set(dataframe[drugname_col])
        self.pdc_scores_df = pd.DataFrame(columns=[patient_id_col, drugname_col, 'DAYSCOVERED', 'TOTALDAYS', 'PDC_SCORE'])
        
    def calculate_pdc(self):
        for patient_id in self.patient_ids:
            for drug in self.drugs:
                subset = self.dataframe[(self.dataframe[self.patient_id_col] == patient_id) & (self.dataframe[self.drugname_col] == drug)]
                if subset.empty:
                    continue
                dates = []
                for i, row in subset.iterrows():
                    start_date = max(row[self.filldate_col], row[self.mbr_elig_start_dt_col])
                    end_date = min(row[self.filldate_col] + pd.Timedelta(days=row[self.supply_days_col]), row[self.mbr_elig_end_dt_col])
                    dates.append((start_date, end_date))
                dates.sort()
                merged_dates = [dates[0]]
                for date_range in dates[1:]:
                    if date_range[0] <= merged_dates[-1][1]:
                        merged_dates[-1] = (merged_dates[-1][0], max(date_range[1], merged_dates[-1][1]))
                    else:
                        merged_dates.append(date_range)
                total_covered = sum([(date_range[1] - date_range[0]).days + 1 for date_range in merged_dates])
                total_days = (subset[self.mbr_elig_end_dt_col].iloc[0] - subset[self.mbr_elig_start_dt_col].iloc[0]).days + 1
                # set PDC_SCORE to zero if TOTALDAYS or DAYSCOVERED is zero
                if total_days == 0 or total_covered == 0:
                    proportion = 0
                else:
                    proportion = total_covered / total_days
                self.pdc_scores_df = pd.concat([self.pdc_scores_df, pd.DataFrame.from_records([{self.patient_id_col: patient_id,
                                                        self.drugname_col: drug,
                                                        'DAYSCOVERED': total_covered,
                                                        'TOTALDAYS': total_days,
                                                        'PDC_SCORE': proportion}])])
                self.pdc_scores_dataframe = self.pdc_scores_df.sort_values(by=[self.patient_id_col, self.drugname_col]).reset_index(drop=True)
        return self.pdc_scores_dataframe