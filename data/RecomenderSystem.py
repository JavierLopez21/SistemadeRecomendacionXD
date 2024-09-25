import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances
class RecomenderSystem:

    def __init__(self,scaler,model,scaled_df,n_songs,sp_client,feats):

        self.model = model
        self.scaler = scaler
        self.scaled_df = scaled_df
        self.n_songs = n_songs
        self.sp_client = sp_client
        self.feats = feats

    
    def get_track_name(self,track_id):
        track = self.sp_client.track(track_id)
        return (track['name'],track['artists'][0]['name'])
    
    def get_track_features(self,track_ids):
        features = self.sp_client.audio_features(track_ids)
        return features

    
    def get_track_id(self,track_name, artist_name):
        query = f'track:{track_name}'
        if artist_name:
            query += f' artist:{artist_name}'
        results = self.sp_client.search(q=query, type='track', limit=1)
        tracks = results['tracks']['items']
        if tracks:
            return tracks[0]['id']
        else:
            return None

    
    def get_recomendations(self,track_name, artist_name):

        track_id = self.get_track_id(track_name, artist_name)

        if track_id:
            print(f"ID de la canción: {track_id}")
        else:
            print("Canción no encontrada")

        data = self.get_track_features(track_id)
        data1 = pd.DataFrame(data)
        mode = data1['mode'].copy()
        feats_without_mode = self.feats.copy()
        feats_without_mode.remove("mode")
        X_new = pd.DataFrame(self.scaler.transform(pd.DataFrame(data)[feats_without_mode]),columns = feats_without_mode)
        X_new1 = X_new.copy()
        X_new1['mode'] = mode

        cluster_pred = self.model.predict(X_new1)[0]

        
        canciones_en_cluster = self.scaled_df[self.scaled_df['Cluster'] == cluster_pred]


        # Calcular la distancia a todas las canciones del cluster
        distancias = euclidean_distances(X_new1, canciones_en_cluster[self.feats])[0]
        canciones_en_cluster['Distancia'] = distancias
        # Obtener los índices de las 5 canciones más cercanas
        canciones_en_cluster = canciones_en_cluster.sort_values(by='Distancia',ascending=False)

        # Obtener los índices de las canciones en el dataset original
        indices_canciones_similares = canciones_en_cluster.head(self.n_songs)

        recomendaciones = indices_canciones_similares['id'].unique()
        return recomendaciones
