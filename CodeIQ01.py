# -*- coding:utf-8 -*-
"""
@brief CodeIQ 'Refine this code for Python 2.7+ and 3'
"""
def generate_array_2d(modified, n, m):
    """
    n * m の２次元配列（値は0で初期化）を返します
    :param bool modified: Trueの場合に修正後の結果を返します
    :param int n: ２次元配列の行数
    :param int m: ２次元配列の列数
    :rtype: list
    :return: 生成した２次元配列
    """
    result = []
    if modified is False:
        # 修正前 : このスコープ内のコードを改善しましょう
        for i in range(n):
            result.append([])
            for j in range(m):
                result[i].append(0)
    else:
        # 修正後 : 同等の戻り値となるよう、なるべく短いコードで書き換えてください
        result = [[0 for j in range(m)] for i in range(n)]
    
    return result

def flip_dict_items(modified, src):
    """
    キーと値を入れ替えた辞書を返します
    :param bool modified: Trueの場合に修正後の結果を返します
    :param dict src: 辞書
    :rtype: dict
    :return: キーと値を入れ替えた辞書
    """
    dst = {}
    if modified is False:
        # 修正前 : このスコープ内のコードを改善しましょう
        for key in src:
            dst[src[key]] = key
    else:
        # 修正後 : 同等の戻り値となるよう、なるべく短いコードで書き換えてください
        dst = {value:key for key, value in src.items()}
    
    return dst

if __name__ == '__main__':
    # 生成した4 * 4の２次元配列の中身を表示します
    print("generate a 4 * 4 array")
    print(generate_array_2d(False, 4, 4))
    print(generate_array_2d(True, 4, 4))
    # キーと値を入れ替えた辞書の中身を表示します
    print("flip keys and values of a dictionary")
    print(flip_dict_items(False, {1: "a", 2: "b"}))
    print(flip_dict_items(True, {1: "a", 2: "b"}))
