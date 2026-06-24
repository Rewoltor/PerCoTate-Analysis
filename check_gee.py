import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.read_csv('/Users/baltaymarci/Documents/Feel Good AI/Analysis/data/processed/merged_trials_exclude.csv') if __import__('os').path.exists('/Users/baltaymarci/Documents/Feel Good AI/Analysis/data/processed/merged_trials_exclude.csv') else None

if df is not None:
    # GEE for original
    df['human_correct_orig'] = (df['human_binary'] == df['gt_original']).astype(int)
    model_orig = smf.gee("human_correct_orig ~ C(condition, Treatment('no_ai'))", "participant_id", df, family=sm.families.Binomial(), cov_struct=sm.cov_struct.Exchangeable())
    result_orig = model_orig.fit()
    print(result_orig.summary())

    df['human_correct_plat'] = (df['human_binary'] == df['gt_plat_binary']).astype(int)
    model_plat = smf.gee("human_correct_plat ~ C(condition, Treatment('no_ai'))", "participant_id", df, family=sm.families.Binomial(), cov_struct=sm.cov_struct.Exchangeable())
    result_plat = model_plat.fit()
    print(result_plat.summary())
