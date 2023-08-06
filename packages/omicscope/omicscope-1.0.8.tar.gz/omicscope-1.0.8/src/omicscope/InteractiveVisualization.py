""" Module for Single Omics Experiment Visualization
This module allows the user to extract information from Omics data using visualization tools.
Here, it is possible to evaluate data normalization (MA-Plot, Volcano Plot, Dynamic range plot,),
individual protein abundance (barplot, boxplots), and perform Principal Component Analysis (PCA) and
Hierarchical clustering analysis (heatmap, pearson correlation plot)

@author: Reis-de-Oliveira G <guioliveirareis@gmail.com>
"""

import copy
import itertools
import random

import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from kneed import KneeLocator
from scipy.stats import zscore
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


def bar_ident(OmicScope, logscale=True):
    """Show the amount of entities identified and differentially regulated
    in the study.

    Args:
        OmicScope (OmicScope): OmicScope Experiment
        logscale (bool, optional): Y-axis log-scaled. Defaults to True.
        col (str, optional): Color. Defaults to 'darkcyan'.
        save (str, optional): Path to save figure. Defaults to ''.
        dpi (int, optional): Resolution to save figure. Defaults to 300.
        vector (bool, optional): Save figure in as vector (.svg). Defaults to
        True.

    Returns:
        ax [matplotlib object]: Barplot
    """
    # Define plt parameters
    OmicScope = copy.copy(OmicScope)
    df = OmicScope.quant_data
    # Get number of identified proteins
    identified = df.Accession.count()
    # Get number of quantified proteins
    quantified = df.dropna(axis=0, subset=[OmicScope.pvalue]).Accession.count()
    # Get number of differentially regulated proteins
    deps = OmicScope.deps['Accession'].count()
    if identified != quantified:
        df = ['Identified', 'Quantified', 'Differentially regulated']
        protein_number = [identified, quantified, deps]
        color = ['lightgray', 'darkgray', 'darkcyan']
    else:
        df = ['Quantified', 'Differentially regulated']
        protein_number = [quantified, deps]
        color = ['darkgray', 'darkcyan']
    df = pd.DataFrame(zip(protein_number, df, color), columns=['Number', 'Protein', 'color'])
    # Log scaling y-axis
    if logscale is True:
        df['log'] = np.log10(df.Number)
    else:
        df['log'] = df.Number
    import altair as alt
    bar = alt.Chart(df).mark_bar().encode(
        y=alt.Y('log', title='# Proteins'),
        x='Protein',
        color=alt.Color('color', scale=None)
    )
    text = bar.mark_text(dy=-5).encode(
        text='Number')

    plot = (bar + text)
    return plot


def volcano_Multicond(OmicScope, pvalue=0.05, palette='viridis',
                      non_regulated='#606060'):
    """Creates a volcano plot for multiple conditions .
    In general, volcano plots are designed to plot 2 conditions.
    Here, we aim to see the distribution of quantified proteins' p-value and
    fold changes among multiple conditions.
    Args:
        OmicScope (OmicScope object): OmicScope Experiment
        pvalue (float, optional): p-value threshold. Defaults to 0.05.
        palette (str, optional): Color palette to differentiate dots.
        Defaults to 'viridis'.
        bcol (str, optional): color for density plot. Defaults to '#962558'.
        non_regulated (str, optional): Proteins not differentially regulated.
         Defaults to '#606060'.
        save (str, optional): Path to save figure. Defaults to ''.
        dpi (int, optional): figure resolution. Defaults to 300.
        vector (bool, optional): Save figure in as vector (.svg). Defaults to
        True.
    """
    OmicScope = copy.copy(OmicScope)
    # Definitions for the axes
    df_initial = OmicScope.quant_data
    fc = df_initial['log2(fc)']
    fc = fc.replace([np.inf], fc.max() + 1)
    fc = fc.replace([-np.inf], fc.max() - 1)
    pval = df_initial[f'-log10({OmicScope.pvalue})']
    pval = pval.replace([np.inf], pval.max() + 1)
    df_initial[f'-log10({OmicScope.pvalue})'] = pval
    df_initial['log2(fc)'] = fc

    # colors per condition
    comparisons = df_initial.Comparison
    comparisons = comparisons.str[-1] + '-' + comparisons.str[0]
    number_of_comparison = len(comparisons.drop_duplicates())
    color_per_comparison = sns.color_palette(palette=palette,
                                             n_colors=number_of_comparison).as_hex()
    color_comp_dict = dict(zip(comparisons, color_per_comparison))
    col = []
    comparison = []
    for pv, comp in zip(pval, comparisons):
        if pv > -np.log10(pvalue):
            comparison.append(comp)
            col.append(comp)
        else:
            col.append(non_regulated)
            comparison.append('Non-regulated')

    col = pd.Series(col)
    comparison = pd.Series(comparison)
    df = pd.DataFrame(data=zip(pval, fc, col, comparison, df_initial.gene_name))
    df.columns = ['pval', 'fc', 'col', 'Regulation', 'gene_name']
    df['pval'] = df['pval'].astype(float)
    df['fc'] = df['fc'].astype(float)
    df['col'] = df.col.replace(color_comp_dict)
    return df


def volcano_2cond(OmicScope, pvalue=0.05,
                  non_regulated='#606060', up_regulated='#E4001B',
                  down_regulated='#6194BC'):
    """Creates a volcano plot for two conditions .

    Args:
        OmicScope (OmicScope object): OmicScope experiment
        pvalue (float, optional): p-value threshold. Defaults to 0.05.
        bcol (str, optional): color for density plot. Defaults to 'darkcyan'.
        non_regulated (str, optional): Proteins not differentially regulated.
         Defaults to '#606060'.
        up_regulated (str, optional): Proteins up-regulated in relation
        to Control group. Defaults to '#E4001B'.
        down_regulated (str, optional): Proteins down-regulated in relation
        to Control group. Defaults to '#6194BC'.
        save (str, optional): Path to save figure. Defaults to ''.
        dpi (int, optional): figure resolution. Defaults to 300.
        vector (bool, optional): Save figure in as vector (.svg). Defaults to
        True.
    """
    OmicScope = copy.copy(OmicScope)
    FoldChange_cutoff = OmicScope.FoldChange_cutoff
    # Definitions for the axes
    df_initial = OmicScope.quant_data
    fc = df_initial['log2(fc)']
    fc = fc.replace([np.inf], fc.max() + 1)
    fc = fc.replace([-np.inf], fc.max() - 1)
    pval = df_initial[f'-log10({OmicScope.pvalue})']
    pval = pval.replace([np.inf], pval.max() + 1)
    df_initial[f'-log10({OmicScope.pvalue})'] = pval
    df_initial['log2(fc)'] = fc
    # Defining colors for dots
    col = []
    comparison = []
    for i, j in zip(fc, pval):
        if j < -np.log10(pvalue):
            col.append(non_regulated)
            comparison.append('non-regulated')
        else:
            if i > FoldChange_cutoff:
                col.append(up_regulated)
                comparison.append('up-regulated')
            elif i < -FoldChange_cutoff:
                col.append(down_regulated)
                comparison.append('down-regulated')
            else:
                col.append(non_regulated)
                comparison.append('non-regulated')
    col, comparison = pd.Series(col), pd.Series(comparison)
    df = pd.DataFrame(zip(pval, fc, col, comparison, df_initial.gene_name))
    df.columns = ['pval', 'fc', 'col', 'Regulation', 'gene_name']
    return df


def volcano(OmicScope,
            pvalue=0.05, palette='viridis',
            non_regulated='#606060', up_regulated='#E4001B',
            down_regulated='#6194BC'):
    """Creates volcano plot.

    Args:
        OmicScope (OmicScope object): OmicScope Experiment
        pvalue (float, optional): p-value threshold. Defaults to 0.05.
        bcol (str, optional): Density plot color. Defaults to '#962558'.
        palette (str, optional): Palette for Multiconditions volcano plot.
         Defaults to 'viridis'.
        non_regulated (str, optional): Color of non-differentially regulated
         proteins. Defaults to '#606060'.
        up_regulated (str, optional): Color of up-regulated proteins for volcano
        with 2 conditions. Defaults to '#E4001B'.
        down_regulated (str, optional): Color of down-regulated proteins for volcano
        with 2 conditions. Defaults to '#6194BC'.
        save (str, optional): Path to save figure. Defaults to ''.
        dpi (int, optional): . Resolution to save figure. Defaults to 300.
        vector (bool, optional): Save figure in as vector (.svg). Defaults to
        True.
    """
    OmicScope = copy.copy(OmicScope)
    if len(OmicScope.Conditions) == 2:
        df = volcano_2cond(OmicScope, pvalue=pvalue,
                           non_regulated=non_regulated, up_regulated=up_regulated,
                           down_regulated=down_regulated,)
    if len(OmicScope.Conditions) > 2:
        df = volcano_Multicond(OmicScope=OmicScope,
                               pvalue=pvalue, palette=palette, )
    import altair as alt

    pval = alt.binding_range(min=0, max=df.pval.max(), step=1, name='Pvalue:')

    selector_pval = alt.selection_single(name="SelectorName", fields=['cutoff'],
                                         bind=pval, init={'cutoff': -np.log10(0.05)})

    A = alt.Chart(df).mark_point(filled=True).encode(
        x='fc:Q',
        y='pval:Q',
        tooltip="gene_name:N",
        color=alt.condition(
            alt.datum.pval < selector_pval.cutoff,
            alt.value('gray'), alt.Color('col', scale=None)
        )
    ).add_selection(
        selector_pval
    ).interactive()
    A
    return A


def heatmap(OmicScope, *Proteins, pvalue=0.05, c_cluster=True,
            palette='RdYlBu_r', line=0.01, color_groups='tab20',
            save='', dpi=300, vector=True):
    """ Heatmap

    Args:
        OmicScope (OmicScope object): OmicScope Experiment
        pvalue (float, optional): P-value threshold. Defaults to 0.05.
        c_cluster (bool, optional): Applies Hierarchical clustering for
        columns. Defaults to True.
        color_groups (str, optional): Palette for group colors.
        Defaults to 'tab20'.
        palette (str, optional): Palette for protein abundance. Defaults to 'RdYlBu_r'.
        line (float, optional): Line width. Defaults to 0.01.
        save (str, optional): Path to save figure. Defaults to ''.
        dpi (int, optional): figure resolution. Defaults to 300.
        vector (bool, optional): Save figure in as vector (.svg). Defaults to
        True.
    """
    plt.style.use('default')
    plt.rcParams["figure.dpi"] = dpi
    OmicScope = copy.copy(OmicScope)
    FoldChange_cutoff = OmicScope.FoldChange_cutoff
    df = OmicScope.quant_data
    pdata = OmicScope.pdata
    sample_condition = dict(zip(pdata.Sample, pdata.Condition))
    sort_columns = list(pdata.sort_values(['Condition'])['Sample'])
    if 'TimeCourse' in pdata.columns:
        sort_columns = list(pdata.sort_values(['Condition', 'TimeCourse'])['Sample'])
        times = pdata.TimeCourse.drop_duplicates()
        ntimes = len(times)
        pal = sns.color_palette(palette='BuPu', as_cmap=False, n_colors=ntimes)
        dic = {}
        for C, c in zip(times, pal):
            dic.update({C: c})
        replacer = dic.get
        time_colors = [replacer(n, n) for n in list(pdata.sort_values(['Condition', 'TimeCourse']).TimeCourse)]
    else:
        time_colors = []
    Conditions = OmicScope.Conditions
    # Creating Heatmap Matrix
    heatmap = df[df.loc[:, OmicScope.pvalue] <= pvalue]
    heatmap = heatmap.loc[(heatmap['log2(fc)'] <= -FoldChange_cutoff)
                          | (heatmap['log2(fc)'] >= FoldChange_cutoff)]
    heatmap = heatmap.dropna()
    # Filtering for specific proteins
    if len(Proteins) > 0:
        heatmap = heatmap[heatmap['gene_name'].isin(Proteins)]
    heatmap = heatmap.set_index('gene_name')
    heatmap = heatmap.loc[:, heatmap.columns.str.contains('.', regex=False)]
    # Log2 transform
    heatmap = np.log2(heatmap).replace([-np.inf], int(0))
    heatmap = heatmap[sort_columns]
    heatmap = heatmap.rename(columns=sample_condition)
    Col = list(heatmap.columns)
    # Creating matrix for group colors
    ngroup = len(Conditions)
    pal = sns.color_palette(palette=color_groups, as_cmap=False, n_colors=ngroup)
    dic = {}
    for C, c in zip(Conditions, pal):
        dic.update({C: c})
    replacer = dic.get
    colcolors = [replacer(n, n) for n in Col]
    colors = [colcolors] + [time_colors]
    if colors[-1] == []:
        colors = colcolors
    # Title
    title = 'Heatmap - ' + OmicScope.ctrl + ' vs ' + '-'.join(OmicScope.experimental)
    # Plot
    sns.clustermap(heatmap,
                   cmap=palette, z_score=0, linewidths=line, linecolor='black',
                   col_colors=colors,
                   col_cluster=c_cluster,
                   figsize=(14, 14), center=0).fig.suptitle(title, y=1.02, size=30)
    # Save
    if save != '':
        if vector is True:
            plt.savefig(save + 'heatmap.svg')
        else:
            plt.savefig(save + 'heatmap.png', dpi=dpi)
    plt.show()


def correlation(OmicScope, *Proteins, pvalue=1.0,
                Method='pearson', palette='RdYlBu_r', line=0.005,
                color_groups='tab20',
                save='', dpi=300, vector=True):
    """Pairwise correlation plot for samples.

    Args:
        OmicScope (OmicScope object): OmicScope Experiment.
        pvalue (float, optional): p-value threshold. Defaults to 1.0.
        Method (str, optional): Method of correlation. Defaults to 'pearson'.
        palette (str, optional): Palette for R-distribution. Defaults to 'RdYlBu_r'.
        line (float, optional): Line width. Defaults to 0.005.
        color_groups (str, optional): Color of each group. Defaults to 'tab20'.
        save (str, optional): Path to save figure. Defaults to ''.
        dpi (int, optional): figure resolution. Defaults to 300.
        vector (bool, optional): Save figure in as vector (.svg). Defaults to
        True.
    """
    plt.style.use('default')
    plt.rcParams["figure.dpi"] = dpi
    OmicScope = copy.copy(OmicScope)
    FoldChange_cutoff = OmicScope.FoldChange_cutoff
    df = OmicScope.quant_data
    pdata = OmicScope.pdata
    sample_condition = dict(zip(pdata.Sample, pdata.Condition))
    sort_columns = list(pdata.sort_values(['Condition'])['Sample'])
    if 'TimeCourse' in pdata.columns:
        sort_columns = list(pdata.sort_values(['Condition', 'TimeCourse'])['Sample'])
        times = pdata.TimeCourse.drop_duplicates()
        ntimes = len(times)
        pal = sns.color_palette(palette='BuPu', as_cmap=False, n_colors=ntimes)
        dic = {}
        for C, c in zip(times, pal):
            dic.update({C: c})
        replacer = dic.get
        time_colors = [replacer(n, n) for n in list(pdata.sort_values(['Condition', 'TimeCourse']).TimeCourse)]
    else:
        time_colors = []
    Conditions = OmicScope.Conditions
    # Selecting Matrix for correlation
    pearson = df[df.loc[:, OmicScope.pvalue] <= pvalue]
    pearson = pearson.loc[(pearson['log2(fc)'] <= -FoldChange_cutoff)
                          | (pearson['log2(fc)'] >= FoldChange_cutoff)]
    pearson = pearson.dropna()
    # Filtering for specific proteins
    if len(Proteins) > 0:
        pearson = pearson[pearson['gene_name'].isin(Proteins)]
    pearson = pearson.set_index('gene_name')
    pearson = pearson.loc[:, pearson.columns.str.contains('.', regex=False)]
    # log2 transform
    pearson = np.log2(pearson).replace([-np.inf], int(0))
    # Performing Pearson's Correlation
    corr_matrix = pearson.corr(method=Method)
    # Creating matrix for group colors

    corr_matrix = corr_matrix[sort_columns]
    corr_matrix = corr_matrix.rename(columns=sample_condition)
    Col = list(corr_matrix.columns)
    # Creating matrix for group colors
    ngroup = len(Conditions)
    pal = sns.color_palette(palette=color_groups, as_cmap=False, n_colors=ngroup)
    dic = {}
    for C, c in zip(Conditions, pal):
        dic.update({C: c})
    replacer = dic.get
    colcolors = [replacer(n, n) for n in Col]
    colors = [colcolors] + [time_colors]
    if colors[-1] == []:
        colors = colcolors
    # Title
    title = 'Heatmap - ' + OmicScope.ctrl + ' vs ' + '-'.join(OmicScope.experimental)
    # Plot
    sns.clustermap(corr_matrix,
                   xticklabels=corr_matrix.columns, row_colors=colors,
                   yticklabels=corr_matrix.columns, col_colors=colors,
                   cmap=palette, linewidths=line, linecolor='black').fig.suptitle(title, y=1.02, size=30)
    if save != '':
        if vector is True:
            plt.savefig(save + 'pearson.svg')
        else:
            plt.savefig(save + 'pearson.png', dpi=dpi)
    plt.show()
    plt.show(block=True)


def Dispersion(OmicScope):
    """Dynamic range and MAplot

    Args:
        OmicScope (OmicScope object): OmicScope Experiment

    """
    OmicScope = copy.copy(OmicScope)
    df = OmicScope.quant_data
    # Dictionary for Accessions
    accession = dict(zip(df.Accession, df.gene_name))
    foldchange = dict(zip(df.Accession, df['log2(fc)']))
    pval = dict(zip(df.Accession, df[OmicScope.pvalue]))
    df = df.set_index('Accession')
    df = df.loc[:, df.columns.str.contains('.', regex=False)]
    df = np.log10(df).transpose()
    # Getting Mean, Max and Min values for each protein
    df = df.describe().transpose()
    df = df.dropna()
    df = df.reset_index()
    # Applying Dictionary to get gene name
    df['gene_name'] = df.Accession.replace(accession)
    # Ranking entities
    df['rank'] = df['mean'].rank(method='first')
    df['fc'] = df.Accession.replace(foldchange)
    df['pval'] = df.Accession.replace(pval)
    df['regulation'] = np.where(df.pval > OmicScope.PValue_cutoff, 'non-regulated',
                                np.where(df.fc < 0, 'down-regulated', 'up-regulated'))
    import altair as alt
    source = df

    brush = alt.selection(type='interval')

    base = alt.Chart(source).mark_point(filled=True, size=50, opacity=1).encode(
        tooltip="gene_name:N",
        color=alt.condition(brush,
                            alt.Color('regulation:N',
                                      scale=alt.Scale(scheme='redblue',
                                                      reverse=True, domainMid=0)),
                            alt.ColorValue(None)),
        opacity=alt.condition(
                alt.datum.pval > 0.05, alt.value(0.4), alt.value(1)
        )
    ).properties(
        width=350,
        height=350)

    base.encode(x='rank', y='mean').interactive() | base.encode(x='mean', y='fc').add_selection(brush)
    return base.encode(x='rank', y='mean').interactive() | base.encode(x='mean', y='fc').add_selection(brush)


def pca(OmicScope, pvalue=1.00,
        FoldChange_cutoff=0,):
    """ Perform Principal Component Analysis.

    Args:
        OmicScope (OmicScope object): OmicScope experiment
        pvalue (float, optional): p-value threshold. Defaults to 1.00.
        FoldChange_cutoff (int, optional): Fold change threshold. Defaults to 0.
    """
    OmicScope = copy.copy(OmicScope)
    df = OmicScope.quant_data
    FoldChange_cutoff = OmicScope.FoldChange_cutoff
    # Filtering P-value and Fold Change
    df = df[df[OmicScope.pvalue] < pvalue]
    if len(OmicScope.Conditions) == 2:
        df = df.loc[(df['log2(fc)'] <= -FoldChange_cutoff) | (df['log2(fc)'] >= FoldChange_cutoff)]
    df = df.loc[:, df.columns.str.contains('.', regex=False)]
    samples = df.columns
    # Getting Conditions
    Conditions = OmicScope.Conditions
    group = []
    for i in Conditions:
        ncond = df.columns.str.contains(i).sum()
        nlist = list(itertools.repeat(i, ncond))
        group.extend(nlist)
    # Center and Scale data
    scaled_data = preprocessing.scale(df.T)
    pca = PCA()  # PCA object
    pca.fit(scaled_data)
    # get PCA coordinates for scaled_data
    pca_data = pca.transform(scaled_data)
    # Scree plot
    per_var = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
    labels = ['PC' + str(x) for x in range(1, len(per_var) + 1)]
    Screeplot = pd.DataFrame(per_var, columns=['Percentage'])
    Screeplot.index = Screeplot.index + 1
    Screeplot = Screeplot.reset_index()
    Screeplot.columns = ['PC', 'Variance(%)']
    # Plot
    pca_df = pd.DataFrame(pca_data, index=samples, columns=labels)

    pdata = OmicScope.pdata
    conditions = pdata.set_index('Sample')[['Condition']]
    if 'TimeCourse' in pdata.columns:
        conditions = pdata.set_index('Sample')[['Condition', 'TimeCourse']]
        pca_df = pca_df.merge(conditions, right_index=True, left_index=True)
        pca_df = pca_df.set_index(['Condition', 'TimeCourse'])
    else:
        pca_df = pca_df.merge(conditions, right_index=True, left_index=True)
        pca_df = pca_df.set_index(['Condition'])
    sample = pca_df.index.to_frame().astype(str).reset_index(drop=True)
    sample = sample.apply(lambda x: '-'.join(x), axis=1)
    pca_df.index = sample
    pca_df = pca_df.reset_index()
    scree = alt.Chart(Screeplot).mark_bar().encode(
        y='Variance(%):Q',
        x='PC'
    ).properties(
        width=350,
        height=350)
    pca = alt.Chart(pca_df).mark_point(filled=True, size=200).encode(
        x='PC1:Q',
        y='PC2:Q',
        tooltip='index',
        color='index'
    ).properties(
        width=350,
        height=350)

    scree | pca.interactive()

    return scree | pca.interactive()


def color_scheme(df, palette):
    """Generate colors to barplot and

    Args:
        df (DataFrame): dataframe
        palette (str): palette

    Returns:
        color (dict): dictionary assign each condition with respective color.
    """
    color = df.index.to_frame().reset_index(drop=True)
    color['variable'] = color.astype(str).apply(lambda x: '_'.join(x), axis=1)
    color = color.drop_duplicates().sort_values('variable')
    colors_scheme = ['red', 'blue', 'orange', 'green', 'darkcyan', 'magenta']
    if 'TimeCourse' in color.columns:
        timecourse = len(color.TimeCourse.drop_duplicates())
    else:
        timecourse = 1
    random.seed(10)
    colors_random = random.sample(colors_scheme, color.Condition.nunique())
    palettes = []
    if timecourse > 1:
        for i in colors_random:
            palette = sns.light_palette(i, n_colors=timecourse).as_hex()
            palettes.append(palette)
    else:
        ncolors = color.Condition.nunique()
        palettes = sns.color_palette(palette=palette, n_colors=ncolors).as_hex()
    color['colors'] = list(pd.Series(palettes).explode())
    color = dict(zip(color.variable, color.colors))
    return color


def bar_protein(OmicScope, *Proteins, logscale=True, palette='Spectral'):
    """Bar plot to show protein abundance in each condition

    Args:
        OmicScope (OmicScope object): OmicScope Experiment
        logscale (bool, optional): Apply abundance log-transformed.
        Defaults to True.

    """
    df = copy.copy(OmicScope.quant_data)
    # Proteins to plot
    df = df[df['gene_name'].isin(Proteins)]
    # Get conditions
    ctrl = [copy.copy(OmicScope.ctrl)]
    conditions = copy.copy(OmicScope.Conditions)
    conditions.remove(ctrl[0])
    # Get protein abundance for each condition
    df = df.set_index('gene_name')
    df = df.iloc[:, df.columns.str.contains('.', regex=False)]
    df = df.melt(var_name='variable', ignore_index=False)
    df = df.reset_index()
    pdata = copy.copy(OmicScope.pdata)
    pdata = pdata.set_index('Sample')
    df = df.set_index('variable')
    df = pdata.merge(df, left_index=True, right_index=True)
    if 'TimeCourse' in df.columns:
        df = df[['Condition',  'TimeCourse', 'gene_name', 'value']]
        df = df.set_index(['Condition', 'TimeCourse'])
    else:
        df = df[['Condition', 'gene_name', 'value']]
        df = df.set_index('Condition')
    # Apply log transformation
    if logscale is True:
        df['value'] = np.log2(df['value'])
        df['value'] = df['value'].replace(-np.inf, np.nan)
    df_index = df.index.to_frame().reset_index(drop=True)
    df_index = df_index.astype(str).apply(lambda x: '_'.join(x), axis=1)
    df.index = df_index
    df = df.reset_index()
    bars = alt.Chart().mark_bar().encode(
        x='index:O',
        y=alt.Y('mean(value):Q', title='log2(fc)'),
        color='index:N',
    )

    error_bars = alt.Chart().mark_errorbar(extent='ci').encode(
        x='index:O',
        y='value:Q'
    )

    A = alt.layer(bars, error_bars, data=df).facet(
        column='gene_name:N'
    )
    return A


def boxplot_protein(OmicScope, *Proteins, logscale=True, palette='Spectral'):
    """Bar plot to show protein abundance in each condition

    Args:
        OmicScope (OmicScope object): OmicScope Experiment
        logscale (bool, optional): Apply abundance log-transformed.
        Defaults to True.

    """
    df = copy.copy(OmicScope.quant_data)
    # Proteins to plot
    df = df[df['gene_name'].isin(Proteins)]
    # Get conditions
    ctrl = [copy.copy(OmicScope.ctrl)]
    conditions = copy.copy(OmicScope.Conditions)
    conditions.remove(ctrl[0])
    # Get protein abundance for each condition
    df = df.set_index('gene_name')
    df = df.iloc[:, df.columns.str.contains('.', regex=False)]
    df = df.melt(var_name='variable', ignore_index=False)
    df = df.reset_index()
    pdata = copy.copy(OmicScope.pdata)
    pdata = pdata.set_index('Sample')
    df = df.set_index('variable')
    df = pdata.merge(df, left_index=True, right_index=True)
    if 'TimeCourse' in df.columns:
        df = df[['Condition',  'TimeCourse', 'gene_name', 'value']]
        df = df.set_index(['Condition', 'TimeCourse'])
    else:
        df = df[['Condition', 'gene_name', 'value']]
        df = df.set_index('Condition')
    # Apply log transformation
    if logscale is True:
        df['value'] = np.log2(df['value'])
        df['value'] = df['value'].replace(-np.inf, np.nan)
    df_index = df.index.to_frame().reset_index(drop=True)
    df_index = df_index.astype(str).apply(lambda x: '_'.join(x), axis=1)
    df.index = df_index
    df = df.reset_index()
    A = alt.Chart(df).mark_boxplot(extent='min-max').encode(
        x='index:O',
        y=alt.Y('value:Q', title='log2(fc)',
                scale=alt.Scale(zero=False)),
        color='index:N',
        facet='gene_name'
    )
    return A


def find_k(df):
    """Find the optimum k clusters"""

    df_norm = df
    sse = {}

    for k in range(1, 21):
        kmeans = KMeans(n_clusters=k, random_state=1)
        kmeans.fit(df_norm)
        sse[k] = kmeans.inertia_

    kn = KneeLocator(x=list(sse.keys()),
                     y=list(sse.values()),
                     curve='convex',
                     direction='decreasing')
    k = kn.knee
    print(k)
    return k


def startrend(OmicScope, pvalue=0.05, k_cluster=None):
    """Perform a K-mean algorithm to identify co-expressed
    proteins/genes and
    Args:
        OmicScope (_type_): _description_
    """
    omics = copy.copy(OmicScope)
    pdata = omics.pdata
    try:
        pdata['sample'] = pdata[['Condition', 'TimeCourse']].astype(str).apply(lambda x: '-'.join(x), axis=1)
    except KeyError:
        pdata['sample'] = pdata[['Condition', 'Biological']].astype(str).apply(lambda x: '-'.join(x), axis=1)
    data = omics.quant_data
    protein_dictionary = dict(zip(data['Accession'], data['gene_name']))
    data = data[data[omics.pvalue] < pvalue]
    data = data.set_index('Accession')
    data = data.iloc[:, data.columns.str.contains('.', regex=False)]
    data = data.replace(0, 0.01)
    data = np.log2(data)
    # Scale protein abundance according to their mean (z-score)
    zscored_data = zscore(data, axis=1)
    if k_cluster is None:
        n_clusters = find_k(zscored_data)
    else:
        n_clusters = k_cluster
    kmeans = KMeans(n_clusters=n_clusters, init="k-means++",
                    max_iter=500)
    protein_cluster_assig = kmeans.fit(zscored_data)
    k_data = zscored_data
    k_data.columns = pdata['sample']
    k_data['cluster'] = protein_cluster_assig.labels_
    k_data_protein = k_data.reset_index().melt(id_vars=['Accession', 'cluster'],
                                               var_name='sample')
    dictionary = dict(zip(pdata['sample'], pdata['Condition']))
    k_data_protein['Condition'] = k_data_protein[['sample']].replace(dictionary)
    k_data_protein['gene_name'] = k_data_protein[['Accession']].replace(protein_dictionary)
    k_data_protein = k_data_protein.groupby(['cluster', 'Condition', 'sample']).sum().reset_index()
    import altair as alt
    line = alt.Chart(k_data_protein).mark_line().encode(
        x='sample:N',
        y='mean(value):Q',
        color='Condition:N'
    ).properties(
    width=300,).facet(
    facet='cluster:N',
    columns=2).configure_axis(grid=False)
    line
    return line