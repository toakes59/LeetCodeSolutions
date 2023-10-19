class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int s =0;
        int cols = matrix[0].size();
        int rows = matrix.size();
        int e = rows*cols-1;
        int mid = s + (e-s)/2;
        int rowIndex, colIndex;
        int element;
        while(s <= e){
            rowIndex = mid /cols;
            colIndex = mid %cols;
            element = matrix[rowIndex][colIndex];
            if(target == element){
                return true;
            }
            else if(target < element){
                e = mid -1;
            }
            else{
                s = mid +1;
            }
            mid = s + (e-s)/2;
        }
        return false;
    }
};
