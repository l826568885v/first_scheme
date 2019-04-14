#!/usr/bin/env python
#-*-coding:utf-8-*-
import os
import sys
import re
def create_repo_info(repo_num=3,branch_num=3):
    branch_flag = []
    for i in repo_num:
        repo_name = "repo"+str(i)+"_info"
        for num in range(branch_num):
            branch_flag.append('branch'+chr(65+i))
        repo_name = {"repo_add":"address"+str(i),"repo_path":"path"+str(i),"branches":branch_flag}
# repo1_info = {"repo_add":"address1","repo_path":"path1","branches":['branchA','branchB','branchC']}
# repo2_info = {"repo_add":"address2","repo_path":"path2","branches":['branchA','branchB','branchC']}
# repo3_info = {"repo_add":"address3","repo_path":"path3","branches":['branchA','branchB','branchC']}
def get_repo(repo_path,path='.'):
    if path is not '.':
        os.system("git clone repo_path path")
    else:
        path = os.path.abspath(os.path.dirname(__file__))
        os.system("git clone repo_path path")
def get_log(repo_path,branch='master',num=10):
    os.chdir(repo_path)
    os.system('git pull --rebase && git checkout branch && git log --pretty=format:"%H %an %ae %ce %cd"')
    
    
def revert_code(commit_ID,repo_add=".",branch_name="master"):
    if path is not '.':
        os.chdir(repo_add)
        os.system("git pull --rebase && git checkout branch_name && git revert commit_ID && git push origin branch_name")
    else: 
        os.system("git pull --rebase && git checkout branch_name && git revert commit_ID && git push origin branch_name")
def cherry_pick(commit_ID,branch2,repo_add="."):
    if path is not '.':
        os.chdir(repo_add)
        os.system("git pull --rebase && git checkout branch2 && git cherry-pick commit_ID && git push origin branch")
if __name__ == "__main__":
    print(os.path.abspath(os.path.dirname(__file__)))
    num =3
    print("repo"+str(num)+"_info")
    print(chr(65))
    flag = []
    for i in range(3):
        print(i)
        flag.append(chr(65+i))
        print('branch'+chr(65+i))  
        print("branch"+i)
    
    # if file.endswith(".mak") or "makefile" in file: 
