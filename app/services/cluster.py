import pandas as pd
from sentence_transformers import util
class ClusterData:
    def __init__(self,model,community_threshold):
        self.model = model
        self.comm_thresh = community_threshold
    
    def do_cluster(self,request_id,input_sents:pd.DataFrame):
        try:
            if input_sents.shape[0]>0:
                sents = input_sents.text.tolist()
                embeddings = self.model.encode(sents,batch_size=32,convert_to_tensor=True)
                cluster_ind = util.community_detection(embeddings,threshold=self.comm_thresh,
                                        min_community_size=1)
                input_sents["cluster"]=None
                for i, ind in enumerate(cluster_ind):
                    input_sents.loc[ind,"cluster"]= i
                input_sents.cluster.fillna(-1,inplace=True)
                return input_sents

            else:
                    return input_sents
        except Exception as e:
            print(f"clustering failed with err {e}")
            return input_sents
            