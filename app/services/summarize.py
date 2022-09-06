import math
import nltk
import pandas as pd
from sentence_transformers import util


# nltk.download()

class SummExtract:
    def __init__(self,cluster_obj,model):
        self.cluster_obj = cluster_obj
        self.model = model

        
    def summerize(self,text,ratio=0.25):
        sents = nltk.sent_tokenize(text)
        sent_df = pd.DataFrame(sents,columns=["text"]).reset_index()
        
        filter_n = math.floor(ratio * sent_df.shape[0])
        sent_df = self.cluster_obj.do_cluster(1,sent_df)
        # print(sent_df)
        if "cluster" in sent_df.columns:
            candidates = pd.DataFrame(columns=sent_df.columns)
            cluster_count = sent_df.cluster.value_counts().to_frame().reset_index()
            cluster_count.columns = ["cluster","count"]
            sent_df = sent_df.merge(cluster_count)
    
            n = 0
            while candidates.shape[0] <filter_n:
                temp = sent_df[sent_df.cluster==n]
                if temp.shape[0]>1:
                    candidates = pd.concat([candidates,temp.iloc[:1]])
                n+=1

            centroids = candidates.text.tolist()
            unique_cadidates = sent_df[sent_df['count']==1].reset_index(drop=True)
            if candidates.shape[0]<filter_n:
                if len(centroids)>0:
                    sim_scores = util.cos_sim(self.model.encode(unique_cadidates.text.tolist()),model.encode(centroids))
                    order_to_select = sim_scores.mean(axis=1).argsort(descending=True)
                    ind = 0
                    while candidates.shape[0]<filter_n:
                        item = order_to_select[ind].item()
                        candidates = pd.concat([candidates,unique_cadidates[item:item+1]])
                        ind+=1
                else:

                    embeds = self.model.encode(unique_cadidates.text.to_list())
                    sim_scores = util.cos_sim(embeds,embeds)
                    for i in range(sim_scores.shape[0]):
                        sim_scores[i][i]=0
                    order_to_select = sim_scores.mean(axis=1).argsort(descending=True)
                    ind = 0
                    while candidates.shape[0]<filter_n:
                        item = order_to_select[ind].item()
                        candidates = pd.concat([candidates,unique_cadidates[item:item+1]])
                        ind+=1
            candidates = candidates.sort_values(by="index")

            return " ".join(candidates.text.tolist())

        else:
            print("failed")
            return ""
            
        
        
        
        