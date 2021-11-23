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

        db_piv = db_numpy[0]
        logger_piv = logger_numpy[0]

        for row in range(1, 368):   #exclude 0th array -> pivot
            db_row = db_numpy[row]
            logger_row = logger_numpy[row]

            db_row = db_row - db_piv
            logger_row = logger_row - logger_piv

            cosine_similarity = self.cos_sim(db_row, logger_row)
            cos_sum += cosine_similarity

            l2norm_similarity = self.l2norm_sim(db_row, logger_row)
            l2_sum += l2norm_similarity

        print(cos_sum / 368.0)
        print(l2_sum / 368.0)
        cos_sim = cos_sum / 368.0
        l2_sim = l2_sum / 368.0

        print("+++")

        if cos_sim >=0.995:
            print("1")
            cos_sum = 0.0
            l2_sum = 0.0
            return(1)
        else:
            cos_sum = 0.0
            l2_sum = 0.0
            return(0)


    def cos_sim(self, db_row, logger_row):
        return (np.dot(db_row, logger_row) / (np.linalg.norm(db_row) * np.linalg.norm(logger_row)))


    def l2norm_sim(self, db_row, logger_row):
        norm_diff = (np.linalg.norm(db_row) - np.linalg.norm(logger_row))
        sim = abs(norm_diff / np.linalg.norm(db_row))
        return (sim)
