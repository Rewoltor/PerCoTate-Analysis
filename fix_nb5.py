import json

with open('NB5_figures.ipynb', 'r') as f:
    nb = json.load(f)

# Find the cell generating Fig 3 / Fig 4 (Accuracy Paradox)
target_cell_idx = None
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        if "Generating Fig 3: Accuracy Paradox" in source:
            target_cell_idx = i
            break

if target_cell_idx is not None:
    new_source = [
        'print("Generating Fig 3: Accuracy Paradox")\n',
        '\n',
        '# Load both datasets: clinical for Original GT (50 images), exclude for Platinum GT (27 images)\n',
        'df_clin = helpers.load_data(\'clinical\', filter_completers=True)\n',
        'df_exc = helpers.load_data(\'exclude\', filter_completers=True)\n',
        '\n',
        '# 1. AI Model Accuracy\n',
        'df_clin_unique = df_clin.drop_duplicates(\'trial_image_name\')\n',
        'df_exc_unique = df_exc.drop_duplicates(\'trial_image_name\')\n',
        'ai_orig = df_clin_unique[\'ai_correct_original\'].mean()\n',
        'ai_plat = df_exc_unique[\'ai_correct_plat\'].mean()\n',
        '\n',
        '# 2. Human (Overall) Accuracy\n',
        'h_overall_orig = df_clin[\'human_correct_original\'].mean()\n',
        'h_overall_plat = df_exc[\'human_correct_plat\'].mean()\n',
        '\n',
        '# 3. Human (No-AI Condition) Accuracy\n',
        'h_noai_orig = df_clin[df_clin[\'condition\'] == \'no_ai\'][\'human_correct_original\'].mean()\n',
        'h_noai_plat = df_exc[df_exc[\'condition\'] == \'no_ai\'][\'human_correct_plat\'].mean()\n',
        '\n',
        '# 4. Human (AI-Assisted Condition) Accuracy\n',
        'h_ai_orig = df_clin[df_clin[\'condition\'] == \'ai\'][\'human_correct_original\'].mean()\n',
        'h_ai_plat = df_exc[df_exc[\'condition\'] == \'ai\'][\'human_correct_plat\'].mean()\n',
        '\n',
        '# Construct plotting dataframe\n',
        'plot_data = pd.DataFrame([\n',
        '    {\'Agent\': \'AI Model\', \'Ground Truth\': \'Original GT\', \'Accuracy\': ai_orig},\n',
        '    {\'Agent\': \'AI Model\', \'Ground Truth\': \'Platinum GT\', \'Accuracy\': ai_plat},\n',
        '    {\'Agent\': \'Human (Overall)\', \'Ground Truth\': \'Original GT\', \'Accuracy\': h_overall_orig},\n',
        '    {\'Agent\': \'Human (Overall)\', \'Ground Truth\': \'Platinum GT\', \'Accuracy\': h_overall_plat},\n',
        '    {\'Agent\': \'Human (No-AI)\', \'Ground Truth\': \'Original GT\', \'Accuracy\': h_noai_orig},\n',
        '    {\'Agent\': \'Human (No-AI)\', \'Ground Truth\': \'Platinum GT\', \'Accuracy\': h_noai_plat},\n',
        '    {\'Agent\': \'Human (AI-Assisted)\', \'Ground Truth\': \'Original GT\', \'Accuracy\': h_ai_orig},\n',
        '    {\'Agent\': \'Human (AI-Assisted)\', \'Ground Truth\': \'Platinum GT\', \'Accuracy\': h_ai_plat}\n',
        '])\n',
        '\n',
        '# Plotting\n',
        'plt.figure(figsize=(10, 6))\n',
        'sns.set_style("whitegrid")\n',
        'ax = sns.barplot(data=plot_data, x=\'Agent\', y=\'Accuracy\', hue=\'Ground Truth\', palette=[\'#E67E22\', \'#2E86C1\'])\n',
        '\n',
        '# Aesthetics and Labeling\n',
        'ax.set_ylim(0, 1.0)\n',
        'ax.set_ylabel(\'Accuracy\', fontsize=12)\n',
        'ax.set_xlabel(\'Condition / Agent\', fontsize=12)\n',
        'ax.set_title(\'The Accuracy Paradox: Impact of GT Noise across Conditions\', fontsize=14, fontweight=\'bold\')\n',
        'ax.legend(title=\'Evaluation GT\', loc=\'lower right\', frameon=True)\n',
        '\n',
        '# Add value labels on top of bars\n',
        'for p in ax.patches:\n',
        '    if p.get_height() > 0:\n',
        '        ax.annotate(f\'{p.get_height():.1%}\', \n',
        '                    (p.get_x() + p.get_width() / 2., p.get_height()), \n',
        '                    ha=\'center\', va=\'center\', \n',
        '                    xytext=(0, 9), \n',
        '                    textcoords=\'offset points\',\n',
        '                    fontsize=10, fontweight=\'bold\')\n',
        '\n',
        'sns.despine()\n',
        'plt.tight_layout()\n',
        'save_fig(plt.gcf(), \'Fig4_Accuracy_Paradox\')\n',
        'plt.show()\n'
    ]
    nb['cells'][target_cell_idx]['source'] = new_source

    with open('NB5_figures.ipynb', 'w') as f:
        json.dump(nb, f, indent=1)
    
    print("Successfully updated NB5_figures.ipynb")
else:
    print("Could not find the target cell")
