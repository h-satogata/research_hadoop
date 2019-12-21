import subprocess
import sqlite3

conn = sqlite3.connect('hadoop_hash_tag_date.db')
cursor = conn.cursor()

def make_dictionary_releasedate():
    git_tag_dict = {}
    git_hash_dict = {}
    git_autherdate_dict = {}
    result_dict = {}

    # 通った(test block)
#    proc_ls = subprocess.Popen(['ls'], cwd='./hadoop/', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#    ls_byte = proc_ls.communicate()
#    print(type(ls_byte[0]))
#    ls_str = ls_byte[0].decode('utf-8')
    # print(test_str)
#    print(ls_str.split('\n'))
    # ここまで

    # git tagコマンドによってタグを取得。tag_strにリスト構造で保存
    proc_tag = subprocess.Popen(['git', 'tag'], cwd='./hadoop/', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    tag_byte = proc_tag.communicate()
    tag_str = tag_byte[0].decode('utf-8')
    for tag_num in range(0, len(tag_str.split('\n'))-1):
        git_tag_dict[tag_num] = tag_str.split('\n')[tag_num]
    # ↓testcode
#    print(tag_str.split('\n'))
#    print(tag_str.split('\n')[0])  # これでタグの要素１つだけ取り出せる

    # git showコマンドによってgit hashを取得
    for tag_num in range(0, len(git_tag_dict)-1):
        proc_hash = subprocess.Popen(['git', 'show', '-s', '--format=%H', git_tag_dict[tag_num]], cwd='./hadoop/',
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        hash_byte = proc_hash.communicate()
        hash_str = hash_byte[0].decode('utf-8')
        # warning対策
        if 'warning: you may want to set your diff.renameLimit variable' in hash_str.split('\n')[-2]:
            git_hash_dict[tag_num] = hash_str.split('\n')[-4]
        else:
            git_hash_dict[tag_num] = hash_str.split('\n')[-2]
        # ↓test print
#        print(git_hash_dict[tag_num])
#        print("---split---")

    # git showコマンドによってAuther_dateを取得
    for tag_num in range(0, len(git_tag_dict) - 1):
        proc_adate = subprocess.Popen(['git', 'show', '-s', '--format=%ad', git_tag_dict[tag_num]], cwd='./hadoop/',
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        adate_byte = proc_adate.communicate()
        adate_str = adate_byte[0].decode('utf-8')
        # warning対策
        if 'warning: you may want to set your diff.renameLimit variable' in adate_str.split('\n')[-2]:
            git_autherdate_dict[tag_num] = adate_str.split('\n')[-4]
        else:
            git_autherdate_dict[tag_num] = adate_str.split('\n')[-2]
#        print(adate_str.split('\n'))
        # ↓test print
#        print(git_autherdate_dict[tag_num])
#        print("---split---")
#    print(type(git_autherdate_dict))


    return result_dict

def create_db():


def print_git():
    print_dict = make_dictionary_releasedate()

    for print_dict in print_dict:
        print(print_dict)

print_git()