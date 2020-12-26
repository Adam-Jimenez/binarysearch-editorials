/*
Smallest Sublist Sum at Least Target

O(N^2) with prefix sums is good enough if you write it in C++ :). Alex's answer using what I think to be a monoqueue of prefix sums is too mind-bending for me.
*/
#include "solution.hpp"
#include <bits/stdc++.h>
using namespace std;


int Solution::solve(vector<int>& nums, int target) {
    int ps[nums.size()] = {0};
    ps[0]=nums[0];
    for (int i = 1; i<nums.size(); i++) {
        ps[i]=ps[i-1]+nums[i];
    }
    for (int k = 0; k<nums.size(); k++) {
        for (int i = 0; i<nums.size()-k; i++) {
            if (ps[i+k]-ps[i]+nums[i]>=target) {
                return k+1;
            }
        }
    }
    return -1;
};
