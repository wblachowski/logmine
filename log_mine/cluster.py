class Cluster():
    def __init__(self, cluster):
        self.pattern = ' '.join(cluster[2])
        self.count = cluster[1]
        self.logs = list(cluster[3])
