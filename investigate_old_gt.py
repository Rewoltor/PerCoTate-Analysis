import helpers
df = helpers.load_data('clinical', filter_completers=True)
df['human_correct_orig'] = (df['final_decision'] == df['gt_original_binary']).astype(int)
mean_acc = df.groupby('condition')['human_correct_orig'].mean()
print(mean_acc)
