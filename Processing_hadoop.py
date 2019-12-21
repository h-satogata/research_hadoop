import subprocess


def make_dictionary_releasedate():
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
    print(tag_str.split('\n'))
    print(tag_str.split('\n')[0])  # これでタグの要素１つだけ取り出せる

    for git_tag in git_tag:
        print(git_tag)
        print('loop')

#    for line in git_tag:
#        print(git_tag[line])
#        print(line)
#    print(git_tag.stdout)
    print(2)

    for line_tag in git_tag:
        git_hash_dict[line_tag] = subprocess.Popen(['git', 'log', '--oneline ', git_tag])

    for line in git_hash_dict:
        result_dict[line] = subprocess.Popen(['git', 'show ', git_hash_dict[line_tag]])

    return result_dict

def print_git():
    print_dict = make_dictionary_releasedate()

    for print_dict in print_dict:
        print(print_dict)

print_git()