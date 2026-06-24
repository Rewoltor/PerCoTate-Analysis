import helpers
df = helpers.load_data(kl1_strategy='clinical', filter_completers=True)
df['ai_correct_orig'] = (df['ai_prediction'] == df['gt_original_binary']).astype(int)
ai_acc = df[df['condition'] == 'ai']['ai_correct_orig'].mean()
print(f"AI Model Accuracy against Original GT (All 50 images): {ai_acc:.3f}")

df2 = helpers.load_data(kl1_strategy='exclude', filter_completers=True)
df2['ai_correct_orig'] = (df2['ai_prediction'] == df2['gt_original_binary']).astype(int)
ai_acc2 = df2[df2['condition'] == 'ai']['ai_correct_orig'].mean()
print(f"AI Model Accuracy against Original GT (27 images): {ai_acc2:.3f}")
