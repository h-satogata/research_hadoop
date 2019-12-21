import subprocess


def make_dictionary_releasedate():
    git_tag_dict = {}
    git_hash_dict = {}
    result_dict = {}

    # 通った
    proc_ls = subprocess.Popen(['ls'], cwd='./hadoop/', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ls_byte = proc_ls.communicate()
    print(type(ls_byte[0]))
    ls_str = ls_byte[0].decode('utf-8')
    # print(test_str)
    print(ls_str.split('\n'))

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
        proc_hash = subprocess.Popen(['git', 'show', '-s', '--format=%H', git_tag_dict[tag_num]], cwd='./hadoop/', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        hash_byte = proc_hash.communicate()
        hash_str = hash_byte[0].decode('utf-8')
        git_hash_dict[tag_num] = hash_str.split('\n')[-2]
        # ↓testcode
#        print(git_hash_dict[tag_num])
#        print("---split---")



    for line in git_hash_dict:
        result_dict[line] = subprocess.Popen(['git', 'show ', git_hash_dict[line_tag]])

    return result_dict

def print_git():
    print_dict = make_dictionary_releasedate()

    for print_dict in print_dict:
        print(print_dict)

print_git()