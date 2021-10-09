import pandas as pd
import numpy as np


class Compare:
    def __init__(self):
        pass

    def compare_user(self, db_df, logger_df):
        # 368 rows, 3 columns data
        db_numpy = db_df.to_numpy()
        logger_numpy = logger_df.to_numpy()
        cos_sum = np.float64(0.0)
        l2_sum = np.float64(0.0)


        for row in range(368):
            db_row = db_numpy[row]
            logger_row = logger_numpy[row]

            cosine_similarity = self.cos_sim(db_row, logger_row)
            cos_sum += cosine_similarity

            l2norm_similarity = self.l2norm_sim(db_row, logger_row)
            l2_sum += l2norm_similarity



        print(cos_sum / 368.0)
        print(l2_sum / 368.0)
        cos_sum = 0.0
        l2_sum = 0.0
        print("+++")
        return(1)

    def cos_sim(self, db_row, logger_row):
        return (np.dot(db_row, logger_row) / (np.linalg.norm(db_row) * np.linalg.norm(logger_row)))

    def l2norm_sim(self, db_row, logger_row):
        norm_diff = (np.linalg.norm(db_row) - np.linalg.norm(logger_row))
        sim = abs(norm_diff / np.linalg.norm(db_row))
        return (sim)
