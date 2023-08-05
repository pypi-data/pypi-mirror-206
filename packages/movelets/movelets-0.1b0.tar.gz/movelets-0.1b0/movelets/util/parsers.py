from pandas import json_normalize

# ------------------------------------------------------------------------------------------------------------
# TRAJECTORY 
# ------------------------------------------------------------------------------------------------------------
def parse_trajectories(df, tid_col='tid', label_col='label', from_traj=0, to_traj=100):
    ls_trajs = []
    def processT(df, tid):
        df_aux = df[df[tid_col] == tid]
        label = df_aux[label_col].unique()[0]
        features = [x for x in df.columns if x not in [tid_col, label_col]]
        points = df_aux[features].to_dict(orient='records')
        return Trajectory(tid, label, features, points, len(points))
    
    tids = list(df[tid_col].unique())
    #tids = tids[from_traj: to_traj if len(tids) > to_traj else len(tids)] # TODO
    ls_trajs = list(map(lambda tid: processT(df, tid), tqdm(tids, desc='Reading Trajectories')))
        
    return ls_trajs

# ------------------------------------------------------------------------------------------------------------
# MOVELETS 
# ------------------------------------------------------------------------------------------------------------
def read_movelets(path_name, name='movelets'):
    count = 0
    path_to_file = glob.glob(os.path.join(path_name, '**', 'moveletsOnTrain.json'), recursive=True)

    movelets = []
    for file_name in path_to_file:
        aux_mov = read_movelets_json(file_name, name, count)
        movelets = movelets + aux_mov
        count = len(movelets)

    return movelets
    
def read_movelets_json(file_name, name='movelets', count=0):
    with open(file_name) as f:
        return parse_movelets(f, name, count)
    return []

def parse_movelets(file, name='movelets', count=0):
    importer(['json'], globals())
    
    #ls_movelets = []
    data = json.load(file)
    if name not in data.keys():
        name='shapelets'
    l = len(data[name])
    #for x in range(0, l):
    def parseM(x):
        nonlocal count
        points = data[name][x]['points_with_only_the_used_features']
        #ls_movelets.append(
        count += 1
        return Movelet(\
                count, data[name][x]['trajectory'],\
                points,\
                float(data[name][x]['quality']['quality'] * 100.0),\
                data[name][x]['label'],\
                data[name][x]['start'],\
                int(data[name][x]['quality']['size']))\
        #)
    ls_movelets = list(map(lambda x: parseM(x), tqdm(range(0, l), desc='Reading Movelets')))

#        count += 1
    ls_movelets.sort(key=lambda x: x.quality, reverse=True)
    return ls_movelets