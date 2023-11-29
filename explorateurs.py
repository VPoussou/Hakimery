
import pandas as pd

# Importation des données
raw_data = pd.read_csv('parcours_explorateurs.csv')

starting_edges = raw_data[raw_data['type_aretes'] == 'depart']
arrival_edges = raw_data[raw_data['type_aretes'] == 'arrivee']
path_edges = raw_data[raw_data['type_aretes'] == 'chemin']
non_starting_edges = raw_data[raw_data['type_aretes'] != 'depart']

# print(type(non_starting_edges))

# Theoretically this is a list that contains lists of rows. So the rows are grouped in a list for each explorer
the_treated_paths = []

for explorator_index, starting_edge in enumerate(starting_edges.iterrows()):
    print(starting_edge, type(starting_edge))
    the_treated_paths.append([pd.DataFrame([starting_edge[1]])])
    current_edge = pd.DataFrame([starting_edge[1]], columns=['noeud_amont','noeud_aval','type_aretes','distance','arete_id'])
    print(current_edge)
    print('snidule',current_edge['type_aretes'])
    while current_edge['type_aretes'] != 'arrivee':
        print(non_starting_edges[non_starting_edges['noeud_amont'] == current_edge[1]['noeud_aval']], type(non_starting_edges[non_starting_edges['noeud_amont'] == current_edge[1]['noeud_aval']]))
        the_treated_paths[explorator_index].append(non_starting_edges[non_starting_edges['noeud_amont'] == current_edge[1]['noeud_aval']])
        current_edge = the_treated_paths[explorator_index][-1]
        # print(current_edge)
        # print(type(current_edge))
        # print('schnidule',current_edge[1]['type_aretes'])

the_distances = [float]
for path_index, path in enumerate(the_treated_paths):
    the_distances.append(0)
    for edge in path:
        the_distances[path_index] += path['distance']

print(the_distances)