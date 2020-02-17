class Solution {
    // Kuhn-Munkres Algorithm for optimal matching of bipartite graph.
    vector<vector<int>> dist;
    vector<int> costW, costB;
    vector<int> match; // match[i] = j means i-th bike assigned to j-th worker
    void initDist(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        dist.resize(workers.size(), vector<int>(bikes.size(), 0));
        for (int i = 0; i < workers.size(); i++) {
            for (int j = 0; j < bikes.size(); j++) {
                dist[i][j] = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]);
            }
        }
    }

    void initCost(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        costW.resize(workers.size(), INT_MAX);
        costB.resize(bikes.size(), 0);
        for (int i = 0; i < workers.size(); i++) {
            for (int j = 0; j < bikes.size(); j++) {
                costW[i] = min(costW[i], dist[i][j]); // different from maximum matching
            }
        }
    }
    
    bool augment(int node, vector<bool> & visW, vector<bool> & visB) {
        visW[node] = true;
        for (int i = 0; i < dist[node].size(); i++) {
            if (visB[i] || costW[node] + costB[i] < dist[node][i]) continue; // This line varies in maximum matching
            visB[i] = true;
            if (match[i] < 0 || augment(match[i], visW, visB)) {
                match[i] = node;
                return true;
            }
        }
        return false;
    }
    
    void update(vector<bool> & visW, vector<bool> & visB) {
        int delta = INT_MAX;
        for (int i = 0; i < costW.size(); i++) {
            if (visW[i]) {
                for (int j = 0; j < costB.size(); j++) {
                    if (!visB[j]) {
                        delta = min(delta, dist[i][j] - costW[i] - costB[j]); // This line varies in maximum matching
                    }
                }
            }
        }
        for (int i = 0; i < costW.size(); i++) {
            if (visW[i]) {
                costW[i] += delta; // This line varies in maximum matching
            }
        }
        for (int i = 0; i < costB.size(); i++) {
            if (visB[i]) {
                costB[i] -= delta; // This line varies in maximum matching
            }
        }
    }
public:
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        initDist(workers, bikes);
        initCost(workers, bikes);
        match.resize(bikes.size(), -1);
        vector<bool> visW(workers.size(), false);
        vector<bool> visB(bikes.size(), false);
        for (int i = 0; i < workers.size(); i++) {
            while (true) {
                fill_n(visW.begin(), workers.size(), false);
                fill_n(visB.begin(), bikes.size(), false);
                if (augment(i, visW, visB)) {
                    break;
                } else {
                    update(visW, visB);
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < bikes.size(); i++) {
            if (match[i] >= 0) {
                ans += dist[match[i]][i];
            }
        }
        return ans;
    }
};

