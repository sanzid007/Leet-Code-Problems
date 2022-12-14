class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int m = size(mat);
        int n = size(mat[0]);
        int total = m*n;
        
        if(r*c != total)
            return mat;
        else
        {
            vector<vector<int>> ans(r, vector<int>(c));
            for(int i=0; i < total; i++)
            {
                ans[i/c][i%c] = mat[i/n][i%n];
            }
            
            return ans;
        }
    }
};