import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from sklearn import decomposition
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.cluster import OPTICS
from sklearn.cluster import DBSCAN

# complete_df = pd.read_csv('CSVs_complete/complete.csv', index_col='object')
# complete_df_no_label = complete_df.drop(columns=['label'])

df_1 = pd.read_csv('11.csv', index_col=0)
df_1['label'] = ['1']
df_2 = pd.read_csv('12.csv', index_col=0)
df_2['label'] = ['2']
df_3 = pd.read_csv('13.csv', index_col=0)
df_3['label'] = ['3']
df_4 = pd.read_csv('14.csv', index_col=0)
df_4['label'] = ['4']
df_5 = pd.read_csv('15.csv', index_col=0)
df_5['label'] = ['5']
df_6 = pd.read_csv('16.csv', index_col=0)
df_6['label'] = ['6']

complete_df = df_1.append(df_2, ignore_index=True)
complete_df = complete_df.append(df_3, ignore_index=True)
complete_df = complete_df.append(df_4, ignore_index=True)
complete_df = complete_df.append(df_5, ignore_index=True)
complete_df = complete_df.append(df_6, ignore_index=True)
print(complete_df)

complete_df_no_label = complete_df.drop(columns=['label'])

#-------------------------------------------------------------------------------------------------------------------------

label_list = []
corredor = ['corredor_' + str(i) for i in range(1, 14)]
encruzilhada = ['encruzilhada_' + str(i) for i in range(1, 11)]
encruzilhada_direita = ['encruzilhada_direita_' + str(i) for i in range(1, 11)]
encruzilhada_esquerda = ['encruzilhada_esquerda_' + str(i) for i in range(1, 11)]
saida_direita_esquerda = ['saida_direita_esquerda_' + str(i) for i in range(1, 2)]
saida_direita = ['saida_direita_' + str(i) for i in range(1, 2)]
saida_esquerda = ['saida_esquerda_' + str(i) for i in range(1, 2)]

for label in complete_df['label']:
	if label in corredor:
		label_list.append('corredor')
	elif label in encruzilhada:
		label_list.append('encruzilhada')
	elif label in encruzilhada_direita:
		label_list.append('encruzilhada_direita')
	elif label in encruzilhada_esquerda:
		label_list.append('encruzilhada_esquerda')
	elif label in saida_direita_esquerda:
		label_list.append('saida_direita_esquerda')
	elif label in saida_direita:
		label_list.append('saida_direita')
	elif label in saida_esquerda:
		label_list.append('saida_esquerda')

#-------------------------------------------------------------------------------------------------------------------------

delta_y = []
delta_y_complete = []
for line in complete_df_no_label.values:
	for i in range(len(line)-1):
		delta_y.append(line[i] - line[i+1])
	delta_y_complete.append(delta_y)
	delta_y = []

delta_y_complete_df = pd.DataFrame(delta_y_complete)
# delta_y_complete_df['label'] = label_list
delta_y_complete_df['label'] = ['1', '2', '3', '4', '5', '6']
delta_y_complete_df.index.name = 'object'
delta_y_complete_df.to_csv('delta_y_complete.csv')

delta_y_complete_df = pd.read_csv('delta_y_complete.csv', index_col='object')
delta_y_complete_df_no_label = delta_y_complete_df.drop(columns=['label'])


fig = make_subplots(rows=2, cols=3)

fig.add_trace(
    go.Scatter(x=list(range(0, 180)), y=delta_y_complete_df_no_label.values[0]),
    row=2, col=2
)
fig.add_trace(
    go.Scatter(x=list(range(0, 180)), y=delta_y_complete_df_no_label.values[1]),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=list(range(0, 180)), y=delta_y_complete_df_no_label.values[2]),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=list(range(0, 180)), y=delta_y_complete_df_no_label.values[3]),
    row=1, col=2
)
fig.add_trace(
    go.Scatter(x=list(range(0, 180)), y=delta_y_complete_df_no_label.values[4]),
    row=1, col=3
)
fig.add_trace(
    go.Scatter(x=list(range(0, 180)), y=delta_y_complete_df_no_label.values[5]),
    row=2, col=3
)

fig.update_layout(height=800, width=1000, title_text="Corredor")
fig.show()

#-------------------------------------------------------------------------------------------------------------------------

# pca = decomposition.PCA(n_components=5)
# pca.fit(delta_y_complete_df_no_label)
# delta_y_pca_no_label = pca.transform(delta_y_complete_df_no_label)
# delta_y_pca_df = pd.DataFrame(delta_y_pca_no_label)
# delta_y_pca_df['label'] = label_list
# delta_y_pca_df.index.name = 'object'
# delta_y_pca_df.to_csv('delta_y_pca_df.csv')
#
# delta_y_pca_df = pd.read_csv('delta_y_pca_df.csv', index_col='object')
# delta_y_pca_df_no_label = delta_y_pca_df.drop(columns=['label'])
#
# fig = px.line(delta_y_pca_df_no_label.values[10861], y=delta_y_pca_df_no_label.values[10861])
# fig.show()

#-------------------------------------------------------------------------------------------------------------------------

# optics = OPTICS(metric='euclidean').fit(delta_y_pca_df_no_label)
# reachability_ = pd.DataFrame(optics.reachability_[optics.ordering_])
# reachability_['label'] = label_list
# reachability_.index = optics.ordering_
# reachability_.to_csv('reachability_.csv')
#
# reachability_ = pd.read_csv('reachability_.csv')
# fig = px.scatter(reachability_, x=reachability_.index, y='0', color='label')
# fig.show()

# fig = ff.create_dendrogram(optics.cluster_hierarchy_)
# fig.update_layout(width=2000, height=1000)
# fig.show()
#
# # delta_y_complete_df['cluster'] = optics.labels_[optics.ordering_]
# # delta_y_complete_df.index = optics.ordering_
# # score = adjusted_rand_score(delta_y_complete_df['label'], delta_y_complete_df['cluster'])
# # fig = px.scatter(delta_y_complete_df, x=delta_y_complete_df.index, y="cluster", color='label', title=str(score))
# # fig.show()

#-------------------------------------------------------------------------------------------------------------------------

# scaler = MinMaxScaler(feature_range=(0,10), copy=False)
# scaler.fit(delta_y_pca_df_no_label)
# scaler.transform(delta_y_pca_df_no_label)

# dbscan = DBSCAN(eps=20, metric='euclidean').fit(delta_y_pca_df_no_label)
#
# delta_y_pca_df_no_label['cluster'] = dbscan.labels_
# delta_y_pca_df_no_label['label'] = label_list
# score = adjusted_rand_score(delta_y_pca_df_no_label['label'], delta_y_pca_df_no_label['cluster'])
#
# fig = px.scatter(delta_y_pca_df_no_label, x=delta_y_pca_df_no_label.index, y="cluster", color='label', title=str(score))
# fig.show()